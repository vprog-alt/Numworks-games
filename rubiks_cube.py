from bprg import *

theme,thm=0,[(0,200,200),(0,0,0),(225,225,225),(255,182,49)]
bg,ln=thm[theme],(0,0,0)
mode=input(">>> 2D ou 3D: ")

blue,red,green,yellow,orange,white,black=(49,28,255),(255,48,0),(0,243,57),(255,255,0),(255,150,0),(255,255,255),(0,0,0)

mag,v=0.04,0.03
scr=scr_mov=om=ov=tms=tm=m=xtext=0
move=rotate=""
scramble,timer,solved=False,False,True

c1=c2=c3=c4=c5=c6=c7=c8=c9=blue
c10=c11=c12=c13=c14=c15=c16=c17=c18=white
c19=c20=c21=c22=c23=c24=c25=c26=c27=green
c28=c29=c30=c31=c32=c33=c34=c35=c36=red
c37=c38=c39=c40=c41=c42=c43=c44=c45=orange
c46=c47=c48=c49=c50=c51=c52=c53=c54=yellow

if mode=="2D":
  t,eq,x,y=16,5,88,88
  def carre(x,y,c):rect(x,y,t,t,c)
  def face(x,y,a1,a2,a3,a4,a5,a6,a7,a8,a9):carre(x,y,a1),carre(x+t,y,a2),carre(x+t*2,y,a3),carre(x,y+t,a4),carre(x+t,y+t,a5),carre(x+t*2,y+t,a6),carre(x,y+t*2,a7),carre(x+t,y+t*2,a8),carre(x+t*2,y+t*2,a9)
  def face_j(x,y,a1,a2,a3,a4,a5,a6,a7,a8,a9):carre(x-t-eq*2,y,a3),carre(x-t-eq*2,y+t,a6),carre(x-t-eq*2,y+t*2,a9),carre(x+t*3,y-t*4-eq*2,a3),carre(x+t*4,y-t*4-eq*2,a2),carre(x+t*5,y-t*4-eq*2,a1),carre(x+t*9+eq*2,y,a1),carre(x+t*9+eq*2,y+t,a4),carre(x+t*9+eq*2,y+t*2,a7),carre(x+t*3,y+t*6+eq*2,a9),carre(x+t*4,y+t*6+eq*2,a8),carre(x+t*5,y+t*6+eq*2,a7)
  def cube():face(x-eq,y,c1,c2,c3,c4,c5,c6,c7,c8,c9),face(x+t*3,y,c10,c11,c12,c13,c14,c15,c16,c17,c18),face(x+t*6+eq,y,c19,c20,c21,c22,c23,c24,c25,c26,c27),face(x+t*3,y-t*3-eq,c28,c29,c30,c31,c32,c33,c34,c35,c36),face(x+t*3,y+t*3+eq,c37,c38,c39,c40,c41,c42,c43,c44,c45),face_j(x,y,c46,c47,c48,c49,c50,c51,c52,c53,c54)
