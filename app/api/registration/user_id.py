""" UserID entity definition """


class UserID:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def to_dict(self):
        return dict(name=self.name, email=self.email)
