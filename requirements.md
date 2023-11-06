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
___________________________________________________________________________________________________________________________________________
## ***1. User Register for An Account (Hoang Nguyen)***
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
___________________________________________________________________________________________________________________________________________


