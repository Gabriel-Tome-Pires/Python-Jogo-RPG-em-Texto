import random
import time

CritRate = [1,2,3,4,5,6,7,8,9,10]
enemy = 0
xp = 0
nv = 1
imunPoi =False
imunBur = False
loot = 0

#FUNÇÕES DAS CONDIÇÕES

def burning(who):
  dano = random.randint(30,45)
  print('\033[31m{} recebeu {} de dano, pois está queimando\033[m'.format(who, dano))
  return dano

def curing(who):
  cura = random.randint(40, 60)
  print(f'\033[32m{who} curou {cura} pontos da própria vida\033[m')
  return cura

def RouboVida(who):
  dano = random.randint(30,40)
  print(f'\033[32m{who} curou {dano/1.2} pontos da própria vida\033[31m\nCausando {dano} de dano\033[m')

def poisoned(who):
    dano = random.randint(30,35)
    print('\033[35m{} recebeu {} de dano, pois está envenenado\033[m'.format(who, dano))
    return dano
  

nome = str(input('Digite o nome do personagem '))
nome = nome.strip()

clas = int(input('Escolha uma das seguintes classes: \033[35m1-mago \033[31m2-guerreiro \033[33m3-monge \033[32m4-druida \033[m'))

print('\nExplicações dos movimentos')
print('<>'*20)
if clas == 1: # MAGO
 atk = atkT = 40
 defe = defeT = 10
 life = 250
 speed = speedT = 20
 print('Incendiar: causa dano e deixa o inimigo queimando(dano pelos próximos turnos)\n')
 print('Terremoto: Golpe de dano comum, mas impossível de errar em qualquer situação\n')
 print('Raio arcano: Toda vez que o golpe for usado, mais forte ele fica, se usar outro golpe, o poder desse zera\n')
 enrolação = input('Aperte enter para continuar')
 Golpe_NV2 = 'Chuva de granizo: Causa baixo dano, mas congela o inimigo, o que causa pouco dano de dano por turno,\n além de temporariamente diminuir defesa e velocidade inimigas' 
 Golpe_NV4 = 'Raio de trovão: Causa dano alto, chance de paralizar o inimigo, dificultando o acerto de golpes dele'

if clas == 2: # GUERREIRO
 atk = atkT = 35
 defe = defeT = 25
 life = 180
 speed = speedT = 15
 print('Machadinhas: Dano baixo, mas é usado várias vezes\n')    
 print('Arco e Flecha: dano comum, mas acerto crítico mais comum e mais poderoso\n')
 print('Machado de guerra: Dano maior, mas maiores chances de errar golpe\n')
 enrolação = input('Aperte enter para continuar')
 Golpe_NV2 = 'Fúria: Toda vez que o golpe for usado, mais forte ele fica, se usar outro golpe ou errar ele, o poder desse zera'
 Golpe_NV4 = 'Modo bersequer: Todos os status negativos são curados, e seus status sobem temporariamente'

if clas == 3: # DRUIDA
 atk= atkT = 30
 defe= defeT = 12
 life =  120
 speed = speedT = 20
 print('Orbe cósmico: Causa alto dano, mas dá ao jogador um efeito aleatório(pode ser positivo ou negativo)\n')  
 print('Selva incontrolável: dá muito dano no adversário, mas devolve parte do dano para você')
 print('Karma: todos os status negativos que estão em você passam para o adversário\nObs:Você não é curado deles')
 enrolação = input('Aperte enter para continuar')
 Golpe_NV2 = 'Raio druídico: ao ser usado uma vez, tem 50%, de chance de ser repetido no próximo turno, sem gastar sua ação do turno'
 Golpe_NV4 = 'Cólera da Natureza: causa roubo de vida e diminui todos os status inimigos'

if clas == 4: # MONGE
 atk = atkT = 28
 defe = defeT = 15
 life = 160
 speed = speedT = 27
 print('Mãos que curam: cura sua vida')
 print('Esmaga ossos: Causa dano e diminui permanentemente a defesa inimiga')
 print('Pressão espiritual: Causa dano e diminui permanentemente a velocidade inimiga')
 enrolação = input('Aperte enter para continuar')
 Golpe_NV2 = 'Paz interior: causa dano e diminui o ataque inimigo'
 Golpe_NV4 = 'Ajuda divina: tem cura constante por certo números de turnos'
def combate(enemy, nv, atk=atk, defe=defe, life=life, speed=speed, imunPoi=imunPoi, imunBur=imunBur):
  danoA = 0
  Dano_Intermediario=0
  atkT = atk
  defeT = defe
  lifeT = life
  speedT = speed
