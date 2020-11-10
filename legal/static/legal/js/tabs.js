$(() => {
  // show appropriate view based on document hash
  if (document.location.hash) {
    setTimeout(function () {
      window.scrollTo(0, 0);
    }, 1);
  }

  function updateTitle(href) {
    let title;
    const suffix = ' - McCarthy Code';

    switch (href) {
      case '#tos':
        title = 'Terms of Service' + suffix;
        break;
      case '#privacy':
        title = 'Privacy Policy' + suffix;
        break;
    }

    document.title = title;

    return title;
  }

  switch (document.location.hash) {
    case '':
    case '#':
      document.location.hash = '#tos';
    case '#tos':
      $('#tos').show();
      $('#tabs_tos').addClass('active');
      break;
    case '#privacy':
      $('#privacy').show();
      $('#tabs_privacy').addClass('active');
  }

  updateTitle(document.location.hash);

  // define tabs behavior
  let $activeTab = $('ul.tabs > li.active');
  const $tabs = $('ul.tabs');
  const $tabsChildren = $('ul.tabs > li');

  $tabsChildren.on('click touchstart', function (event) {
    event.preventDefault();
    event.stopPropagation();

    $tabsChildren.removeClass('active');
    const href = $(this).data('href');

    if (event.type === 'click') {
      $tabsChildren.removeClass('active').each(function () {
        $($(this).data('href')).hide();
      });

      $activeTab = $(this);
      $(href).show();
    } else {
      $(this).addClass('active');
    }

    const title = updateTitle(href);
    const path = `/legal/${href}`;
    history.pushState({ urlPath: path }, title, path);
  });

  $tabsChildren.on('touchend', function (event) {
    const changes = event.changedTouches[0];
    const $endElement = $(
      document.elementFromPoint(changes.pageX, changes.pageY),
    );

    if ($endElement.parent('.tabs').length) {
      $tabsChildren.removeClass('active').each(function () {
        $($(this).data('href')).hide();
      });

      $activeTab = $endElement;
      $endElement.addClass('active');
      $($endElement.data('href')).show();
      event.stopPropagation();
    }
  });

  $tabs.on('mouseenter', () => {
    $activeTab.removeClass('active');
  });
  $tabs.on('mouseleave', () => {
    $activeTab.addClass('active');
  });

  $(window).on('touchstart', function () {
    $activeTab.addClass('active');
  });
  $(window).on('touchend', function () {
    $tabsChildren.removeClass('active');
    $activeTab.addClass('active');
  });
});
