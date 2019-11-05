$(document).ready(() => {
  $('a.external-link')
    .append(' <i class="fas fa-external-link-alt" title="External Link"></i>');
  
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
});
