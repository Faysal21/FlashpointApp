class Deck:
    def __init__(self, deck_id='', user_id='', deck_name=''):
        self.deck_id = deck_id
        self.user_id = user_id  # owner id refers to user id of creator
        self.deck_name = deck_name

    def __repr__(self):
        return str({
            'deck_id': self.deck_id,
            'user_id': self.user_id,
            'deck_name': self.deck_name
        })

    def json(self):
        return {
            'deckId': self.deck_id,
            'userId': self.user_id,
            'deckName': self.deck_name
        }
