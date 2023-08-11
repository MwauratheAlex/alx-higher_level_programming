$('#toggle_header').on('click', () => {
  const hdr = $('header');

  if (hdr.hasClass('red')) {
    hdr.removeClass('red');
    hdr.addClass('green');
  } else {
    hdr.removeClass('green');
    hdr.addClass('red');
  }
});
