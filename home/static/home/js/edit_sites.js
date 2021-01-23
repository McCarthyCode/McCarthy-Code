$(() => {
  $('#toggle_screenshots').on('click touchend', function (event) {
    event.preventDefault();

    const $this = $(this);
    const $span = $this.children('span');
    const $i = $this.children('i');
    const $screenshotList = $('.screenshot-list');

    $screenshotList.slideToggle(500, function () {
      $span.text($screenshotList.is(':visible') ? 'Hide' : 'Show');
      $i.toggleClass(['fa-chevron-up', 'fa-chevron-down']);
    });
  });
});
