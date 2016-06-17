#!/usr/bin/env python
from flask import Flask, url_for, jsonify, request

import ghstreak

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
  return jsonify({
      'endpoints': {
        'user_streak': '/<username>'
      }
    })

@app.route('/<username>', methods=['GET'])
def user_streak(username):
  return jsonify({
      'streak': ghstreak.get_streak_for_user(username)
    })

if __name__ == '__main__':
  app.run('0.0.0.0', debug=False)