elif mode=="3D":
  mag,t,x,y=mag-0.01,20,94,35
  def carre_left(x,y,c):
    a=-1
    for i in range(0,t,2):
      a+=1
      rect(x+i,y+a,2,t+2,c)
  def carre_right(x,y,c):
    a=t//2
    for i in range(0,t,2):
      a-=1
      rect(x+i,y+a,2,t+2,c)
  def carre_up(x,y,c):
    a,x=0,x+t 
    for i in range(t//2):
      rect(x,y+i,a*4,1,c)
      a,x=a+1,x-2
    for i in range(t//2):
      rect(x,y+i+t//2,a*4,1,c)
      a,x=a-1,x+2
  def face_left(x,y,a1,a2,a3,a4,a5,a6,a7,a8,a9):carre_left(x,y,a1),carre_left(x+t+2,y+t//2+1,a2),carre_left(x+t*2+4,y+t+2,a3),carre_left(x,y+t+5,a4),carre_left(x+t+2,y+t+t//2+6,a5),carre_left(x+t*2+4,y+t*2+7,a6),carre_left(x,y+t*2+10,a7),carre_left(x+t+2,y+t*2+t//2+11,a8),carre_left(x+t*2+4,y+t*3+12,a9)
  def face_right(x,y,a1,a2,a3,a4,a5,a6,a7,a8,a9):carre_right(x,y+t+2,a1),carre_right(x+t+2,y+t//2+1,a2),carre_right(x+t*2+4,y,a3),carre_right(x,y+t*2+7,a4),carre_right(x+t+2,y+t+t//2+6,a5),carre_right(x+t*2+4,y+t+5,a6),carre_right(x,y+t*3+12,a7),carre_right(x+t+2,y+t*2+t//2+11,a8),carre_right(x+t*2+4,y+t*2+10,a9)
  def face_up(x,y,a1,a2,a3,a4,a5,a6,a7,a8,a9):carre_up(x+t*2+5,y-t//2+5,a1),carre_up(x+t*3+7,y+6,a2),carre_up(x+t*4+9,y+t//2+7,a3),carre_up(x+t+3,y+t//2-4,a4),carre_up(x+t*2+5,y+t-3,a5),carre_up(x+t*3+7,y+t+t//2-2,a6),carre_up(x+1,y+t-3,a7),carre_up(x+t+3,y+t+t//2-2,a8),carre_up(x+t*2+5,y+t*2-1,a9)
  def cube():face_left(x,y+t*2,c10,c11,c12,c13,c14,c15,c16,c17,c18),face_right(x+t*3+6,y+t*2,c19,c20,c21,c22,c23,c24,c25,c26,c27),face_up(x,y+t//2,c28,c29,c30,c31,c32,c33,c34,c35,c36)

def face_anclk(*R):return R[1:]+(R[0],)
def face_clk(*R):return R[-1:]+R[:-1]

background(bg),cube()

while True:

##### L #####
  if key(12) or scr==1:#L'
    move="L'"
    for i in range(3):
      if i<2:c1,c2,c3,c6,c9,c8,c7,c4=face_anclk(c1,c2,c3,c6,c9,c8,c7,c4)
      c10,c13,c16,c37,c40,c43,c54,c51,c48,c28,c31,c34=face_anclk(c10,c13,c16,c37,c40,c43,c54,c51,c48,c28,c31,c34)
      cube(),sleep(v)
    sleep(mag)
  if key(18) or scr==2:#L
    move="L"
    for i in range(3):
      if i<2:c1,c2,c3,c6,c9,c8,c7,c4=face_clk(c1,c2,c3,c6,c9,c8,c7,c4)
      c10,c13,c16,c37,c40,c43,c54,c51,c48,c28,c31,c34=face_clk(c10,c13,c16,c37,c40,c43,c54,c51,c48,c28,c31,c34)
      cube(),sleep(v)
    sleep(mag)

##### R #####
  if key(17) or scr==3:#R
    move="R"
    for i in range(3):
      if i<2:c19,c20,c21,c24,c27,c26,c25,c22=face_clk(c19,c20,c21,c24,c27,c26,c25,c22)
      c12,c15,c18,c39,c42,c45,c52,c49,c46,c30,c33,c36=face_anclk(c12,c15,c18,c39,c42,c45,c52,c49,c46,c30,c33,c36)
      cube(),sleep(v)
    sleep(mag)
  if key(23) or scr==4:#R'
    move="R'"
    for i in range(3):
      if i<2:c19,c20,c21,c24,c27,c26,c25,c22=face_anclk(c19,c20,c21,c24,c27,c26,c25,c22)
      c12,c15,c18,c39,c42,c45,c52,c49,c46,c30,c33,c36=face_clk(c12,c15,c18,c39,c42,c45,c52,c49,c46,c30,c33,c36)
      cube(),sleep(v)
    sleep(mag)

##### U #####
  if key(13) or scr==5:#U
    move="U"
    for i in range(3):
      if i<2:c28,c29,c30,c33,c36,c35,c34,c31=face_clk(c28,c29,c30,c33,c36,c35,c34,c31)
      c48,c47,c46,c21,c20,c19,c12,c11,c10,c3,c2,c1=face_clk(c48,c47,c46,c21,c20,c19,c12,c11,c10,c3,c2,c1)
      cube(),sleep(v)
    sleep(mag)
  if key(16) or scr==6:#U'
    move="U'"
    for i in range(3):
      if i<2:c28,c29,c30,c33,c36,c35,c34,c31=face_anclk(c28,c29,c30,c33,c36,c35,c34,c31)
      c48,c47,c46,c21,c20,c19,c12,c11,c10,c3,c2,c1=face_anclk(c48,c47,c46,c21,c20,c19,c12,c11,c10,c3,c2,c1)
      cube(),sleep(v)
    sleep(mag)

##### D #####
  if key(19) or scr==7:#D
    move="D"
    for i in range(3):
      if i<2:c37,c38,c39,c42,c45,c44,c43,c40=face_anclk(c37,c38,c39,c42,c45,c44,c43,c40)
      c16,c17,c18,c25,c26,c27,c52,c53,c54,c7,c8,c9=face_anclk(c16,c17,c18,c25,c26,c27,c52,c53,c54,c7,c8,c9)
      cube(),sleep(v)
    sleep(mag)
  if key(22) or scr==8:#D'
    move="D'"
    for i in range(3):
      if i<2:c37,c38,c39,c42,c45,c44,c43,c40=face_clk(c37,c38,c39,c42,c45,c44,c43,c40)
      c16,c17,c18,c25,c26,c27,c52,c53,c54,c7,c8,c9=face_clk(c16,c17,c18,c25,c26,c27,c52,c53,c54,c7,c8,c9)
      cube(),sleep(v)
    sleep(mag)

##### F #####
  if key(14) or scr==9:#F'
    move="F'"
    for i in range(3):
      if i <2:c10,c11,c12,c15,c18,c17,c16,c13=face_anclk(c10,c11,c12,c15,c18,c17,c16,c13)
      c34,c35,c36,c19,c22,c25,c39,c38,c37,c9,c6,c3=face_anclk(c34,c35,c36,c19,c22,c25,c39,c38,c37,c9,c6,c3)
      cube(),sleep(v)
    sleep(mag)
  if key(15) or scr==10:#F
    move="F"
    for i in range(3):
      if i <2:c10,c11,c12,c15,c18,c17,c16,c13=face_clk(c10,c11,c12,c15,c18,c17,c16,c13)
      c34,c35,c36,c19,c22,c25,c39,c38,c37,c9,c6,c3=face_clk(c34,c35,c36,c19,c22,c25,c39,c38,c37,c9,c6,c3)
      cube(),sleep(v)
    sleep(mag)

##### B #####
  if key(20) or scr==12:#B
    move="B"
    for i in range(3):
      if i<2:c48,c47,c46,c49,c52,c53,c54,c51=face_anclk(c48,c47,c46,c49,c52,c53,c54,c51)
      c28,c29,c30,c21,c24,c27,c45,c44,c43,c7,c4,c1=face_anclk(c28,c29,c30,c21,c24,c27,c45,c44,c43,c7,c4,c1)
      cube(),sleep(v)
    sleep(mag)
  if key(21) or scr==11:#B'
    move="B'"
    for i in range(3):
      if i<2:c48,c47,c46,c49,c52,c53,c54,c51=face_clk(c48,c47,c46,c49,c52,c53,c54,c51)
      c28,c29,c30,c21,c24,c27,c45,c44,c43,c7,c4,c1=face_clk(c28,c29,c30,c21,c24,c27,c45,c44,c43,c7,c4,c1)
      cube(),sleep(v)
    sleep(mag)

##### CENTERS #####
  if key(24) or scr==13:#M'
    move="M'"
    for i in range(3):
      c11,c14,c17,c38,c41,c44,c53,c50,c47,c29,c32,c35=face_clk(c11,c14,c17,c38,c41,c44,c53,c50,c47,c29,c32,c35)
      cube(),sleep(v)
    sleep(mag)
  if key(29) or scr==14:#M
    move="M"
    for i in range(3):
      c11,c14,c17,c38,c41,c44,c53,c50,c47,c29,c32,c35=face_anclk(c11,c14,c17,c38,c41,c44,c53,c50,c47,c29,c32,c35)
      cube(),sleep(v)
    sleep(mag)
  if key(25) or scr==15:#E
    move="E"
    for i in range(3):
      c4,c5,c6,c13,c14,c15,c22,c23,c24,c49,c50,c51=face_anclk(c4,c5,c6,c13,c14,c15,c22,c23,c24,c49,c50,c51)
      cube(),sleep(v)
    sleep(mag)
  if key(28) or scr==16:#E'
    move="E'"
    for i in range(3):
      c4,c5,c6,c13,c14,c15,c22,c23,c24,c49,c50,c51=face_clk(c4,c5,c6,c13,c14,c15,c22,c23,c24,c49,c50,c51)
      cube(),sleep(v)
    sleep(mag)
  if key(26) or scr==17:#S'
    move="S'"
    for i in range(3):
      c31,c32,c33,c20,c23,c26,c42,c41,c40,c8,c5,c2=face_anclk(c31,c32,c33,c20,c23,c26,c42,c41,c40,c8,c5,c2)
      cube(),sleep(v)
    sleep(mag)
  if key(27) or scr==18:#S
    move="S"
    for i in range(3):
      c31,c32,c33,c20,c23,c26,c42,c41,c40,c8,c5,c2=face_clk(c31,c32,c33,c20,c23,c26,c42,c41,c40,c8,c5,c2)
      cube(),sleep(v)
    sleep(mag)

##### ROTATE #####
  if key(0) and rotate=="":rotate,scr_mov,om,ov="L",3,mag,v 
  if key(3) and rotate=="":rotate,scr_mov,om,ov="R",3,mag,v 
  if key(1) and rotate=="":rotate,scr_mov,om,ov="U",3,mag,v 
  if key(2) and rotate=="":rotate,scr_mov,om,ov="D",3,mag,v 
  if key(33) and rotate=="":rotate,scr_mov,om,ov="B",3,mag,v
  if key(34) and rotate=="":rotate,scr_mov,om,ov="F",3,mag,v
  if rotate!="":
    mag,v=0,0
    if rotate=="L":
      if scr_mov==3:scr=5
      if scr_mov==2:scr=15
      if scr_mov==1:scr=7
    if rotate=="R":
      if scr_mov==3:scr=6
      if scr_mov==2:scr=16
      if scr_mov==1:scr=8
    if rotate=="U":
      if scr_mov==3:scr=1
      if scr_mov==2:scr=14
      if scr_mov==1:scr=3
    if rotate=="D":
      if scr_mov==3:scr=2
      if scr_mov==2:scr=13
      if scr_mov==1:scr=4
    if rotate=="B":
      if scr_mov==3:scr=9
      if scr_mov==2:scr=17
      if scr_mov==1:scr=12
    if rotate=="F":
      if scr_mov==3:scr=10
      if scr_mov==2:scr=18
      if scr_mov==1:scr=11
    scr_mov-=1
    if scr_mov<0:mag,v,scr,rotate=om,ov,"",""
     
##### SCRAMBLE #####
  if keyS(50) and scramble==False:
    scramble,solved,om,ov,scr_mov=True,False,mag,v,31
    mag=v=0
  if scramble==True:
    scr,scr_mov=randint(1,18),scr_mov-1
    if scr_mov<0:mag,v,scr,scramble=om,ov,"",False

#### RESET #####
  if keyS(48):
    c1=c2=c3=c4=c5=c6=c7=c8=c9=blue
    c10=c11=c12=c13=c14=c15=c16=c17=c18=white
    c19=c20=c21=c22=c23=c24=c25=c26=c27=green
    c28=c29=c30=c31=c32=c33=c34=c35=c36=red
    c37=c38=c39=c40=c41=c42=c43=c44=c45=orange
    c46=c47=c48=c49=c50=c51=c52=c53=c54=yellow
    scr=scr_mov=om=ov=tms=tm=m=0
    timer,scramble,solved=False,False,True
    move=rotate=""
    rect(0,0,320,18+t,bg),cube()

#### TIMER #####
  m=monotonic()
  if c1==c2==c3==c4==c5==c6==c7==c8==c9 and c10==c11==c12==c13==c14==c15==c16==c17==c18 and c19==c20==c21==c22==c23==c24==c25==c26==c27 and c28==c29==c30==c31==c32==c33==c34==c35==c36 and c37==c38==c39==c40==c41==c42==c43==c44==c45 and c46==c47==c48==c49==c50==c51==c52==c53==c54:solved=True
  else:solved=False
  
  while key(4) and solved==False and timer==False:
    if monotonic()>=m and monotonic()<m+0.4:rect(0,0,t,t,red)
    if monotonic()>=m+0.4:
      rect(0,0,t,t,green),release(4)
      timer,tms=True,monotonic()
  if timer==True:
    rect(0,0,t,t,blue)
    xtext=259
    if monotonic()-tms<10:xtext=269
    draw(str(monotonic()-tms),xtext,1,blue,bg)
    tm=monotonic()-tms
    if solved==True:
      timer=False
      rect(0,0,t,t,green),draw(str(tm),xtext,1,green,bg),wait(4),rect(0,0,320,t+17,bg),cube()
  if keyS(51):
    theme=passlimits(theme+1,0,len(thm)-1)
    bg=thm[theme]
    background(bg),cube()
  if key(52):exit
