document.addEventListener("DOMContentLoaded", function() {
    console.log("The website is loaded and ready!");

    // Example of a simple form validation
    const contactForm = document.getElementById('contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function(event) {
            const name = document.getElementById('name').value;
            if (!name) {
                alert("Please enter your name.");
                event.preventDefault(); // Prevent form from submitting
            }
            // Add more validations as needed
        });
    }
});

// Function to toggle visibility of elements
function toggleVisibility(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        element.style.display = element.style.display === 'none' ? 'block' : 'none';
    }
}

// Log a message when an important button is clicked
function logButtonClick(buttonId) {
    const button = document.getElementById(buttonId);
    button.addEventListener('click', function() {
        console.log(`${buttonId} was clicked`);
    });
}