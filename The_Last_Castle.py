import pyxel
import euclid3
import random

#MODOS DE JOGO:
inicio_de_jogo = 0
jogando = 1
game_over = 2

#VIDA
class Vida:
    def __init__(self,x,y,i=False):
        self.posicao_x = x
        self.posicao_y = y
        self.recebeu_dano = i

    def draw(self):
        if self.recebeu_dano == False:
            pyxel.blt(self.posicao_x,self.posicao_y,0,32,112,16,16,0)
            
        else:
            pyxel.blt(self.posicao_x,self.posicao_y,0,32,96,16,16,0)

#MONTANHA
class Montanha:
    def __init__(self, x, y):
        self.posicao_x = x
        self.posicao_y = y
    
    def draw(self, i):
        if i == 0:
            pyxel.blt(self.posicao_x, self.posicao_y,0,64,48,16,16,7)
        elif i == 1:
            pyxel.blt(self.posicao_x, self.posicao_y,0,80,48,16,16,7)
        elif i == 2:
            pyxel.blt(self.posicao_x, self.posicao_y,0,96,48,16,16,7)

#CHÃO
class Chao:
    def __init__(self,x,y):
        self.posicao_x = x
        self.posicao_y = y

    def draw(self,i):
        if i == 0:
            pyxel.blt(self.posicao_x, self.posicao_y, 0,64,64,16,16,7)
        elif i == 1:
            pyxel.blt(self.posicao_x, self.posicao_y, 0,64,80,16,16)
        elif i == 2:
            pyxel.blt(self.posicao_x, self.posicao_y, 0,80,80,16,16)

#ARVORES
class Arvores:
    def __init__(self, x, y):
        self.posicao_x = x
        self.posicao_y = y

    def draw(self,i):
        if i == 0:
            pyxel.blt(self.posicao_x, self.posicao_y, 0,48,16,16,16,7) 
        elif i == 1:
            pyxel.blt(self.posicao_x, self.posicao_y, 0,32,7,16,9,7) 

#RELAMPAGOS
class Relampago:
    def __init__(self,i,x,y):
        self.indice = i
        self.posicao_x = x
        self.posicao_y = y
    
    def draw(self):
        if self.indice == 0:
            pyxel.blt(self.posicao_x,self.posicao_y,0,8,32,16,16,0)
        if self.indice == 1:
            pyxel.blt(self.posicao_x,self.posicao_y,0,24,24,16,24,0)

#NUVENS
class Nuvem:
    def __init__(self, i, x =255):
        self. indice = i
        self.posicao_x = x
        self.posicao_y = random.randint(10,80)
        self.velocidade = -1* (random.randint(1,5)/10)
        
    def update(self):
        self.posicao_x += self.velocidade

    def draw(self):
        i = self.indice
        if i == 0:
            pyxel.blt(self.posicao_x, self.posicao_y,0,0,16,24,16,7)
        elif i == 1:
            pyxel.blt(self.posicao_x,self.posicao_y,0,24,16,24,8,7)      

#LUA
class Lua:
    def __init__(self):
        self.posicao_x = 255
        self.posicao_y = 20
        self.velocidade = 0.02

    def update(self):
        self.posicao_x -= self.velocidade
        #if self.posicao_y > 5:
        #    self.posicao_y -= self.velocidade
        #elif self.posicao_y <=5:
        #    self.posicao_y += self.velocidade
    
    def draw(self):
        pyxel.blt(self.posicao_x,self.posicao_y,0,48,32,16,16,0)

#ESTRELAS
class Estrelas:
    def __init__(self, i, x =255):
        self. indice = i
        self.posicao_x = x
        self.posicao_y = random.randint(0,100)
        self.velocidade = -0.001
        
    def update(self):
        self.posicao_x += self.velocidade

    def draw(self):
        i = self.indice
        if i == 0:
            pyxel.blt(self.posicao_x, self.posicao_y,0,0,96,16,16,0)
        elif i == 1:
            pyxel.blt(self.posicao_x,self.posicao_y,0,0,112,16,16,0)
        elif i == 2:
            pyxel.blt(self.posicao_x,self.posicao_y,0,16,96,16,16,0)
        elif i == 3:
            pyxel.blt(self.posicao_x,self.posicao_y,0,16,112,16,16,0)
        elif i == 4:
            pyxel.blt(self.posicao_x,self.posicao_y,0,16,112,16,16,0)

