from flask import Flask, render_template
import random as r

app = Flask(__name__)


def read_word():
    rand = r.randint(0, 34009)
    word = ""
    file = open("word_rus.txt", encoding="UTF8")
    for i, line in enumerate(file):
        if i == rand:
            word = line
    file.close()
    return word.rstrip('\n')


def scramble_word(word):
    l = list(word)
    r.shuffle(l)
    return "".join(l)


@app.route('/')
def hello_world():
    word = read_word()
    scrable = scramble_word(word)
    result = {"word": word, "scramble": scrable}
    return render_template("index.html", result=result)
