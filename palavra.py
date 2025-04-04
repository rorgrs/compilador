from tokens import Token


class Palavra:
    def __init__(self, token: Token, lexema = None):
        self.token = token
        self.lexema = lexema

    def __repr__(self):
        return f'Token({self.lexema}, {self.token})' if self.lexema else f'Token({self.token})'