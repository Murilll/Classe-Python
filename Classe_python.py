class Cliente:
    def __init__(self, nome, sobrenome, email, idade, plano):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.idade = idade
        self.lista_planos = ["Individual", "Familia", "Empresa"]
        if plano in self.lista_planos:
            self.lista_plano = plano
        else:
            #print("Plano invalido") # ele ainda estancia 
            raise Exception ("Plano invalido")
            

cliente1 = Cliente("Murilo", "Sertorio", "murilosertorio@gmail.com", 18, "Familia")
print(cliente1.lista_planos)

print(cliente1.__dict__) # mostrar todos os elementos da classe