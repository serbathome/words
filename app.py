from flask import Flask, render_template, jsonify
import random as r

app = Flask(__name__)

# define global words dictionary
words = {}
words["easy"] = []
words["medium"] = []
words["hard"] = []

# load words
file = open("word_rus_short.txt", encoding="UTF8")
for i, word in enumerate(file):
    word = word.rstrip('\n')
    if len(word) <= 4:
        words["easy"].append(word)
    if len(word) >= 5 and len(word) <= 8:
        words["medium"].append(word)
    if len(word) > 8:
        words["hard"].append(word)
file.close()


def scramble_word(word):
    scramble = word
    l = list(word)
    while scramble == word:
        r.shuffle(l)
        scramble = "".join(l)
    return scramble


@app.route('/')
def index():
    rand = r.randint(0, len(words["medium"]))
    word = words["medium"][rand]
    scrable = scramble_word(word)
    result = {"word": word, "scramble": scrable}
    return render_template("index.html", result=result)


@app.route('/next/<level>')
def next(level):
    l = int(level)
    word = ""
    if l == 1:
        rand = r.randint(0, len(words["easy"]))
        word = words["easy"][rand]
    if l == 2:
        rand = r.randint(0, len(words["medium"]))
        word = words["medium"][rand]
    if l == 3:
        rand = r.randint(0, len(words["hard"]))
        word = words["hard"][rand]
    scramble = scramble_word(word)
    result = {"word": word, "scramble": scramble}
    return jsonify(result)
