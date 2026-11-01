#converts gint.image objects into 2darrays and vice versa

from gint import image
from math import ceil


def img(yxgrid,prof=0,ceil=ceil,image=image):
  def ss(s,i,v):
    out=list(s)
    out[i]=str(v)
    out="".join(out)
    return out
  gh=len(yxgrid)
  gw=len(yxgrid[0])
  dh=gh
  dw=4*ceil(gw/32)
  #edr=""
  #for i in range(dw):
  #  edr.append("00000000")
  data=[]
  for y in range(dh):
    xx=0
    for bx in range(dw):
      byt="00000000"
      for x in range(0,8):
        try:
          byt=ss(byt,x,yxgrid[y][xx])
        except:
          byt=ss(byt,x,"0")
        xx+=1
      data.append(int(byt,2))
  return image(prof,gw,gh,bytearray(data))

def grid(img,ceil=ceil):
  def sbin(num):
    sb=str(bin(num))[2:]
    while len(sb)<8:
      sb="0"+sb
    return sb
  w=img.width
  h=img.height
  data=img.data
  rdlen=len(img.data)
  mdlen=4*ceil(w/32)*h
  rdlen==mdlen
  dlen=mdlen
  bw=dlen//h
  data2d=[]
  for y in range(h):
    #print("y",y,h)
    row=[]
    for x in range(w):
      #print("x",x,w)
      #print("i",(y*bw)+x)
      row.append(data[(y*bw)+x])
      #print((h*bw)+w,data[(y*bw)+x])
    data2d.append(row)
  grid=[]
  for y in range(len(data2d)):
    row=""
    #print(data2d)
    for b in data2d[y]:
      row+=sbin(b)
    grid.append(list(row[:img.width]))
  return grid

__dir__=["img","grid","i","__dir__"]
for i in list(globals().keys()):
  if not (i in __dir__):
    del globals()[i]

