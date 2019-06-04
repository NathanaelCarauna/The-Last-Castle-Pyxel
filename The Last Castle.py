import pyxel
import euclid3
import random

#MODOS DE JOGO:
inicio_de_jogo = 0
jogando = 1
game_over = 2

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
                pyxel.blt(self.posicao_x,self.posicao_y, 0,80,0,16,16,0)
            else:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,80,16,16,16,0)

        if self.upgrade == 1:
            if self.pode_evoluir == False:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,96,0,16,16,0)
            else:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,96,16,16,16,0)

        if self.upgrade == 2:
            if self.pode_evoluir == False:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,112,0,16,16,0)
            else:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,112,16,16,16,0)

        if self.upgrade == 3:
            if self.pode_evoluir == False:
                pyxel.blt(self.posicao_x,self.posicao_y, 0,128,0,16,16,0)
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
    def __init__(self,x,y,i=False):
        self.posicao_x = x
        self.posicao_y = y
        self.recebeu_dano = i

    def draw(self):
        if self.recebeu_dano == False:
            pyxel.blt(self.posicao_x,self.posicao_y,0,32,112,16,16,7)
            
        else:
            pyxel.blt(self.posicao_x,self.posicao_y,0,32,96,16,16,7)

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
        if self.tipo_de_castelo == 0:
            pyxel.blt(self.posicao_x, self.posicao_y,0,0,48,27,32,7)
        if self.tipo_de_castelo == 2:
            pyxel.blt(self.posicao_x, self.posicao_y,0,96,96,32,32,7)

#TIROS
class Tiros:
    def __init__(self,i, v, x= 30, y=88):
        self.posicao_x = x
        self.posicao_y = y
        self.tipo_de_projetil = i
        self.velocidade_x = 1*v
    
    def update(self):
        self.posicao_x += self.velocidade_x

    def draw(self):
        if 0 <= self.tipo_de_projetil <1 :
            pyxel.blt(self.posicao_x,self.posicao_y,0,64,6,2,3,7)
        if 1 <= self.tipo_de_projetil < 2:
            pyxel.blt(self.posicao_x,self.posicao_y,0,64,2,2,3,7)
        if 2 <= self.tipo_de_projetil < 3:
            pyxel.blt(self.posicao_x,self.posicao_y,0,64,0,2,3,7)
        if 3 <= self.tipo_de_projetil <= 4:
            pyxel.blt(self.posicao_x,self.posicao_y,0,64,4,2,3,7)

