# casio gint game engine named gamma
import gint
from phy3 import aabb
from time import time
from gridphy import grid as Grid

globals()["prevF"]=time()


class obj:
  def __init__(self,pos,size,Vec=(0,0),img=None):
    self.size=size
    self.pos=pos
    self.vec=Vec
    if img!=None:
      self.img=None
  colls=[]
  def vadd(self,v):
    self.vec=(self.vec[0]+v[0],self.vec[1]+v[1])
  def padd(self,v):
    self.pos=(self.pos[0]+v[0],self.pos[1]+v[1])
  def vset(self,v):
    self.vec=v
  def pset(self,p):
    self.pos=p
  def draw(self,offset=(0,0),rect=True):
    x=int(round(self.pos[0]+offset[0]))
    y=int(round(self.pos[1]+offset[1]))
    if rect:
      gint.drect(x,y,x+self.size[0],y+self.size[1],3)
    else:
      print(self.img)
      gint.dimage(x,y,self.img)

class World:
  gx=0
  gy=0
  mobs=[]
  def __init__(self,objs={},gx=0,gy=0,grid=Grid([[]])):
    self.grid=grid
    self.objs=objs
    self.gx=gx
    self.gy=gy
    #if collide!=None:
    #  self.collide=collide
  objs={}
  def draw(self,offset=(0,0),rect=True,debug=False):
    gint.dclear(0)
    self.grid.draw(offset[0],offset[1])
    for o in list(self.objs.values()):
      try:
        o.draw(offset,rect=rect)
      except:
        o.draw(offset,rect=True)
    globals()["now"]=time()
    globals()["fps"]=globals()["now"]-globals()["prevF"]
    globals()["prevF"]=globals()["now"]
    if debug:
      try:fpss=(1/globals()["fps"])
      except:fpss=0
      gint.dtext(0,0,5,"fps:"+str(round(fpss,2)))
      gint.dtext(0,10,5,"objs:"+str(len(self.objs)))
      gint.dtext(0,20,5,"mobs:"+str(len(self.mobs)))
    gint.dupdate()
  def add(self,key,obj,static=True):
    self.objs[key]=obj
    if not static:
      self.mobs.append(key)
    return self.objs[key]
  def kill(self,key):
    del self.objs[key]
    try:
      del self.mobs[key]
    except:
      pass
  def step(self,keys=None,get_all_colls=True):
    aobjs=list(self.objs.keys())
    if keys==None:
      keys=self.mobs
    for key in keys:
      if True:
        colls=[]
        cobj=self.objs[key]
        if len(cobj.colls)==0:
          cobj.vadd((self.gx,self.gy))
        oldpos=cobj.pos
        cobj.pos=(cobj.pos[0]+cobj.vec[0],cobj.pos[1]+cobj.vec[1])
        if 1 in self.grid.colltid(cobj.pos,cobj.size):
          #print("colliding with grid")
          colls.append(self.grid)
          cobj.pos=oldpos
          cobj.vec=(cobj.vec[0]//3,cobj.vec[1]//3)
        for tkey in aobjs:
          if tkey!=key:
            tobj=self.objs[tkey]
            if aabb(cobj.pos,cobj.size,tobj.pos,tobj.size,key):
              colls.append(tkey)
              cobj.pos=oldpos
              tobj.vec=cobj.vec
              cobj.vec=(0,0)
        #self.collide(key,colls)
        cobj.colls=colls
  def collide(self,key,okeys):
    pass
  def set_vec(self,key,Vec):
    self.objs[key].vec=(Vec[0],Vec[1])
  def add_vec(self,key,Vec):
    cov=self.objs[key].vec
    self.objs[key].vec=(cov[0]+Vec[0],cov[1]+Vec[1])
  def def_group(self,key,*keys):
    group=[]
    for k in keys:
      group.append(self.objs[k])
    self.objs[key]=group
  def add_group(self,key,*objs):
    group=[]
    for o in objs:
      group.append(o)
    self.objs[key]=group



#tst()
