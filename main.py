from flask import Flask
from flask import render_template
from flask import request
import database_interface as db

# Global variables
is_logged_in = False

# Create an instance of the Flask class in the app variable
app = Flask(__name__)

# Define the route for the index page at domain root
@app.route("/", methods=["GET", "POST"])
@app.route("/index.html", methods=["GET", "POST"])
def index_page():
    global is_logged_in
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        is_logged_in = db.check_login(email, password)
        if is_logged_in:
            app.logger.critical(f"{email} has logged in")
        else:
            app.logger.critical(f"{email} has failed to log in")
    else:
        is_logged_in = False
    return render_template("index.html", is_logged_in=is_logged_in), 200


# Define the route for the display page
@app.route("/display.html", methods=["GET"])
def display_page():
    return render_template("display.html"), 200


# Initialise the Flask application
if __name__ == "__main__":
    app.run(debug=True)

