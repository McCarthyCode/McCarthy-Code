$(document).ready(() => {
  const navHeight = $('#navbar').outerHeight();

  // scroll buttons
  $('#portfolio > section:not(:last-of-type)').each(function () {
    let $next = $(this).next();

    $(this).find('.chevron i').click(function () {
      $('html, body').animate({
        scrollTop: $next.offset().top - navHeight,
      }, 1000);
    });
  });

  // resize sections
  function resizeSections() {
    $('section').each(function () {
      const $this = $(this);
      const $container = $this.find('.container');

      const mobileHeight = $this.find('.mobile').outerHeight();
      const desktopHeight = $this.find('.desktop').outerHeight();

      const maxHeight = Math.max(mobileHeight, desktopHeight);

      $this.css('height', maxHeight + 32 + 64);
      $container.css('height', maxHeight + 32);
    });
  };

  resizeSections();
  $(window).on('resize orientationchange', resizeSections);
});
