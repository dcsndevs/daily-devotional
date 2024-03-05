# ![Haven-church](documentation/haven-church-home.png)

## Welcome,
Haven Daily devotional is a product of Haven Church. The devotional is a source of spiritual enrichment for Christians. Aside from daily devotional, the website features a bible app, an event registration platform and a social page for connecting with other registered and profiled members.
 

The link to the deployed site can be found [Here](https://devotional-db11bc3466f9.herokuapp.com/)


## User Stories

### First-Time Visitor Goals: 
As a first-time visitor, the goals are:

- Read current and archived devotionals
- Comment on devotionals
- View upcoming events
- Register for an event
- Register as a basic user
- Contact the church through the website

### Member Goals: 
As a member, the goals are:
- Read current and archived devotionals
- Comment on devotionals
- Like a devotional and comments from others
- View upcoming events
- Register for an event
- Register as a basic user
- Become a member by creating my profile
- View profiles of other members
- View and study the Holy bible
- Contact the church through the website

### Admin/Owner Goals: 
As an admin, the goals are:
- Create devotionals and assign dates that they become active
- Create events and assign important dates and slots to it
- Approve new user registration
- Suspend/delete user profiles and accounts
- Delete comments from posts


## Logic Flowchart 
# ![Flowchart](documentation/flowchart.png)

## Entity Relationship Diagram (Models)
# ![Raw ERD](documentation/erd.png)

## Features 
# ![Main Menu](documentation/main-menu.png)

### Main Menu:
The app utilizes student names as usernames, ensuring a personalized experience.

- **Select Options:**
  - Press `1` to view existing students.


## Testing
Rigorous manual testing was performed to ensure the app's functionality, including user inputs, menu navigation, and responsiveness across screens.



### Manual Testing: 
| Feature | Key Action | Expected Result | Tested | Passed | Comments |
| --- | --- | --- | --- | --- | --- |
| *Main Menu Option 1* |  |  |  |  |  |
|Welcome|Enter 1|Select existing students|Yes|Yes|
|Welcome to Student Portal |Enter Student Name|Menu Options for student|Yes|Yes|
|Input New Record|Enter 1|Welcome to Student's Care Progress|Yes|Yes| |
|Enter Health Progress Value |Enter 0 - 10 value|Opens Education input |Yes|Yes| |
|Enter Education Progress Value |Enter 0 - 10 value|Accepts values and upload |Yes|Yes| |
|View Student Overall Progress|Enter 2|Student progress Displayed successfully|Yes|Yes|
|Rename Student Name |Enter 3 > Enter New name| Name successfully renamed|Yes|Yes|
|Delete Student Name & Record|Enter 4 > Confirm Y or N |Type Student's Name > Successfully delete|Yes|Yes|
| *Main Menu Option 2* |  |  |  |  |
|Create a new student|Enter 2|Input prompt > New student name created.|Yes|Yes|
| *Main Menu Option 3* |  |  |  |  |
|View program instructions|Enter 3|Programme Instruction displayed|Yes|Yes|
|Return to Main menu|Enter 'm' or any key| Return to main menu|Yes|Yes|
|Exit|Enter 'exit' from any input box|The application exits|Yes|Yes|
|     |     |     |     |     |   

## Bugs:
| Issue|Solution |
|-|-|
| The profile pictures of users who uploaded images through their Iphones was not showing. The was because Apples image extension is different from what was expected.|After researching cloudinary's website, I learnt about the CloudinaryImage class. It enabled me to convert any image format to jpg before storing to the database|

### CI Python Linter:
The CI Python Linter https://pep8ci.herokuapp.com/ was used to test for errors in the code. All codes were then formatted by following the software's recommendation.

### W3 Validator:
The W3 validator was used to check errors and all found errors were correct. There were however warnings concerning text with the "article" elements on the devotional pages and programmes page. The warning advised on the use of headings (h2-h6) to write the articles.



## Technologies used:
- [Django](https://docs.djangoproject.com/) is the web framework that was used to manage this project.
- [Python](https://python.org) is the main technology used in this application
- [Lucid](https://lucid.com) was used to create workflows for guidance in building the application
- [VScode](https://vscode.com/) was used to write and edit the codes and host the site on my local  computer
- [Git](https://github.com) was used for the version control of the application
- [Heroku](https://heroku.com) was used to host the deployed application
- [ChatGPT](https://chat.openai.com/) was often consulted regarding the usage and construction of codes
- [Google Chrome](https://chrome.google.com/) Developer tool was often used to check issues arising from codes, responsiveness, and general testing.
- [Code Institute Python Linter](https://pep8ci.herokuapp.com/) was used to check code for any issues

## Deployment

The template for this app was generated from Code-Institute-Org/p4-template. The repository was cloned on a local VSCode machine and then stored/managed on GitHub. 

The Heroku git URl is https://git.heroku.com/devotional.git


The app was then deployed on Heroku via Github:

1. Heroku Account Setup:

    Log in to your existing Heroku account or create a new account.

2. Create a New App:

    On the Heroku dashboard, click "New" and select "Create new app."

3. Configure Your App:

    Choose a unique app name and select your preferred region.
    Click "Create app" to initiate the app creation process.

4. Environment Configuration:

    In the app dashboard, find the "Settings" tab and locate "Config Vars."
    Click "Reveal Config Vars" and add a new variable with the key "PORT" and the value "8000." Click "Add" to save.

5. Set Up Buildpacks:

    Scroll down to the "Buildpack" section in the settings.
    Click "Add," select "Python," and add it. Ensure that "Python" is listed first.
    Repeat the process, this time adding "Node.js" as a build pack.

6. Deploy Your App:

    Navigate to the "Deploy" tab at the top of the dashboard.
    Choose GitHub as your deployment method and link your repository to the app.

7. Automatic or Manual Deployment:

    Scroll down to the deployment section.
    Choose either "Enable Automatic Deploys" for continuous integration or "Manual Deploy" for manual control.

Deployed site -> [Here](https://devotional-db11bc3466f9.herokuapp.com/)


### Local Deployment:
To clone this project, you can do so using VsCode or any code editor that has an integrated development Environment (IDE), using this command: 

1. Clone the repository: `git clone https://github.com/your-username/daily-devotional.git`
2. Install dependencies: `pip install -r requirements.txt`



## Requirements and Dependencies

- [Requirements](https://github.com/dcsndevs/daily-devotional/blob/main/requirements.txt)


## Usage

Follow the on-screen prompts to navigate through the application. Input valid data as guided by the application.

## Future Development and Limitations
More functionalities would be handy in this application. Extra functionality to include, manually determining the period of time that a student's overall progress should be populated. It would also go further to include exporting this information to a local machine or sending it to a user provided email address.


## Credits

### Code Institute:
Special thanks to Code Institute for providing the template used in this project. The template served as a valuable foundation, streamlining the development process and contributing to the overall project structure and theref after deployment.

### Google:
The Care Plus App relies on Google Cloud services, including the Google Sheets API, for efficient data management. I extend my gratitude to Google Cloud for providing a free, robust and reliable cloud solutions that contribute to the functionality of this application.

### API: 
Also to the team that created the Gspread and its documentation, and to Google Drive and Google Sheets API. The Care Plus App utilizes the gspread library to interact with the Google Sheets API for efficient data management. We appreciate the developers of gspread for providing a convenient and Pythonic way to work with Google Sheets.

### Code Reference:
[W3schools](https://w3schools.com/) was instrumental to the success of this project. It was often used to learn quick features or to compare and see where errors are.

### CarePlus Logic: 
The logic behind the application is a real life application called [©WellTree] (https://www.welltree.info/)
WellTree inputs are manually done on an excel worksheet, but this application was built with the intention of automating the inputs and view student progress over time.

### Acknowledgments:
I like to thank [Juliia Konn](https://github.com/IuliiaKonovalova/), my mentor at Code Institute. She exemplifies her mentorship with a knack for high-quality projects. Her desire for quality has always challenged me to do better in my work. I remain grateful to her.

I also like to thank my loving wife for her continuous support. She's a source of strength as always.