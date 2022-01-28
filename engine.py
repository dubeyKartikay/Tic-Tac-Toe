import pygame
from itertools import combinations
class rects:
    def __init__(self,posn,scale,imgo,imgx,imgwx,imgwo):
        self.posn=posn
        self.scale=scale
        self.state=""
        self.imgo=imgo
        self.imgx=imgx
        self.imgwx=imgwx
        self.imgwo=imgwo
    def update(self,list_rects,posn_of_click,chance):
        state=self.collidepoint(posn_of_click)
        if state:
            if self.state=="":
                if chance%2==0:
                    self.state="o"
                else:
                    self.state="x"
        x,i=self.check_if_won("x",list_rects)
        y,j=self.check_if_won("o",list_rects)
        if x==True:
            a,b,c=i
            a.state="w"+a.state
            b.state="w"+b.state
            c.state="w"+c.state
            return True,"X"
        if y==True:
            a,b,c=j
            a.state="w"+a.state
            b.state="w"+b.state
            c.state="w"+c.state
            return True,"O"
        return False , ""
##        print(self.state)
    def check_if_won(self,player,list_rects):
        players=[]
        for i in list_rects:
            if i.state==player:
                players.append(i)
        comb=combinations(players,3)
        comb=list(comb)
        for i in comb:
            result=self.in_same_line(i)
            if result:
                return True,i
        return False,None
            
    def collidepoint(self,point):
        x,y=point
        x1,y1=self.posn
        w,h=self.scale
        if x1<x<(x1+w) and y1<y<y1+h:
            return True
        else:
            return False
    def in_same_line(self,comb):
        a,b,c=comb
        x,y=a.posn
        x1,y1=b.posn
        x2,y2=c.posn
##        if x==x1==x2:
##            return True
##        if x==x1:
##            return False
##        if x2==x1:
##            return False
        if (y-y1)*(x2-x1)==(y2-y1)*(x-x1):
            return True
        return False
        
    def draw(self,target_surface):
        x,y=self.posn
        posn=(x+35,y+35)
        if self.state=="o":
            target_surface.blit(self.imgo,posn)
        elif self.state=="x":
            target_surface.blit(self.imgx,posn)
        elif self.state=="wo":
            target_surface.blit(self.imgwo,posn)
        elif self.state=="wx":
            target_surface.blit(self.imgwx,posn)



























    
