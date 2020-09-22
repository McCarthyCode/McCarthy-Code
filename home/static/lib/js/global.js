$(() => {
  // external link icon
  $('a.external-link').after(
    ' <i class="fas fa-external-link-alt" title="External Link"></i>',
  );

  // adjust .navbarBrand breakpoints with scrollbar
  const breakpointsBrand = {
    min: 308,
    full: 403,
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
      $navbarBrand.css('display', 'inline').attr('data-content', 'M. C.');
    } else {
      $navbarBrand
        .css('display', 'inline')
        .attr('data-content', 'McCarthy Code');
    }
  }

  $(window).on('resize orientationchange', adjustNavbar);
  adjustNavbar();

  // textarea character counter
  $('textarea').each(function () {
    const $this = $(this);
    const currentLength = $this.val().length;
    const maxlength = $this.attr('maxlength');

    if ($this.is(':visible')) {
      const $div = $('<div>');
      const $small = $('<small>').html(`${currentLength}/${maxlength}`);

      $this.after($div.append($small));
    }
  });

  $('textarea').on('input', function () {
    const $this = $(this);
    const $small = $this.next('div').children('small');
    const currentLength = $this.val().length;
    const maxlength = $this.attr('maxlength');

    $small.html(`${currentLength}/${maxlength}`);
  });
});
