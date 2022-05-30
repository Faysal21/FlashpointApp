import unittest
from models.card import Card
from repos.card_impl import CardImpl

repo = CardImpl()


class TestCardRepo(unittest.TestCase):
    sample_card = Card()

    def test_1_create(self):
        TestCardRepo.sample_card = repo.create_card(self.sample_card)
        self.assertEqual(self.sample_card.json(), Card(card_id=self.sample_card.card_id,
                                                       question="",
                                                       answer="", deck_id=None).json())

    def test_2_get(self):
        card = repo.get_card(3).json()
        self.assertEqual(card, Card(card_id=3,
                                    question="Who is the Main character in the anime Trigun?",
                                    answer="Vash The Stampede...", deck_id=2).json())

    def test_3_get_all(self):
        cards = repo.all_card()
        self.assertGreater(len(cards), 2)

    def test_4_update(self):
        TestCardRepo.sample_card = repo.update_card(Card(card_id=10,
                                                         question="Why is Gamora?",
                                                         answer="", deck_id=5))
        self.assertEqual(self.sample_card.question, "Why is Gamora?")
        print(self.sample_card)

    def test_5_delete(self):
        self.assertIsNotNone(repo.delete_card(13))

    def test_6_get_card_by_deck(self):
        cards = [card.json() for card in repo.get_card_by_deck(5)]

        self.assertIn(Card(card_id=10,
                           question="Why is Gamora?",
                           answer="", deck_id=5).json(), cards)


if __name__ == '__main__':
    unittest.main()
