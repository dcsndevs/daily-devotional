// Get all elements with the class "commentfocus"
var linkElements = document.querySelectorAll(".commentfocus");

// Add event listener to each link element
linkElements.forEach(function(linkElement) {
    linkElement.addEventListener("click", function(event) {
        event.preventDefault(); // Prevent the default behavior of the link
        // Find the textarea input with the id "id_body"
        var commentInput = document.getElementById("id_body");
        commentInput.focus(); // Focus on the textarea input
    });
});

// Initialize tooltips to guide users
$(document).ready(function(){
    $('[data-bs-toggle="tooltip"]').tooltip();
});

// Function to automatically close Django messages after 5seconds
function closeMessages() {
    setTimeout(function() {
        document.querySelectorAll('.alert').forEach(function(message) {
            message.remove();
        });
    }, 5000); // Adjust the duration (in milliseconds) as needed
}

window.onload = function() {
    closeMessages();
};