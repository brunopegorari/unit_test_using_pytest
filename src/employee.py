from datetime import date

class Funcionario:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario

    @property
    def nome(self):
        return self._nome

    @property
    def salario(self):
        return self._salario

    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/')
        ano_nascimento = int(data_nascimento_quebrada[-1])
        ano_atual = date.today().year
        if ano_nascimento > ano_atual:
            return 'Invalid date'
        else:        
            return ano_atual - ano_nascimento

    def sobrenome(self):
        nome_completo = self.nome.strip()
        nome_quebrado =  nome_completo.split(' ')
        if len(nome_quebrado) == 1:
            return "There isn't Last Name, please insert a Last Name!"
        else:
            return nome_quebrado[-1]

    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            valor = 0
        return valor

    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'