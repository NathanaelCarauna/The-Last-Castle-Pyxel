import pyxel
import random
#import pygame

#MODOS DE JOGO:
inicio_de_jogo = 0

jogando = 1
game_over = 2
win = 3

def gold_de_upgrade(x):
            novo_valor = x+(x/4)
            return(novo_valor)
def reset(self):
    self.indice_de_vidas = 0
    self.vidas = [Vida()]
    self.contador_para_waves = 0
    self.inimigos = []
    self.tiros = []
    self.tipo_de_projétil = 0
    self.velocidade = 1
    self.poder_de_ataque = 1
    self.gold_total = 50
    self.fire_rate = 37
    self.dano_preço = 30
    self.qtd_tiros_preço = 30
    self.velocidade_preço = 30
    self.vida_preço = 150
    self.castelo[0].tipo_de_castelo = 0
    for vida in  self.vidas:
        vida.cheio = True

#UPGRADES
class Upgrades:
    def __init__(self, up, pup, x, y):
        self.posicao_x = x
        self.posicao_y = y
        self.upgrade = up
        self.pode_evoluir = pup
    
    def draw(self):
        if self.upgrade == 0:
            if self.pode_evoluir == False:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,80,0,16,16,0)                #DANO
            else:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,80,16,16,16,0)

        if self.upgrade == 1:
            if self.pode_evoluir == False:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,96,0,16,16,0)                #VELOCIDADE
            else:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,96,16,16,16,0)

        if self.upgrade == 2:
            if self.pode_evoluir == False:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,112,0,16,16,0)               #QTD DE TIROS
            else:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,112,16,16,16,0)

        if self.upgrade == 3:
            if self.pode_evoluir == False:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,128,0,16,16,0)               #QTD DE VIDAS
            else:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,128,16,16,16,0)

#OURO
class Ouro:
    def __init__(self,tipo=1, x=210, y=0):
        self.posicao_x = x
        self.posicao_y = y
        self.tipo = tipo
        
    def update(self):
        self.posicao_y -= 0.3

    def draw(self):
        if self.tipo == 0:
            pyxel.blt(self.posicao_x,self.posicao_y,0,48,96,16,16,0)
        else:
            pyxel.blt(self.posicao_x,self.posicao_y,0,48,112,8,8,0)  
#VIDA
class Vida:
    def __init__(self):
        self.sprite_cheio = (0,32,112,16,16,7)
        self.sprite_vazio = (0,32,96,16,16,7)
        self.cheio = True

    def draw(self, x, y):
        if self.cheio:
            pyxel.blt(x,y,*self.sprite_cheio)
            
        else:
            pyxel.blt(x,y,*self.sprite_vazio)

#MONTANHA
class Montanha:
    def __init__(self, x, y, i):
        self.posicao_x = x
        self.posicao_y = y
        self.tipo = i
    def draw(self):
        if self.tipo == 0:
            pyxel.blt(self.posicao_x, self.posicao_y,0,64,48,16,16,7)
        elif self.tipo == 1:
            pyxel.blt(self.posicao_x, self.posicao_y,0,80,48,16,16,7)
        elif self.tipo == 2:
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
            pyxel.blt(self.posicao_x, self.posicao_y,0,0,16,24,16,15)
        elif i == 1:
            pyxel.blt(self.posicao_x,self.posicao_y,0,24,16,24,8,15)      

#LUA
class Lua:
    def __init__(self):
        self.posicao_x = 255
        self.posicao_y = 20
        self.velocidade = 0.02

    def update(self):
        self.posicao_x -= self.velocidade

    
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
    def __init__(self,i,x,y):
        self.tipo_de_castelo = i
        self.posicao_x = x
        self.posicao_y = y

    def draw(self):
        if 0 <= self.tipo_de_castelo <3:
            pyxel.blt(self.posicao_x, self.posicao_y,0,0,48,40,32,7)

        if 3<= self.tipo_de_castelo < 5:
            pyxel.blt(self.posicao_x, self.posicao_y,0,64,96,40,32,7)

        if self.tipo_de_castelo >= 5:
            pyxel.blt(self.posicao_x, self.posicao_y,0,104,96,40,32,7)

