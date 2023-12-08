# Noted!
## Team 5: [Team Lead] Hoang Nguyen (@Daoranger), Aadarsh Marahatta (@amarahatta), Evan Nishi (@Evan-Nishi), Andre Nassar (@Andrenassar)

Noted! is a website that helps individuals create notes and to-do lists for themselves. Users can register for an account, log in with Google Authentication, and edit their user profile. The website’s main features include the ability to create, edit, and delete multiple notes and to-do list tasks.

When creating a note, users can add a title and a description. Users can edit and delete their notes at any time.

For the to-do list, users can create tasks and mark them as complete or incomplete. They can also delete tasks that are no longer needed. The website allows users to reset their to-do list to start fresh with a new empty list. 

Noted! is a great tool for anyone who wants to stay organized and keep track of their tasks and notes all in one place. It’s easy to use and has a clean and simple interface that makes it easy to navigate. Give it a try and let us know what you think!

# Table of Contents
- [Steps to Run the Website](#steps-to-run-the-website)
- [Contribution](#milestone-2-contribution)
- [Video Presentation](#video-presentation)
- [Snapshots](#snapshots)
- [References](#references)

### Purposes

The purposes of this project is to put into practice what we've learned in the CMPE-131: Software Engineering course by building a website. We're using Python, Flask, HTML, and SQLAlchemy to create it. Flask helps with the behind-the-scenes stuff, HTML is for how it looks, and SQLAlchemy manages the database. The aim is to bring all these pieces together smoothly to make a functional and well-designed website. 

Moreover, in addition to building the website, our project aims to enhance our understanding of crucial tools and concepts in software engineering. This includes gaining proficiency in Linux commands for efficient system management, utilizing GitHub for version control, and mastering Git for collaborative development. By incorporating these skills, we aim to cultivate a comprehensive understanding of the broader software engineering ecosystem, preparing ourselves for real-world applications and collaborative software development practices.

### Goals and Intended Usage

Our goal is to create a website that allow user to use it as an application that would help create note and todo-list. Our targeted audience range from students to adults to anyone who need a free and simple application that would help them store their important notes and create a list for their tasks. Morever, the website should have many features that allow user to have control customization over their account like any other baisc websites. The main goals of this website are provide users a free, simple, reliable and secure website.

### Functionality and User Operations

1. Main
  * Register: Users can register a new account with a username, password, and email. This feature is essential for creating a personalized experience for users.
  * Login: Users are able to log in to their account and manage their notes. This feature allows users to access their notes from any device and keep them secure.
  * Logout: Users can log out of their account. This feature ensures that users’ accounts are secure and that they are not accidentally logged in to their account on a public device.
  * Edit profile: Users can edit their account to change their username and password. This feature allows users to customize their account and keep their information up-to-date.
  * Contact us: Users can contact developers with feedback or any issues. This feature provides a way for users to get help when they need it and provide feedback to improve the app.
2. Notes
  * Create Note:  Users can create a note. This feature allows users to jot down ideas, thoughts, and reminders.
  * Delete Note:  Users can delete a note. This feature allows users to remove notes that are no longer needed.
  * Edit Note: Users can edit a note. This feature allows users to modify notes that need to be updated.
  * Create note form file:  Users can create a note from a file. This feature allows users to import notes from other sources.
  * View note page: Users can view a note page. This feature allows users to see all the details of a note in one place.
3. To-do List
  * Add task: Users can add a task. This feature allows users to keep track of things they need to do.
  * Delete task: Users can delete a task. This feature allows users to remove tasks that are no longer needed.
  * Mark task:  Users can mark a task as complete. This feature allows users to keep track of what they have accomplished and what they need to complete.
  * Reset todo list: Users can reset the to-do list. This feature allows users to start fresh with a new to-do list.


### Steps to Run the Website
1. Create a clone repo of our website
   * Install all the librabries including python3, flask, etc
   * Create a virtual envieronment and installed all the requirements from our requirements.txt file
2. Open your choice of open source operating system (recommended Ubuntu)
   * CD into the CMPE-131-Team5-Project directory
   * Run the website by typing: python3 run.py (note if it is not working that mean you haven't install all the requirements)
   * The system will give you the link to our website
   * Use any web browser (recommended Chrome) to launch the website using the link
3. Create your first account and explore!

### Milestone 2 Contribution 
* Hoang worked on:
  * Login, Register/Create an Account, Logout, Edit User Profile (username OR password), Contact Us (user send a gmail to the developer gmail)
* Evan worked on:
  * Note features (create/edit/delete), Database functions
* Aadarsh worked on:
  * To-do list features (create/delete/marking/reset)
* Andre worked on:
  * Proposing Requirements


### Milestone 3 Contribution 
* Evan worked on:
  * Create note from file, view note page
 
### Video Presentation
https://drive.google.com/file/d/1ZhYlfpNtDpuc4CYg7VwsJqp6m1b8HS8c/preview

### Snapshots
Registar Page:
<img width="1000" alt="Screenshot 2023-11-29 at 9 06 18 PM" src="https://github.com/Daoranger/CMPE-131-Team5-Project/blob/2dc47724ecde4a7455b34b0fa0fc29998eaeba3b/snapshots/createaccount.png">

Login Page:
<img width="1000" alt="Screenshot 2023-11-29 at 8 59 44 PM" src="https://github.com/Daoranger/CMPE-131-Team5-Project/blob/main/snapshots/login.png">

Home Page:
<img width="1000" alt="Screenshot 2023-11-29 at 9 04 47 PM" src="https://github.com/Daoranger/CMPE-131-Team5-Project/blob/main/snapshots/Dashboard.png">

Creating a Note:
<img width="1000" alt="Screenshot 2023-11-29 at 9 07 57 PM" src="https://github.com/Daoranger/CMPE-131-Team5-Project/blob/2dc47724ecde4a7455b34b0fa0fc29998eaeba3b/snapshots/createnote.png">

Search a Note:
<img width="1000" alt="Screenshot 2023-11-29 at 9 07 57 PM" src="https://github.com/Daoranger/CMPE-131-Team5-Project/blob/2dc47724ecde4a7455b34b0fa0fc29998eaeba3b/snapshots/search.png">

To Do List:
<img width="1000" alt="Screenshot 2023-11-29 at 9 05 33 PM" src="https://github.com/Daoranger/CMPE-131-Team5-Project/blob/2dc47724ecde4a7455b34b0fa0fc29998eaeba3b/snapshots/todo.png">

Edit Profile Page:
<img width="1000" alt="Screenshot 2023-11-29 at 9 06 18 PM" src="https://github.com/Daoranger/CMPE-131-Team5-Project/blob/2dc47724ecde4a7455b34b0fa0fc29998eaeba3b/snapshots/editprofile.png">

Contact Us Page:
<img width="1000" alt="Screenshot 2023-11-29 at 9 06 18 PM" src="https://github.com/Daoranger/CMPE-131-Team5-Project/blob/2dc47724ecde4a7455b34b0fa0fc29998eaeba3b/snapshots/contact.png">

Logout:
<img width="1000" alt="Screenshot 2023-11-29 at 9 07 00 PM" src="https://github.com/Daoranger/CMPE-131-Team5-Project/assets/35211839/072306b1-3af1-4d55-8290-a4bc9a0af491">



### References
[1] https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login

[2] https://www.techwithtim.net/tutorials/flask

[3] https://www.geeksforgeeks.org/sending-emails-using-api-in-flask-mail/

