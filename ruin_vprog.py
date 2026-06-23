from bprg import *
from kandinsky import fill_rect as drawRect,draw_string as drawTxt,get_pixel as getPxl
from ion import keydown as key
from time import monotonic as cTime,sleep
from random import randint as rInt,seed as rSeed

TARG_SPF=0.02 #50fps

NAME,AUTH,START_MSG,EDITOR_URL=" R U | N "," by F | M E ","Press [OK] to start","/python/fime/ruin_lvl_maker"
SAVEFILE="ruin.sav"

def save_prog(lvl,frames):
  try:
    f = open(SAVEFILE,"w")
    f.truncate(0)
    f.write("%s\n%s"%(lvl,frames))
  except:return
def load_prog():
  try:
    with open(SAVEFILE,"r") as f:
      lvl=int(f.readline())
      frames=int(f.readline())
      return lvl,frames
  except:return 0,0

class Entity():
  def __init__(it,x,y,w,h,drawFonc):
    it.x,it.y,it.w,it.h=x,y,w,h
    it.draw=lambda:drawFonc(it)
  def hitBox(it,it2):
    if it.x<it2.x+it2.w and it2.x<it.x+it.w and it.y<it2.y+it2.h and it2.y<it.y+it.h:return 1
    return 0
class Platform(Entity):
  def __init__(it,x,y,w,h):super().__init__(x,y,w,h,drawPlatform)
  def hitBox(it,it2):
    if super().hitBox(it2) and it2.y+it2.h<it.y+it.h:return 1
    return 0
class Movable(Entity):
  def __init__(it,*arg):
    super().__init__(*arg)
    it.vx,it.vy,it.grounded=0,0,0
  def setVel(it,vx,vy):it.vx,it.vy=vx,vy
  def addVel(it,vx,vy):
    it.vx+=vx
    it.vy+=vy
  def applyPhysics(it):
    if it.grounded:
      it2=it.grounded
      it.vy=0
      if it.x>it2.x+it2.w or it2.x>it.x+it.w:
        it.grounded=0
    else :
      it.addVel(0,0.2)
      it.y+=min(it.vy,4)
    it.vx/=1.3
    it.x+=it.vx
    it.x=max(min(it.x,320-it.w),0)
  def onPlatform(it,plat):
    if plat.hitBox(it) and not it.grounded and it.vy>0:
      it.grounded=plat
      it.vy,it.y=0,plat.y-it.h
  def jump(it):it.vy,it.grounded=-4.3,0
class Enemy(Movable):
  def __init__(it,*arg):
    super().__init__(*list(arg)+[drawEnemy])
  def applyPhysics(it):
    if it.grounded:
      it2=it.grounded
      if it2.w>20:
        if it.x<it2.x+it.w:
          it.vx+=0.05
        elif it.x>it2.x+it2.w-it.w*2:
          it.vx-=0.05
        elif it.vx==0:
          it.vx=1
    super().applyPhysics()
    it.vx*=1.3
class Bullet(Movable):
  def __init__(it,it2,input_vy):
    super().__init__(it2.x+it2.w/2,it2.y+it2.h/2,3,3,drawBullet)
    it.setVel(copysign(3,it2.vx)+it2.vx,it2.vy+input_vy*2-1)
  def applyPhysics(it):
    it.addVel(0,0.2)
    it.x+=it.vx
    it.y+=it.vy

def fade(col1,col2,n):return tuple([i1*(1-n)+i2*n for i1,i2 in zip(col1,col2)])
def hideEntity(it):
  drawRect(int(it.x),int(it.y),int(it.w),int(it.h),BG_COL)

#def shadow(it):""
def shadow(it):
  for i in range(1,6):
    drawRect(int(it.x-i*2),int(it.y+i*it.h),it.w-i,it.h,fade(BLACK,BG_COL,i/6))
#def drawBaseEntity(it,col):
#  drawRect(int(it.x),int(it.y),it.w,it.h,col)
def drawBaseEntity(it,col):
  drawRect(int(it.x+2),int(it.y),it.w-2,it.h,col)
  drawRect(int(it.x),int(it.y),2,it.h,BLACK)
