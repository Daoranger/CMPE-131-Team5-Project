## <remove all of the example text and notes in < > such as this one>

## Functional Requirements
1. Login User Account
2. Register for An Account
3. User Authentication via Email
4. User Profile Management 
5. requirement
6. requirement
7. requirement
8. requirement
9. requirement
10. requirement
11. requirement
12. requirement
13. requirement
14. requirement

<using the syntax [](images/ui1.png) add images in a folder called images/ and place sketches of your webpages>

## Non-functional Requirements
1. Support Multiples Languages
2. Contact Information/Feedback options

<each of the 14 requirements will have a use case associated with it>
## Use Cases <Add name of who will write (this specific requirement) and implement (in subsequent milestones) the use case below>
1. User Register for An Account (Hoang Nguyen)
- **Pre-condition:** <can be a list or short description>
  + User don’t have an account yet
  + User has access to registration process
- **Trigger:** <can be a list or short description>
  + User initiates the registration process
- **Primary Sequence:**
1. User accesses the registration page
2. User filled in their personal information (email, username, password, phone number)
3. User click register button
4. System validates the provided information
5. If the information is valid, create new user account with those information
6. A confirmation message showed after click register button 
- **Primary Postconditions:** <can be a list or short description>
  + User can now sign in with their new account
  + User have to go to the login page to sign in
- **Alternate Sequence 1:** <you can have more than one alternate sequence to
describe multiple issues that may arise and their outcomes>
1. The information provided is invalid
2. User re-enter the correct information (whatever was invalid)
3. User resubmit the registration form
- **Alternate Sequence 2:** <you can have more than one alternate sequence to describe multiple issues that may arise>
1. There is already an account with the email address user provided
2. Ask the user to login instead
- **Alternate Sequence 3:**
1. There is already an account with the username user chose
2. Ask the user to choose a different username
___________________________________________________________________________________________________________________________________________
5. Function to add an image to notes (Andre Nassar)
- **Pre-Condition:**
  + The user is logged in into the system and has the permissions to edit and add an image within their notes
- **Trigger:** The user selects or clicks a specific icon or button within the user interface to add an image to their notes or text
- **Primary Sequence:**
1. The user navigates to the text box that they want  to add an image to
2. The user clicks a symbol that is identified as an image symbol in the text editor
3. The interface then opens their file manager which allows the user to select a file or image  to   the desired repository
4. The user selects the image they want to upload and the system accepts the request as long as it is the correct file type, such as PNG, PDF, etc
5. The interface/system then uploads the image to the server
6. When the image is uploaded to the server the user will be allowed to see a preview of what they upload into the text box
7. This will then allow the user to adjust the dimensions of their image before uploading
8. The user will then press a confirmation button which then allows the system to insert the image into the text box
- **Primary Postconditions:** 
  + User can now type in their text box and move the image where it is needed
- **Alternate Sequence 1:** 
1. User upload a file type that is not allowed
2. Prompt user to upload allowed file type
- **Alternate Sequence 2:** 
1. Users image is too large to input into their text box
2. Users image is too large to input into their text box



