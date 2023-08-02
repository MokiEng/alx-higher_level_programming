// Include jQuery in your HTML before using this script

$(document).ready(function() {
  // Attach click event handlers to the respective div elements

  // Add item to the list
  $('div#add_item').click(function() {
    $('ul.my_list').append('<li>Item</li>');
  });

  // Remove last item from the list
  $('div#remove_item').click(function() {
    $('ul.my_list li:last-child').remove();
  });

  // Clear the entire list
  $('div#clear_list').click(function() {
    $('ul.my_list').empty();
  });
});
