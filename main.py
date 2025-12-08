from flask import Flask
from flask import render_template
from flask import request
import database_interface as db
import database_ORM_interface as dbORM

# Global variables
is_logged_in = False

# Create an instance of the Flask class in the app variable
app = Flask(__name__)

# Define the route for the index page at domain root
@app.route("/", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def index_page():
    global is_logged_in

    # If a post method, attempt to log them in
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        is_logged_in = db.check_login(email, password)
        if is_logged_in:
            app.logger.critical(f"{email} has logged in")
        else:
            app.logger.critical(f"{email} has failed to log in")

    # If a get method, reset to log them out
    else:
        is_logged_in = False
    return render_template("index.html", is_logged_in=is_logged_in), 200


# Define the route for the display page
@app.route("/display.html", methods=["GET"])
def display_page():
    data = db.listExtension()
    return render_template("display.html", content=data), 200

# Define the route for the display ORM page
@app.route("/displayORM.html", methods=["GET"])
def display_ORM_page():
    data = dbORM.listExtensionORM()
    return render_template("displayORM.html", content=data), 200

# Define the route for the arguments page
@app.route("/arguments.html", methods=["GET"])
def arguments_page():
    pageVer = request.args.get("ver", "default")
    return render_template("arguments.html", pageVersion=pageVer), 200

# Initialise the Flask application
if __name__ == "__main__":
    app.run(debug=True)

