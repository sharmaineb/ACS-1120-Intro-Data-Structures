"""Main script, uses other modules to generate sentences."""
from flask import Flask, render_template
from markov import Markov


app = Flask(__name__)

source_text = "./data/b99.txt"
markov = Markov(source_text)
amount = 15

@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    sentence = markov.sentence(amount)

    context = {
        "sentence": sentence
    }
    
    return render_template("index.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