#CASTELO
class Castelo:
    def __init__(self,x,y):
        self.posicao_x = x
        self.posicao_y = y

    def draw(self):
        pyxel.blt(self.posicao_x, self.posicao_y,0,0,48,27,32,7)

#INIMIGOS
class Inimigo:
    def __init__(self,x=255):
        self.posicao_x = x
        self.posicao_y = random.randint(99,102)
        self.velocidade = -1*(random.randint(1,8)/10)
    
    def update(self):
        self.posicao_x += self.velocidade

    def draw(self):
        pyxel.blt(self.posicao_x,self.posicao_y,0,48,7,8,9,7)

class Chefao:
    def __init__(self, x, y):
        self.posicao_x = x
        self.posicao_y = y
        self.velocidade = -0.5
    
    def update(self):
        self.posicao_x += self.velocidade

    def draw(self):
        pyxel.blt(self.posicao_x,self.posicao_y,0,40,74,16,22,7)

#JOGO
class Jogo:
    def __init__(self):
        #CONTADORES
        self.contador_para_waves = 0
        self.indice_de_vidas = 3

        #LISTA DE VIDA
        self.vidas = [Vida(0,0),Vida(13,0),Vida(26,0),Vida(39,0)] 
        

        #LISTA DE INIMIGOS
        self.inimigos = []

        #LISTA DE CASTELO
        self.castelo = [Castelo(15,79)]

        #LISTA DE LUA
        self.lua = [Lua()]

        #LISTA DE ESTRELAS
        self.estrelas = []
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))
        self.estrelas.append(Estrelas(random.randint(0,5),random.randint(0,255)))

        #LISTA DE NUVENS
        self.nuvens = []
        self.nuvens.append(Nuvem(random.randint(0,1),random.randint(0,255)))
        self.nuvens.append(Nuvem(random.randint(0,1),random.randint(0,255)))
        self.nuvens.append(Nuvem(random.randint(0,1),random.randint(0,255)))
        self.nuvens.append(Nuvem(random.randint(0,1),random.randint(0,255)))
        self.nuvens.append(Nuvem(random.randint(0,1),random.randint(0,255)))
        self.nuvens.append(Nuvem(random.randint(0,1),random.randint(0,255)))
        self.nuvens.append(Nuvem(random.randint(0,1),random.randint(0,255)))

        #LISTA DE RELAMPAGOS
        self.relampagos = []

        #LISTA DE ARVORES
        self.arvores = [Arvores(150,95),]

        #LISTA DE CHAO
        self.chao = [Chao(16,104),Chao(32,104),Chao(48,104),Chao(64,104),Chao(80,104),
                    Chao(96,104),Chao(112,104),Chao(128,104),Chao(144,104),Chao(160,104),Chao(176,104),
                    Chao(192,104),Chao(208,104),Chao(224,104),Chao(240,104),Chao(256,104)]        

        self.estado_de_jogo = inicio_de_jogo
        pyxel.init(255,120)
        pyxel.mouse(True)
        pyxel.load("towerdefense.pyxel")
        pyxel.run(self.update,self.draw)

    def update(self):
        #QUIT
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        #PLAY
        if pyxel.btn(pyxel.KEY_ENTER):
            self.estado_de_jogo = jogando

        #ATUALIZAÇÃO QUANDO O JOGO INICIA
        if self.estado_de_jogo == jogando:

            #INCREMENTAR CONTADOR
            self.contador_para_waves += 1

            #MOVER E GERAR INIMIGO
            if self.contador_para_waves >100 and self.contador_para_waves<105:
                self.inimigos.append(Inimigo())
            for inimigo in self.inimigos:
                inimigo.update()
                if inimigo.posicao_x <= 30:
                    self.indice_de_vidas -= 1
                    self.inimigos.remove(inimigo)
                    self.vidas[self.indice_de_vidas].recebeu_dano = True
            
            #VERIFICADOR DE VIDA
            if self.indice_de_vidas <0:
                self.estado_de_jogo = game_over

            #MOVER E GERAR ESTRELAS
            for i in range(11):
                if i == 10:
                    if len(self.estrelas)<20:
                        self.estrelas.append(Estrelas(random.randint(0,5)))
                for estrela in self.estrelas:
                    estrela.update()
                    if estrela.posicao_x <-16:
                        self.estrelas.remove(estrela)

            #MOVER E GERAR LUA
            for i in range(11):
                if i == 10:
                    if len(self.lua)<1:
                        self.lua.append(Lua())
            for lua in self.lua:
                lua.update()
                if lua.posicao_x<-32:
                    self.lua.remove(lua)

            #MOVER E GERAR NUVENS
            for i in range(11):
                if i == 10:
                    if len(self.nuvens)<7:
                        self.nuvens.append(Nuvem(random.randint(0,1)))
            for nuvem in self.nuvens:
                nuvem.update()
                if nuvem.posicao_x<-30:
                    self.nuvens.remove(nuvem)
            
             
    def draw(self):
        #TIRAR RASTRO
        pyxel.cls(0)

        #MENU PRINCIPAL
        if self.estado_de_jogo == inicio_de_jogo:
            pyxel.text(120,50,"The Last Castle",8)
            pyxel.text(10,95,"Pressione 'enter' para jogar", 7)
            pyxel.text(10,105,"Pressione 'Q' para sair", 7)

        #QUANDO O JOGO INICIAR
        elif self.estado_de_jogo == jogando:
            pyxel.cls(1)

            #ESTRELAS
            for estrela in self.estrelas:
                estrela.draw()

            #LUA
            for lua in self.lua:
                lua.draw()

            #CHAO
            Chao(0,104).draw(1)
            for chao in self.chao:
                chao.draw(0)
                
            #MONHANHAS
            Montanha(0,88).draw(1)
            Montanha(0,72).draw(0)
            Montanha(0,72).draw(2)
            Montanha(16,88).draw(1)
            Montanha(32,88).draw(1)
            Montanha(16,72).draw(1)
            Montanha(16,56).draw(0)
            Montanha(32,56).draw(2)
            Montanha(32,72).draw(1)
            Montanha(32,88).draw(1)
            Montanha(48,88).draw(1)
            Montanha(48,72).draw(2)
            Montanha(64,88).draw(2)
            Montanha(64,88).draw(0)
            Montanha(80,88).draw(1)
            Montanha(96,88).draw(1)
            Montanha(112,88).draw(1)
            Montanha(128,88).draw(1)
            Montanha(144,88).draw(1)
            Montanha(160,88).draw(1)
            Montanha(176,88).draw(1)
            Montanha(96,72).draw(1)
            Montanha(112,72).draw(1)
            Montanha(128,72).draw(1)
            Montanha(144,72).draw(1)
            Montanha(160,72).draw(1)
            Montanha(112,56).draw(1)
            Montanha(128,56).draw(1)
            Montanha(144,56).draw(1)
            Montanha(80,72).draw(0)
            Montanha(96,56).draw(0)
            Montanha(112,40).draw(0)
            Montanha(128,40).draw(1)
            Montanha(144,40).draw(2)
            Montanha(160,56).draw(2)
            Montanha(176,72).draw(2)
            Montanha(192,88).draw(2)
            Montanha(176,72).draw(0)
            Montanha(192,72).draw(2)
            Montanha(192,88).draw(1)
            Montanha(208,88).draw(0)
            Montanha(208,88).draw(2)
            Montanha(224,88).draw(2)
            
            #CHEFAO NA MONTANHA
            Chefao(128,18).draw()

            #NUVENS
            for nuvem in self.nuvens:
                nuvem.draw()

            #ARVORES
            Arvores(47,89).draw(0)
            Arvores(70,88).draw(0)
            Arvores(200,88).draw(0)
            
            #INIMIGO
            for inimigo in self.inimigos:
               inimigo.draw()
        
            # CASTELO
            for castelo in self.castelo:
                castelo.draw()

            #ARVORES
            for arvore in self.arvores:
                arvore.draw(0)
            Arvores(120,104).draw(1)
            Arvores(220,109).draw(1)

            #VIDAS
            for vida in self.vidas:
                vida.draw()

        elif self.estado_de_jogo == game_over:
            pyxel.cls(0)
            pyxel.text(100,55,"O CASTELO FOI DESTRUIDO",8)

Jogo()
