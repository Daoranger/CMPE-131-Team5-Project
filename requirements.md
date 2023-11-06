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
### ***1. User Register for An Account (Hoang Nguyen)***
- **Pre-condition:** 
  + User don’t have an account yet
  + User has access to registration process
- **Trigger:** 
  + User initiates the registration process
- **Primary Sequence:**
1. User accesses the registration page
2. User filled in their personal information (email, username, password, phone number)
3. User click register button
4. System validates the provided information
5. If the information is valid, create new user account with those information
6. A confirmation message showed after click register button 
- **Primary Postconditions:** 
  + User can now sign in with their new account
  + User have to go to the login page to sign in
- **Alternate Sequence 1:** 
1. The information provided is invalid
2. User re-enter the correct information (whatever was invalid)
3. User resubmit the registration form
- **Alternate Sequence 2:** 
1. There is already an account with the email address user provided
2. Ask the user to login instead
- **Alternate Sequence 3:**
1. There is already an account with the username user chose
2. Ask the user to choose a different username
___________________________________________________________________________________________________________________________________________
***2. User Login to the Account (Hoang Nguyen)***
- **Pre-condition:** 
  + User had registered for an account and had one created
  + User has access to login process
- **Trigger:** 
  + User initiates the registration process
  + User go to login page
- **Primary Sequence:**
1. User access to the login page
2. User provided username/email and password
3. Give user option to check “remember me” box
4. User click login button
5. If information is valid, let user log in
- **Primary Postconditions:** 
  + User can now sign in with their new account
  + User have to go to the login page to sign in
- **Alternate Sequence 1:** 
1. User provide invalid login information
2. Prompt the user to re-enter
- **Alternate Sequence 2:** 
1. User forgot their password and used Forgot Password
2. User receive an email to reset password
3. User enter new password and successfully create new password
4. User should be able to login with new password
___________________________________________________________________________________________________________________________________________
***3. Authentication during Login via Email (Hoang Nguyen)***
- **Pre-condition:** 
  + User had registered for an account and had one created
  + User has an Email linked with the account
  + User has access to their email address 
  + User had logged in and have access to user setting
  + User is in the user authentication setting page
- **Trigger:** 
  + User choose to set up authentication 
- **Primary Sequence:**
1. User is in the set up authentication page
2. Prompt user to re-enter password for security reason
3. User re-enter password
4. If valid, the authentication form pop up
5. User confirm that they want to use the email they provided
6. Enable email-based authentication
- **Primary Postconditions:** 
  + User has successfully set up  their chosen email-based authentication
  + User get a email confirm that their authentication in set up
  + Whenever the user login now, an email with the security code will sent to them
- **Alternate Sequence 1:** 
1. User want to remove authentication
2. Ask to re-enter password
3. Prompt user if to confirm removal of authentication
4. Email-based authentication is removed.
- **Alternate Sequence 2:** 
1. User enter invalid password
2. User authentication form will not pop up
3. System ask user to re-enter until 3 tries
- **Alternate Sequence 3:**
1. User enter valid password
2. User authentication form pop up
3. User want to cancel to process
4. User click the cancel button
5. Close the authentication form
6. Bring user back to dashboard
___________________________________________________________________________________________________________________________________________
***4. User managing their user profile (Hoang Nguyen)***
- **Pre-condition:** 
  + User registered and logged into the account
  + User is in the dashboard and have access to user profile
- **Trigger:** 
  + User click on their user profile
- **Primary Sequence:**
1. User navigates to user profile editing page
2. User click edit profile button
3. Edit profile form pop up
4. User can now editing whatever information they want to change
5. User save changes that they made
6. If the changes are valid, user profile is update
7. Confirmation message that their profile had successfully updated
- **Primary Postconditions:** 
  + User profile had successfully updated with the changes
  + User can now view their updated profile
- **Alternate Sequence 1:** 
1. User edit their profile
2. User want to cancel their changes
3. Click cancel button, and nothing will be change
- **Alternate Sequence 2:** 
1. User changes their information
2. The changes are invalid
3. Prompt the user to enter following the requirements
4. The user can now re-enter the correct information
__________________________________________________________________________________________________________________________________________
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
___________________________________________________________________________________________________________________________________________
6. Search Note Functionality (Andre Nassar)
- **Pre-Condition:**
  + The user is logged in into the system and the search functionality is accessible on the interface
- **Trigger:** The user initiates the search function
- **Primary Sequence:**
1. The user selects the search function on the interface 
2. The user enters a keyword or term in the search function
3. The user enters the key phrase or word from the search function
4.  The system processes the search request
5. The system displays the results from the users input
6. The user can review the results they received in a list format
7. The user then clicks their desired result. 
- **Primary Postconditions:** 
  + User can now access the content they were searching for
- **Alternate Sequence 1:** 
1. If the user searches something that there isn't in the system the system will display a “no results” message
2. Depending on the search the system may tell you to refine your search or keywords
__________________________________________________________________________________________________________________________________________
7. Logout of User Account
- **Pre-Condition:**
  + The user is currently logged into their account
- **Trigger:** The user initiates the logout function.
- **Primary Sequence:**
1. The user selects the logout process by clicking on a logout option found in the navigation menu
2. The system receives the logout request and checks the user’s session and status
3. The system displays a confirmation message to the user informing them they have been successfully logged out
4. The user is directed back to the home page/ login page
- **Primary Postconditions:** 
  + User is logged out of the system and their account
  + User is redirected to the login page
- **Alternate Sequence 1:** 
1. The user is not active for a certain period of time, so their session is expired prompting to log the user out



