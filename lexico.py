from palavra import Palavra
from tokens import Token, RESERVADAS, SIMBOLOS


class Lexico:
    def __init__(self, texto):
        self.texto = texto
        self.pos = 0
        self.char_atual = self.texto[self.pos] if self.texto else None

    # avanca o leitor do arquivo em uma posicao e coloca o caractere lido na variavel char_atual
    def avancar(self):
        self.pos += 1
        if self.pos >= len(self.texto):
            self.char_atual = None
        else:
            self.char_atual = self.texto[self.pos]

        #if not (self.char_atual == ' ' or self.char_atual == '\t' or self.char_atual == '\n' or self.char_atual == '\r\n'):
        #    print(self.char_atual)

    # avanca o leitor ate encontrar algum caractere que nao seja de espaçamento
    def pular_espacos(self):
        while self.char_atual is not None and (self.char_atual == ' ' or self.char_atual == '\t' or self.char_atual == '\n' or self.char_atual == '\r\n'):
            self.avancar()

    # retorna o caractere que esta na proxima posicao do char_atual
    # usado para verificacoes dos simbolos de multiplos caracteres
    def proximo_char(self):
        peek_pos = self.pos + 1
        if peek_pos >= len(self.texto):
            return None
        return self.texto[peek_pos]

    # retorna o literal de dentro de uma string
    def tratar_string(self):
        resultado = ''
        self.avancar()  # pular aspas iniciais
        while self.char_atual is not None and self.char_atual != '"':
            resultado += self.char_atual
            self.avancar()
        if self.char_atual != '"':
            raise Exception("String não finalizada")
        self.avancar()  # pular aspas fechando
        return Palavra(Token.LITERAL, resultado)

    # retorna o numero inteiro ou real
    def tratar_numero(self):
        resultado = ''
        while self.char_atual is not None and self.char_atual.isdigit():
            resultado += self.char_atual
            self.avancar()

        if self.char_atual == '.':
            resultado += self.char_atual
            self.avancar()
            while self.char_atual is not None and self.char_atual.isdigit():
                resultado += self.char_atual
                self.avancar()
            return Palavra(Token.NREAL, resultado)

        return Palavra(Token.NINT, resultado)

    # avanca ate o comentario acabar
    def tratar_comentario(self):
        while self.char_atual != '\n' and self.char_atual != '\r\n' and self.char_atual is not None:
            self.avancar()

    # avanca ate o comentario acabar
    def tratar_comentario_bloco(self):
        while self.char_atual != '?' and self.char_atual is not None:
            self.avancar()
        if self.char_atual != '?':
            raise Exception("Comentário não finalizado")
        self.avancar()

    # retorna a palavra reservada ou um identificador qualquer
    def tratar_identificador(self):
        resultado = ''
        while self.char_atual is not None and (self.char_atual.isalnum() or self.char_atual == '_'):
            resultado += self.char_atual
            self.avancar()

        #pega o token da palavar reservada, se nao usa o token de identificador
        token_identificador = RESERVADAS.get(resultado.lower(), Token.IDENT)
        return Palavra(token_identificador, resultado)

    # retorna a proxima palavra a ser lida
    def proxima_palavra(self):
        while self.char_atual is not None:
            if self.char_atual == ' ' or self.char_atual == '\t':
                self.pular_espacos()
                continue

            if self.char_atual == '\n' or self.char_atual == '\r\n':
                self.pular_espacos()
                continue

            if self.char_atual == '!' and self.proximo_char() == '!':
                self.avancar()
                self.avancar()
                self.tratar_comentario()
                continue

            if self.char_atual == '?':
                self.avancar()
                self.tratar_comentario_bloco()
                continue

            if self.char_atual == '"':
                return self.tratar_string()

            if self.char_atual.isdigit():
                return self.tratar_numero()

            if self.char_atual.isalpha() or self.char_atual == '_':
                return self.tratar_identificador()

            # verifiar simbolos de multiplos caracteres antes dos outros
            if self.char_atual == ':' and self.proximo_char() == '=':
                self.avancar()
                self.avancar()
                return Palavra(Token.ATTRIB, ':=')

            if self.char_atual == '>' and self.proximo_char() == '=':
                self.avancar()
                self.avancar()
                return Palavra(Token.GTE, '>=')

            if self.char_atual == '<':
                next_char = self.proximo_char()
                if next_char == '=':
                    self.avancar()
                    self.avancar()
                    return Palavra(Token.LTE, '<=')
                elif next_char == '>':
                    self.avancar()
                    self.avancar()
                    return Palavra(Token.DIFF, '<>')

            # verificar simbolos de apeans um caractere
            token_simbolo = SIMBOLOS.get(self.char_atual)
            if token_simbolo is not None:
                resultado = Palavra(token_simbolo, self.char_atual)
                self.avancar()
                return resultado

            raise Exception(f'Caractere inválido: {self.char_atual}')

        return Palavra(Token.EOF)

palavras = []

with open('codigo_exemplo.txt', 'r') as file:
    lexico = Lexico(file.read())
    palavra = lexico.proxima_palavra()
    while palavra.token != Token.EOF:
        print(palavra.__repr__())
        palavras.append(palavra)
        palavra = lexico.proxima_palavra()
    print(palavra)  # EOF