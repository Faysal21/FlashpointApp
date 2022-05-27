from flask import Flask
import controllers.main_controller as main_controller

app = Flask(__name__)

main_controller.route(app)

if __name__ == '__main__':
    app.run()
