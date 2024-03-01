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

// Initialize tooltips
$(document).ready(function(){
    $('[data-bs-toggle="tooltip"]').tooltip();
});