#ARMA
class Arma:
    def __init__(self, x = 30, y = 105):
        self.posicao_x = x
        self.posicao_y = y
        self.arma = 1

    def draw(self):
        if self.arma == 1:
            pyxel.blt(self.posicao_x,self.posicao_y,0,80,64,8,8,7)
        elif self.arma == 2:
            pyxel.blt(self.posicao_x,self.posicao_y,0,80,72,8,8,7)
        elif self.arma == 0:
            pyxel.blt(self.posicao_x,self.posicao_y,0,88,72,8,8,7)

#TIROS
class Tiros:
    def __init__(self,i, v, x= 30, y=88):
        self.posicao_x = x
        self.posicao_y = y
        self.tipo_de_projetil = i
        self.velocidade_x = 1*v #((pyxel.mouse_x - self.posicao_x)/pyxel.mouse_x)*v
        self.velocidade_y = ((pyxel.mouse_y - self.posicao_y)/self.posicao_y)*v

    def update(self):
        self.posicao_x += self.velocidade_x
        self.posicao_y += self.velocidade_y


    def draw(self):
        if 0 <= self.tipo_de_projetil <1 :
            pyxel.blt(self.posicao_x,self.posicao_y,0,64,6,2,3,7)
        if 1 <= self.tipo_de_projetil < 2:
            pyxel.blt(self.posicao_x,self.posicao_y,0,64,2,2,3,7)
        if 2 <= self.tipo_de_projetil < 3:
            pyxel.blt(self.posicao_x,self.posicao_y,0,64,0,2,3,7)
        if 3 <= self.tipo_de_projetil <= 4:
            pyxel.blt(self.posicao_x,self.posicao_y,0,64,4,2,3,7)
        if 4 <= self.tipo_de_projetil <= 5:
            pyxel.blt(self.posicao_x,self.posicao_y,0,73,5,3,3,7)
        if 5 <= self.tipo_de_projetil <= 6:
            pyxel.blt(self.posicao_x,self.posicao_y,0,73,3,3,3,7)

#INIMIGOS
class Inimigo:
    def __init__(self,ti, x=255):
        self.tipo_de_inimigo = ti
        self.posicao_x = x
        if self.tipo_de_inimigo == 3:
            self.posicao_y = random.randint(86,96)
        else:
            self.posicao_y = random.randint(96,106)
        self.velocidade = -1*(random.randint(1,6)/10)
        self.animar = True
        self.vivo = True
        self.pode_dar_ouro = True
        if self.tipo_de_inimigo == 0:
            self.life = 3
        if self.tipo_de_inimigo == 1:
            self.life = 10
        elif self.tipo_de_inimigo == 2:
            self.life = 25
        elif self.tipo_de_inimigo == 3:
            self.life = 80
        

    def update(self):
        if self.vivo:
            self.posicao_x += self.velocidade

    def draw(self):
        #INIMIGO MAIS FRACO
        if self.tipo_de_inimigo == 0:
            #ANIMAÇÃO DA MARCHA
            if self.vivo == True:
                if self.animar == True:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,64,8,8,8,7)
                else:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,72,8,8,8,7)

            #ANIMAÇÃO DA MORTE
            if self.vivo == False:
                if self.animar == True:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,64,16,8,8,7)
                else:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,72,16,8,8,7)
        #INIMIGO DE LANÇA
        elif self.tipo_de_inimigo == 1:
            #ANIMAÇÃO DA MARCHA
            if self.vivo == True:
                if self.animar == True:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,48,7,8,9,7)
                else:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,56,7,8,9,7)

            #ANIMAÇÃO DA MORTE
            else:
                if self.animar == True:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,72,39,8,9,7)
                else:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,80,39,16,9,7)

        #INIMIGO DE ESCUDO
        elif self.tipo_de_inimigo == 2:
            #ANIMAÇÃO DA MARCHA
            if self.vivo:
                if self.animar == True:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,0,5,8,10,7)
                else:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,8,5,8,10,7)
                    
            #ANIMAÇÃO DA MORTE
            else:
                if self.animar == True:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,96,37,8,10,7)
                else:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,104,37,16,10,7)
        
        #INIMIGO GIGANTE
        elif self.tipo_de_inimigo == 3:
            #ANIMAÇÃO DA MARCHA
            if self.vivo:
                if self.animar == True:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,16,0,16,16,7)
                else:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,40,48,16,16,7)

            #ANIMAÇÃO DA MORTE
            else:
                if self.animar == True:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,120,32,16,16,7)
                else:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,136,32,16,16,7)