#CONDIÇÕES
  EnemyParalized = 0
  AlyParalized = 0
  EnemyBurning = 0
  AlyBurning = 0
  EnemyPoisoned = 0
  AlyPoisoned = 0
  AlyCure = 0
  EnemyCure = 0
  AlyRoubo = 0
  EnemyRoubo = 0
  AlyFreezing = 0
  EnemyFreezing = 0
  #status do inimigo
  if enemy == 1:
      atki= atkiT = 25
      defei= defeiT = 5
      lifei= lifeiT = 120
      speedi= speediT = 5
      nomeI = 'zumbi'
  if enemy == 2:
      atki= atkiT = 27
      defei= defeiT = 3
      lifei= lifeiT = 200
      speedi= speediT = 2
      nomeI = 'horda de goblins'
  if enemy == 3:
      atki= atkiT = 25
      defei= defeiT = 5
      lifei= lifeiT = 120
      speedi= speediT = 15
      nomeI = 'vampiro'
  if enemy == 4:
      atki= atkiT = 30
      defei= defeiT = 5
      lifei= lifeiT = 100
      speedi= speediT = 20
      nomeI = 'bandido'
  if enemy == 5:
      atki= atkiT = 40
      defei= defeiT = 15
      lifei= lifeiT = 150
      speedi= speediT = 12
      nomeI = 'Rei goblin'
  if enemy == 6:
      atki= atkiT = 50
      defei= defeiT = 15
      lifei= lifeiT = 110
      speedi= speediT = 15
      nomeI = 'Dragão jovem'
  if enemy == 7:
      atki= atkiT = 30
      defei= defeiT = 30
      lifei= lifeiT = 150
      speedi= speediT = 8
      nomeI = 'Draconato'
  if enemy == 8:
      atki= atkiT = 60
      defei= defeiT = 8
      lifei= lifeiT = 220
      speedi= speediT = 1
      nomeI = 'Dragão Ancião'
  if enemy == 9:
      atki= atkiT = 65
      defei= defeiT = 15
      lifei= lifeiT = 250
      speedi= speediT = 5
      nomeI = 'Tiamat'
  if enemy == 10:
      atki= atkiT = 50
      defei= defeiT = 0
      lifei= lifeiT = 250
      speedi= speediT = 3
      nomeI = 'Morfgan'
  if enemy == 11:
      atki= atkiT = 30
      defei= defeiT = 5
      lifei= lifeiT = 140
      speedi= speediT = 6
      nomeI = 'Jovem mago'
  if enemy == 12:
      atki= atkiT = 40
      defei= defeiT = 8
      lifei= lifeiT = 220
      speedi= speediT = 7
      nomeI = 'Arqui-mago'
  if enemy == 13:
      atki= atkiT = 50
      defei= defeiT = 10
      lifei= lifeiT = 210
      speedi= speediT = 12
      nomeI = 'Tauros'
  if enemy == 14:
      atki= atkiT = 30
      defei= defeiT = 2
      lifei= lifeiT = 120
      speedi= speediT = 20
      nomeI = 'Slime'
  if enemy == 15:
      atki= atkiT = 35
      defei= defeiT = 4
      lifei= lifeiT = 140
      speedi= speediT = 25
      nomeI = 'Rei slime'
  if enemy == 16:
      atki= atkiT = 45
      defei= defeiT = 20
      lifei= lifeiT = 250
      speedi= speediT = 20
      nomeI = 'Elemental supremo'
  if enemy == 17:
      atki= atkiT = 35
      defei= defeiT = 50
      lifei= lifeiT = 120
      speedi= speediT = 1
      nomeI = 'Tartaruga gigante'
  if enemy == 18:
      atki= atkiT = 32
      defei= defeiT = 15
      lifei= lifeiT = 120
      speedi= speediT = 4
      nomeI = 'Soldado'
  if enemy == 19:
      atki= atkiT = 35
      defei= defeiT = 20
      lifei= lifeiT = 300
      speedi= speediT = 8
      nomeI = 'Joia da alma'
  if enemy == 20:
      atki= atkiT = 40
      defei= defeiT = 10
      lifei= lifeiT = 320
      speedi= speediT = 15
      nomeI = 'Capitão'

  print(f'\nUm {nomeI} apareceu')

  print('\033[4;31mO COMBATE FOI INICIADO\033[m')
  print('<>'*20)
  time.sleep(1)
  # COMBATE
  FimDoCombate = False
  turn = 0
  while FimDoCombate == False:
    time.sleep(1) 
    turn +=1
    print('Turno {}'.format(turn))
    print('<>'*20)

    #ÁREA DAS CONDIÇÕES DOS HERÓIS: INÍCIO
    if AlyFreezing > 0:
      AlyFreezing-=1
      time.sleep(1)
      dano = random.randint(15,20)
      life-=dano
      if defe > (defeT/100)*60:
       defe -= 6
      if speed > (speedT/100)*50:
       speed -= 6
      print(f'\033[36m{nome} recebeu {dano} de dano pois está congelando\nSua velocidade e defesa também caíram\033[m')
      if AlyFreezing == 0:
        defe = defeT
        speed = speedT
    
    if AlyParalized > 0:
      speedi = 85
      AlyParalized -= 1
      print(f'\033[33m{nome} está paralizado\ndifícilmente acertará um golpe assim\033[m')
      if AlyParalized == 0:
        speedi = speediT

    if AlyBurning > 0 & imunBur == False:
      AlyBurning-=1
      time.sleep(1)
      dano = burning(nome)
      life -=dano
    
    if AlyCure > 0:
      AlyCure-=1
      time.sleep(1)
      cura = curing(nome)
      life += cura

    if AlyRoubo > 0:
      AlyRoubo-=1
      time.sleep(1)  
      dano = RouboVida(nome)
      life += dano/1.25
      lifei -= dano  

    if AlyPoisoned > 0 & imunPoi == False:
      AlyPoisoned-=1
      time.sleep(1)
      dano = poisoned(nome)
      life -=dano
    #ÁREA DAS CONDIÇÕES DOS HERÓIS: FIM
    time.sleep(1)
    if clas == 1:
      #MAGO
          print('Escolha um dos movimentos: \033[31m1-Incendiar\033[m \033[32m2-Terremoto\033[35m 3-Raio arcano \033[m')
          if nv >= 2:
            print('\033[36m4-Chuva de granito\033[m')#pouco dano. dá congelar
          if nv >= 4:
            print('\033[33m5-Raio de trovão\033[m')#dano alto. chance de paralisar
          ChoseMove = int(input(''))
          i = random.choice(CritRate)
          time.sleep(1)
          #BOLA DE FOGO 
          #dano comum, faz o inimigo queimar por 1, 2 ou 3 turnos.
          if speedi < random.randint(1,100) or ChoseMove == 2:
            if ChoseMove == 1:
              danoA=0
              TurnRange = [1,2,3]
              EnemyBurning = random.choice(TurnRange)
              #CRÍTICO
              if i == 1:
                dano = atk
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                print('\033[33mO inimigo está pegando fogo\033[m') 
                lifei -= dano
                EnemyBurning +=2
              #FIM CRÍTICO
              else:
                print('\033[33mO inimigo está pegando fogo\033[m') 
                dano = atk - defei*0.01*atk - 4
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano
            
            #TERREMOTO 
            #impossível errar esse ataque. dano comum
            if ChoseMove == 2:
              danoA = 0
            #CRÍTICO
              if i == 1:
                dano = atk*1.3
                print('CRÍTICO!!!')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano
              #FIM CRÍTICO
              else:
                dano = atk - defei*0.01*atk
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano

            #RAIO ARCANO
            #toda vez que seu usa raio arcano e se acerta, o dano de raio arcano aumenta. dano começa baixo
            if ChoseMove == 3:
              #CRÍTICO
              if i == 1:
                danoA += atk/2
                lifei -= danoA
                print('CRÍTICO!!!')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, danoA))

              #FIM CRÍTICO
              else:
                danoA += (atk - defei*0.01*atk)/2
                lifei -= danoA
                print('\033[33m{} causou {} de dano\033[m'.format(nome, danoA))
            
            #CHUVA DE GRANITO
            #dano baixo, dá congelar
            if ChoseMove == 4 and nv >= 2:
            #CRÍTICO
              danoA=0
              if i == 1:
                EnemyFreezing = random.randint(2,4)
                dano = atk*0.75
                lifei -= dano
                print('CRÍTICO!!!')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))

              #FIM CRÍTICO
              else:
                EnemyFreezing = random.randint(1,3)
                dano = atk - defei*0.01*atk
                lifei -= dano
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
            elif ChoseMove == 4 and nv == 1: 
                print('Esta magia é muito avançada, você falhou em conjurá-la')
            
            #TROVÃO
            if ChoseMove == 5 and nv >= 4:
            #CRÍTICO
              danoA = 0
              if i == 1:
                dano = atk*1.6
                lifei -= dano
                print('CRÍTICO!!!')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))

              #FIM CRÍTICO
              else:
                dano = atk*1.2
                lifei -= dano
                ParChance = random.randint(1,100)
                if ParChance >= 60:
                  EnemyParalized = random.randint(1,3)
                  print(f'{nomeI} foi paralizado')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
            elif ChoseMove == 5 and nv <= 3: 
                print('Esta magia é muito avançada, você falhou em conjurá-la')
          else:
            print(f'{nomeI} desviou do seu ataque')
            danoA = 0
    if clas == 2:
      #GUERREIRO
          if duration > 0:
            duration-=1
            if duration > 0:
             print(f'Modo bersequer durará mais {duration} turnos')
            if duration == 0:
             atk = atkT
             defe = defeT
             speed = speedT
            print('O modo bersequer acabou')
          print('Escolha um dos movimentos: \033[31m1-Machadinhas\033[m \033[32m2-Arco e Flecha\033[m 3-Machado de Guerra ')
          if nv >= 2:
            print('4-Fúria ')
          if nv >= 4:
            print('5-Modo Bersequer ')
          ChoseMove = int(input())
          i = random.choice(CritRate)
          time.sleep(1)
          if speedi < random.randint(1,100):
          #MACHADINHAS
           if ChoseMove == 1:
            Dano_Intermediario = 0
            repete= random.randint(1,6)
            for c in range(repete):
              i = random.randint(1,5)
              #CRÍTICO 
              if i == 1:
              
                dano = atk
                print('CRÍTICO!!!')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano/2
                time.sleep(1)
                #FIM CRÍTICO
              else:
                dano = atk - defei*0.01*atk
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano/3
                time.sleep(1)

          #ARCO E FLECHA
           if ChoseMove == 2:
            Dano_Intermediario = 0
          #CRÍTICO
            if i >= 8:
              dano = atk*1.6
              print('CRÍTICO!!!')
              print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
              lifei -= dano
            #FIM CRÍTICO

            dano = atk - defei*0.01*atk
            print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
            lifei -= dano

          #MACHADO DE GUERRA
           Dano_Intermediario = 0
           if ChoseMove == 3:
            p = random.randint(1,5)
            if p != 5:
            #CRÍTICO 
              if i == 1:
                dano = atk*1.8
                print('CRÍTICO!!!')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano
                #FIM CRÍTICO

                dano = atk*1.5
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano
          
          #FÚRIA
           if ChoseMove == 4 and nv >= 2:
          #CRÍTICO
              if i == 1:
                Dano_Intermediario += atk/1.4
                dano = Dano_Intermediario
                lifei -= dano
                print('CRÍTICO!!!')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))

                #FIM CRÍTICO

                Dano_Intermediario += atk/1.6 - defei*0.01*atk
                dano = Dano_Intermediario
                lifei -= dano
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
              elif ChoseMove == 4 and nv == 1: 
                print('Esta técnica é muito avançada, você não foi capaz de utilizar ela')
          

          #MODO BERSEQUER
           if ChoseMove == 5 and nv >= 4:
            Dano_Intermediario = 0

            AlyBurning = 0
            AlyFreezing = 0
            AlyParalized = 0
            AlyPoisoned = 0

            if atkT*1.5 <= atk:
             atk += random.randint(2,5)*0.01*atk
            if defeT*1.5 <= defe:
             defe += random.randint(3,5)
            if speedT*1.5 <= speed:
             speed += random.randint(2,4)

            duration = random.randint(2,4)
            print(f'Modo bersequer ira durar {duration} turnos')
           elif ChoseMove == 4 and nv <= 3:
              Dano_Intermediario = 0
              print('Esta técnica é muito avançada, você não foi capaz de utilizar ela')
          else:
            Dano_Intermediario = 0
            print(f'{nomeI} desviou do seu ataque')
    if clas == 3:
       #DRUIDA
          if raio == True:
            dano = atk - defei*0.01*atk
            lifei-= dano/2
            print(f'O raio Druídico acertou o adversário\nCausou {dano/2} de dano')
            Q= random.randint(1,10)
            if Q >= 6:
             raio = False
             print('O inimigo se libertou do raio druídico')

          print('Escolha um dos movimentos: \033[31m1-Orbe cósmico\033[m \033[32m2-Selva incontrolável\033[m 3-Karma ')
          if nv >= 2:
            print('4-Raio druídico')
          if nv >= 4:
            print('5-Cólera da natureza')
          ChoseMove = int(input(''))
          i = random.choice(CritRate)
          time.sleep(1)
          if speedi < random.randint(1,100):
          #ORBE CÓSMICO
            if ChoseMove == 1:
              dano = atk*1.2
              print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
              t = random.randint(1,2)
              efect = random.randint(1,6)
              if efect == 1:
                 AlyCure += t
                 a = 'se curando'
              if efect == 2:
                 AlyBurning += t
                 a = 'queimando'
              if efect == 3:
                 AlyFreezing += t
                 a = 'congelado'
              if efect == 4:
                 AlyParalized += t
                 a= 'paralizado'
              if efect == 5:
                 AlyPoisoned +=t
                 a= 'envenenado'
              if efect == 6: 
                 AlyRoubo +=t
                 a= 'roubando vida do adversário'

              print(f'Por causa do Orbe, você agora está {a} por {t} turnos') 
              #CRÍTICO
              if i >= 8:
                dano = atk*1.5
                print('CRÍTICO!!!')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano
                #FIM CRÍTICO
              else:
                lifei -= dano

            #SELVA INCONTROLÁVEL 
            if ChoseMove == 2:
              #CRÍTICOS
              if i == 1:
                dano = atk*1.7
                print('CRÍTICO!!!')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                print(f'você recebeu {dano/2.5} de dano, por causa do seu próprio ataque')
                lifei -= dano
                life -= dano/2.5
                #FIM CRÍTICO
              else:
                dano = atk*1.3
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano
                life -= dano/2.5
                print(f'você recebeu {dano/2.5} de dano, por causa do seu próprio ataque')

            #KARMA
            if ChoseMove == 3:
              #CRÍTICO
              if i == 1:
                print('CRÍTICO!!!')
                EnemyBurning += AlyBurning+1
                EnemyFreezing += AlyFreezing+1
                EnemyParalized += AlyParalized+1
                EnemyPoisoned += AlyPoisoned+1
                print(f'\033[33m Todos os seus status negativos foram transferidos para o inimigo\033[m]')
                #FIM CRÍTICO
              else:
                print('CRÍTICO!!!')
                EnemyBurning += AlyBurning
                EnemyFreezing += AlyFreezing
                EnemyParalized += AlyParalized
                EnemyPoisoned += AlyPoisoned
                print(f'\033[33m Todos os seus status negativos foram transferidos para o inimigo\033[m]')
            
            #RAIO DRUÍDICO
            if ChoseMove == 4 and nv >= 2:
              
              if CritRate == 1:
                dano = atk*1.3
                lifei-= dano
                print('CRÍTICO!!!')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                raio = True
              else:
                dano = atk - defei*0.01*atk
                lifei-= dano
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))

                raio = True

            elif ChoseMove == 4 and nv == 1: 
                print('Esta técnica é muito avançada, você não foi capaz de utilizar ela')
            

            #CÓLERA DA NATUREZA
            if ChoseMove == 5 and nv >= 4:
                
                AlyRoubo += random.randint(2,4)
                
                Q = random.randint(1,3)
                #DIMINUINDO O ATAQUE
                if Q == 1:
                  if atkiT*0.6 >= atki:
                    a = random.randint(2,5)
                    atki -= a
                    print(f'O inimigo teve seu ataque diminuído em {a} pontos')
                  else:
                    print('O ataque inimigo não foi diminuido,\npois já está muito baixo')
                #DIMINUINDO A DEFESA
                if Q == 2:
                  if defeiT*0.6 >= defei:
                    a = random.randint(2,5)
                    defei -= a
                    print(f'O inimigo teve sua defesa diminuída em {a} pontos')
                  else:
                    print('A defesa inimiga não foi diminuida,\npois já está muito baixa')
                #DIMINUINDO A VELOCIDADE
                if Q == 3:
                  if atkiT*0.6 >= atki:
                    a = random.randint(2,5)
                    atki -= a
                    print(f'O inimigo teve sua velocidade diminuída em {a} pontos')
                  else:
                    print('A velocidade inimiga não foi diminuida,\npois já está muito baixa')
            elif ChoseMove == 5 and nv <= 3: 
                print('Esta técnica é muito avançada, você não foi capaz de utilizar ela') 
          else:
              print(f'{nomeI} desviou do seu ataque')
    if clas == 4:
         #MONGE
          print('Escolha um dos movimentos: \033[31m1-Mãos que Curam\033[m \033[32m2-Esmaga Ossos\033[m 3-Pressão Espiritual \n')
          if nv >= 2:
            print('4-Paz interior')
          if nv >= 4:
            print('5-Ajuda Divina')
          ChoseMove = int(input(''))
          i = random.choice(CritRate)
          time.sleep(1)
          if speedi < random.randint(1,100) or ChoseMove == 1 or ChoseMove == 5:
          #MÃOS QUE CURAM
          #movimento que cura a vida do personagem
            if ChoseMove == 1:
            #CRÍTICOS
              if i == 1:
                cura = random.randint(30,35)
                print('CRÍTICO!!!')
                print('\033[33m{} recuperou {} pontos da sua própria vida\033[m'.format(nome, dano))
                life += cura
                #FIM CRÍTICO
              else:
                cura = random.randint(25,30)
                print('\033[33m{} recuperou {} pontos da sua própria vida\033[m'.format(nome, dano))
                life += cura

            #ESMAGA OSSOS  
            #ataque que além de causar danos, diminui de forma permanente a defesa do inimigo
            if ChoseMove == 2:
              #CRÍTICO
              if i == 1:
                dano = atk*1.3
                print('CRÍTICO!!!')
                if defei > (defeiT/100)*40:
                  a = random.randint(3,6) + 2
                  defei-= a
                  print(f'\033[30mO inimigo perdeu {a} de defesa')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano
                #FIM CRÍTICO
              else:
                if defei > (defeiT/100)*40:  
                  a = random.randint(3,6) + 2
                  defei-= a
                  print(f'\033[30mO inimigo perdeu {a} de defesa')
                dano = atk - defei*0.05*atk
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano

            #PRESSÃO ESPÍRITUAL 
            # ataque que além do dano aumenta a chances do monge acertar o ataque
            # (diminuindo a speed do inimigo) 
            if ChoseMove == 3:
              #CRÍTICO
              if i == 1:
                if speedi > (speediT/100)*50:
                  a = random.randint(3,6)
                  speedi-= a
                  print(f'{nomeI} agora tem menos {a}% de chance de se esquivar')
                dano = atk*1.3
                print('CRÍTICO!!!')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano
                #FIM CRÍTICO
              else:
                if speedi > (speediT/100)*50:
                  a = random.randint(2,4)
                  speedi-= a
                  print(f'{nomeI} agora tem menos {a}% de chance de se esquivar')
                dano = atk - defei*0.05*atk
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
                lifei -= dano
            
            #PAZ INTERIOR
            # diminui o ataque do inimigo e causa dano
            if ChoseMove == 4 and nv >= 2:
            #CRÍTICO
              if i == 1:
                if atki > (atkiT/100)*60:
                  a = random.randint(6,12)
                  atki-= a
                  print(f'\033[30mO inimigo perdeu {a} de ataque')
                dano = atk*1.3
                lifei -= dano
                print('CRÍTICO!!!')
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))

                #FIM CRÍTICO
              else:
                if atk > (atkiT/100)*60:
                  a = random.randint(5,9)
                  speedi-= a
                  print(f'\033[30mO inimigo perdeu {a} de ataque')
                dano = atk - defei*0.01*atk
                lifei -= dano
                print('\033[33m{} causou {} de dano\033[m'.format(nome, dano))
            elif ChoseMove == 4 and nv == 1: 
                print('Esta técnica é muito avançada, você não foi capaz de utilizar ela')
            

            #AJUDA DIVINA
            # ataque que ativa uma cura constante por um número pseudo aleatório de turnos
            if ChoseMove == 5 and nv >= 4:
            #CRÍTICO
              if i == 1:
                AlyCure += random.randint(2,3) + 1
                print('\033[33m{} terá uma ajuda divina por {} turnos\033[m'.format(nome, AlyCure))

                #FIM CRÍTICO
              else:
                AlyCure += random.randint(1,3) 
                print('\033[33m{} terá uma ajuda divina por {} turnos\033[m'.format(nome, AlyCure))
            elif ChoseMove == 4 and nv <= 3: 
                print('Esta técnica é muito avançada, você não foi capaz de utilizar ela')
          else:
            print(f'{nomeI} desviou do seu ataque')
    
    #ÁREA DAS CONDIÇÕES DOS INIMIGOS: INÍCIO
    if EnemyParalized > 0:
      speed = 85
      EnemyParalized -= 1
      print(f'\033[33m{nomeI} está paralizado\ndifícilmente acertará um golpe assim\033[m')
      if EnemyParalized == 0:
        speed = speedT

    if EnemyFreezing > 0:
      EnemyFreezing-=1
      time.sleep(1)
      dano = random.randint(15,20)
      lifei -= dano
      print(f'\033[36m{nomeI} recebeu {dano} de dano, pois está congelado\nSua velocidade e defesa também caíram\033[m')
      if defei > (defeiT/100)*60:
       defei -= 6
      if speedi > (speediT/100)*50:
       speedi -= 6
      if EnemyFreezing == 0:
        defei = defeiT
        speedi = speediT

    if EnemyBurning > 0:
        EnemyBurning-=1
        time.sleep(1)
        dano = burning(nomeI)
        lifei-=dano
    
    if EnemyCure > 0:
      EnemyCure-=1
      time.sleep(1)
      cura = curing(nomeI)
      lifei += cura

    if EnemyRoubo > 0:
      EnemyRoubo-=1
      time.sleep(1)  
      dano = RouboVida(nomeI)
      lifei += dano/1.25
      life -= dano
    if EnemyPoisoned > 0:
          EnemyPoisoned-=1
          time.sleep(1)
          dano = poisoned(nomeI)
          lifei-=dano
    #ÁREA DE CONDIÇÕES DOS INIMIGOS: FIM 

    time.sleep(1)
    #ÁREA DOS LOOTS 
    if(lifei <= 0):
        print('\033[32mParabéns, você venceu\033[m')
        loot = random.randint(1,10)
        return loot
    #FIM DA PARTE SOBRE LOOTS
    
    #ÁREA DOS INIMIGOS
