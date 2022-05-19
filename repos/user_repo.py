from models.user import User
from utils.db_conn import connection


def build_user(user_record):
    return User(user_id=int(user_record[0]), username=user_record[1], password=user_record[2], role=user_record[3])


class UserRepo:
    def create_user(self, new_user: User):
        cursor = connection.cursor()

        sql_line = "INSERT INTO users VALUES(DEFAULT, %s, %s, %s) RETURNING *"
        owner_details = [new_user.username, new_user.password, new_user.role]

        cursor.execute(sql_line, owner_details)
        connection.commit()
        user_record = cursor.fetchone()
        return build_user(user_record)

    def get_user(self, user_id):
        cursor = connection.cursor()

        sql_line = "SELECT * FROM users WHERE user_id=%s"
        cursor.execute(sql_line, [user_id])
        user_record = cursor.fetchone()
        if user_record:
            return build_user(user_record)
        else:
            # TODO: raise a "User not found" exception
            pass

    def update_user(self, updated_user: User):
        cursor = connection.cursor()

        sql_line = "UPDATE users SET username=%s, password=%s, user_role-%s WHERE user_id =&s RETURNING *"
        owner_details = [updated_user.username, updated_user.password, updated_user.role, updated_user.user_id]

        cursor.execute(sql_line, owner_details)
        connection.commit()
        user_record = cursor.fetchone()
        return build_user(user_record)

    def delete_user(self, user_id):
        cursor = connection.cursor()
        sql_line = "DELETE FROM users WHERE user_id = %s"

        cursor.execute(sql_line, [user_id])
