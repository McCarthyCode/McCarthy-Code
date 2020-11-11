$(() => {
  // add content to .brand elements
  $('.brand').text('McCarthy Code');

  // external link icon
  $('a.external-link').after(
    '<span class="user-select-none"> <i class="fas fa-external-link-alt" title="External Link"></i></span>',
  );

  // stylized checkboxes
  $('input[type="checkbox"]').after('<span class="checkbox"></span>');

  // textarea character counter
  $('textarea').each(function () {
    const $this = $(this);
    const currentLength = $this.val().length;
    const maxlength = $this.attr('maxlength');

    if ($this.is(':visible')) {
      const $div = $('<div>');
      const $small = $('<small>').html(`${currentLength}/${maxlength}`);

      $this.after($div.append($small));
    }
  });

  $('textarea').on('input', function () {
    const $this = $(this);
    const $small = $this.next('div').children('small');
    const currentLength = $this.val().length;
    const maxlength = $this.attr('maxlength');

    $small.html(`${currentLength}/${maxlength}`);
  });
});