class Chefao:
    def __init__(self,ti, x, y):
        self.posicao_x = x
        self.posicao_y = y
        self.velocidade = -0.1
        self.tipo_de_inimigo = ti
        self.vivo = True
        self.animar = True
        self.life = 2000

    def update(self):
        if self.vivo:
            self.posicao_x += self.velocidade

    def draw(self):
        if self.tipo_de_inimigo == 0:
            pyxel.blt(self.posicao_x,self.posicao_y,0,40,74,16,22,7)

        if self.tipo_de_inimigo == 4:
            if self.vivo:
                if self.animar == True:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,152,4,36,67,7)
                else:
                    pyxel.blt(self.posicao_x,self.posicao_y,0,200,4,36,67,7)

#JOGO
class Jogo:
#DEFINIR CONSTRUCTOR DO JOGO
    def __init__(self):

    #UPGRADES
        self.upgrades = [Upgrades(0,False,51+120,122), Upgrades(1,False,71+120,122), Upgrades(3,False,91+120,122), Upgrades(2,False,111+120,122)]
        self.vida_pode_evoluir = False
        self.dano_pode_evoluir = False
        self.velocidade_pode_evoluir = False
        self.quantidade_de_tiros_pode_evoluir = False
        self.fire_rate = 37
        self.atirou = False


    #CONTADORES
        self.contador_para_waves = 0
        self.indice_de_vidas = 0
        self.relampago_time = 10
        self.tick_fire_rate = self.fire_rate

    #PREÇOS DO UPGRADE
        self.dano_preço = 30
        self.velocidade_preço = 30
        self.qtd_tiros_preço = 30
        self.vida_preço = 150

    #GOLD
        self.gold_total = 50000
        self.gold = []

    #LISTA DE VIDA
        self.vidas = [Vida()]
        
    #LISTA DE INIMIGOS
        self.inimigos = []

    #LISTA DE CASTELO E ARMA
        self.castelo = [Castelo(0,15,83)]
        self.armas = [Arma(40,103)]
    #LISTA DE TIROS
        self.tiros = []
        self.poder_de_ataque = 1
        self.quantidade_de_tiros = 1
        self.velocidade = 1
        self.tipo_de_projétil = 0

    #LISTA DE LUA
        self.lua = [Lua()]

    #LISTA DE ESTRELAS
        self.estrelas = [Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),
                        Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),
                        Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),
                        Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),
                        Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),Estrelas(random.randint(0,5),random.randint(0,255)),
                        Estrelas(random.randint(0,5),random.randint(0,255))]
        

    #LISTA DE NUVENS
        self.nuvens = [Nuvem(random.randint(0,1),random.randint(0,255)),Nuvem(random.randint(0,1),random.randint(0,255)),
                        Nuvem(random.randint(0,1),random.randint(0,255)),Nuvem(random.randint(0,1),random.randint(0,255)),
                        Nuvem(random.randint(0,1),random.randint(0,255))]
        
    #LISTA DE RELAMPAGOS
        self.relampagos = []

    #LISTA DE ARVORES
        self.arvores = [Arvores(150,95),]

    #LISTA DE CHAO
        self.chao = [Chao(16,104),Chao(32,104),Chao(48,104),Chao(64,104),Chao(80,104),
                    Chao(96,104),Chao(112,104),Chao(128,104),Chao(144,104),Chao(160,104),Chao(176,104),
                    Chao(192,104),Chao(208,104),Chao(224,104),Chao(240,104),Chao(256,104)]        

    #LISTA DE MONTANHAS
        self.montanhas = [Montanha(0,88,1),Montanha(0,72,0),Montanha(0,72,2),Montanha(16,88,1),Montanha(32,88,1),Montanha(16,72,1), Montanha(16,56,0),Montanha(32,56,2),Montanha(32,72,1),
            Montanha(32,88,1),Montanha(48,88,1),Montanha(48,72,2),Montanha(64,88,2),Montanha(64,88,0),Montanha(80,88,1),Montanha(96,88,1),Montanha(112,88,1),
            Montanha(128,88,1),Montanha(144,88,1),Montanha(160,88,1),Montanha(176,88,1),Montanha(96,72,1), Montanha(112,72,1),Montanha(128,72,1),Montanha(144,72,1),
            Montanha(160,72,1), Montanha(112,56,1),Montanha(128,56,1), Montanha(144,56,1), Montanha(80,72,0),Montanha(96,56,0), Montanha(112,40,0), Montanha(128,40,1),
            Montanha(144,40,2), Montanha(160,56,2), Montanha(176,72,2),  Montanha(192,88,2),Montanha(176,72,0), Montanha(192,72,2),Montanha(192,88,1), Montanha(208,88,0),
            Montanha(208,88,2), Montanha(224,88,2)]

    #CONFIGURAÇÕES DO  JOGO
        self.estado_de_jogo = inicio_de_jogo
        pyxel.init(255,140)
        pyxel.mouse(True)
        pyxel.load("The_Last_Castle.pyxel")
        pyxel.run(self.update,self.draw)

    
