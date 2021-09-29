import flask
import json
from flask import request

app = flask.Flask(__name__)
app.config['DEBUG'] = True

songList = {'Apple': 1, 'Cameron': 2, 'BestSong': 3}

@app.route('/', methods=['GET'])
def getAll():
    sortedSongs = sorted(songList.items(), key=lambda x: x[1], reverse=True)
    return json.dumps(dict(sortedSongs), indent = 4)

@app.route('/', methods=['POST'])
def addSong():
    songName = request.args.get('song')
    songList[songName] = 1
    return ('', 200)

@app.route('/', methods=['DELETE'])
def deleteAll():
    songName = request.args.get('song')
    if (songName):
        songList.pop[songName]
    else:
        songList = {}
    return ('', 200)

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
