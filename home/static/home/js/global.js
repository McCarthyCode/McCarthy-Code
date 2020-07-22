$(document).ready(() => {
  // external link icon
  $('a.external-link')
    .after(' <i class="fas fa-external-link-alt" title="External Link"></i>');

  // navbar menu
  const breakpointMd = 768;

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

  // textarea character counter
  $('textarea').each(function () {
    const maxlength = $(this).attr('maxlength');
    const currentLength = $(this).val().length;

    $(this).after($('<small>').html(`${currentLength}/${maxlength}`));
  });

  $('textarea').on('input', function () {
    const maxlength = $(this).attr('maxlength');
    const currentLength = $(this).val().length;

    $(this).next('small').html(`${currentLength}/${maxlength}`)
  });
});
