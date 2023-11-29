from flask import Flask, flash,render_template,redirect,request,redirect,session,url_for
from flask_sqlalchemy import SQLAlchemy
from app import db
from app import myapp_obj
from app import routes

class Todo(db.Model):
    task_id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

@myapp_obj.route('/todo')
def home():
    if 'user_id' not in session:
        flash('Please login before viewing the to-do list')
        return redirect('/login')
    todo_list = Todo.query.all()
    return render_template('todo.html', todo_list = todo_list)

@myapp_obj.route('/add', methods=['POST'])
def add():
    if 'user_id' not in session:
        flash('Please log in before adding a task')
        return redirect('/login')
    name = request.form.get("name")
    if not name:
        flash("Must enter a task!")
        return redirect(url_for("home"))
    else: 
        new_task = Todo(name = name, complete = False)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home"))

@myapp_obj.route('/update/<int:todo_id>')
def update(todo_id):
    if 'user_id' not in session:
        flash('Please login before updating a task')
        return redirect('/login')
    todo = Todo.query.get(todo_id)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("home"))


@myapp_obj.route('/delete/<int:todo_id>')
def delete(todo_id):
    if 'user_id' not in session:
        flash('Please login before deleting a task')
        return redirect('/login')
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("home"))

@myapp_obj.route('/delete_all', methods=['POST'])
def delete_all():
    if 'user_id' not in session:
        flash('Please login before deleting all tasks')
        return redirect('/login')
    Todo.query.delete()
    db.session.commit()
    flash("All tasks deleted successfully!")
    return redirect(url_for("home"))