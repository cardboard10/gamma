#defines simple aabb collison formula for gamma

def aabb(pa,sa,pb,sb,key=""):
  if pb[1]+sb[1]>pa[1]\
   and pa[1]+sa[1]>pb[1]\
   and pa[0]+sa[0]>pb[0]\
   and pb[0]+sb[0]>pa[0]:
     return True
  else:
    return False