#INIMIGOS
class Inimigo:
    def __init__(self,ti, x=255):
        self.tipo_de_inimigo = ti
        self.posicao_x = x
        self.posicao_y = random.randint(99,102)
        self.velocidade = -1*(random.randint(1,8)/10)
        #if self.tipo_de_inimigo == 0:
        self.life = 3
        if self.tipo_de_inimigo == 1:
            self.life = 9
        elif self.tipo_de_inimigo == 2:
            self.life = 30
        elif self.tipo_de_inimigo == 3:
            self.life = 80
    
    def update(self):
        self.posicao_x += self.velocidade

    def draw(self):
        if self.tipo_de_inimigo == 0:
            pyxel.blt(self.posicao_x,self.posicao_y,0,64,8,8,8,7)
        elif self.tipo_de_inimigo == 1:
            pyxel.blt(self.posicao_x,self.posicao_y,0,48,7,8,9,7)
        elif self.tipo_de_inimigo == 2:
            pyxel.blt(self.posicao_x,self.posicao_y,0,0,5,8,10,7)
        elif self.tipo_de_inimigo == 3:
            pyxel.blt(self.posicao_x,self.posicao_y,0,16,0,16,16,7)

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
#DEFINIR CONSTRUCTOR DO JOGO
    def __init__(self):

    #UPGRADES
        self.upgrades = [Upgrades(0,False,51,122), Upgrades(1,False,71,122), Upgrades(3,False,91,122), Upgrades(2,False,111,122)]
        self.vida_pode_evoluir = False
        self.dano_pode_evoluir = False
        self.velocidade_pode_evoluir = False
        self.quantidade_de_tiros_pode_evoluir = False
        #self.bonus_de_ouro_pode_evoluir = False
        #self.tiro_perfurador_pode_evoluir = False

    #CONTADORES
        self.contador_para_waves = 0
        self.indice_de_vidas = 0
        self.relampago_time = 10

    #GOLD
        self.gold_total = 0
        self.gold = []
        self.gold_time = 200
        self.bonificador = 1.0

    #LISTA DE VIDA
        self.vidas = [Vida(0,0), Vida(13,0), Vida(26,0), Vida(39,0)] 
        

    #LISTA DE INIMIGOS
        self.inimigos = []

    #LISTA DE CASTELO
        self.castelo = [Castelo(0,15,79)]

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
        #PLAY
            if pyxel.btn(pyxel.KEY_ENTER):
                self.estado_de_jogo = jogando

    #ATUALIZAÇÃO QUANDO O JOGO INICIA
        elif self.estado_de_jogo == jogando:

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
            if self.gold_total >= 75:
                self.dano_pode_evoluir = True
                self.velocidade_pode_evoluir = True
            else:
                self.dano_pode_evoluir = False
                self.velocidade_pode_evoluir = False

            if self.gold_total >= 150:
                self.vida_pode_evoluir = True
            else:
                self.vida_pode_evoluir = False

        #COMPRAR UPGRADES:
            if 51<=pyxel.mouse_x <=67 and 122<=pyxel.mouse_y<=138 and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.dano_pode_evoluir:
                self.gold_total -= 75
                self.poder_de_ataque += 1
                self.dano_pode_evoluir = False
                self.tipo_de_projétil += 0.2

            if 71<= pyxel.mouse_x <= 87  and 122<=pyxel.mouse_y<=138 and pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and self.velocidade_pode_evoluir:
                self.gold_total -= 75
                self.velocidade +=0.2
                self.velocidade_pode_evoluir = False

                
        #INCREMENTAR CONTADORES
            self.contador_para_waves += 1
            self.gold_time -= 1

        #GERAR INIMIGO
                #WAVE 1
            if self.contador_para_waves> 100 and self.contador_para_waves<106:
                    self.inimigos.append(Inimigo(0))
                    
                #WAVE 2
            if self.contador_para_waves> 500 and self.contador_para_waves<511:
                self.inimigos.append(Inimigo(0))

                #WAVE 3
            if self.contador_para_waves>900 and self.contador_para_waves<916:
                self.inimigos.append(Inimigo(0))
            if self.contador_para_waves>910 and self.contador_para_waves<916:
                self.inimigos.append(Inimigo(1))

                #WAVE 4
            if self.contador_para_waves>1300 and self.contador_para_waves<1321:
                self.inimigos.append(Inimigo(0))
            if self.contador_para_waves>1310 and self.contador_para_waves<1321:
                self.inimigos.append(Inimigo(1))

                #WAVE 5
            if self.contador_para_waves>1700 and self.contador_para_waves<1731:
                self.inimigos.append(Inimigo(1))

                #WAVE 6
            if self.contador_para_waves>2100 and self.contador_para_waves<2151:
                self.inimigos.append(Inimigo(1))
            
                #WAVE 7
            if self.contador_para_waves>2700 and self.contador_para_waves<2751:
                self.inimigos.append(Inimigo(0))
            if self.contador_para_waves>2720 and self.contador_para_waves<2751:
                self.inimigos.append(Inimigo(1))
            if self.contador_para_waves>2735 and self.contador_para_waves<2751:
                self.inimigos.append(Inimigo(2))

        #MOVER INIMIGO
            for inimigo in self.inimigos:
                inimigo.update()
                
                #DANO AO CASTELO
                if inimigo.posicao_x <= 30:
                    self.indice_de_vidas -= 1
                    self.inimigos.remove(inimigo)
                    self.vidas[self.indice_de_vidas].recebeu_dano = True
            
        #VERIFICADOR DE VIDA DO CASTELO
            if self.indice_de_vidas == (len(self.vidas)*-1):
                self.estado_de_jogo = game_over

        #GERAR TIRO
            if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and pyxel.mouse_y <= 120:
                self.tiros.append(Tiros(self.tipo_de_projétil,self.velocidade,30,105))

        #MOVER PROJÉTIL
            for tiro in self.tiros:
                tiro.update()
                if tiro.posicao_x > 255:
                    self.tiros.remove(tiro)
                #DANO AOS INIMIGOS
                for inimigo in self.inimigos:
                    if tiro.posicao_x >= inimigo.posicao_x:
                        inimigo.life -= self.poder_de_ataque
                        if inimigo.life <= 0:

                            #INIMIGOS COM VALORES DIFERENTES
                            if inimigo.tipo_de_inimigo == 0:
                                self.gold_total += 10
                            elif inimigo.tipo_de_inimigo == 1:
                                self.gold_total += 25
                            elif inimigo.tipo_de_inimigo == 2:
                                self.gold_total += 50
                            elif inimigo.tipo_de_inimigo == 3:
                                self.gold_total += 100
                            self.inimigos.remove(inimigo)
                            self.gold.append(Ouro(1, inimigo.posicao_x, inimigo.posicao_y-5))

                        try:
                            self.tiros.remove(tiro)
                        except:
                            None

        #OURO SOBRE OS INIMIGOS
            for ouro in self.gold:
                ouro.update()
                if self.gold_time <=0:
                    self.gold.remove(ouro)        

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
                self.indice_de_vidas = 0
                self.contador_para_waves = 0
                self.inimigos = []
                self.tiros = []
                self.tipo_de_projétil = 0
                self.velocidade = 1
                self.poder_de_ataque = 1
                self.gold_total = 0
                for vida in  self.vidas:
                    vida.recebeu_dano = False

#DESENHAR             
    def draw(self):
    #TIRAR RASTRO
        pyxel.cls(0)

    #MENU PRINCIPAL
        if self.estado_de_jogo == inicio_de_jogo:
            pyxel.text(122,50,"The Last Castle",8)
            pyxel.text(10,95,"Pressione 'enter' para jogar", 7)
            pyxel.text(10,105,"Pressione 'Q' para sair", 7)
            Castelo(2,30,40).draw()

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
            Chefao(128,18).draw()

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

        #ARVORES
            for arvore in self.arvores:
                arvore.draw(0)
            Arvores(122,104).draw(1)
            Arvores(220,109).draw(1)

        #MENU DE UPGRADE
            pyxel.rect(0,120,255,140,8)        #BORDA ROSA
            pyxel.rect(2,121,131,138,0)        #RETANGULO PRETO ESQUERDO
            pyxel.rect(133,120,255,140,0)      #RETANGULO PRETO DIREITO
            pyxel.text(5,127,"UPGRADES",9)
            for upgrade in self.upgrades:
                upgrade.draw()


        #VIDAS
            for vida in self.vidas:
                vida.draw()
            
        #OURO:
            Ouro(0,215).draw()
            pyxel.text(235,6,"{}".format(self.gold_total),9)

    #TELA DE GAME OVER
        if self.estado_de_jogo == game_over:
            pyxel.cls(0)
            pyxel.text(100,55,"O CASTELO FOI DESTRUIDO",8)
            pyxel.text(100,90,"Pressione 'enter'",7)
            pyxel.text(100,100,"'Q' para sair", 7)
            

Jogo()