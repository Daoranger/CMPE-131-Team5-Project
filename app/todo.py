from flask import Flask, flash,render_template,redirect,request,redirect,session,url_for
from flask_sqlalchemy import SQLAlchemy
from app import db
from app import myapp_obj
from app import routes

# Define the Todo class to creat the todo list
class Todo(db.Model):
    task_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

# Base method that show the todo list with the template
@myapp_obj.route('/todo')
def home():
    # Check if the user is logged into ther account before accessing the list otherwise redirect them to login.
    if 'user_id' not in session:
        flash('Please login before viewing the to-do list')
        return redirect('/login')
    # Get the to do list task form the database
    todo_list = Todo.query.all()
    # Render the todo.html template
    return render_template('todo.html', todo_list = todo_list)

# Add method that adds a task to the todo list
@myapp_obj.route('/add', methods=['POST'])
def add():
    # Check if the user is logged into their account before adding a task to the list otherwise redirect them to login.
    if 'user_id' not in session:
        flash('Please log in before adding a task')
        return redirect('/login')
    #Get the task name form the form
    name = request.form.get("name")
    # Check if the name is empty ie. the user hasnt written a task. If yes than show the flash message.
    if not name:
        flash("Must enter a task!")
        return redirect(url_for("home"))
    else: 
        # Create a new todo task object
        new_task = Todo(name = name, complete = False)
        #Adds and commits the tasks the user made into the database
        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for("home"))

# Change the update value on the todo list so either incomplete or complete
@myapp_obj.route('/update/<int:todo_id>')
def update(todo_id):
    # Check if the user is logged into their account before updating a task on the list otherwise redirect them to login.
    if 'user_id' not in session:
        flash('Please login before updating a task')
        return redirect('/login')
    # Get the task form the database
    todo = Todo.query.get(todo_id)
    # This updates the status of the todo list task then the commit is what actually updates it in the database
    todo.complete = not todo.complete
    db.session.commit()

    return redirect(url_for("home"))

# Delete a task from the todo list
@myapp_obj.route('/delete/<int:todo_id>')
def delete(todo_id):
    # Check if the user is logged into ther account before deleting a task from their list otherwise redirect them to login.
    if 'user_id' not in session:
        flash('Please login before deleting a task')
        return redirect('/login')
    # Get the todo list task form the database
    todo = Todo.query.get(todo_id)
    #delete the task form the database and then commit the change to the database
    db.session.delete(todo)
    db.session.commit()

    return redirect(url_for("home"))

#Reseting the todo list by deleting all the tasks
@myapp_obj.route('/delete_all', methods=['POST'])
def delete_all():
    # Check if the user is logged into ther account before deleting all tasks from the list otherwise redirect them to login.
    if 'user_id' not in session:
        flash('Please login before deleting all tasks')
        return redirect('/login')
    # Delete all the tasks using the object not just one using the id. Then commmit the change to the database.
    Todo.query.delete()
    db.session.commit()
    # Dispaly a flash message indicating to the user that all tasks are deleted
    flash("All tasks deleted successfully!")
    
    return redirect(url_for("home"))