#ATUALIZAR
    def update(self):
    #QUIT
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if self.estado_de_jogo == inicio_de_jogo:
            pyxel.stop(1)
            
        #PLAY
            if pyxel.btn(pyxel.KEY_ENTER):
                self.estado_de_jogo = jogando
                pyxel.sound(1).speed = 90
                pyxel.play(1,1, loop = True)

    #ATUALIZAÇÃO QUANDO O JOGO INICIA
        elif self.estado_de_jogo == jogando:

        #ANIMAÇÃO
            for inimigo in self.inimigos:
                if inimigo.vivo:
                    if pyxel.frame_count % 5 == 0:
                        inimigo.animar = not inimigo.animar
                else:
                    if pyxel.frame_count % 20 == 0:
                        inimigo.animar = False

        #SISTEMA DE UPGRADE
             #TROCAR ICONE DE UPGRADE QUANDO PUDER EVOLUIR
            if self.dano_pode_evoluir == True:
                self.upgrades[0].pode_evoluir = True
            else:
                self.upgrades[0].pode_evoluir = False

            if self.velocidade_pode_evoluir == True:
                self.upgrades[1].pode_evoluir = True
            else:
                self.upgrades[1].pode_evoluir = False

            if self.quantidade_de_tiros_pode_evoluir == True:
                self.upgrades[2].pode_evoluir = True
            else:
                self.upgrades[2].pode_evoluir = False
            
            if self.vida_pode_evoluir == True:
                self.upgrades[3].pode_evoluir = True
            else:
                self.upgrades[3].pode_evoluir = False

        #ATIVADOR ÍCONE DOS UPGRADES COM BASE NO OURO
            if self.gold_total >= self.dano_preço:
                self.dano_pode_evoluir = True 
            else:
                self.dano_pode_evoluir = False
                
            if self.gold_total >= self.velocidade_preço:
                self.velocidade_pode_evoluir = True
            else:
                self.velocidade_pode_evoluir = False

            if self.gold_total >= self.qtd_tiros_preço:
                self.quantidade_de_tiros_pode_evoluir = True
            else:
                self.quantidade_de_tiros_pode_evoluir = False

            if self.gold_total >= self.vida_preço:
                self.vida_pode_evoluir = True
            else:
                self.vida_pode_evoluir = False

        #COMPRAR UPGRADES:
            #EVOLUIR PODER DE ATAQUE
            if 51+120<=pyxel.mouse_x <=67+120 and 122<=pyxel.mouse_y<=138 and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.dano_pode_evoluir:
                self.gold_total -= int(self.dano_preço)
                self.poder_de_ataque += 1
                self.dano_pode_evoluir = False
                self.tipo_de_projétil += 0.2
                self.dano_preço = gold_de_upgrade(self.dano_preço)

            #EVOLUIR VELOCIDADE DE ATAQUE
            if 71+120<= pyxel.mouse_x <= 87+120  and 122<=pyxel.mouse_y<=138 and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.velocidade_pode_evoluir:
                self.gold_total -= int(self.velocidade_preço)
                self.velocidade +=0.2
                self.velocidade_pode_evoluir = False
                self.velocidade_preço = gold_de_upgrade(self.velocidade_preço)
            
            #EVOLUIR FIRE_RATE
            if 91+120<= pyxel.mouse_x <= 107+120  and 122<=pyxel.mouse_y<=138 and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.quantidade_de_tiros_pode_evoluir:
                self.gold_total -= int(self.qtd_tiros_preço)
                self.fire_rate -= 3
                self.tick_fire_rate = self.fire_rate
                self.quantidade_de_tiros_pode_evoluir = False
                self.qtd_tiros_preço = gold_de_upgrade(self.qtd_tiros_preço)

            #EVOLUIR VIDA
            if 111+120<=pyxel.mouse_x <= 127+120 and 122<=pyxel.mouse_y<=138 and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.vida_pode_evoluir:
                self.gold_total-= int(self.vida_preço)
                self.vidas.append(Vida())
                self.vida_pode_evoluir = False
                self.castelo[0].tipo_de_castelo += 1
                self.vida_preço = gold_de_upgrade(self.vida_preço)
               
        #INCREMENTAR CONTADORES
            self.contador_para_waves += 1

        #GERAR INIMIGO
                #WAVE 1
            if self.contador_para_waves> 100 and self.contador_para_waves<103:
                    self.inimigos.append(Inimigo(0))
                    #self.inimigos.append(Chefao(4,255,40))
                    
                #WAVE 2
            if self.contador_para_waves> 500 and self.contador_para_waves<508:
                self.inimigos.append(Inimigo(0))
                pyxel.sound(1).speed = 80

                #WAVE 3
            if self.contador_para_waves>1100 and self.contador_para_waves<1113:
                self.inimigos.append(Inimigo(0))
            if self.contador_para_waves>1110 and self.contador_para_waves<1114:
                self.inimigos.append(Inimigo(0))
                pyxel.sound(1).speed = 70

                #WAVE 4
            if self.contador_para_waves>1800 and self.contador_para_waves<1815:
                self.inimigos.append(Inimigo(0))
            if self.contador_para_waves>1810 and self.contador_para_waves<1816:
                self.inimigos.append(Inimigo(1))
                pyxel.sound(1).speed = 60

                #WAVE 5
            if self.contador_para_waves>2600 and self.contador_para_waves<2615:
                self.inimigos.append(Inimigo(1))
                pyxel.sound(1).speed = 50

                #WAVE 6
            if self.contador_para_waves>3300 and self.contador_para_waves<3320:
                self.inimigos.append(Inimigo(1))
                

                #WAVE 7
            if self.contador_para_waves>3900 and self.contador_para_waves<3931:
                pyxel.sound(1).speed = 45
                self.inimigos.append(Inimigo(0))
            if self.contador_para_waves>3920 and self.contador_para_waves<3921:
                self.inimigos.append(Inimigo(1))
            if self.contador_para_waves>3935 and self.contador_para_waves<3940:
                self.inimigos.append(Inimigo(0))

                #WAVE 8
            if 4500 <self.contador_para_waves<4510:
                self.inimigos.append(Inimigo(2))
                

                #WAVE 9
            if 5200 <self.contador_para_waves<5230:
                pyxel.sound(1).speed = 30
                self.inimigos.append(Inimigo(0))
            if 5230 <self.contador_para_waves<5250:
                self.inimigos.append(Inimigo(1))
            if 5250 <self.contador_para_waves<5265:
                self.inimigos.append(Inimigo(2))
            
                #WAVE 10
            if 5800 <self.contador_para_waves<5802:
                self.inimigos.append(Inimigo(3))
            
                #WAVE 11
            if 6500 <self.contador_para_waves<6530:
                pyxel.sound(1).speed = 25
                self.inimigos.append(Inimigo(2))
            if 6524 <self.contador_para_waves<6530:
                self.inimigos.append(Inimigo(3))
                

                #WAVE 12
            if 7210 <self.contador_para_waves<7250:
                self.inimigos.append(Inimigo(2))
            if 7239 <self.contador_para_waves<7250:
                self.inimigos.append(Inimigo(3))

                #CHEFÃO
            if 8000<self.contador_para_waves<8002:
                self.inimigos.append(Chefao(4,255,40))

        #MOVER INIMIGO
            for inimigo in self.inimigos:
                inimigo.update()
                
        #DANO AO CASTELO
                if inimigo.posicao_x <= 30:
                    self.indice_de_vidas -= 1
                    self.inimigos.remove(inimigo)
                    self.vidas[self.indice_de_vidas].cheio = False
            
        #VERIFICADOR DE VIDA DO CASTELO
            if self.indice_de_vidas == (len(self.vidas)*-1):
                self.estado_de_jogo = game_over
                pyxel.stop(1)

        #MUDAR SPRITE DA ARMA
            for arma in self.armas:
                if pyxel.mouse_y <103:
                    arma.arma = 2
                elif pyxel.mouse_y >103:
                    arma.arma = 0
                else:
                    arma.arma = 1
            
        #GERAR TIRO
            
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.tick_fire_rate == self.fire_rate and self.atirou == False:
                #pyxel.play(2,4)
                self.tiros.append(Tiros(self.tipo_de_projétil,self.velocidade,40,105))
                self.atirou = True

            if self.atirou:
                self.tick_fire_rate -= 1

            if self.tick_fire_rate <=0:
                self.tick_fire_rate = self.fire_rate
                self.atirou = False

        #MOVER PROJÉTIL
            for tiro in self.tiros:
                tiro.update()
                if tiro.posicao_x > 255 or tiro.posicao_x<0 or tiro.posicao_y>140 or tiro.posicao_y<0:
                    self.tiros.remove(tiro)
                    
        #DANO AOS INIMIGOS
                for inimigo in self.inimigos:
                    if inimigo.vivo:
                        if inimigo.tipo_de_inimigo == 4:
                            if tiro.posicao_x >= inimigo.posicao_x + 16 and tiro.posicao_x < inimigo.posicao_x + 50 and inimigo.posicao_y <= tiro.posicao_y<= inimigo.posicao_y+67:
                                inimigo.life -= self.poder_de_ataque
                                try:
                                    self.tiros.remove(tiro)
                                except:
                                    None

                                if inimigo.life <= 0:
                                    self.estado_de_jogo = win
                                    pyxel.stop(1)
                                    pyxel.play(1,5, loop= True)

                        if inimigo.tipo_de_inimigo == 3:
                            if tiro.posicao_x >= inimigo.posicao_x + 4 and tiro.posicao_x < inimigo.posicao_x + 16 and inimigo.posicao_y <= tiro.posicao_y<= inimigo.posicao_y+16:
                                inimigo.life -= self.poder_de_ataque
                                if inimigo.life <= 0:
                                    if inimigo.pode_dar_ouro:
                                        self.gold_total+=100
                                        inimigo.pode_dar_ouro = False
                                    inimigo.vivo = False
                                try:
                                    self.tiros.remove(tiro)
                                except:
                                    None

                        if inimigo.tipo_de_inimigo == 2:
                            if tiro.posicao_x >= inimigo.posicao_x + 2 and tiro.posicao_x < inimigo.posicao_x + 6 and inimigo.posicao_y <= tiro.posicao_y<= inimigo.posicao_y+8:
                                inimigo.life -= self.poder_de_ataque
                                if inimigo.life <= 0:
                                    if inimigo.pode_dar_ouro:
                                        self.gold_total+=50
                                        inimigo.pode_dar_ouro = False
                                    inimigo.vivo = False
                                try:
                                    self.tiros.remove(tiro)
                                except:
                                    None

                        if inimigo.tipo_de_inimigo == 1:
                            if tiro.posicao_x >= inimigo.posicao_x + 2 and tiro.posicao_x < inimigo.posicao_x + 6 and inimigo.posicao_y <= tiro.posicao_y<= inimigo.posicao_y+8:
                                inimigo.life -= self.poder_de_ataque
                                if inimigo.life <= 0:
                                    if inimigo.pode_dar_ouro:
                                        self.gold_total+=25
                                        inimigo.pode_dar_ouro = False
                                    inimigo.vivo = False
                                try:
                                    self.tiros.remove(tiro)
                                except:
                                    None

                        if inimigo.tipo_de_inimigo == 0:
                            if tiro.posicao_x >= inimigo.posicao_x + 2 and tiro.posicao_x < inimigo.posicao_x + 6 and inimigo.posicao_y <= tiro.posicao_y<= inimigo.posicao_y+8:
                                inimigo.life -= self.poder_de_ataque
                                if inimigo.life <= 0:
                                    if inimigo.pode_dar_ouro:
                                        self.gold_total+= 15
                                        inimigo.pode_dar_ouro = False
                                    inimigo.vivo = False
                                try:
                                    self.tiros.remove(tiro)
                                except:
                                    None        
                              
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
            
        #ADICIONAR RELAMPAGOS
            for i in range(random.randint(0,100)):                                                                  #LOOP COM UM TEMPO ALEATÓRIO PARA OS RELAMPAGOS APARECEREM
                nuvem = self.nuvens[random.randint(0,len(self.nuvens)-1)]                                           #UMA NUVEM ALEATÓRIA DA LISTA SELF.NUVENS
                if nuvem.indice == 0:
                    self.relampagos.append(Relampago(random.randint(0,60),nuvem.posicao_x+6,nuvem.posicao_y+13))    #RELAMPAGOS APARECEM NA NUVEM DEFINIDA
                else:
                    self.relampagos.append(Relampago(random.randint(0,100),nuvem.posicao_x+4,nuvem.posicao_y+6))
                self.relampago_time -= 1                                                                            #DECREMENTADOR PARA O RELAMPAGO DESAPARECER
                for relampago in self.relampagos:
                    if self.relampago_time <=0:
                        self.relampagos.remove(relampago)                                                           #RELAMPAGO DESAPARECE
                
                
                    
    #GAME OVER, RESETAR JOGO
        if self.estado_de_jogo == game_over:
            if pyxel.btnr(pyxel.KEY_ENTER):
                self.estado_de_jogo = inicio_de_jogo
                reset(self)

    #VITÓRIA
        if self.estado_de_jogo == win:
            if pyxel.btnr(pyxel.KEY_ENTER):
                self.estado_de_jogo = inicio_de_jogo
                reset(self)
                
