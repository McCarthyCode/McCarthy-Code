$(document).ready(() => {
  let keys = [...Array(5).keys()];
  keys.splice(0, 1);

  const navHeight = $('#navbar').outerHeight();

  keys.forEach(index => {
    $(`section:nth-child(${index}) .chevron i`).click(() => {
      $('html, body').animate({
        scrollTop: $(`section:nth-child(${index + 1})`).offset().top - navHeight,
      }, 1000);
    });
  });
});
