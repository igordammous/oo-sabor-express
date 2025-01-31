class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self) 
    
    def __str__(self):
        return f'{self._nome.ljust(15)} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(15)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante.categoria.ljust(15)} | {restaurante.ativo}')


    @property
    def ativo(self):
            return 'Restaurante Ativo' if self._ativo else 'Restaurante inativo'

    def alternar_estado(self):
         self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Italiana')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('pizza Place', 'Fast Food')

Restaurante.listar_restaurantes()

