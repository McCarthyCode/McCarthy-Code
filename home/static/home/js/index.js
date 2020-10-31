$(() => {
  const navbarHeight = 52;

  function adjust() {
    const windowWidth = $(window).width();
    const windowHeight = $(window).height();

    (function adjustTitle() {
      const $title = $('header .h1');
      const breakpoint = 275 + 32;
      const scale = windowWidth / breakpoint;

      if (windowWidth < breakpoint) {
        $title.css({
          '-webkit-transform': `scale(${scale})`,
          '-ms-transform': `scale(${scale})`,
          transform: `scale(${scale})`,
        });
      } else {
        $title.prop('style', false);
      }

      const height = $title.outerHeight();
      $('header').prop('min-height', `${height * scale + 32}px`);
    })();

    (function adjustIcons() {
      const $container = $('#icons .container');
      const $options = $container.children('#options');
      const $buttons = $options.find('button');
      const $icons = $buttons.children('i');

      const initDiameter = 150;
      const ulGap = 16;
      const containerPadding = 16;
      const aGap = 16;
      const labelHeight = 20;
      const chevron = 64;

      const breakpoints = {
        row: {
          width: 3 * initDiameter + 4 * ulGap + 2 * containerPadding,
          height:
            navbarHeight +
            1 * (initDiameter + aGap + labelHeight) +
            2 * containerPadding +
            chevron,
        },
        col: {
          width: initDiameter + 2 * containerPadding,
          height:
            navbarHeight +
            3 * (initDiameter + aGap + labelHeight) +
            2 * ulGap +
            2 * containerPadding +
            chevron,
        },
      };

      let scale;

      if (windowWidth >= windowHeight) {
        $options.css({ 'flex-direction': 'row' });

        const scales = {
          x:
            (windowWidth - breakpoints.row.width + 3 * initDiameter) /
            (3 * initDiameter),
          y:
            (windowHeight - breakpoints.row.height + initDiameter) /
            initDiameter,
        };

        scale = Math.min(scales.x, scales.y, 1);
      } else {
        $options.css({ 'flex-direction': 'column' });

        const scales = {
          x:
            (windowWidth - breakpoints.col.width + initDiameter) / initDiameter,
          y:
            (windowHeight - breakpoints.col.height + 3 * initDiameter) /
            (3 * initDiameter),
        };

        scale = Math.min(scales.x, scales.y, 1);
      }

      if (scale < 0.25) {
        $buttons.hide();
      } else {
        $buttons.show();

        const diameter = initDiameter * scale;

        $buttons.css({
          height: `${diameter}px`,
          width: `${diameter}px`,
        });

        $icons.css({ 'font-size': `${5 * scale}em` });
      }
    })();
  }

  $(window).on('resize orientationchange', adjust);
  adjust();

  $('header .chevron').on('click', () => {
    $('html, body').animate(
      { scrollTop: $('#icons').offset().top - navbarHeight },
      1000,
    );
  });

  $('#icons .chevron, #options li:nth-child(3) a').on('click', () => {
    $('html, body').animate(
      { scrollTop: $('#contact').offset().top - navbarHeight },
      1000,
    );
  });
});
