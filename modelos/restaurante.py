from modelos.avaliacao import Avaliacao

class Restaurante:
    restaurantes = []
    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        self._avaliacao = []
        Restaurante.restaurantes.append(self) 
    
    def __str__(self):
        return f'{self._nome.ljust(15)} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f'{'Nome do Restaurante'.ljust(20)} | {'Categoria'.ljust(15)} | {'Avaliação'.ljust(10)} | {'Status'}')
        for restaurante in cls.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante.categoria.ljust(15)} | {str(restaurante.media_avaliacao).ljust(10)} | {restaurante.ativo}')


    @property
    def ativo(self):
            return 'Restaurante Ativo' if self._ativo else 'Restaurante inativo'

    def alternar_estado(self):
         self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        avaliacao = Avaliacao(cliente, nota)
        self._avaliacao.append(avaliacao)

    @property
    def media_avaliacao(self):
         if not self._avaliacao:
              return 0
         soma_das_notas = sum(avaliacao._nota for avaliacao in self._avaliacao)
         media = round(soma_das_notas / len(self._avaliacao),1)
         return media