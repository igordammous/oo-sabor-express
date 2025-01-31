class Musica:
    musicas = []
    def __init__ (self, nome, artista, duracao):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        Musica.musicas.append(self)
    
    def __str__ (self):
        return f'{self.nome.ljust(15)} | {self.categoria}'

    def listar_musicas():
        for musica in Musica.musicas:
            print(f'Música: {musica.nome.ljust(20)} - Banda: {musica.artista.ljust(20)} - {musica.duracao} segundos')


musica_starway_to_heaven = Musica('Starway to Heaven', 'Led Zepplin', 483)
musica_bohemian_rhapsody = Musica('Bohemian Rhapsody', 'Queen', 360)
musica_i_choose_you = Musica('I Choose You', 'Forest Blakk', 178)

Musica.listar_musicas()