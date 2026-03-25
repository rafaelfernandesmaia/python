from math import radians, sin, cos, tan
an = float(input('Digite o ângulo que você deseja: '))
seno = sin(radians(an))
print(f'O ângulo de {an} temo SENO de {seno:.2f}')
cos = cos(radians(an))
print(f'O ângulo de {an} tem o COSSENO de {cos:.2f}')
tag = tan(radians(an))
print(f'O ângulo de {an} tem a TANGENTE de {tag:.2f}')
