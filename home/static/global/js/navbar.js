$(() => {
  // adjust .navbarBrand breakpoints with scrollbar
  const breakpointsBrand = {
    min: 308,
    full: 414,
  };

  const scrollBarWidth = (function () {
    const $outer = $('<div>')
      .css({
        visibility: 'hidden',
        width: 100,
        overflow: 'scroll',
      })
      .appendTo('body');
    const widthWithScroll = $('<div>')
      .css({ width: '100%' })
      .appendTo($outer)
      .outerWidth();

    $outer.remove();
    return 100 - widthWithScroll;
  })();

  Object.keys(breakpointsBrand).forEach(function (key) {
    breakpointsBrand[key] += scrollBarWidth;
  });

  // adjust navbar menu visibility and dynamic brand length/visibility
  $('#navbarMenuButton').on('click', () => {
    $('#navbarCollapse').slideToggle();
  });

  function adjustNavbar() {
    const windowWidth = $(this).width();
    const $navbarBrand = $('.navbar-brand');
    const $navbarCollapse = $('#navbarCollapse');

    if (windowWidth < 992) {
      $navbarCollapse.hide();
    } else {
      $navbarCollapse.css('display', 'inline');
    }

    if (windowWidth < breakpointsBrand['min']) {
      $navbarBrand.hide();
    } else if (windowWidth < breakpointsBrand['full']) {
      $navbarBrand.css('display', 'inline').text('M. C.').removeClass('brand');
    } else {
      $navbarBrand
        .css('display', 'inline')
        .text('McCarthy Code')
        .addClass('brand');
    }
  }

  $(window).on('resize orientationchange', adjustNavbar);
  adjustNavbar();
});
