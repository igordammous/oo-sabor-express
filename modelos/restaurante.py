class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self) 
    
    def __str__(self):
        return f'{self.nome.ljust(15)} | {self.categoria}'

    def listar_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(15)} | {restaurante.categoria.ljust(10)} | {restaurante.ativo}')


restaurante_praca = Restaurante('Praça', 'Italiana')
restaurante_pizza = Restaurante('Pizza Place', 'Fast Food')

Restaurante.listar_restaurantes()

