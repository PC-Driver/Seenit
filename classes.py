class User:

    def __init__(self, u_id, u_name, email):
        self.u_id = u_id
        self.u_name = u_name
        self.email = email

    @property
    def fullname(self):
        return '{} {}'.format(self.u_name)
