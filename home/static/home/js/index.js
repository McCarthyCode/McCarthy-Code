$(document).ready(() => {
  function adjustTitle() {
    let width = $(this).width();
    let $title = $('header .h1');

    const breakpoint = 488 + 32;
    const scale = width / breakpoint;
    if (width < breakpoint) {
      $title.css({
        '-webkit-transform':
          `translate(-50%, -50%) scale(${scale})`,
        '-ms-transform':
          `translate(-50%, -50%) scale(${scale})`,
        'transform':
          `translate(-50%, -50%) scale(${scale})`,
      });
    } else {
      $title.css({
        '-webkit-transform': `translate(-50%, -50%)`,
        '-ms-transform': `translate(-50%, -50%)`,
        'transform': `translate(-50%, -50%)`,
      });
    }

    const height = $title.outerHeight();
    $('header').prop('min-height', `${height * scale + 32}px`);
  }

  function adjustIcons() {
    let windowWidth = $(window).width();
    let windowHeight = $(window).height();
    let $icons = $('#options li .option-icon');

    let breakpoint = 0;
    let scale = 1;

    if (windowWidth < 364) {
      breakpoint = 754
      scale = (windowHeight - 304) / 450 > 1 ? 1 : (windowHeight - 304) / 450;
    } else if (windowWidth < 530) {
      breakpoint = 548
      scale = (windowHeight - 248) / 300 > 1 ? 1 : (windowHeight - 248) / 300;
    } else {
      breakpoint = 342
      scale = (windowHeight - 192) / 150 > 1 ? 1 : (windowHeight - 192) / 150;
    }

    if (windowHeight < breakpoint) {
      const circumference = 150 * scale;

      $icons.css({
        'height': `${circumference}px`,
        'width': `${circumference}px`,
      });

      $icons.find('i').css({
        'font-size': `${5 * scale}em`,
      });
    } else {
      $('.option-icon, .option-icon i').prop('style', false);
    }
  }

  function adjustContact() {
    let width = $(this).width();
    let $contact = $('#contact > div');

    const breakpoint = 359;
    const scale = width / breakpoint;

    if (width < breakpoint) {
      $contact.css({
        '-webkit-transform':
          `translate(-50%, -50%) scale(${scale})`,
        '-ms-transform':
          `translate(-50%, -50%) scale(${scale})`,
        'transform':
          `translate(-50%, -50%) scale(${scale})`,
      });
    } else {
      $contact.css({
        '-webkit-transform': `translate(-50%, -50%)`,
        '-ms-transform': `translate(-50%, -50%)`,
        'transform': `translate(-50%, -50%)`,
      });
    }

    const winHeight = $(window).outerHeight();
    const navbarHeight = $('#navbar').outerHeight();
    const footerHeight = $('#footer').outerHeight();
    const contactHeight = $contact.outerHeight();

    $('section:nth-child(4)').css('min-height', `${Math.max(winHeight - navbarHeight - footerHeight, contactHeight * Math.min(1, scale) + 32)}px`);
  }

  function adjust() {
    adjustTitle();
    adjustIcons();
    adjustContact();
  }

  $(window).on('resize orientationchange', adjust);
  adjust();

  let navHeight = 56;
  $('header .chevron').click(() => {
    $('html, body').animate({
      scrollTop: $('#icons').offset().top - navHeight,
    }, 1000);
  });

  $('#icons .chevron, #options li:nth-child(3) a').click(() => {
    $('html, body').animate({
      scrollTop: $('#contact').offset().top - navHeight,
    }, 1000);
  });
});
