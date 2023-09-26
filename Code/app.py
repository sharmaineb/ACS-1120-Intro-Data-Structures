"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template



app = Flask(__name__)



@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""



    return render_template("index.html")

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)