import hashlib
import os

from base64 import b16encode
from functools import partial
from io import BytesIO
from PIL import Image
from slugify import slugify

from django.db import models

from mwd.settings import MEDIA_ROOT

class TimestampedModel(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class ThumbnailedImage(TimestampedModel):
    image = models.ImageField(blank=True, null=True, default=None, upload_to='')
    _image_hash = models.BinaryField(editable=False, null=True, default=None, max_length=16)
    thumbnail = models.ImageField(blank=True, null=True, default=None, upload_to='')
    _thumbnail_hash = models.BinaryField(editable=False, null=True, default=None, max_length=16)

    @classmethod
    def create(cls, *args, **kwargs):
        image = cls(**kwargs)
        image.image_ops()

        return image

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.thumbnail.delete()

        return super().delete(*args, **kwargs)

    def __str__(self):
        return self.image.name

    def image_ops(
        self, relative_path='', max_size=(1920, 1080),
        thumbnail_size=(300, 169),
    ):
        self._generate_thumbnail(relative_path, thumbnail_size)
        self._hash_thumbnail(relative_path)
        self._resize_image(relative_path, max_size)
        self._hash_image(relative_path)

    def _generate_thumbnail(self, relative_path, thumbnail_size):
        img = Image.open(self.image).convert('RGB')
        width, height = img.size
        max_longest, max_shortest = thumbnail_size

        if not self.thumbnail and (width >= height and (width > max_longest or height > max_shortest)) or (height > width and (height > max_longest or width > max_shortest)):
            if width > height:
                if (height * max_longest/ width) > max_shortest:
                    new_height = max_shortest
                    new_width = int(width * new_height / height)
                else:
                    new_width = max_longest
                    new_height = int(height * new_width / width)
            else:
                if (width * max_longest / height) > max_shortest:
                    new_width = max_shortest
                    new_height = int(height * new_width / width)
                else:
                    new_height = max_longest
                    new_width = int(width * new_height / height)

            img = img.resize((new_width, new_height), Image.ANTIALIAS)

        img_file = BytesIO()
        img.save(img_file, 'JPEG', quality=90)

        new_name = 'thumbnail_' + self.image.name.split('.')[0].replace(relative_path, '') + '.jpg'
        self.thumbnail.save(new_name, img_file)

    def _hash_thumbnail(self, relative_path, block_size=65536):
        hasher = hashlib.md5()
        filename = MEDIA_ROOT + '/' + self.thumbnail.name

        with open(filename, 'rb') as f:
            for buf in iter(partial(f.read, block_size), b''):
                hasher.update(buf)

            if not self.thumbnail_hash or self.thumbnail_hash != hasher.hexdigest().lower():
                self._thumbnail_hash = hasher.digest()
                self.thumbnail.name = relative_path + hasher.hexdigest().lower() + '.jpg'
                new_filename = MEDIA_ROOT + '/' + self.thumbnail.name
                os.rename(filename, new_filename)

    def _resize_image(self, relative_path, max_size):
        img = Image.open(self.image).convert('RGB')
        width, height = img.size
        max_width, max_height = max_size

        if (width >= height and (width > max_width or height > max_height)) or (height > width and (height > max_height or width > max_width)):
            if width > height:
                if (height * max_width/ width) > max_height:
                    new_height = max_height
                    new_width = int(width * new_height / height)
                else:
                    new_width = max_width
                    new_height = int(height * new_width / width)
            else:
                if (width * max_width / height) > max_height:
                    new_width = max_height
                    new_height = int(height * new_width / width)
                else:
                    new_height = max_width
                    new_width = int(width * new_height / height)

            img = img.resize((new_width, new_height), Image.ANTIALIAS)

        img_file = BytesIO()
        img.save(img_file, 'JPEG', quality=90)

        new_name = self.image.name.split('.')[0].replace(relative_path, '') + '.jpg'
        self.image.delete()
        self.image.save(new_name, img_file)

    def _hash_image(self, relative_path, block_size=65536):
        hasher = hashlib.md5()
        filename = MEDIA_ROOT + '/' + self.image.name

        with open(filename, 'rb') as f:
            for buf in iter(partial(f.read, block_size), b''):
                hasher.update(buf)

            if not self.image_hash or self.image_hash != hasher.hexdigest().lower():
                self._image_hash = hasher.digest()
                self.image.name = relative_path + hasher.hexdigest().lower() + '.jpg'
                new_filename = MEDIA_ROOT + '/' + self.image.name
                os.rename(filename, new_filename)

    @property
    def image_hash(self):
        return str(b16encode(self._image_hash).lower(), 'utf-8') if self._image_hash else None

    @property
    def thumbnail_hash(self):
        return str(b16encode(self._thumbnail_hash).lower(), 'utf-8') if self._thumbnail_hash else None

    class Meta:
        abstract = True

class Site(TimestampedModel):
    name = models.CharField(max_length=80)
    slug = models.SlugField(default='', max_length=80, null=True, blank=True)
    url = models.URLField()
    github = models.URLField()
    description = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField(default=0)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        super().save(*args, **kwargs)

    def delete_screenshots(self, *args, **kwargs):
        for screenshot in Screenshot.objects.filter(site=self):
            screenshot.delete(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.delete_screenshots(*args, **kwargs)

        return super().delete(*args, **kwargs)

class Screenshot(ThumbnailedImage):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
