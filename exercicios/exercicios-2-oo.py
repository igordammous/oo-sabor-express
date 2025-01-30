class Carro:
    carros = []
    def __init__ (self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano
        Carro.carros.append(self)

    def __str__(self):
        return f'{self.nome} | {self.cor} | {self.ano}'
    
    def listar_carros():
        for carro in Carro.carros:
            print(f'Modelo: {carro.modelo.ljust(15)} | Cor: {carro.cor.ljust(10)} | {carro.ano}')

carro_argo = Carro('Fiat Argo', 'Branco', 2019)

Carro.listar_carros()

class Restaurante:
    restaurantes = []
    def __init__ (self, nome, categoria, ativo, delivery, tempo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        self.delivery = delivery
        self.tempo = tempo
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo} | {self.delivery} | {self.tempo}'
    
    def listar_restaurante():
        for restaurante in Restaurante.restaurantes:
            print(f'Nome: {restaurante.nome.ljust(15)} | Categoria: {restaurante.categoria.ljust(10)} | Ativo: {restaurante.ativo} | Tem delivery: {restaurante.delivery.ljust(5)} | Tempo de entrega: {restaurante.tempo} minutos.')

restaurante_Dacho = Restaurante('Dacho', 'Japonês', True, 'Sim', 70)

Restaurante.listar_restaurante()

class Cliente:
    clientes = []
    def __init__(self, nome, idade, profissao, empregado):
        self.nome = nome
        self.idade = int(idade)
        self.profissao = profissao
        self.empregado = False
        Cliente.clientes.append(self)
    
    def __str__(self):
        return f'{self.nome} | {self.idade} | {self.profissao} | {self.empregado}'
    
    def listar_clientes():
        for cliente in Cliente.clientes:
            print(f'Nome: {cliente.nome.ljust(10)} | Idade: {cliente.idade} | Profissão: {cliente.profissao.ljust(10)}')

cliente_Igor = Cliente('Igor', 31, 'Engenheiro Civil', 'Sim')

Cliente.listar_clientes()