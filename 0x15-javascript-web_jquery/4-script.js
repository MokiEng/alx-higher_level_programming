// Include jQuery in your HTML before using this script

$(document).ready(function() {
  // Attach a click event handler to the <div> element with id "toggle_header"
  $('div#toggle_header').click(function() {
    // Toggle the "red" and "green" classes of the <header> element
    $('header').toggleClass('red green');
  });
});
