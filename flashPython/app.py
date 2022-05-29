from flask import Flask
from flask_cors import CORS
import controllers.main_controller as main_controller

app = Flask(__name__)
cors = CORS(app)

main_controller.route(app)

if __name__ == '__main__':
    app.run()
