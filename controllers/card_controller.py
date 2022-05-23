from repos.card_impl import CardImpl
from services.card_serv import CardServ
from models.card import Card
from exceptions.resource_not_found import ResourceNotFound
from flask import request, jsonify

repo = CardImpl()
serv = CardServ(repo)

def route(app):
    @app.route('/cards', methods=['POST'])
    def create_card():
        return "This path creates a new card."

    @app.route('/cards/<card_id>', methods=['GET'])
    def get_card(card_id):
        try:
            return serv.get_card(int(card_id)).json()
        except ResourceNotFound as r:
            return r.message, 404

    @app.route('/cards', methods=['GET'])
    def all_card():
        return jsonify([card.json() for card in serv.all_card()])

    @app.route('/cards/<card_id>', methods=['PUT'])
    def update_card(card_id):
        try:
            card = serv.get_card(int(card_id))
        except ResourceNotFound as r:
            return r.message, 404

        body = request.json

        card = Card(card_id=int(card_id), question=body['question'],
                    answer=body['answer'], deck_id=body['deckID'])

        card = serv.update_card(card)
        return card.json()

    @app.route('/cards/<card_id>', methods=['DELETE'])
    def delete_card(card_id):
        try:
            card = serv.get_card(int(card_id))
        except ResourceNotFound as r:
            return r.message, 404

        serv.delete_card(int(card_id))

        return "Card with ID no. " + card_id + " was deleted."
