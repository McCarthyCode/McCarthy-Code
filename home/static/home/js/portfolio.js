$(document).ready(() => {
  const navHeight = $('#navbar').outerHeight();

  // scroll buttons
  $('#portfolio > section:not(:last-of-type)').each(function () {
    let $next = $(this).next();

    $(this).find('.chevron').click(function () {
      $('html, body').animate({
        scrollTop: $next.offset().top - navHeight,
      }, 1000);
    });
  });
});
