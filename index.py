import os

from flask import Flask, render_template


app = Flask(__name__)

@app.route("/")
def index():
  return 'Index Page'
if __name__ == "__main__":
  port = init(os..environ.get("PORT",80))
  app.run(host="0.0.0.0", port=port)