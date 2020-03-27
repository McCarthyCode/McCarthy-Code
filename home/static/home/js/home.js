$(document).ready(() => {
  function adjustTitle() {
    let width = $(this).width();
    let $title = $('header .h1');

    const breakpoint = 624;
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
  function adjustContact() {
    let width = $(this).width();
    let $contact = $('section:nth-child(4) > div');

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
    adjustContact();
  }

  adjust();
  $(window).on('resize orientationchange', adjust);

  let navHeight = $('#navbar').outerHeight();
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
