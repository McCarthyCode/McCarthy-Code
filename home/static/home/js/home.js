$(document).ready(() => {
  function adjustTitle() {
    let width = $(this).width();
    let $title = $('header .h1');

    if (width < 624) {
      $title.css('-webkit-transform', `translate(-50%, -50%) scale(${width / 624})`);
      $title.css('-ms-transform', `translate(-50%, -50%) scale(${width / 624})`);
      $title.css('transform', `translate(-50%, -50%) scale(${width / 624})`);
    } else {
      $title.css('-webkit-transform', 'translate(-50%, -50%)');
      $title.css('-ms-transform', 'translate(-50%, -50%)');
      $title.css('transform', 'translate(-50%, -50%)');
    }
  }

  adjustTitle();
  $(window).on('resize orientationchange', adjustTitle);

  let navHeight = $('nav').first().outerHeight();
  $('header .chevron i').click(() => {
    $('html, body').animate({
      scrollTop: $('section:nth-child(3)').offset().top - navHeight,
    }, 1000);
  });

  $('section:nth-child(3) .chevron i').click(() => {
    $('html, body').animate({
      scrollTop: $('section:nth-child(4)').offset().top - navHeight,
    }, 1000);
  });
});