from envVariables import app, api, db
from flask_restful import Resource, reqparse
import api

if __name__ == "__main__":
    app.run(debug=True)
