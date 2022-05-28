from abc import ABC, abstractmethod


class DecksRepo(ABC):
    pass

    @abstractmethod
    def create_deck(self, deck):
        pass

    @abstractmethod
    def get_deck(self, deck_id):
        pass

    @abstractmethod
    def all_decks(self):
        pass

    @abstractmethod
    def update_deck(self, change):
        pass

    @abstractmethod
    def delete_deck(self, deck_id):
        pass


