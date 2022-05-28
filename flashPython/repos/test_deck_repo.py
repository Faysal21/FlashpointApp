import unittest

from models.deck import Deck
from repos.deck_repo_impl import DeckRepoImpl

dr = DeckRepoImpl()
test_deck = Deck(deck_id=1, user_id=1, deck_name="Manga")
unittest.TestLoader.sortTestMethodsUsing = None


class TestDeckRepo(unittest.TestCase):
    def test_create(self):
        deck = dr.create_deck(test_deck).json()
        self.assertEqual(deck, test_deck.json())

    def test_get(self):
        deck = dr.get_deck(3).json()
        deck2 = Deck(deck_id=3, user_id=1, deck_name='Coding Languages').json()
        self.assertEqual(deck, deck2)
        pass

    def test_all(self):
        decks = dr.all_decks()
        self.assertGreater(len(decks), 7)

    def test_update(self):
        deck = dr.get_deck(1)
        deck.deck_name = 'Manhwa'
        update = dr.update_deck(deck)
        deck2 = Deck(deck_id=test_deck.deck_id, user_id=1, deck_name='Manhwa').json()
        self.assertEqual(update.json(), deck2)

    def test_delete(self):
        self.assertIsNone(dr.delete_deck(5))
