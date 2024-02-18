const editButtons = document.getElementsByClassName("btn-edit");
const profileText = document.getElementById("id_body");
const profileForm = document.getElementById("MembershipForm");
const submitButton = document.getElementById("submitButton");

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated profile's ID upon click.
* - Fetches the content of the corresponding profile.
* - Populates the `profileText` input/textarea with the profile's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_profile/{profileId}` endpoint.
*/
for (let button of editButtons) {
  button.addEventListener("click", (e) => {
    let profileId = e.target.getAttribute("owner_id");
    let profileContent = document.getElementById(`profile${profileId}`).innerText;
    profileText.value = profileContent;
    submitButton.innerText = "Update";
    profileForm.setAttribute("action", `edit_profile/${profileId}`);
  });
}

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated profile's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific profile.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
      let profileId = e.target.getAttribute("profile.id");
      deleteConfirm.href = `delete_member/${profileId}`;
      deleteModal.show();
    });
  }