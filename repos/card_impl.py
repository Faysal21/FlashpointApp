from exceptions.resource_not_found import ResourceNotFound
from models.card import Card
from repository.card_repo import CardRepo
from utility.db_conn import connection


def _build_card(query):
    return Card(card_id=query[0], question=query[1], answer=query[2], deck_id=query[3])


class CardImpl(CardRepo):
    def create_card(self, card):
        sql = 'insert into cards values (default, %s,%s,%s) returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [card.question, card.answer, card.deck_id])
        connection.commit()
        query = cursor.fetchone()
        return _build_card(query)

    def update_card(self, update):
        sql = 'update cards set question=%s, answer=%s, deck_id=%s where card_id=%s' \
              'returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [update.question, update.answer, update.deck_id, update.card_id])
        connection.commit()
        query = cursor.fetchone()
        if query:
            return _build_card(query)
        else:
            raise ResourceNotFound(f'No record found for Card {update.card_id}')

    def get_card(self, card_id):
        sql = 'select * from cards where card_id = %s'
        cursor = connection.cursor()
        cursor.execute(sql, [card_id])
        query = cursor.fetchone()
        if query:
            return _build_card(query)
        else:
            raise ResourceNotFound(f'No record found for Card {card_id}')

    def all_card(self):
        sql = 'select * from cards'
        cursor = connection.cursor()
        cursor.execute(sql)
        query = cursor.fetchall()
        card_list = [_build_card(card) for card in query]
        return card_list

    def delete_card(self, card_id):
        sql = 'delete from cards where card_id =%s returning *'
        cursor = connection.cursor()
        cursor.execute(sql, [card_id])
        connection.commit()
        return f'Card id {card_id} successfully deleted'


def _test():
    cr = CardImpl()
    # card = Card(question='What Anime did Vash the Stampede appear', answer='Trigun', deck_id=2)
    card = cr.get_card(2)
    card.question = 'Who is the Main character in the anime Trigun?'
    card.answer = 'Vash The Stampede'
    card = cr.update_card(card)
    print(card)


if __name__ == '__main__':
    _test()
