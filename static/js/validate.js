    // Wait for the page to load before running the JavaScript
    document.addEventListener('DOMContentLoaded', function() {
        // Get the form and submit button
        const form = document.querySelector('form');
        const submitBtn = getElementById('#submit-btn');

        // Disable the submit button initially
        submitBtn.disabled = true;

        // Add event listeners to each form input/select element
        const inputs = form.querySelectorAll('input, select, textarea');
        inputs.forEach(function(input) {
            input.addEventListener('change', function() {
                // Check if all inputs are valid
                let valid = true;
                inputs.forEach(function(input) {
                    if (!input.value) {
                        valid = false;
                    }
                });

                // Enable/disable submit button based on input validity
                if (valid) {
                    submitBtn.disabled = false;
                } else {
                    submitBtn.disabled = true;
                }
            });
        });
    });