#ZOMBIE 
    if enemy == 1:
        print('\nZombie está com {} de vida'.format(lifei))
        print('')
        time.sleep(1)
        ZombieMoves = [1,2,3]
        EnemyMove = random.choice(ZombieMoves)
        if speed < random.randint(1,100):
          if EnemyMove == 1: 
                dano = atki - defe*0.01*atki
                life-=dano
                AtaqueNome = 'Pancada'
                print('\033[31mZumbi causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2:
                TurnRange = [1,2,3]
                dano = atki - atki*(defe*0.01) - 5
                life-=dano
                AtaqueNome = 'Cuspe ácido'
                AlyPoisoned = random.choice(TurnRange)
                print('Zombie usou cuspe ácido, o herói está envenenado')
                print('\033[31mZumbi causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 3:
                dano = atki - atki*(defe*0.01) + 2

                AtaqueNome = 'Mordida'
                print ('\033[31mZumbi causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))
                life-=dano
        
        else:
          print(f'{nome} se esquivou do ataque inimigo')
#GOBLIN
    if enemy == 2:
        print('\nHorda de goblins está com {} de vida\n'.format(lifei))

        time.sleep(1)
        EnemyMove = random.randint(1,3)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
            AtaqueNome = 'chuva de flechas'
            dano = atki - atki*0.01*defe
            life -= dano
            print('\033[31mhorda de goblins causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2:
            dano = atki/1.5
            lifei += dano
            print('\033[31mGoblins receberam reforços. Eles recuperaram {} da própria vida\033[m'.format(dano)) 
          if EnemyMove == 3:
            dano = atki*1.2
            life -= dano
            print('\033[31mhorda de goblins causou {} de dano cercando e atacando você\033[m'.format(dano))
        else:
          print(f'{nome} se esquivou do ataque inimigo')
#LORDE VAMPIRO
    if enemy == 3:
        print('\nLorde vampiro está com {} de vida\n'.format(lifei))
        speedi = speediT
        time.sleep(1)
        EnemyMove = random.randint(1,6)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
            AtaqueNome = 'Recuperação tenebrosa'
            lifei += dano*1.5
            print(f'\033[31mLorde vampiro recuperou {dano*1.5} de vida usando {AtaqueNome}\033[m')

          if EnemyMove == 2 or EnemyMove == 3:
            dano = atki - defe*0.01*atki
            AtaqueNome = 'Mordida'
            AlyPoisoned = random.randint(1,4)
            life -= dano
            life += dano*0.6
            print('\033[31mLorde vampiro causou {} de dano e roubou {} de vida usando {}\033[m'.format(dano, dano*0.6, AtaqueNome)) 
          if EnemyMove == 4 or EnemyMove == 5:
            #HORDA DE MORCEGOS
            #Dano e muito roubo de vida
            AtaqueNome = 'horda de morcegos'
            dano = atki - defe*0.01*atki
            life-=dano
            lifei+=dano*0.9
            print('\033[31mLorde vampiro causou {} de dano e roubou {} de vida usando {}\033[m'.format(dano, dano*0.6, AtaqueNome))
          if EnemyMove == 6:
            #TRANSFORMAÇÃO EM MORCEGO
            #Desvia do próximo ataque
            print('Lorde vampiro se transformou em morcego, ele provavelmente desviará do seu próximo ataque')
            speedi == 95
        else:
          print(f'{nome} se esquivou do ataque inimigo')
#BANDIDO
    if enemy == 4:
        print('\nO bandido está com {} de vida\n'.format(lifei))
        
        time.sleep(1)
        EnemyMove = random.randint(1,3)
        if speed < random.randint(1,100):
          #ATAQUE DE BESTA  
          if EnemyMove == 1:
            AtaqueNome = 'Tiro de besta'
            i = random.randint(1,10)
             #CRÍTICO
            if i >= 8:
              dano = atki*1.5
              print('CRÍTICO!!!')
              print('\033[33m bandido causou {} de dano atirando com sua besta\033[m'.format(dano))
              life -= dano
            #FIM CRÍTICO
            else:
              dano = atki - defe*0.01*atki
              print('\033[33m bandido causou {} de dano atirando com sua besta\033[m'.format(dano))
              life -= dano
          #ATAQUE DE ADAGA
          if EnemyMove == 2 or EnemyMove == 3:
            dano = atki - defe*0.01*atki
            AlyPoisoned = random.randint(0,3)
            life -= dano
            print('\033[33m bandido causou {} de dano atacando com sua adaga envenenada\033[m'.format(dano))
        else:
           print(f'{nome} se esquivou do ataque inimigo')
#GOBLIN REI
    if enemy == 5:
        print('\nGoblim rei está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,4)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
            AtaqueNome = 'chuva de fogo'
            dano = atki - atki*0.01*defe
            life -= dano
            AlyBurning += random.randint(1,3)
            print('\033[31mGoblin rei causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2:
            dano = atki - atki*0.01*defe 
            lifei += dano/3
            life -= dano
            print('\033[31mGoblim rei causou {} de dano e recuperou {} de vida\033[m'.format(dano, dano/3)) 
          if EnemyMove == 3:
            dano = atki*1.2
            life -= dano
            print('\033[31mGoblim rei causou {} de dano usando raio espectral\033[m'.format(dano))
          if EnemyMove == 4:
            AlyParalized += random.randint(1,2)
            print(f'{nome} está paralizado por {AlyParalized} turnos')
        else:
          print(f'{nome} se esquivou do ataque inimigo')
#DRAGÃO JOVEM
    if enemy == 6:
        speedi=speediT
        print('\nDragão jovem está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,3)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
            AtaqueNome = 'bafo de fogo'
            dano = atki - atki*0.01*defe
            life -= dano
            AlyBurning += random.randint(1,2)
            print('\033[31mDragão jovem causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2:
            #RABADA
            dano = atki - atki*0.01*defe 
            life -= dano
            print('\033[31mDragão jovem causou {} de dano atacando com a cauda\033[m'.format(dano)) 

          if EnemyMove == 3:
            dano = atki
            lifei += dano/3
            print('\033[31mDragão jovem voou e recuperou {} de vida\033[m'.format(dano/3))
            print('Por está voando, ele desviara do seu próximo ataque')
            speedi=100
        else:
          print(f'{nome} se esquivou do ataque inimigo')
#DRACONATO
    if enemy == 7:
        print('\nDraconato está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,2)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
            AtaqueNome = 'bafo de fogo'
            dano = atki - atki*0.01*defe
            life -= dano
            AlyBurning += random.randint(1,2)
            print('\033[31mDraconato causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2:
            #MACHADINHAS
            repete= random.randint(1,4)
            for c in range(repete):
              i = random.randint(1,4)
              #CRÍTICO 
              if i == 1:
              
                dano = atki
                print('CRÍTICO!!!')
                print('\033[33m Draconato causou {} de dano\033[m'.format(dano))
                life -= dano/2
                time.sleep(1)
                #FIM CRÍTICO
              else:
                dano = atki - defe*0.01*atki
                print('\033[33m Draconato causou {} de dano\033[m'.format(dano))
                life -= dano/3
                time.sleep(1)
        else:
          print(f'{nome} se esquivou do ataque inimigo')
#DRAGÃO ANCIÃO  
    if enemy == 8:
        print('\nDragão Ancião está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,10)
        if speed < random.randint(1,100):
          if EnemyMove == 1 or EnemyMove == 2 or EnemyMove == 3:
            AtaqueNome = 'bafo de fogo'
            dano = atki - atki*0.01*defe
            life -= dano
            AlyBurning += random.randint(1,2)
            print('\033[31mDragão Ancião causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 4 or EnemyMove == 5:
            #VOAR
            dano = atki
            lifei += dano/3
            print('\033[31mDragão Ancião voou e recuperou {} de vida\033[m'.format(dano/3))
            print('Por está voando, ele desviara do seu próximo ataque')
            speedi=100
          if EnemyMove == 6 or EnemyMove == 7:
            #ATAQUE COM ASAS
            print('Dragão Ancião balança suas asas criando fortes ventos')
            print(f'{nome} fica paralisado devido aos ventos')
            AlyParalized += 1
          if EnemyMove == 8 or EnemyMove == 9:
            #MORDIDA
            dano = atki - defe*0.01*atki
            life -= dano
            print(f'Dragão Ancião causou {dano} de dano com sua mordida')
          if EnemyMove == 10:
            #LABAREDAS DA DEVASTAÇÃO
            life -= atki*random.choice(1.5,1.7,1.3)
            print('\033[31m Labaredas da Devastação\033[m')
            time.sleep(1)
            print(f'Dragão Ancião causou {dano} de dano usando Labaredas da Devastação')
        else:
          print(f'{nome} se esquivou do ataque inimigo')
#TIAMAT
    if enemy == 9:
        print('\nTiamat está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,9)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
            life -= atki*random.choice(1.5,1.7,1.3)
            print('\033[31m Labaredas da Devastação\033[m')
            time.sleep(1)
            AlyBurning = random.randint(2,4)
            print(f'Dragão Ancião causou {dano} de dano usando Labaredas da Devastação')

          if EnemyMove == 2 or EnemyMove == 3:
            #FRIO DA DESOLAÇÃO
            dano = atki
            life -= dano
            AlyFreezing = random.randint(3,6)
            print('\033[31mTiamat causou {} de dano usando\033[34m frio da desolação\033[m'.format(dano)) 

          if EnemyMove == 4 or EnemyMove == 5:
            #VENENO DA MORTIFICAÇÃO
            dano = life/10
            life -= dano
            AlyPoisoned = random.randint(2,4)
            print('\033[31mTiamat causou {} de dano usando\033[32m veneno da mortificação\033[m'.format(dano))
          
          if EnemyMove == 6 or EnemyMove == 7 or EnemyMove == 8:
            #RAIOS DA PERDIÇÃO
            dano = atki - defe*0.01*atki
            life-=dano
            print('\033[31mTiamat causou {} de dano usando\033[33m raios da perdição\033[m'.format(dano))
          if EnemyMove == 9:
            #DESTRUIÇÃO ELEMENTAL
            AlyParalized += 3
            AlyBurning += 3
            AlyFreezing += 3
            AlyPoisoned += 3
            print(f'Tiamat usou Destruição Elemental, {nome} está paralizado, congelado, queimando e envenenado')
        else:
          print(f'{nome} se esquivou do ataque inimigo') 
#MORFGAN
    if enemy == 10:

        print('\nMorfgan está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,5)
        if speed < random.randint(1,100):
          if EnemyMove == 1 or EnemyMove == 2:
            AtaqueNome = 'Pancada de fogo'
            dano = atki - atki*0.01*defe
            life -= dano
            print('\033[31mMorfgan causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 3 or EnemyMove == 4:
            #LANÇA CHAMAS
            dano = atki - atki*0.01*defe 
            life -= dano
            AlyBurning += random.randint(3,5)
            print('\033[31mMorfgan causou {} de dano lançando fogo de suas mãos\033[m'.format(dano)) 
          if EnemyMove == 5:
            #METEORO ARDENTE
            dano= atki*1.4
            lifei-= dano
            print(f'Morfgan causou {dano} de dano usando Meteoro Ardente')
          atkiT += dano/7
          atki = atkiT

        else:
          print(f'{nome} se esquivou do ataque inimigo')
#MAGO
    if enemy == 11:
        print('\nMago jovem está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,5)
        if speed < random.randint(1,100) or EnemyMove == 4 or EnemyMove == 5:
          if EnemyMove == 1:
            #RAIO TROVÃO
            #Alto dano e baixa chance de paralizar
            AtaqueNome = 'Raio trovão'
            dano = atki - atki*0.01*defe
            life -= dano*1.3
            if 4 == random.randint(1,4):
              AlyParalized = random.randint(1,2)
            print('\033[31mMago jovem causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2 or EnemyMove == 3:
            #CHUVA DE GRANIZO
            #Baixo dano, congela o personagem
            dano = atki - atki*0.01*defe 
            life -= dano*0.5
            AlyFreezing = random.randint(1,3)
            print('\033[31mMago jovem causou {} de dano usando chuva de granizo\033[m'.format(dano)) 

          if EnemyMove == 4 or EnemyMove == 5:
            #TERREMOTO
            #Impossível errar este golpe, dá um pouco menos de dano
            dano = atki - defe*0.02*atki
            life -= dano
            print('\033[31mMago jovem causou {} de dano usando terremoto\033[m'.format(dano))

        else:
          print(f'{nome} se esquivou do ataque inimigo')
#ARQUI-MAGO
    if enemy == 12:
        print('\nArqui-mago está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(2,4)
        if lifei <= 100:
          EnemyMove = 1
        if speed < random.randint(1,100):
          if EnemyMove == 1 and Usou_Uma_Vez==False:
            #CHUVA ÁCIDA
            #Usado somente quando está com pouca vida, ativa um roubo de vida até o fim da luta(usado somente uma vez)
            EnemyRoubo = 1000
            Usou_Uma_Vez = True
            print('\033[31mArqui-mago usou chuva ácida, e roubará sua vida até o fim da luta\033[m')
          else:
            EnemyMove = random.randint(2,4)
          if EnemyMove == 2:
            #TORNADO DE FOGO
            #O dano é incerto, pode baixo, médio ou muito alto
            dano = random.choice(atki/2, atki, atki*1.5) 
            life -= dano
            print('\033[31mArqui-mago usou tornado de fogo e causou {} de dano\033[m'.format(dano)) 

          if EnemyMove == 3:
            #ESTACAS DE GELO
            #Dano normal e congela
            dano = atki - defe*0.01*atki
            life -= dano
            AlyFreezing = random.randint(1,3)
            print('\033[31mArqui-mago causou {} de dano usando estacas de gelo\033[m'.format(dano))
          if EnemyMove == 4:
            #CHUVA DE METEOROS
            #Baixo dano, se repete um número incostante de vezes
            print('Arqui-mago usou chuva de meteoros')
            rep = random.randint(3,6)
            dano = atki - defe*0.01*atki
            for i in range(1,rep):
              auxiliar = random.choice(0.3,0.5,0.1)
              lifei-=dano*auxiliar
              print(f'Meteoro causou {dano} de dano')
              time.sleep(1)

            print(f'{rep} meteoros cairam')
        else:
          print(f'{nome} se esquivou do ataque inimigo') 
#TAUROS
    if enemy == 13:
        print('\nTauros está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,8)
        if speed < random.randint(1,100) or EnemyMove == 4 or EnemyMove == 5:
          if EnemyMove == 1 and Usou_Uma_Vez == False:
            #GÁS VENENOSO
            #Envenena até o fim da partida
            AlyPoisoned = 1000
            Usou_Uma_Vez = True
            print(f'\033[31mTauros usou gás venenoso, e {nome} ficará envenenado até o fim da partida\033[m')
          else:
            EnemyMove = random.randint(2,8)

          if EnemyMove == 2 or EnemyMove == 3:
            #MORDIDA
            #Dano maior que o comum
            dano = atki - atki*0.01*defe 
            life -= dano*1.5
            print('\033[31mTauros causou {} de dano usando mordida\033[m'.format(dano)) 

          if EnemyMove == 4:
            #OLHOS HIPNÓTICOS
            #Paralisa por pouco tempo
            AlyParalized = random.randint(1,2)
            print(f'\033[31mTauros paralisou {nome} com seus olhos hipnóticos\033[m'.format(dano))
          if EnemyMove == 5 or EnemyMove == 6:
            #INVESTIDA
            #Dano comum
            dano = atki - atki*0.01*defe 
            life -= dano
            print('\033[31mTauros causou {} de dano usando mordida\033[m'.format(dano))
          if EnemyMove == 7 or EnemyMove == 8:
            #RAIO CONSUMIDOR
            #Rouba de vida
            dano = atki - atki*0.01*defe 
            life -= dano
            lifei += dano
            print(f'\033[31mTauros causou {dano} de dano e recuperou {dano} de vida usando raio consumidor \033[m') 
            time.sleep(2)
        else:
          print(f'{nome} se esquivou do ataque inimigo')  
#SLIME
    if enemy == 14:
        print('\nSlime está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,2)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
            AtaqueNome = 'gosma ácida'
            dano = atki - atki*0.01*defe
            life -= dano
            print('\033[31mSlime causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2:
            lifei += atki/2
            print(f'O slime recuperou {atki/2} de vida')

        else:
          print(f'{nome} se esquivou do ataque inimigo')  
#SLIME REI
    if enemy == 15:
        print('\nSlime rei está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,3)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
            #GOSMA ÁCIDA
            #Dá dano
            AtaqueNome = 'gosma ácida'
            dano = atki - atki*0.01*defe
            life -= dano
            print('\033[31mSlime rei causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2:
            #REGENERAÇÃO
            #Recupera um pouco de vida
            lifei += atki*0.7
            print(f'O slime rei recuperou {atki*0.7} de vida')
          if EnemyMove == 3:
            #RAIO DE LUZ
            #Dá dano e tem chance de paralisar
            dano = atki
            life -= dano
            if 5 == random.randint(1,5):
              AlyParalized = 1
              print(f'{nome} está paralisado')
            print(f'O slime rei causou {dano} de dano')

        else:
          print(f'{nome} se esquivou do ataque inimigo')
#ELEMENTAL SUPREMO
    if enemy == 16:
        print('\nElemental supremo está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,4)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
            #CHAMAS INTENSAS
            #Causa dano e queimar
            AtaqueNome = 'chamas intensas'
            dano = atki - atki*0.01*defe
            life -= dano
            AlyBurning = random.randint(1,4)
            print('\033[31mElemental supremo causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2:
            #ÁGUAS TERMAIS
            #Cura e remove status negativos
            lifei += atki*0.8
            EnemyBurning = 0
            EnemyParalized = 0
            EnemyPoisoned = 0
            EnemyFreezing = 0
            print(f'Elemental supremo recuperou {atki*0.8} de vida e se curou de todos os status negativos')
            time.sleep(1)
          if EnemyMove == 3:
            #ROCHAS TECTONICAS
            #Causa baixo dano e aumenta a defesa do Elemental
            dano = atki - defe*0.03*atki
            life -= dano
            if defei <= defeiT*1.5:
             defei += random.randint(3,6)
            print(f'Elemental supremo causou {dano} de dano e aumentou sua defesa, usando rochas tectonicas')
          if EnemyMove == 4:
            #VENTOS FEROZES
            #Aumenta a velocidade e o ataque do Elemental supremo
            if speedi <= speediT*1.5:
             speedi += random.randint(2,3)
            if atki <= atkiT*1.5:
             atki += random.randint(10,15)
            print(f'Elemental supremo ficou mais rápido e mais forte usando ventos ferozes')

        else:
          print(f'{nome} se esquivou do ataque inimigo')
#TARTARUGA GIGANTE
    if enemy == 17:
        print('\nTartaruga gigante está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,3)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
            #ONDA GIGANTE
            #Causa dano
            AtaqueNome = 'onda gigante'
            dano = atki - atki*0.01*defe
            life -= dano
            print('\033[31mTartaruga gigante causou {} de dano usando {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2:
            #ATAQUE DE BARBATANA
            #Causa dano
            dano = atki - atki*0.01*defe
            life -= dano*1.2
            print(f'A tartaruga gigante move sua barbatana e ataca {nome}')
            print(f'Causa {dano} de dano')
          if EnemyMove == 3:
            #MORDIDA
            #Causa dano
            dano = atki - atki*0.01*defe
            life -= dano*1.5
            print(f'Esticando sua cabeça, a grande tartaruga morde {nome}')
            print(f'Causa {dano} de dano')

        else:
          print(f'{nome} se esquivou do ataque inimigo')
#SOLDADO
    if enemy == 18:
        print('\nSoldado está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,2)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
            #MACHADO DE GUERRA
            #Chance maior de errar, dano básico maior
            chance = random.randint(1,4)
            if chance == 4:
              print('O soldado errou o ataque')
            else:
              AtaqueNome = 'machado de guerra'
              dano = atki - atki*0.01*defe
              life -= dano*1.4
              print('\033[31mO soldado causou {} de dano usando o {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2:
            #MODO BERSERQUER
            #Aumenta os status e recupera dos status negativos
            print('O soldado entrou no modo Berserquer')
            print('Ele ficou mais forte e anulou os status negativos')
            time.sleep(1)
            atki += random.randint(3,9)
            defei += random.randint(2,4)
            speedi += random.randint(1,3)
            EnemyBurning =0
            EnemyFreezing =0
            EnemyParalized =0
            EnemyPoisoned =0

        else:
          print(f'{nome} se esquivou do ataque inimigo')
#JOIA DA ALMA POSSUINDO O CAPITÃO
    if enemy == 19:
        print('\nA joia está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,4)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
              #PROJÉTEIS DE CRISTAL
              #Causa dano
              AtaqueNome = 'projéteis de cristal'
              dano = atki - atki*0.01*defe
              life -= dano
              print('\033[31mO cristal causou {} de dano usando o {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2:
            #ESTACAS DE CRISTAL
            #Congela e causa dano
            AtaqueNome = 'estacas de cristal'
            dano = atki - atki*0.01*defe
            life -= dano
            AlyFreezing = random.randint(1,3)
            print('\033[31mO cristal causou {} de dano usando o {}\033[m'.format(dano, AtaqueNome))
            print(f'{nome} está congelado')
          
          if EnemyMove == 3:
            #PRISÃO DE CRISTAL
            #Paralisa
            AlyParalized = random.randint(1,2)
            print(f'O cristal fez uma prisão de cristal, {nome} está paralisado')
          
          if EnemyMove == 4:
            #CHUVA DE CRISTAL
            #Dano baixo que se repete número inconstante de vezes
            print('O cristal usou chuva de cristal')
            rep = random.randint(3,6)
            dano = atki - defe*0.01*atki
            for i in range(1,rep):
              auxiliar = random.choice(0.3,0.5,0.2)
              lifei-=dano*auxiliar
              print(f'Um cristal caiu em {nome} e causou {dano} de dano')
              time.sleep(1)

            print(f'{rep} cristais cairam')
        else:
          print(f'{nome} se esquivou do ataque inimigo')
#CAPITÃO USANDO A PEDRA
    if enemy == 20:
        #O CAPITÃO TEM A PASSIVA DE REGENERAR VIDA
        auxiliar = random.randint(10,25)
        print(f'O capitão regenerou {auxiliar} de vida')
        lifei += auxiliar
        print('\nO capitão está com {} de vida\n'.format(lifei))
        time.sleep(1)
        EnemyMove = random.randint(1,3)
        if speed < random.randint(1,100):
          if EnemyMove == 1:
              #RAIO DE LUZ INTENSO
              #Causa dano
              AtaqueNome = 'Raio de luz intenso'
              dano = atki - atki*0.01*defe
              life -= dano*1.3
              print('\033[31mO capitão causou {} de dano usando o {}\033[m'.format(dano, AtaqueNome))

          if EnemyMove == 2:
            #TOQUE ABSORVENTE
            #Dano e roubo de vida
            AtaqueNome = 'toque absorvente'
            dano = atki - atki*0.01*defe
            life -= dano
            lifei += dano
            print('\033[31mO capitão causou {} de dano e recuperou {} de vida usando o {}\033[m'.format(dano, dano, AtaqueNome))
            time.sleep(1)
          
          if EnemyMove == 3:
            #LUZ SEGUANTE
            #Paralisa
            AlyParalized = random.randint(1,2)
            print(f'O capitão usou uma luz seguante, {nome} está paralisado')
        else:
          print(f'{nome} se esquivou do ataque inimigo')
    
    print(f'\033[32m{nome} está com {life} de vida\033[m')
    
    if life <= 0:
      FimDoCombate = True
      print('\033[31mSinto muito, você perdeu\033[m')
      exit()
#FIM DA FUNÇÃO COMBATE

def LootAndXp(loot, xp, nv, intermediario, imunPoi = imunPoi, imunBur = imunBur, atk=atk, life=life, defe=defe, speed=speed, Golpe_NV4= Golpe_NV4, Golpe_NV2= Golpe_NV2):
    ganhos={'nv':nv, 'atk': 0, 'defe': 0, 'life': 0, 'speed': 0, 'imunPoi': imunPoi, 'imunBur': imunBur}
    if loot == 1 or loot == 2 or loot == 3 or loot == 9:
            print('Você conseguiu uma\033[32m espada melhor\n\033[36mSeu ataque sobe 5 pontos\033[m')
            ganhos.update({'atk':5})
    if loot == 2 or loot == 4 or loot == 5:
                print('Você conseguiu um\033[32m escudo melhor\n\033[36mSua defesa sobe 5 pontos\033[m')
                ganhos.update({'defe':5})
    if loot == 10 and imunPoi==False or loot == 9 and imunPoi==False:
                print ('Você conseguiu o\033[35m anel de Argroth\n\033[36mAgora você é imune a veneno \033[m')
                ganhos.update({'imunPoi':True})
    if loot == 8 and imunBur==False or loot == 5 and imunBur==False:
                print('Você conseguiu o\033[35m manto de Morfgan\n\033[36mAgora você é imune a queimar \033[m')
                ganhos.update({'imunBur':True})
    if loot == 7 or loot == 6 or loot == 10:
                print('Você conseguiu o\033[34m colar de Tultri\n\033[36mSua vida sobe 15 pontos e sua velocidade sobe 5\033[m')
                ganhos.update({'life':15})
                ganhos.update({'speed':5})
            
            #PARTE SOBRE PONTOS DE EXPERIÊNCIA E PASSAGEM DE NÍVEL
    xp += intermediario
    ganhos.update({'xp': xp})
    print(f'Você ganhou {intermediario} pontos de experiência, agora você tem {xp}\n')
    if nv == 1 and xp >= 80:
                ganhos.update({'nv': 2})
                ganhos.update({'atk': atk*0.05})
                ganhos.update({'defe': defe*0.05})
                ganhos.update({'speed': speed*0.05})
                ganhos.update({'life': life*0.05})
                print('Parabéns, agora você está no nível 2\n Seus status aumentaram e você desbloqueou um novo ataque\n')
                print(Golpe_NV2)
    if nv == 2 and xp >= 200:
                ganhos.update({'nv': 3})
                ganhos.update({'atk': atk*0.05})
                ganhos.update({'defe': defe*0.05})
                ganhos.update({'speed': speed*0.05})
                ganhos.update({'life': life*0.05})
                print('Parabéns, agora você está no nível 3\n Seus status aumentaram\n')
    if nv == 3 and xp >= 350:
                ganhos.update({'nv': 4})
                ganhos.update({'atk': atk*0.05})
                ganhos.update({'defe': defe*0.05})
                ganhos.update({'speed': speed*0.05})
                ganhos.update({'life': life*0.05})
                print('Parabéns, agora você está no nível 4\n Seus status aumentaram e você desbloqueou um novo ataque\n')
                print(Golpe_NV4)
    return ganhos

#História início
time.sleep(1)
print(f'\n\nDepois de dias de viagem, {nome} finalmente chega à cidade de Mystra, capital do reino, depois de dias de viagem')
time.sleep(3)
print('Vendo as pessoas andando de um lado para o outro ele sente a energia e se sente vivo, parece que sua vida começa agora')
time.sleep(3)
print(f'{nome} então decide ir para a taverna em busca de emprego, ele encontra dois interessantes no quadro de avisos')
time.sleep(3)
print(f'-Hei, esses aí já são meus\n Um homem armado com uma faca ataca nosso heroi\n')
enrolação = input('\nEscreva qualquer coisa para continuar\n')

ganhos=LootAndXp(combate(4, nv), 0, 1, 500)
xp = ganhos['xp']
nv = ganhos['nv']
atk+=ganhos['atk']
defe+=ganhos['defe']
life+=ganhos['life']
speed+=ganhos['speed']
imunBur=ganhos['imunBur']
imunPoi=ganhos['imunPoi']

print(f'nível: {nv}')

time.sleep(2)
print(f'{nome}, depois de derrotar seu adversário, lê suas opções de trabalho')
time.sleep(2)
print('1.Precisamos que alguém investigue o número anormal de goblins nos arredores da montanha Moftar.')
time.sleep(2)
print('2.Socorro, um exército de slimes frequentemente ataca nossa pequena vila, nos ajude por favor.')
time.sleep(2)
escolha = int(input(f'Qual {nome} escolhe?'))

#História caso escolha os goblins
if escolha == 1:
  time.sleep(2)
  print(f'Andando algumas horas, {nome} finalmente chega na temida montanha de Moftar')
  time.sleep(2)
  print(f'O que estaria causando esse alvoroço entre os goblins, se perguntou')
  time.sleep(2)
  print(f'Caminhando mais um pouco, {nome} logo encontra uma caverna e ele é recepcionado pelos moradores\n')
  time.sleep(2)
  enrolação = input('digite qualquer coisa para continuar')

  ganhos=LootAndXp(combate(2, nv), xp, nv, random.randint(30,50))
  xp = ganhos['xp']
  nv = ganhos['nv']
  atk+=ganhos['atk']
  defe+=ganhos['defe']
  life+=ganhos['life']
  speed+=ganhos['speed']
  imunBur=ganhos['imunBur']
  imunPoi=ganhos['imunPoi']

  time.sleep(2)
  print('Adentrando mais na caverna, se esgueirando, você encontra uma sala com grande tesouro')
  time.sleep(2)
  print(f'{nome} também encontrou o motivo de tudo aquilo, um goblin rei havia aparecido e estava reunindo um pequeno exército')
  time.sleep(2)
  print('O goblin rei percebe sua presença e lhe ataca')
  time.sleep(2)
  enrolação= input('Digite qualquer coisa para continuar')
  
  ganhos=LootAndXp(combate(5, nv), xp, nv, random.randint(45,60))
  xp = ganhos['xp']
  nv = ganhos['nv']
  atk+=ganhos['atk']
  defe+=ganhos['defe']
  life+=ganhos['life']
  speed+=ganhos['speed']
  imunBur=ganhos['imunBur']
  imunPoi=ganhos['imunPoi']

  time.sleep(2)
  print(f'{nome} consegue derrotar o poderoso goblin, os outros fugiram após ver a derrota de seu líder')
  time.sleep(2)
  print(f'A adrenalina baixou, e, olhando em volta, {nome} percebe o grande tesouro que esses seres haviam acumulado')
  time.sleep(2)
  print('O que ele irá fazer?')
  time.sleep(2)
  escolha = int(input('1-Ficar com todas as riquezas\n2-Devolver o tesouro para as cidades\n'))
  if escolha == 1:
    #escolheu ficar com todo o dinheiro
    time.sleep(2)
    print(f'Toda essa riqueza repentina fez despertar a ganância de {nome}')
    time.sleep(1)
    print('Isso o fez buscar mais e mais, depois de uns dias, ele descobriu algo interessante')
    time.sleep(2)
    print('A localização do covil de um poderoso dragão,\nsem pensar 2 vezes, ele parte em direção a seu novo objetivo')
    time.sleep(2)
    print(f'Finalmente {nome} chegou até um grande vulcão')
    time.sleep(1)
    print(f'Adentrando ao vulcão, lava e fogo vinham de todos os lados')
    time.sleep(2)
    print('E pulando do meio de uma labareda um jovem dragão lhe ataca')
    enrolação= input('Digite qualquer coisa para continuar')
    ganhos=LootAndXp(combate(6, nv), xp, nv,random.randint(40,50))
    xp = ganhos['xp']
    nv = ganhos['nv']
    atk+=ganhos['atk']
    defe+=ganhos['defe']
    life+=ganhos['life']
    speed+=ganhos['speed']
    imunBur=ganhos['imunBur']
    imunPoi=ganhos['imunPoi']
    
    time.sleep(2)
    print(f'Depois de conseguir derrotar o dragão, {nome} avança pelas cavernas')
    time.sleep(2)
    print('Até que ele encontra uma grande sala, santuário na verdade')
    time.sleep(2)
    print(f'E então {nome} percebe que é o local onde fanáticos adoram o dragão')
    time.sleep(2)
    print(f'Ele também vê um draconato vindo em sua direção')
    enrolação= input('Digite qualquer coisa para continuar')

    ganhos = LootAndXp(combate(7, nv), xp, nv,random.randint(40,50))
    xp = ganhos['xp']
    nv = ganhos['nv']
    atk+=ganhos['atk']
    defe+=ganhos['defe']
    life+=ganhos['life']
    speed+=ganhos['speed']
    imunBur=ganhos['imunBur']
    imunPoi=ganhos['imunPoi']

    time.sleep(2)
    print('O draconato não foi um grande desafio, mas o inimigo real vinha agora')
    time.sleep(1)
    print(f'O barulho ecoava por toda a caverna, {nome} não sabia de onde vinha')
    time.sleep(1)
    print('Um barulho de grandes asas batendo e de uma respiração furioso')
    time.sleep(1)
    print(f'Por fim, um grande rugido que estremeceu todo o vulcão, o alvo de {nome} havia chegado')
    enrolação= input('Digite qualquer coisa para continuar')

    ganhos = LootAndXp(combate(8, nv), xp, nv,random.randint(60,75))
    xp = ganhos['xp']
    nv = ganhos['nv']
    atk+=ganhos['atk']
    defe+=ganhos['defe']
    life+=ganhos['life']
    speed+=ganhos['speed']
    imunBur=ganhos['imunBur']
    imunPoi=ganhos['imunPoi']

    time.sleep(2)
    print('A batalha havia sido intensa, o lugar estava todo destruído')
    time.sleep(1)
    print('O dragão estava deitado no chão, passando seus últimos momentos')
    time.sleep(1)
    print(f'Andando um pouco, {nome} logo acha a sala dos tesouros do dragão')
    time.sleep(1)
    print(f'O dragão, reunindo suas últimas forças, disse:')
    time.sleep(1)
    print('-Faça o que quiser com meu tesouro grande guereiro, mas não abra o portal selado')
    time.sleep(1)
    print(f'Logo após isso, ele morreu, mas...\n o que {nome} irá fazer?')
    escolha = int(input('1-Abrir o portal\n2-Ficar com todo o tesouro que já está ali\n'))

    if escolha == 1:
      print(f'O coração de {nome} só deseja mais poder e riqueza')
      time.sleep(1)
      print('Respeitar o pedido do morto nem passou por sua cabeça')
      time.sleep(1)
      print('Ele corre em direção ao portal e o ativa')
      time.sleep(1)
      print('Após um intenso barulho, o portal se abriu, mas não havia tesouros do outro lado')
      time.sleep(1)
      print(f'Tudo o que {nome} conseguia ver eram 8 pontos luminosos que vinham em sua direção')
      time.sleep(1)
      print(f'Saindo de dentro do portal e jogando {nome} para longe era...')
      time.sleep(1)
      print('Tiamat, a mãe dos dragões, ela havia sido selada a milênios\npelos seus desejos de exterminar toda forma de vida')
      time.sleep(2)
      print(f'Ela se vira para {nome} e suas 4 cabeças dizem em unisono\n-Enfrente-me mortal')
      enrolação= input('Digite qualquer coisa para continuar')

      combate(9, nv)

      print('Com seu último golpe você a deixou atordoada, e abrindo o portal novamente\n ela foi sugada para sua antiga prisão mais uma vez')
      time.sleep(2)
      print(f'{nome} ficou com todas as riquezas do Dragão Ancião e dos goblins, agora ele é bem mais rico que vários reis')
      time.sleep(2)
      print('Ele foi comprando terrenos discretamente e depois de 2 anos\nele havia comprando o equivalente a um reino de porte médio')
      time.sleep(2)
      print(f'Os outros reinos não gostaram muito disso, e declararam guerra ao reino de {nome}lândia, nome dado por {nome}')
      time.sleep(2)
      print(f'{nome} passou o resto de sua vida em guerras intermináveis e morreu em uma delas poucos anos após se declarar rei')
      exit()

    if escolha == 2:
      print(f'{nome} temeu o que havia naquele portal, e não o abriu')
      time.sleep(2)
      print('Se satisfez com todo aquele tisouro, no meio dele, viu um belo ruby')
      time.sleep(1)
      print('Ao chegar mais perto dele viu que estava rachado')
      time.sleep(1)
      print('Além disso, vazava uma energia vermelha dele')
      time.sleep(1)
      print('Subtamente, o ruby se quebrou em vários pedaços e dele um imenso ser de fogo saiu de lá')
      time.sleep(1)
      print('- Eu sou morfgan, o senhos das chamas, me vingarei daqueles que me aprisionaram')
      time.sleep(1)
      enrolação= input('Digite qualquer coisa para continuar')

      combate(10, nv)
      time.sleep(1)
      print(f'Morfgan grune e se decipa no ar, {nome} é o vencedor')
      time.sleep(1)
      print('Agora todo aquele tesouro pertencia a ele, mas ele teria que defende-lo de ladrões')
      time.sleep(1)
      print('transportando seu dinheiro para lá, isolou-se do resto do mundo e dedicou sua vida a cuidar de suas riquezas')
      time.sleep(1)
      print('Lendas surgiram sobre o velho louco que guardava um grande tesouro,\n os que iam ver com seus próprios olhos, jamais retornavam')
      time.sleep(1)
      print(f'Esse foi o fim do grande {nome}')
      exit()
  if escolha == 2:
  #ESCOLHEU DEVOLVER TODO O TESOURO
   time.sleep(1) 
   print(f'Sem seder aos desejos de ficar com todo aquele ouro\n{nome} devolve tudo para os que foram roubados ')
   time.sleep(1) 
   print(f'Tal atitude, de tão nobre, chamou atenção do rei, que convocou {nome} até sua presença')
   time.sleep(1)
   print(f'{nome} chega ao castelo e o rei havia preparado um banquete em sua homenagem')
   time.sleep(1)
   print('Após horas comendo, conversando e não bebendo nada que fosse alcoolico')
   time.sleep(1)
   print(f'{nome} sentiu vontade de ir ao banheiro')
   time.sleep(1)
   print(f'Pedindo licença e se retirando, foi caminhando pelo castelo e parou para ouvir uma conversa escondido')
   time.sleep(1)
   print('Era o arqui-mago real e um jovem mago')
   time.sleep(1)
   print('Ouvindo a conversa entendeu que falavam sobre o dia que matariam o rei')
   time.sleep(1)
   print(f'Ao ouvir isso, {nome} se assustou e fez barulho')
   time.sleep(1)
   print('-Quem está ai? perguntou o arqui-mago que fez um sinal com a cabeça para o mago ir checar')
   time.sleep(1)
   print(f'Não havendo outra alternativa, {nome} se revela e enfrenta o mago')
   enrolação = input('Aperte enter para continuar')

   ganhos = LootAndXp(combate(11, nv), xp, nv, random.randint(50,65))
   xp = ganhos['xp']
   nv = ganhos['nv']
   atk+=ganhos['atk']
   defe+=ganhos['defe']
   life+=ganhos['life']
   speed+=ganhos['speed']
   imunBur=ganhos['imunBur']
   imunPoi=ganhos['imunPoi']

   time.sleep(1)
   print('Após derrotar o jovem mago, o arqui-mago olha para você e ri')
   time.sleep(1)
   print('-O que você fará agora? me atacar?')
   time.sleep(1)
   print(f'O que {nome} vai fazer?')
   escolha = int(input('1-Atacar o arqui-mago\n2-Contar tudo para o rei'))
   
   if escolha == 1:
   #ATACAR O ARQUI-MAGO
    time.sleep(1)
    print(f'{nome} avança na direção do arqui-mago')
    time.sleep(1)

    combate(12, nv)
    time.sleep(1)
    print(f'A luta acabou, {nome} derrotou o arqui-mago')
    time.sleep(1)
    print('A luta chamou atenção do rei e dos guardas que agoram o cercavam')
    time.sleep(1)
    print('O rei estava furioso')
    print('-Eu lhe convido para meu castelo e você mata meus homens de confiança?')
    time.sleep(1)
    print(f'{nome} tenta explicar, mas o rei ignora')
    print('-Guardas, prendam-no, daqui a 3 dias será sua execução')
    time.sleep(1)
    print(f'{nome} fica na prisão, e no terceiro dia o próprio rei vai até lá')
    time.sleep(1)
    print(f'-Você estava certo, diversos soldados e magos confessaram, meu antigo amigo queria me matar')
    time.sleep(1)
    print(f'-Peço que me perdoe, para compensar, lhe ofereço o cargo no conselho real')
    time.sleep(1)
    print(f'{nome} aceita a proposta, com seus conselhos o reino passa pela sua época de ouro')
    time.sleep(1)
    print(f'{nome} morreu com muita idade, sendo o mais honrado membro do conselho')
    exit()
   if escolha == 2:
     time.sleep(1)
     print(f'{nome} corre em direção á sala de jantar e conta tudo o que houve para o rei')
     time.sleep(1)
     print(f'O rei fica furioso... contra {nome}')
     time.sleep(1)
     print('Como ousa caluniar meu mais fiel amigo?')
     time.sleep(1)
     print('Guardas, prendam-no, sua execução será em 3 dias')
     time.sleep(1)
     print(f'Passando 3 dias na prisão, {nome} estava perdendo as esperanças')
     time.sleep(1)
     print('Quando derrepente um terremoto imenso foi capaz de derrubar a grade da sela')
     time.sleep(1)
     print(f'{nome}, correndo pelos corredores do castelo, queria saber o que foi aquilo')
     time.sleep(1)
     print(f'Na sala do trono, {nome} então vê o que causou aquilo')
     time.sleep(1)
     print('Uma grande serpente, invocada pelas mãos do arqui-mago')
     time.sleep(1)
     print('-Eu me chamo Tauros, a consumidora de mundos- disse a serpente')
     time.sleep(1)
     print('-Eu sou o novo rei e seu senhor Tauros- disse o arqui-mago')
     time.sleep(1)
     print('-Tauros não tem senhores- após dizer isso, a serpente matou o arqui-mago')
     time.sleep(1)
     print(f'E olhando para {nome} disse: -Você é o próximo')
     enrolação = input('Aperte enter para continuar')

     combate(13, nv)

     print(f'{nome} conseguiu, derrotou a temida serpente')
     time.sleep(1)
     print('Devido a tal feito, seu nome se espalhou por todo o mundo')
     time.sleep(1)
     print(f'{nome} passou o resto de sua vida viajando e ganhando muito ajudando pessoas contra todo tipo de criatura')
     time.sleep(1)
     print(f'{nome} foi a pessoa mais heroica do mundo, segundo o povo e os historiadores')
     exit()
if escolha == 2:
  #ESCOLHEU ENFRENTAR O SLIMES
  time.sleep(1)
  print(f'{nome} escolhe ir ajudar a vila e lutar contra os slimes')
  time.sleep(1)
  print('Ele encontra vários slimes atacando uma pequena vila')
  time.sleep(1)
  print(f'{nome} se prepara e avança na direção dos slimes')
  enrolação = input('Aperte enter para continuar')
  
  ganhos = LootAndXp(combate(14, nv), xp, nv, random.randint(40,50))
  xp = ganhos['xp']
  nv = ganhos['nv']
  atk+=ganhos['atk']
  defe+=ganhos['defe']
  life+=ganhos['life']
  speed+=ganhos['speed']
  imunBur=ganhos['imunBur']
  imunPoi=ganhos['imunPoi']
  
  time.sleep(1)
  print(f'{nome} conseguiu esmagar cada um dos slimes')
  time.sleep(1)
  print('Mas, mesmo cada um deles tendo virado possas de gosma')
  time.sleep(1)
  print('Elas começaram a se mexer e a se unir')
  time.sleep(1)
  print('Formaram então um slime gigante,\ncom um pedra brilhante em seu centro que se formou da união dos vários slimes')
  time.sleep(2)
  enrolação = input('Aperte enter para continuar')

  LootAndXp(combate(15, nv), xp, nv, random.randint(45,60))
  xp = ganhos['xp']
  nv = ganhos['nv']
  atk+=ganhos['atk']
  defe+=ganhos['defe']
  life+=ganhos['life']
  speed+=ganhos['speed']
  imunBur=ganhos['imunBur']
  imunPoi=ganhos['imunPoi']

  time.sleep(1)
  print('Derrotando o rei slime, a gosma dele começa a evaporar')
  time.sleep(1)
  print('No meio de onde estava a gosma, é possível ver a pedra que estava no coração do rei slime')
  time.sleep(1)
  print(f'{nome} então vai e a pega')
  time.sleep(1)
  print('Ao tocar na pedra, ela faz um pedido de ajuda')
  time.sleep(1)
  print(f'O que {nome} faz?')
  time.sleep(1)
  escolha = int(input('1-Aceita ajudar a pedra\n2-Rejeita ajudar\n'))

  if escolha == 1:
    #ACEITA AJUDAR A PEDRA
    time.sleep(1)
    print('A pedra lhe transmite um sentimento de felicidade\n e depois o teletransporta para uma ilha, com um grande templo no meio')
    time.sleep(2)
    print(f'{nome} logo entende que deve deixar a pedra lá')
    time.sleep(1)
    print('Mas no caminho ele é surpreendido por zumbis, os antigos habitantes da ilha')
    enrolação = input('Aperte enter para continuar')

    LootAndXp(combate(1, nv), xp, nv, random.randint(40,50))
    xp = ganhos['xp']
    nv = ganhos['nv']
    atk+=ganhos['atk']
    defe+=ganhos['defe']
    life+=ganhos['life']
    speed+=ganhos['speed']
    imunBur=ganhos['imunBur']
    imunPoi=ganhos['imunPoi']
    
    time.sleep(1)
    print(f'Conseguindo exterminar a horda, {nome} avança em direção ao templo')
    time.sleep(1)
    print('Quando finalmente chega mais perto, percebe que o templo está no meio de um grande lago')
    time.sleep(1)
    print('Antes que pudesse pensar em como passar, uma gigantesca tartaruga aparece')
    time.sleep(1)
    enrolação = input('Aperte enter para continuar')
    
    LootAndXp(combate(17, nv), xp, nv, random.randint(55,75))
    xp = ganhos['xp']
    nv = ganhos['nv']
    atk+=ganhos['atk']
    defe+=ganhos['defe']
    life+=ganhos['life']
    speed+=ganhos['speed']
    imunBur=ganhos['imunBur']
    imunPoi=ganhos['imunPoi']

    time.sleep(1)
    print('A grande criatura berra e cai morta')
    time.sleep(1)
    print(f'{nome} arranca um pedaço do casco e usa como bote')
    time.sleep(1)
    print('Então finalmente chega ao templo, sobe sua escadaria e coloca o cristal no altar')
    time.sleep(1)
    print('Um forte raio de luz sai da pedra em direção aos céus')
    time.sleep(1)
    print('O cristal então lhe revela que a cidade de Mystra está sendo atacada')
    time.sleep(1)
    print(f'O cristal pode levar {nome} para lá, mas também pode manda-lo para longe')
    time.sleep(1)
    print(f'O que {nome} faz?')
    time.sleep(1)
    escolha == int(input('1-Levar para Mystra\n2-Levar para longe\n'))
    
    if escolha == 1:
      #LEVAR PARA MYSTRA
      time.sleep(1)
      print(f'-Eu escolho Mystra, pois tem mais gente a ser salva- disse {nome}')
      time.sleep(1)
      print(f'O cristal se enfurece, e {nome} é levado para a sala do trono no castelo de Mystra')
      time.sleep(1)
      print('O lugar esta bem acabado, toda a parede e o teto estavam destruidos')
      time.sleep(1)
      print('Os pedaços, grandes e pequenos, de pedra giravam ao redor de lá por causa de um poderoso tornado')
      time.sleep(1)
      print('-TOLO- gritou um imenso ser de pele cinza com 4 braços')
      time.sleep(1)
      print('Aquela era a verdadeira forma do cristal, o Elemental supremo')
      time.sleep(1)
      print('-Eu me libertei graças a você, tentei lhe retribuir dano a oportunidade de fugir')
      time.sleep(1)
      print('-Mas você recusou, agora sou obrigado a mata-lo')
      time.sleep(1)
      enrolação = input('Aperte enter para continuar')

      combate(16, nv)

      print(f'Impressionante, {nome} consegue derrotar o Elemental supremo, ele explode em pequenos cristais')
      time.sleep(1)
      print(f'{nome} tem realmente o coração puro, escolheu salvar o mundo à sua própria vida')
      time.sleep(1)
      print(f'O mundo agradece e {nome} é coroado o novo rei(ou rainha) de Mystra')
      time.sleep(1)
      print(f'{nome} foi um lendário governate, reconhecido por todo o mundo, em todos os tempos')
      exit()

    if escolha == 2:
      #LEVAR PARA LONGE
      print(f'-Eu escolho ir para longe, não tenho como enfrentar tal ameaça- disse {nome}')
      time.sleep(1)
      print('O cristal o leva para um campo aberto, lindo e verde')
      time.sleep(1)
      print('Mas detras de uma árvore sai um homem com um sobretudo preto e um grande chapeu')
      time.sleep(1)
      print(f'O homem de olhos vermelhos vê {nome} e sorri')
      time.sleep(1)
      print('-Sou o lorde vampiro subordinado ao Elemental supremo, ou pedra mágica como você deve conhece-la')
      time.sleep(1)
      print('-Obrigado por libertar meu senhor, ele agora me deu uma ordem')
      time.sleep(1)
      print('Matar você')
      time.sleep(1)
      enrolação = input('Aperte enter para continuar')
      
      combate(3, nv)
      
      time.sleep(1)
      print(f'Foi por pouco, mas {nome} conseguiu derrotar seu inimigo')
      time.sleep(1)
      print('Mesmo estando longe, ele conseguia ver a fumaça vindo de Mystra')
      time.sleep(1)
      print('Ele tinha feito uma escolha e agora se arrependia')
      time.sleep(1)
      print('Passou o resto de seus dias fugindo dos elementais feitos pelo Elemental supremo')
      exit()
  if escolha == 2:
    #RECUSA AJUDAR A PEDRA
    time.sleep(1)
    print(f'Julgando ter sido um delírio, {nome} ignora a pedra e volta para Mystra')
    time.sleep(1)
    print('Ao chegar lá, um soldado lhe recepciona e diz que seu capitão o chama')
    time.sleep(1)
    print(f'{nome} o segue e encontra o tal capitão')
    time.sleep(1)
    print('-Olá, sou capitão da guarda real, eu tenho grandes planos para esta pedra mágica')
    time.sleep(1)
    print('-Você poderia dar ela para mim?')
    time.sleep(1)
    escolha = int(input('1-Dar a pedra\n2-Não dar a pedra\n'))
    if escolha == 1:
      #DAR A PEDRA
      time.sleep(1)
      print('Ao entregar a pedra, o capitão sorri')
      time.sleep(1)
      print('Ele segura a pedra e linhas luminosas surgem em seu braço e se espalham para todo o corpo')
      time.sleep(1)
      print('O capitão toca em seus soldados e os absorve, deixando seus corpos secos cairem')
      time.sleep(1)
      print('Depois disso, ele vai na sua direção')
      enrolação = input('Aperte enter para continuar')

      combate(20, nv)

      print(f'Acabou, {nome} derrotou o capitão')
      time.sleep(1)
      print('O povo comemora e faz um festa em homenagem ao herói')
      time.sleep(1)
      print(f'O rei estabelece {nome} como soldado do reino')
      time.sleep(1)
      print(f'{nome} logo é promovido e foi o maior capitão da história do reino')
      exit()
    if escolha == 2:
      time.sleep(1)
      print('Se recusando a entregar, o capitão dá um sinal com a cabeça para seu soldado')
      time.sleep(1)
      print(f'O soldado puxa um grande machado e vai até {nome}')

      LootAndXp(combate(18, nv), xp, nv, random.randint(50,60))
      xp = ganhos['xp']
      nv = ganhos['nv']
      atk+=ganhos['atk']
      defe+=ganhos['defe']
      life+=ganhos['life']
      speed+=ganhos['speed']
      imunBur=ganhos['imunBur']
      imunPoi=ganhos['imunPoi']

      time.sleep(1)
      print('Durante a luta, o cristal foi danificado')
      time.sleep(1)
      print('O capitão pula na sua direção e toma a pedra')
      time.sleep(1)
      print('A pedra explode, levando os dois para um plano alternativo')
      time.sleep(1)
      print(f'Perambulando por aquele lugar, {nome} encontra o capitão sendo possuido pelo cristal')
      time.sleep(1)
      print('-Acabe com isso agora! O cristal está me controlando, socorro')
      time.sleep(1)
      combate(19, nv)

      print('Após derrotar o cristal, o capitão consegue ficar liberto')
      time.sleep(1)
      print(f'Como agradecimento, ele oferece a {nome} um cargo como principal subordinado dele')
      time.sleep(1)
      print(f'{nome} recusa e diz que vai seguir seu próprio caminho')
      time.sleep(1)
      print(f'{nome} decide explorar o mundo em busca de artefatos mágicos perigosos')
      time.sleep(1)
      print('Ele livrou o mundo de diversos perigos, obteve a imortalidade e continua protegendo o mundo até hj')
      time.sleep(1)
      print('Mas fez tudo isso em segredo, e nunca foi reconhecido')
      exit()
      
