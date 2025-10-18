# cat gpt v1
import random as rm
from flask import Flask, render_template, request

app = Flask(__name__)

puncs = ["?", "!", ".", "..."]
breaks = [",", ";", "-"]
words = ["meow", "mew", "meooowww", "hiss", "purr", "yowl"]

def word():
    w = words[rm.randint(0,5)]
    return w

def sec(n):
    return " ".join(word() for _ in range(n))

def cat_reply():
    start = word().capitalize()
    s1 = sec(rm.randint(1,6))
    b = breaks[rm.randint(0,2)]
    s2 = sec(rm.randint(1,6))
    punc = puncs[rm.randint(0,3)]

    return(f"{start} {s1}{b} {s2}{punc}")

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    if request.method =="POST":
        user_message = request.form.get("user_input")
        if user_message and user_message.lower() != "exit":
            response = cat_reply()
        else:
            response = "Purr..."

    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)