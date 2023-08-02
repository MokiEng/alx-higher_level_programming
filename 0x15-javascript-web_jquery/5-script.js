// Include jQuery in your HTML before using this script

$(document).ready(function() {
  // Attach a click event handler to the <div> element with id "add_item"
  $('div#add_item').click(function() {
    // Create a new <li> element
    var newItem = $('<li>Item</li>');
    
    // Append the new <li> element to the <ul> with class "my_list"
    $('ul.my_list').append(newItem);
  });
});
