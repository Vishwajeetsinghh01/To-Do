from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(app)

class Todo(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    task = DB.Column(DB.String(200), nullable=False)
    completed = DB.Column(DB.Boolean, default=False)

with app.app_context():
    DB.create_all()

@app.route('/')
def home():
    todos = Todo.query.all()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_task():
    task = request.form['task']

    new_task = Todo(task=task)

    DB.session.add(new_task)
    DB.session.commit()

    return redirect('/')

@app.route('/delete/<int:id>')
def delete_task(id):
    task = Todo.query.get(id)

    DB.session.delete(task)
    DB.session.commit()

    return redirect('/')

@app.route('/complete/<int:id>')
def complete_task(id):
    task = Todo.query.get(id)

    task.completed = not task.completed

    DB.session.commit()

    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)