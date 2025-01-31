class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self._titulo = titulo.title()
        self._autor = autor.title()
        self._ano_publicacao = ano_publicacao
        self._disponivel = True

    def __str__(self):
        return f'Título do livro: {self._titulo.ljust(25)} | Autor: {self._autor.ljust(25)} | Ano de Publicação: {str(self._ano_publicacao).ljust(25)} | Disponível para empréstimo: {self.emprestimo}'
    
    @property
    def emprestimo(self):
        return 'Livro Disponível' if self._disponivel else 'Livro indisponível'

    def emprestar_livro(self):
        self._disponivel = not self._disponivel

    def verificar_disponibilidade(ano):
        livros_disponiveis = [livro for livro in Livro.livros if livro._ano_publicacao == ano and livro._disponivel]
        return livros_disponiveis

livro1 = Livro("Aprendendo Python", "John Doe", 2022)

livro2 = Livro("Data Science Fundamentals", "Jane Smith", 2020)

livro1.emprestar_livro()

print(livro1)

print(livro2)

