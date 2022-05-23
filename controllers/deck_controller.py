from flask import jsonify, request

from exceptions.resource_not_found import ResourceNotFound
from models.deck import Deck
from repository.deck_repo_impl import DeckRepoImpl
from services.deck_serv import DecksServ

dr = DeckRepoImpl()
serv = DecksServ(dr)


def route(app):
    @app.route('/decks', methods=['get'])
    def all_decks():
        decks = [deck.json() for deck in serv.all_deck()]
        return jsonify(decks)

    @app.route('/decks/<deck_id>', methods=['get'])
    def get_deck(deck_id):
        try:
            deck = serv.get_deck(int(deck_id))
            return deck.json()
        except ValueError:
            return f'{deck_id} not a Valid Deck ID'
        except ResourceNotFound as r:
            return r.message, 404

    @app.route('/decks', methods=['post'])
    def create_deck():
        body = request.json
        deck = Deck(deck_id=int(body['deckId']), user_id=int(body['userId']), deck_name=body['deckName'])
        ndeck = serv.create_deck(deck)
        return jsonify(ndeck.json())

    @app.route('/decks/<deck_id>', methods=['put'])
    def update_deck(deck_id):
        try:
            deck = serv.get_deck(deck_id)
            body = request.json
            deck = Deck(deck_id=deck_id, user_id=body['userId'], deck_name=body['deckName'])
            ndeck = serv.update_deck(deck)
            return ndeck.json()
        except ResourceNotFound as r:
            return r.message, 404

    @app.route('/decks/<deck_id>', methods=['delete'])
    def delete_deck(deck_id):
        try:
            deck = serv.get_deck(deck_id)
            serv.delete_deck(deck_id)
            return f'Deck {deck_id} has been deleted'
        except ResourceNotFound as r:
            return r.message, 404



