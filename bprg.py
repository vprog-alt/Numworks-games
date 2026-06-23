from math import *
from random import *
from random import randint as rand
from kandinsky import *
from kandinsky import fill_rect as rect, draw_string as draw, set_pixel as pix, get_pixel as get, set_pixel as set
from ion import *
from ion import keydown as key
from time import *
#from turtle import *
#from newfont import *

#FILL
def background(bg):rect(0,0,320,222,bg)
def carre(x,y,t,c):rect(x,y,t,t,c)
def circle_0(cx,cy,r,color):
  for angle in range(360):
    rad=angle*pi/180
    x,y=int(cx+r*cos(rad)+0.5),int(cy+r*sin(rad)+0.5)
    set(x,y,color)
def circle(cx,cy,r,color):
  for y in range(-r,r+1):
    dx=int((r*r-y*y)**0.5)
    rect(cx-dx,cy+y,2*dx,1,color)
def line(x1,y1,x2,y2,c):
  v_x,v_y=(x2-x1)/320,(y2-y1)/320
  for _ in range(320):
    set_pixel(floor(x1),floor(y1),c)
    x1,y1=x1+v_x,y1+v_y
def fade(step,segments,*colors):
  n=len(colors)-1
  if n==0:return colors[0]
  i=min(int((step/segments)*n),n-1)
  return tuple(int(a+(b-a)*(((step/segments)*n)-i)) for a,b in zip(colors[i],colors[i+1]))
def timefade(*colors):
  step,segments=abs(sin(monotonic())),1
  n=len(colors)-1
  if n==0:return colors[0]
  i=min(int((step/segments)*n),n-1)
  return tuple(int(a+(b-a)*(((step/segments)*n)-i)) for a,b in zip(colors[i],colors[i+1]))

#KEYDOWN
pressed_state={}
def release(k):
  while keydown(k):pass
def wait(k):
  while not keydown(k):""
def stopall(k):release(k),wait(k),release(k)
def keyS(k):
  if k not in pressed_state:pressed_state[k]=False
  if not keydown(k):
    pressed_state[k]=False
    return False
  if not pressed_state[k]:
    pressed_state[k]=True
    return True
  return False

#MODULO
def limits(nb,mi,ma):return min(max(nb,mi),ma)
def passlimits(nb,mi,ma):
  if nb<mi:nb=ma-(mi-nb)+1
  elif nb>ma:nb=mi-(ma-nb)-1
  return limits(nb,mi,ma)

#CONVERT
def C_H(RVB,HEX=""):
  for h in RVB:
    new=hex(h)[2:]
    HEX+=str(("0" if len(new)==1 else "")+new)
  return HEX
def H_C(HEX):return (int("0x"+HEX[:2]),int("0x"+HEX[2:][:2]),int("0x"+HEX[4:][:2]))


#LIST
def same(lst):return [row[:] for row in lst]

release(4)
