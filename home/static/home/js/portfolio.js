$(document).ready(() => {
  const navHeight = $('#navbar').outerHeight();

  // contents
  $('.contents a').click(function (event) {
    event.preventDefault();
    history.pushState({}, '', this.href);

    $('html, body').animate({
      scrollTop: $(`#${$(this).data('slug')}`).offset().top - navHeight,
    }, 1000);
  });

  // scroll buttons
  $('#portfolio > header:not(:last-child), #portfolio > section:not(:last-child)').each(function () {
    const $next = $(this).next();

    $(this).find('.chevron').click(function () {
      $('html, body').animate({
        scrollTop: $next.offset().top - navHeight,
      }, 1000);
    });
  });
});
