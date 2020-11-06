__author__ = 'aovolkov'
from sentiment_classifier import SentimentClassifier
from codecs import open
import sys
import time
from flask import Flask, render_template, request
app = Flask(__name__)

print("Preparing classifier")
start_time = time.time()
classifier = SentimentClassifier()
print("Classifier is ready")
print(time.time() - start_time, "seconds")

@app.route("/sentiment-demo", methods=["POST", "GET"])
def index_page(text="", prediction_message=""):
    if request.method == "POST":
        text = request.form["text"]
    logfile = open("demo_logs.txt", "a", "utf-8")
    print(text)
    old_stdout = sys.stdout
    sys.stdout = logfile
    print("<response>")
    print(text)
    prediction_message = classifier.get_prediction_message(text)
    print(prediction_message)
    print("</response>")
    logfile.close()
    sys.stdout = old_stdout
    return render_template('demo.html', text=text, prediction_message=prediction_message)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
