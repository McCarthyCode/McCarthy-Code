$(document).ready(() => {
  const navHeight = $('#navbar').outerHeight();

  $('#portfolio > section:not(:last-of-type)').each(function () {
    let $next = $(this).next();

    $(this).find('.chevron i').click(function () {
      $('html, body').animate({
        scrollTop: $next.offset().top - navHeight,
      }, 1000);
    });
  });
});
