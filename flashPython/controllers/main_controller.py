from controllers import card_controller, deck_controller

def route(app):
    card_controller.route(app)
    deck_controller.route(app)