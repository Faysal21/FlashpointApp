from abc import ABC, abstractmethod


class CardRepo(ABC):
    @abstractmethod
    def create_card(self, card):
        pass

    @abstractmethod
    def update_card(self, update):
        pass

    @abstractmethod
    def get_card(self, card_id):
        pass

    @abstractmethod
    def all_card(self):
        pass

    @abstractmethod
    def delete_card(self, card_id):
        pass

    @abstractmethod
    def get_card_by_deck(self, deck_id):
        pass
