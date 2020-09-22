$(() => {
  // reorder screenshots by clicking arrows
  const $up = $('.screenshot-list .controls :first-child');
  const $down = $('.screenshot-list .controls :last-child');

  $up.on('click', () => {
    const $li = $(this).parents('li');

    if (!$li.is(':first-of-type')) {
      const $prev = $li.prev();

      $li.animate({'bottom': `${$prev.outerHeight() + 8}px`}, 500, function () {
        $(this).after($prev.detach()).prop('style', '');
      });

      $prev.animate({'top': `${$li.outerHeight() + 8}px`}, 500, function () {
        $(this).prop('style', '');
      });
    }
  });

  $down.on('click', () => {
    const $li = $(this).parents('li');

    if (!$li.is(':last-of-type')) {
      const $next = $li.next();

      $li.animate({'top': `${$next.outerHeight() + 8}px`}, 500, function () {
        $(this).before($next.detach()).prop('style', '');
      });

      $next.animate({'bottom': `${$li.outerHeight() + 8}px`}, 500, function () {
        $(this).prop('style', '');
      });
    }
  });

  // update value of hidden order field on submit
  $('form').submit(function () {
    let order = "[";

    $('.screenshot-list li').each(function () {
      order += `${$(this).data('id')}`;

      if (!$(this).is('.screenshot-list li:last-child')) {
        order += ", ";
      }
    });

    order += "]";

    $('input[name="order"]').val(order);

    return true;
  });
});