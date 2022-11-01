class Cliente:
    def __init__(self, nome, sobrenome, email, idade, plano):
        self.nome = nome # o self me da a opção de usar o nome em outras funções
        self.sobrenome = sobrenome
        self.email = email
        self.idade = idade
        self.lista_planos = ["Individual", "Familia", "Empresa"]
        if plano in self.lista_planos:
            self.lista_plano = plano
        else:
            #print("Plano invalido") # ele ainda estancia 
            raise Exception ("Plano invalido")
            
    def mudar_plano(self, mudar_plano):
        if mudar_plano in self.lista_planos:
            self.lista_planos = mudar_plano
        else:
            print("Plano invalido")


cliente1 = Cliente("Murilo", "Sertorio", "murilosertorio@gmail.com", 18, "Familia")
print(cliente1.lista_planos)

print(cliente1.__dict__) # mostrar todos os elementos da classe


class Personagem:
    def __init__(self, name, classe, poder, life, speed, damage):
        self.name = name
        self.classe = classe
        self.poder = poder
        self.life = life
        self.speed = speed
        self.damage = damage
        
Zomo = Personagem("Zomo", "Assassino", 998, 100, 500, 777)
print(Zomo.__dict__)