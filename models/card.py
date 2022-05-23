class Card:
    def __init__(self, card_id=0, question='', answer='', deck_id=None):
        self.card_id = card_id
        self.question = question
        self.answer = answer
        self.deck_id = deck_id

    def __repr__(self):
        return str({
            'card_id': self.card_id,
            'question': self.question,
            'answer': self.answer,
            'deck_id': self.deck_id
        })

    def json(self):
        return {
            'cardId': self.card_id,
            'question': self.question,
            'answer': self.answer,
            'deckID': self.deck_id
        }