import os
from flask import Flask
from flask_graphql import GraphQLView
from api.model.user import schema

app = Flask(__name__)
# app.debug = True

@app.route("/")
def index():
  return 'SATO AND TOGASHI. Hello Worlds'

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True  # GraphiQLを表示
    )
)

if __name__ == "__main__":
  port = int(os.environ.get("PORT", 5000))
  app.run(host="0.0.0.0", port=port)