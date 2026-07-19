class Times:
    def __init__(self, nome, cidade, pontos = 0):
        self.nome = nome
        self.cidade = cidade
        self.pontos = pontos
    
    def somar_pontos(self, qtd):
        self.pontos += qtd

    def mostrar_status(self):
        print(f"{self.nome} ({self.cidade}) - {self.pontos}")
    
time1 = Times("Flamengo", "Rio de Janeiro", 15)
time2 = Times("Palmeiras", "São Paulo", 22)
time3 = Times("Fortaleza", "Fortaleza", 18)
time4 = Times("Bahia", "Salvador", 9)

maior = time1

if time2.pontos > maior.pontos:
    maior = time2

if time3.pontos > maior.pontos:
    maior = time3

if time4.pontos > maior.pontos:
    maior = time4

print(f"O time com mais pontos é o {maior.nome}, com {maior.pontos} pontos.")