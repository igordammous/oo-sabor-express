class Musica:
    nome = ''
    artista = ''
    duracao = int

musica_starway_to_heaven = Musica()
musica_starway_to_heaven.nome = 'Starway to Heaven'
musica_starway_to_heaven.artista = 'Led Zepplin'
musica_starway_to_heaven.duracao = 483

print(vars(musica_starway_to_heaven))

musica_bohemian_rhapsody = Musica()
musica_bohemian_rhapsody.nome = 'Bohemian Rhapsody'
musica_bohemian_rhapsody.artista = 'Queen'
musica_bohemian_rhapsody.duracao = 360

print(vars(musica_bohemian_rhapsody))

musica_i_choose_you = Musica()
musica_i_choose_you.nome = 'I Choose You'
musica_i_choose_you.artista = 'Forest Blakk'
musica_i_choose_you.duracao = 178

print(f'Música: {musica_i_choose_you.nome} - Banda: {musica_i_choose_you.artista} - {musica_i_choose_you.duracao} segundos')