$(document).ready(() => {
  // external link icon
  $('a.external-link')
    .after('<i class="fas fa-external-link-alt" title="External Link"></i>');

  // navbar menu
  $('#navbarMenuButton').click(() => {
    $('#navbarCollapse').slideToggle();
  });
  $(window).on('resize orientationchange', () => {
    if ($(this).width() >= breakpointMd) {
      $('#navbarCollapse').css('display', 'inline');
    } else {
      $('#navbarCollapse').hide();
    }
  });
});
