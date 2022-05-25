from repos.card_repo import CardRepo


class CardServ:
    def __init__(self, card_repo: CardRepo):
        self.card_repo = card_repo

    def create_card(self, card):
        return self.card_repo.create_card(card)

    def update_card(self, update):
        return self.card_repo.update_card(update)

    def get_card(self, card_id):
        return self.card_repo.get_card(card_id)

    def all_card(self):
        return self.card_repo.all_card()

    def delete_card(self, card_id):
        return self.card_repo.delete_card(card_id)

    def get_card_by_deck(self, deck_id):
        return self.card_repo.get_card_by_deck(deck_id)
