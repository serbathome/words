from flask import Flask, render_template, jsonify
import random as r
import csv

app = Flask(__name__)

# define global words dictionary
words = {}
words["easy"] = []
words["medium"] = []
words["hard"] = []

# load words (russian and english)
with open('words.csv', newline='\n', encoding="UTF8") as csvfile:
    wordreader = csv.reader(csvfile, delimiter=';')
    for row in wordreader:
        rus = row[0]
        eng = row[1]
        if len(rus) <= 4:
            words["easy"].append((rus, eng))
        if len(rus) >= 5 and len(rus) <= 8:
            words["medium"].append((rus, eng))
        if len(rus) > 8:
            words["hard"].append((rus, eng))


def scramble_word(word):
    if len(word) == 0:
        return ""
    scramble = word
    l = list(word)
    while scramble == word:
        r.shuffle(l)
        scramble = "".join(l)
    return scramble


@app.route('/')
def index():
    rand = r.randint(0, len(words["medium"]))
    word = words["medium"][rand][0]
    eng = words["medium"][rand][1]
    scrable = scramble_word(word)
    result = {"word": word, "scramble": scrable, "eng": eng}
    return render_template("index.html", result=result)


@app.route('/next/<level>')
def next(level):
    l = int(level)
    word = ""
    eng = ""
    if l == 1:
        rand = r.randint(0, len(words["easy"]))
        word = words["easy"][rand][0]
        eng = words["easy"][rand][1]
    if l == 2:
        rand = r.randint(0, len(words["medium"]))
        word = words["medium"][rand][0]
        eng = words["medium"][rand][1]
    if l == 3:
        rand = r.randint(0, len(words["hard"]))
        word = words["hard"][rand][0]
        eng = words["hard"][rand][1]
    scramble = scramble_word(word)
    result = {"word": word, "scramble": scramble, "eng": eng}
    return jsonify(result)
