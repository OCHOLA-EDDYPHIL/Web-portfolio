//$(document).ready(function() {
//  $('#my-form').on('submit', function(event) {
//    event.preventDefault(); // Prevent default form submission behavior
//
//    // Display the loading screen
//    $('#loading-screen').show();
//
//    // Send the form data to the server
//    $.ajax({
//      url: '/send-email/', // Replace with your server-side endpoint
//      method: 'POST',
//      data: $(this).serialize(),
//      success: function(response) {
//        // Update the loading screen with the success message
//        $('#loading-screen').html('<p>Email sent successfully!</p>');
//
//        // Hide the loading screen after 3 seconds
//        setTimeout(function() {
//          $('#loading-screen').hide();
//        }, 3000);
//      },
//      error: function() {
//        // Update the loading screen with the error message
//        $('#loading-screen').html('<p>Error sending email.</p>');
//
//        // Hide the loading screen after 3 seconds
//        setTimeout(function() {
//          $('#loading-screen').hide();
//        }, 3000);
//      }
//    });
//  });
//});
//$(document).ready(function() {
//  $('form').submit(function(event) {
//    event.preventDefault();
//
//    $.ajax({
//      type: 'POST',
//      url: '/submit_application/',
//      data: $('form').serialize(),
//      dataType: 'json',
//      success: function(data) {
//        if (data.status === 'success') {
//          $('#success-message').fadeIn();
//          setTimeout(function() {
//            $('#success-message').fadeOut();
//          }, 3000);
//        }
//      }
//    });
//  });
//});