#provides the grid(2dlist level loading) support for gamma

import gint
from math import floor,ceil
class tile:
  x=int
  y=int
  pos=(int,int)
  val=int
  def __init__(self,x,y,val):
    self.x=x
    self.y=y
    self.pos=(x,y)
    self.val=val
class grid:
  grid=[[]]
  tilesize=8
  def __init__(self,grid,tilesize=8):
    self.grid=grid
    self.tilesize=tilesize
  def draw(self,ox,oy):
    for y,row in zip(range(len(self.grid)),self.grid):
      for x,tile in zip(range(len(row)),row):
        if tile!=0:
          gint.drect(floor(ox+x*self.tilesize),round(oy+y*self.tilesize),round(ox+(x+1)*self.tilesize),
            floor(oy+(y+1)*self.tilesize),3)
  def collide(self,pos,size):
    tpos=(pos[0]/self.tilesize,pos[1]/self.tilesize)
    tsiz=(size[0]/self.tilesize,size[1]/self.tilesize)
    tposa=(floor(tpos[0]),floor(tpos[1]))
    tposb=(ceil(tpos[0]+tsiz[0]),ceil(tpos[1]+tsiz[1]))
    out=[]
    for x in range(tposa[0],tposb[0]):
      for y in range(tposa[1],tposb[1]):
        try:out.append(tile(x=x,y=y,val=self.grid[y][x]))
        except IndexError:out.append(tile(x=-1,y=-1,val=1))
    return out
  def colltid(self,pos,size):
    tpos=(pos[0]/self.tilesize,pos[1]/self.tilesize)
    tsiz=(size[0]/self.tilesize,size[1]/self.tilesize)
    tposa=(floor(tpos[0]),floor(tpos[1]))
    tposb=(ceil(tpos[0]+tsiz[0]),ceil(tpos[1]+tsiz[1]))
    out=[]
    for x in range(tposa[0],tposb[0]):
      for y in range(tposa[1],tposb[1]):
        try:out.append(self.grid[y][x])
        except IndexError:out.append(1)
    return out
  def collpos(self,pos,size):
    tpos=(pos[0]/self.tilesize,pos[1]/self.tilesize)
    tsiz=(size[0]/self.tilesize,size[1]/self.tilesize)
    tposa=(floor(tpos[0]),floor(tpos[1]))
    tposb=(ceil(tpos[0]+tsiz[0]),ceil(tpos[1]+tsiz[1]))
    out=[]
    for x in range(tposa[0],tposb[0]):
      for y in range(tposa[1],tposb[1]):
        try:out.append((x,y))
        except IndexError:out.append((-1,-1))
    return out




