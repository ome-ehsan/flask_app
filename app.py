from flask import Flask, render_template
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy


#my app
app = Flask(__name__)
Scss(app)



# homepage of my app
@app.route("/")
def index(): #homepage
    return render_template("index.html")


if __name__ in "__main__":
    app.run(debug=True)