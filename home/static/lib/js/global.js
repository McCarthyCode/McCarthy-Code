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