#def drawPlayer(it):
#  drawBaseEntity(it,PL_COL)
def drawPlayer(it):
  drawBaseEntity(it,PL_COL)
  drawRect(int(it.x+it.w/2),int(it.y+7),2,3,BLACK)
  for i in (3,it.h-3):drawRect(int(it.x+i+it.vx/4),int(it.y+2),2,2,BLACK)
#def drawEnemy(it):
#  drawBaseEntity(it,NMY_COL)
#  drawRect(int(it.x),int(it.y+it.h/2),it.w,it.h//2,NMY_COL2)
def drawEnemy(it):
  drawBaseEntity(it,NMY_COL)
  drawRect(int(it.x+2),int(it.y+it.h/2),it.w-2,it.h//2,NMY_COL2)
  for i in (3,it.h-3):drawRect(int(it.x+i),int(it.y+it.h/2-2),2,5,BLACK)
#def drawPlatform(it):
#  drawRect(int(it.x),int(it.y),it.w,it.h*2,PTF_COL)
def drawPlatform(it):
  drawBaseEntity(it,PTF_COL)
  shadow(it)
#def drawDoor(it):
#  drawRect(int(it.x),int(it.y-it.h//2),it.w,it.h+it.h//2,BLACK)
def drawDoor(it):
  drawRect(int(it.x),int(it.y),it.w,it.h,BLACK)
  for i in range(1,5):
    drawRect(int(it.x+1),int(it.y+it.h-i*2),int(it.w/2-i*2+3),1,fade(PTF_COL,BLACK,i/6))

def drawBullet(it):
  drawRect(int(it.x),int(it.y),it.w,it.h,BLT_COL)

def createDoor(l1):
  x,y,w,h=l1
  x,y,w,h=x+w//2-7.5,y-15,15,15
  return Entity(x,y,w,h,drawDoor)
def createPlayer(l1):
  x,y,w,h=l1
  y,w,h=y-10,10,10
  return Movable(x,y,w,h,drawPlayer)
def createEnemy(l1,id):
  x,y,w,h=l1
  x,y,w,h=x+10*id,y-10,10,10
  return Enemy(x,y,w,h)
def unpackPlatforms(n,type):
  string=levels(type)[n]
  Hex2Int=lambda n:int("0x"+n)
  level=[]
  for i in range(0,len(string),9):
    ptf_str=string[i:i+9]
    plat=[]
    for j in range(0,8,2):plat+=[Hex2Int(ptf_str[j:j+2])*5]
    plat.append(int(ptf_str[-1]))
    level.append(plat)
  return level
def loadLevel(lvl,type):
  file=unpackPlatforms(lvl,type)
  platforms,enemies=[],[]
  for i in file:
    platforms+=[Platform(*i[0:4])]
    if i[4]:
      enemies+=[createEnemy(i[0:4],j) for j in range(i[4])]
  player,door=createPlayer(file[0][0:4]),createDoor(file[-1][:4])
  return [player,platforms,enemies,door]

def titleAnim(h=150):
  y,s_init,p=int(h),20,0
  drawRect(0,0,320,222,BG_COL)
  while y>5:
    if key(4):p=1
    s=(1-y/h)*s_init+p
    y=round(y-s,1)
    sleep(TARG_SPF*2)
    if p:drawRect(0,0,320,222,BG_COL)
    drawTxt(NAME,160-len(NAME)*5,int(101+h-y),BG_COL,PTF_COL)
    drawTxt(AUTH,160-len(AUTH)*5,int(131+h-y),PTF_COL,BG_COL)
    drawTxt(" "+difficulty+" ",150-5*len(difficulty),int(171+h-y),BG_COL,fade(BG_COL,PL_COL,abs(sin(cTime()))))
    drawTxt(START_MSG,160-len(START_MSG)*5,int(196+h-y),fade(BG_COL,PL_COL,abs(sin(cTime()))),BG_COL)
def shortTransition():
  for i in range(30):drawRect(0,0,320,222,fade(BG_COL,BLACK,sin(i/30)))
def gameover():
  drawRect(0,0,320,222,BG_COL)
  drawTxt(" YOU DIED ",110,106,BG_COL,PTF_COL)
  release(4)
  while not key(4):drawTxt("press [OK] to exit",70,196,fade(BG_COL,PL_COL,abs(sin(cTime()))),BG_COL)
  exit()
  
def releaseKey(x):
  while key(x):pass

class GameEngine():
  def __init__(it,lvl_type="original"):
    it.status,it.lvl_type,it.lvl_nb=0,lvl_type,len(levels(lvl_type))
    it.lvl,it.total_frame=load_prog()
  def nextLevel(it):
    if it.status==2:
      it.playTransition(mode=1)
      it.lvl+=1
      save_prog(it.lvl,it.total_frame)
      it.playTransition()
    else:shortTransition()
  def endMsg(it):
    global lives
    t=it.total_frame*TARG_SPF
    msg=["You finished the ",
"{} original levels !".format(it.lvl_nb),
"","Virtual time: {} min {}s".format(t//60,round(t%60,2)),
"","Download the level maker at :",
"my.numworks.com",
EDITOR_URL]
    if it.lvl_type=="custom":msg=[msg[3]]
    for i,txt in enumerate(msg):
      drawTxt(txt,160-len(txt)*5,111-(len(msg)//2-i)*20,PTF_COL,BG_COL)
    save_prog(0,0)
    lives=3
    it.lvl,it.frame_nb,it.total_frame=0,0,0
    while not key(4):
      drawTxt("Press [OK] to exit",70,200,fade(BG_COL,PL_COL,abs(sin(cTime()))),BG_COL)
    releaseKey(4)
    titleAnim(),game.playTransition()
  def playTransition(it,h=222,mode=0):
    try:l=loadLevel(it.lvl,it.lvl_type)
    except:return
    entities,s_init,y=l[1]+[l[3]],20,int(h)
    if not mode:
      entities+=[l[0]]+l[2]
      for entity in entities:entity.y-=y
    del l
    while 1:
      if y<1:break
      if mode:s=(1-y/h)*s_init+5
      else:s=sqrt(y/h)*s_init
      y=round(y-s,1)
      sleep(TARG_SPF*2)
      drawRect(0,0,320,222,BG_COL)
      for entity in entities:
        entity.y+=s
        entity.draw()
  def playLevel(it):
    global lives,blt
    if it.status==1:
      if difficulty=="hardcore":gameover()
      elif difficulty=="hearts":lives-=1
    if lives==0:gameover()
    motion=0  
    drawRect(0,0,320,222,BG_COL)
    player,platforms,enemies,door=loadLevel(it.lvl,it.lvl_type)
    frame_nb,shot_frame,bullets,it.status=0,0,[],0
    while it.status==0:
      if difficulty=="hearts":
        for i in range(lives):rect(160-16+i*12,3,8,8,(255,0,0))
      elif difficulty=="3 bullets":
        for i in range(blt):rect(160-16+i*12,3,8,8,(255,255,0))
      t=cTime()
      frame_nb+=1
      player.addVel(key(3)-key(0),0.1*(1-key(4)))
      if (frame_nb+9)%10==0:door.draw()
      for b in bullets:
        hideEntity(b)
        b.applyPhysics()
        if b.y>222:bullets.remove(b)
        else:b.draw()
      for movable in enemies+[player]:
        hideEntity(movable)
        if movable!=player:
          if movable.hitBox(player):
            it.status=1
            break
          for b in bullets:
            if b.hitBox(movable):
              movable.addVel(b.vx/3,b.vy/3)
          if movable.y>222:
            enemies.remove(movable)
        movable.applyPhysics()
        for platform in platforms:
          movable.onPlatform(platform)
          if (frame_nb+9)%10==0 and movable==player:platform.draw()
          if movable==player:platform.draw()
        movable.draw()
        if frame_nb-shot_frame>10 and key(16) and blt>0:
          shot_frame=frame_nb
          bullets+=[Bullet(player,key(2)-key(1))]
          if difficulty=="3 bullets":
            blt-=1
            rect(160-16,3,32,8,BG_COL)
      if player.grounded:
        if key(4):player.jump()          
        if player.hitBox(door)==1:it.status=2
      if player.y>222:it.status=1
      while cTime()-t<TARG_SPF:pass
      if key(17):
        drawTxt(" P A U S E D ",95,101,BG_COL,PTF_COL)
        frame_nb+=10-frame_nb%10
        releaseKey(17)
        while not key(17):pass
        releaseKey(17)
        drawRect(95,101,130,20,BG_COL)
      it.total_frame+=frame_nb
      if key(52):exit()

def levels(lvl_type):
  if lvl_type!="custom":return ("011606010071632010391606010",
"011606010111606010231606010341606010",
"0216060101e1601010331606010",
"042306010161c060100e1410011290f06011350f06010",
"08280601026280a011342102010291b020100f1b0201003140a011190d0201026080a010",
"0624060101a28020102b220201031190a01118160a0110a0e020101b070201030070a010",
"0527060101927010102a27010103420060112819060110c19060110511010100b09010101a060a013330606010",
"0428060100c2001010041c010100c16010102f1e01010391801010301101010260b0601012070a010",
"0128060101526010103026010103921010102d1a010101a1501010230e01010310d0a010",
"052506010051e06011051606011050f06011050806011301806010",
"0628060101623060110c1e020101719020102b19020103b12020102b0c02010170c02010060906010",
"0228060101d28060103122060111d1d020100e1b020100515020100e0f02010240d06011320d06010",
"0105040100c05350100823010101a1f060111e1801010341206011280e06010280e06010",
"362706010292006011351a020102f1302010042006011041706011080f010100c0706010",
"032806010242806011342106011251906011081901010021201010090c01010150706011270706010",
"042806010192306011251e06010311a060112514060100316060110a0e01010140806010",
"3726060101f2601010042601010081e010101019010102519010102f1006011220b06010",
"1a28060102a2306010331b01010251701010141706011051201010100a010101c0606010",
"0327060100c20010101619010102119030112d1903011351306010260a060111a0a01010050a06010",
"0220060101d1b020113117020111c0f06010",
"2f28060101428040110422020100e1b04010271a04011321402010270e040110e0e04011040806010")
  else:
    return [edited[0]]

edited=["0220060101d1b020113117020111c0f06010"]

BG_COL,PTF_COL,NMY_COL,NMY_COL2,PL_COL,BLACK=(75,40,40),(200,100,100),(0,150,255),(0,50,200),(240,10,10),(0,0,0)
mod=["normal","hearts","3 bullets","hardcore","custom"]
difficulty=mod[0]

s,ms=0,1

releaseKey(4)
while not key(4):
  s=passlimits(s+keyS(3)-keyS(0),0,len(mod)-1)
  difficulty=mod[s]
  if difficulty=="normal":BG_COL,PTF_COL,NMY_COL,NMY_COL2,PL_COL=(75,40,40),(200,100,100),(0,150,255),(0,50,200),(240,10,10)
  if difficulty=="hearts":BG_COL,PTF_COL,NMY_COL,NMY_COL2,PL_COL=(40,75,75),(100,200,200),(255,200,180),(255,150,0),(255,255,255)
  if difficulty=="3 bullets":BG_COL,PTF_COL,NMY_COL,NMY_COL2,PL_COL=(0,40,75),(130,130,130),(255,0,0),(0,0,0),(255,130,0)
  if difficulty=="hardcore":BG_COL,PTF_COL,NMY_COL,NMY_COL2,PL_COL=(40,40,40),(150,150,150),(255,255,225),(100,0,255),(10,200,10)
  if difficulty=="custom":BG_COL,PTF_COL,NMY_COL,NMY_COL2,PL_COL=(255,182,49),(255,255,255),(0,100,200),(170,170,170),(255,0,0)
  if ms!=s:
    background(BG_COL),drawRect(90,90,140,40,PTF_COL),drawTxt("     MODE     ",90,91,BG_COL,PTF_COL)
    drawRect(92,110,136,18,BG_COL),drawTxt(difficulty,160-5*len(difficulty),110,PTF_COL,BG_COL)
    for i in range(5):rect(94+i,119-i,1,i*2,PL_COL),rect(225-i,119-i,1,i*2,PL_COL)
    ms=s

BLT_COL=PTF_COL if difficulty!="3 bullets" else (255,255,0)

lvl_type=difficulty
releaseKey(4)

game=GameEngine(lvl_type)
titleAnim(),game.playTransition()
lives=blt=3

while 1:
  if game.lvl>=game.lvl_nb:
    game.endMsg()
  game.playLevel()
  game.nextLevel()