#DESENHAR             
    def draw(self):
    #TIRAR RASTRO
        pyxel.cls(0)

    #MENU PRINCIPAL
        if self.estado_de_jogo == inicio_de_jogo:
            pyxel.text(122,50,"The Last Castle",8)
            pyxel.text(10,95,"Pressione 'enter' para jogar", 7)
            pyxel.text(10,105,"Pressione 'Q' para sair", 7)
            Castelo(0,30,40).draw()

    #QUANDO O JOGO INICIAR

        if self.estado_de_jogo == jogando:
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
            for montanha in self.montanhas:
                montanha.draw()
            
        #CHEFAO NA MONTANHA
            
            Chefao(0,128,18).draw()

        #RELAMPAGOS
            for Relampago in self.relampagos:
                Relampago.draw()

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

        #OURO DE INIMIGO
            for ouro in self.gold:
                ouro.draw()

        # CASTELO
            for castelo in self.castelo:
                castelo.draw()

        #TIROS
            for tiro in self.tiros:
                tiro.draw()

        #ARMA
            for arma in self.armas:
                arma.draw()

        #ARVORES
            for arvore in self.arvores:
                arvore.draw(0)
            Arvores(122,104).draw(1)
            Arvores(220,109).draw(1)

        #MENU DE UPGRADE
            pyxel.rect(0,119,255,140,0)        #BORDA VERLMELHA
            pyxel.rect(2+120,121,131,138,0)        #RETANGULO PRETO ESQUERDO
            pyxel.rect(133+120,120,255,140,0)      #RETANGULO PRETO DIREITO
            pyxel.text(5+120,127,"UPGRADES",9)
            for upgrade in self.upgrades:
                upgrade.draw()


        #VIDAS
            for i, vida in enumerate(self.vidas):
                vida.draw(i*13, 0)
            
        #OURO:
            Ouro(0,215).draw()
            pyxel.text(235,6,"{}".format(self.gold_total),9)

    #TELA DE GAME OVER
        if self.estado_de_jogo == game_over:
            pyxel.cls(0)
            Castelo(0,30,40).draw()
            pyxel.text(75,55,"O CASTELO FOI DESTRUIDO, FIM DE JOGO!",8)
            pyxel.text(20,90,"Pressione 'enter' para voltar ao menu do jogo",7)
            pyxel.text(20,100,"Pressione 'Q' para sair", 7)
    
    #TELA DE VITÓRIA
        if self.estado_de_jogo == win:
            pyxel.cls(7)
            Castelo(5,100,20).draw()
            pyxel.text(5,55,"VOCE CONSEGUIU SOBREVIVER E DERROTOU O EXÉRCITO MALIGNO!",random.randint(0,16))
            pyxel.text(30,70,"VOCE SALVOU A HUMANIDADE!", random.randint(0,16))
            pyxel.text(60,90,"Pressione 'enter' para voltar ao menu do jogo",0)
            pyxel.text(100,100,"Pressione 'Q' para sair", 0)
            

Jogo()