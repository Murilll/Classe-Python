class Celular:
    def __init__(self, tela, cor, android, memoriaram):
        self.tela = tela
        self.cor = cor
        self.android = android
        self.memoriaram = memoriaram
        self.flash = False

    def LigarFlash(self):
        self.flash = self.flash

celular1 = Celular("6.2pl","preto","12","8gb")
celular2 = Celular("4.5pl","branco","10","2gb")
celular3 = Celular("5pl","Azul","11","6gb")
celular1.LigarFlash()

print(celular1.tela)
print(celular1.flash)

