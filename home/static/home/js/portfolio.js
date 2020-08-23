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
    const $this = $(this);
    const $next = $this.next();

    // decimal heights throw off positioning. GET. RIIIIID.
    $next.height(Math.ceil($next.height()));

    $this.find('.chevron').click(function () {
      $('html, body').animate({
        scrollTop: $next.offset().top - navHeight,
      }, 1000);
    });
  });

  // remove heights added by scroll buttons
  function removeHeights() {
    $('#portfolio > header, #portfolio > section').each(function () {
      $(this).css({'height': ''});
    });
  }

  $(window).on('resize orientationchange', removeHeights);
});
