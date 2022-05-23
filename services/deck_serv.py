from repository.deck_repo import DecksRepo


class DecksServ:
    def __init__(self, decks_repo: DecksRepo):
        self.decks_repo = decks_repo

    def create_deck(self, deck):
        return self.decks_repo.create_deck(deck)

    def get_deck(self, deck_id):
        return self.decks_repo.get_deck(deck_id)

    def all_deck(self):
        return self.decks_repo.all_decks()

    def update_deck(self, change):
        return self.decks_repo.update_deck(change)

    def delete_deck(self, deck_id):
        return self.decks_repo.delete_deck(deck_id)
