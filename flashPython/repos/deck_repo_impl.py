from exceptions.resource_not_found import ResourceNotFound
from models.deck import Deck
from repos.deck_repo import DecksRepo
from utils.db_conn import connection


def _build_deck(record):
    return Deck(deck_id=(record[0]), deck_name=(record[1]), user_id=(record[2]))

class DeckRepoImpl(DecksRepo):

# CREATE--------------------------------------

    def create_deck(self, deck):
        sql = "INSERT INTO decks VALUES (%s,%s,%s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [deck.deck_id, deck.deck_name, deck.user_id])

        connection.commit()
        record = cursor.fetchone()

        return _build_deck(record)

# READ REQUESTS--------------------------------

    def get_deck(self, deck_id):
        sql = "SELECT * FROM decks WHERE deck_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [deck_id])

        record = cursor.fetchone()

        if record:
            return _build_deck(record)
        else:
            raise ResourceNotFound(f"Deck with id: {deck_id} - Not Found")

    def all_decks(self):
        sql = "SELECT * FROM decks ORDER BY deck_id ASC"
        cursor = connection.cursor()
        cursor.execute(sql)

        records = cursor.fetchall()

        deck_list = []

        for record in records:
            deck = _build_deck(record)
            deck_list.append(deck)

        return deck_list

# UPDATE REQUEST--------------------------------

    def update_deck(self, change):

        sql = "UPDATE decks SET deck_name=%s, user_id=%s WHERE deck_id=%s RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, [change.deck_name, change.user_id, change.deck_id])

        connection.commit()
        record = cursor.fetchone()

        return _build_deck(record)

# DELETE REQUEST--------------------------------

    def delete_deck(self, deck_id):

        sql = "DELETE FROM decks WHERE deck_id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [deck_id])
        connection.commit()

# TESTS-------------------------------------------

def _test():
    # GET decks tests
    print("-------GET--------")
    dr = DeckRepoImpl()
    deck = dr.get_deck(2)
    print(deck)

    print(dr.all_decks())

    # CREATE new deck test

    # print("------CREATE------")
    # deck = Deck(deck_id=6, deck_name="Coding Languages", owner_id=1)
    # print(dr.create_deck(deck))
    # print(dr.all_decks())

    # UPDATE deck test
    deck = dr.get_deck(6)
    deck.deck_name = "Programming Languages"
    deck = dr.update_deck(deck)
    print(deck)


if __name__=='__main__':
    _test()