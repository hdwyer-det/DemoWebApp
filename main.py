from flask import Flask
from flask import render_template
from flask import request

# Global variables
is_logged_in = False

# Create an instance of the Flask class in the app variable
app = Flask(__name__)

# Define the rout for the index page at domain root
@app.route("/", methods=["GET", "POST"])
def index_page():
    global is_logged_in
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        is_logged_in = True
        app.logger.critical(f"{email} has logged in")
    else:
        is_logged_in = False
    return render_template("index.html", is_logged_in=is_logged_in), 200

# Initialise the Flask application
if __name__ == "__main__":
    app.run(debug=True)

