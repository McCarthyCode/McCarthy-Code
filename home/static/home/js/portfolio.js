$(document).ready(() => {
  const navHeight = $('#navbar').outerHeight();

  // scroll buttons
  $('#portfolio > header:not(:last-child), #portfolio > section:not(:last-child)').each(function () {
    let $next = $(this).next();

    $(this).find('.chevron').click(function () {
      $('html, body').animate({
        scrollTop: $next.offset().top - navHeight,
      }, 1000);
    });
  });
});
