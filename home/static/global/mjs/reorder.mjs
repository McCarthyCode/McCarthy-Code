export default reorder = ($ul) => {
  // reorder screenshots by clicking arrows
  const $up = $ul.find('.controls :first-child');
  const $down = $ul.find('.controls :last-child');
  const paddingBottom = 8;

  $up.on('click', function () {
    const $li = $(this).parents('li');

    if (!$li.is(':first-child')) {
      const $prev = $li.prev();

      $li.animate(
        { bottom: `${$prev.outerHeight() + paddingBottom}px` },
        500,
        function () {
          $(this).after($prev.detach()).prop('style', '');
        },
      );

      $prev.animate(
        { top: `${$li.outerHeight() + paddingBottom}px` },
        500,
        function () {
          $(this).prop('style', '');
        },
      );
    }
  });

  $down.on('click', () => {
    const $li = $(this).parents('li');

    if (!$li.is(':last-child')) {
      const $next = $li.next();

      $li.animate(
        { top: `${$next.outerHeight() + paddingBottom}px` },
        500,
        function () {
          $(this).before($next.detach()).prop('style', '');
        },
      );

      $next.animate(
        { bottom: `${$li.outerHeight() + paddingBottom}px` },
        500,
        function () {
          $(this).prop('style', '');
        },
      );
    }
  });

  // update value of hidden order field on submit
  $('form').on('submit', function () {
    // let order = '[';

    // $ul.children('li').each(function () {
    //   order += `${$(this).data('id')}`;

    //   if (!$(this).is(':last-child')) {
    //     order += ', ';
    //   }
    // });

    // order += ']';

    // $('input[name="order"]').val(order);

    $('input[name="order"]').val(
      JSON.stringify(
        $ul.children('li').map(function () {
          return $(this).data('id');
        }),
      ),
    );

    return true;
  });
};
