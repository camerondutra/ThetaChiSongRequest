import flask
import json
from flask import request, render_template, redirect, url_for

app = flask.Flask(__name__)
app.config['DEBUG'] = True

SONGLIST = {'Apple': 1, 'Cameron': 2, 'BestSong': 3}

@app.route('/', methods=['GET'])
def getAll():
    return render_template("vote.html", songList=SONGLIST)

@app.route('/', methods=['POST'])
def addSong():
    songName = request.form.get('song')
    SONGLIST[songName] = 1
    return redirect(url_for("getAll"))

@app.route("/delete/<song>")
def delete(song):
    del SONGLIST[song]
    return redirect(url_for("getAll"))

@app.route('/upvote/', methods=['PUT'])
def upvote():
    try:
        songName = request.args.get('song')
        if (songList[songName]):
            songList[songName] = songList[songName] + 1
    except Exception as e:
        print('Can\'t find song')
    return ('', 200)

@app.route('/downvote/', methods=['PUT'])
def downvote():
    try:
        songName = request.args.get('song')
        if (songList[songName]):
            songList[songName] = songList[songName] - 1
    except Exception as e:
        print('Can\'t find song')
    return ('', 200)

app.run()