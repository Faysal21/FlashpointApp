class User:
    def __init__(self, user_id=0, username='', password='', role='Card User'):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return str({
            'user_id': self.user_id,
            'username': self.username,
            'password': self.password,
            'role': self.role
        })

    def json(self):
        return {
            'userId': self.user_id,
            'username': self.username,
            'password': self.password,
            'role': self.role
        }
