$(document).ready(function() {
  // Attach a click event handler to the <div> element with id "update_header"
  $('div#update_header').click(function() {
    // Update the text of the <header> element to "New Header!!!"
    $('header').text('New Header!!!');
  });
});
