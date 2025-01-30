class Restaurante:
    nome = ''
    categoria = ''
    ativo = False

restaurante_praca = Restaurante()
restaurante_praca.nome = 'Praça'
restaurante_praca.categoria = 'Italiana'

restaurante_pizza = Restaurante()
restaurante_pizza.nome = 'Pizza Place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True

restaurantes = [restaurante_praca]

nome_do_restaurante = restaurante_praca.nome

if restaurante_praca.ativo == False:
    print('O restaurante está inativo')
else:
    print('O restaurante está ativo.')

if restaurante_pizza.categoria == 'Fast Food':
    print('O restaurante é um fast food.')
else:
    print('O restaurante não é um fast food.')

print(vars(restaurante_praca))
print(f'Nome: {restaurante_pizza.nome}, Categoria: {restaurante_pizza.categoria}')
