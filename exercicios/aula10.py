lanches = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for cont in range(0, len(lanches)):
    print(f'Eu vou comer {lanches[cont]}')

for comida in lanches:
    print(f'Eu vou comer {comida}')

for pos, comida in enumerate(lanches):
    print(f'Eu vou comer {comida} na posição {pos}')

print('Comi pra caramba!')

# ---------------------------------------------------------------------------------------- #

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print(sorted(lanche))
print(lanche)

# ------------------------------------------------------------------------------------------- #

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

# -------------------------------------------------------------------------------------------- #

pessoa = ('Rafael', '18', 'M', 99.88)
del(pessoa)
print(pessoa)