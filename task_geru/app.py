from task_geru.api.find_zen_quotes.viewer import ns as quotes
from task_geru.api import api
from flask import Flask, Blueprint
from flask_cors import CORS

app = Flask(__name__)
blueprint = Blueprint('api', __name__)

api.init_app(blueprint)
api.add_namespace(quotes, '/')
app.register_blueprint(blueprint)

cors = CORS(app, resources={r"/*": {"origins": "*"}})


if __name__ == "__main__":
    host = '0.0.0.0'
    port = '15000'
    debug = True
    app.run(host, int(port), debug)