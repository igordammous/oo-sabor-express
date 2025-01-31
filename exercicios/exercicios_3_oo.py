class Pessoa:
    def __init__(self, nome, idade, profissao):
        self._nome = nome.title()
        self._idade = idade
        self._profissao = profissao.title()

    def __str__(self):
        return f'Nome: {self._nome.ljust(25)} | Idade: {self._idade.ljust(20)} | Profissão: {self._profissao}.'

    @property
    def saudacao(self):
        return f'Seja bem vindo(a) {self._profissao}.'

    def aniversario(self):
        self._idade += 1
        print(f'Feliz aniversário {self._nome}! Parabéns por seus {self._idade} anos.')

pessoa1 = Pessoa(nome='Alice', idade=25, profissao='Engenheira')
pessoa2 = Pessoa(nome='Luiza', idade=30, profissao='Desenvolvedor')
pessoa3 = Pessoa(nome='Jaque', idade=22, profissao= '')

pessoa1.aniversario()
pessoa3.aniversario()

print(pessoa1.saudacao)
print(pessoa2.saudacao)
print(pessoa3.saudacao)

class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Nome do Titular: {self._titular.ljust(20)} | Saldo: R${self._saldo} | Status: {self.ativo}.'
    
    def dados_conta(self):
        print(f'Nome do Titular: {self._titular.ljust(20)} | Saldo: R${self._saldo} | Status: {self.ativo}.')

    @property
    def ativo(self):
        return f'Conta ativa' if self._ativo else 'Conta inativa'

    def ativar_conta(self):
        self._ativo = not self._ativo

titular1 = ContaBancaria(titular = 'igor dammous', saldo = 1000)
titular1.ativar_conta()

titular1.dados_conta()

class ContaBancariaPythonica:
    def __init__(self, titular, saldo):
        self._titular = titular.title()
        self._saldo = saldo
        self._ativo = False

    @property
    def titular(self):
        return self._titular

    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return self._ativo
    
conta2 = ContaBancariaPythonica('milene egea', 2000)
print(f'Titular da conta 2: {conta2._titular}')

