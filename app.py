from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime




# my app
app = Flask(__name__)
Scss(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasksDatabase.db"
db = SQLAlchemy(app)
# databse models
class Tasks(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(150), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    created = db.Column(db.DateTime, default = datetime.now)
    
    def __repr__(self) -> str:
        return f"Task {self.id}"
    
    
   
   
    
# homepage of my app
@app.route("/", method = ["POST","GET"])  # http methods to add task to db and get tasks from db
def index(): #homepage
    
    #add a task
    if request.method == "POST" :
        # gotta grab the task from 'form in index.html'
        grabbed_task = request.form["content"]
        task_to_be_sent = Tasks(task = grabbed_task)
        try:
            db.session.add(task_to_be_sent)
            db.session.commit()
        except Exception as e:
            print(f"ERROR : {e}")
            return f"ERROR : {e}"
        
    #get tasks
    else:
        tasks = Tasks.query.order_by(Tasks.created).all()
        return render_template("index.html", tasks = tasks)


if __name__ in "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)