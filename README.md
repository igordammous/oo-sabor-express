# Curso Python: aplicando a Orientação a Objetos
---

Continuação de desenvolvimento do aplicativo "Sabor Express"

## Aula 1 - Classes

Criação de classes e objetos em Python. E outros pontos importantes como o conceito de atributos de uma classe, que são as características específicas de cada objeto criado a partir dessa classe. Nesta aula, aprendemos a definir atributos como nome, 
categoria e ativo para a classe Restaurante. Também vimos que as classes permitem organizar o código de forma mais modular e reutilizável, facilitando a manutenção e o desenvolvimento de aplicações mais complexas. Continue estudando e praticando!

## Aula 2 - Construtor e instanciando objetos

Aprendizagem do metodo __init__ que sempre que for criar a instancia de um objeto, esse metodo é chamado e espera uma informação.

---
Exemplo:
class Musica:
    def __init__ (self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica_starway_to_heaven = Musica('Starway to Heaven', 'Led Zepplin', 483)
---

Aprendizagem do metodo __str__ que pega o objeto e mostra ele como forma de texto.