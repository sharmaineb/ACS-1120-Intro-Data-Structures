"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from markov import Markov

app = Flask(__name__)

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    source_text = "./data/b99.txt"
    markov = Markov(source_text)
    sentence = markov.sentence(15)
    
    return render_template("index.html", sentence=sentence)


if __name__ == "__main__":
    app.run(debug=True)
