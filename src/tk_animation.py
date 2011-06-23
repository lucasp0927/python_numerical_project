## 3-Button 

from Tkinter import Tk, Canvas, Frame, Button, Label, Scale  ###, TclError
from Tkconstants import *

class Rectangle:
    """Movable Rectangle on a Tkinter Canvas"""
    def __init__(self,cv,pos,length,height,colour):
        """creates disc on given Canvas cv at given pos-ition"""
        x0, y0 = pos
        x1, x2 = x0-length/2.0, x0+length/2.0
        y1, y2 = y0-height, y0
        self.cv = cv
        self.item = cv.create_rectangle(x1,y1,x2,y2,
                                        fill = "#%02x%02x%02x" % colour)   
    def move_to(self, new_pos, speed):
        """moves bottom center of disc to position (x,y).
           speed is intended to assume values from 1 to 10"""
        x1,y1,x2,y2 = self.cv.coords(self.item)
        x0, y0 = (x1 + x2)/2, y2
        x,y=new_pos
        dx, dy = x-x0, y-y0
        d = (dx**2+dy**2)**0.5
        steps = int(d/(10*speed-5)) + 1
        dx, dy = dx/steps, dy/steps
        for i in range(steps):
            self.cv.move(self.item,dx,dy)
            self.cv.update()
            self.cv.after(20)


class Ball:
    """Movable circle on a Tkinter Canvas"""
    def __init__(self,cv,pos,radius,colour):
        """creates disc on given Canvas cv at given pos-ition"""
        x0, y0 = pos
        x1, x2 = x0-radius, x0+radius
        y1, y2 = y0-radius, y0+radius
        self.cv = cv
        self.item = cv.create_oval(x1,y1,x2,y2,
                                        fill = "#%02x%02x%02x" % colour)   
    def move_to(self, new_pos, speed):
        """moves bottom center of disc to position (x,y).
           speed is intended to assume values from 1 to 10"""
        x1,y1,x2,y2 = self.cv.coords(self.item)
        x0, y0 = (x1 + x2)/2, y2
        x,y=new_pos
        dx, dy = x-x0, y-y0
        d = (dx**2+dy**2)**0.5
        steps = int(d/(10*speed-5)) + 1
        dx, dy = dx/steps, dy/steps
        for i in range(steps):
            self.cv.move(self.item,dx,dy)
            self.cv.update()
            self.cv.after(20)

class Projectile:
    """Projectile object """
    def __init__(self,x,y=0.0):
        """ creates a projectile, (x,y) is the initial position"""
        self.x=x
        self.y=y
    def pos(self):
        return int(10+160*self.x),int(400+160*self.y)

class Bullet:
    """Bullet"""
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def pos(self):
        return int(10+160*self.x),int(400+160*self.y)
    
class DrawEngine:
    """Plays the Hanoi-game on a given canvas."""
    def __init__(self, canvas, speed,  exactsol, sol, display_bullet_coor,display_proj_coor,display_time,display_error):
        self.cv = canvas
        self.t0,self.l, self.c, self.x_int= sol
        self.texact,self.xexact=exactsol
        self.speed = speed
        self.dispbulletcoor=display_bullet_coor
        self.dispprojcoor=display_proj_coor
        self.disptime=display_time
        self.disperror=display_error
        # y=0 is set at y_canvas=400, x=0 is set at x_canvas=10
        self.x0_canvas=10
        self.y0_canvas=210
        self.projectile=Projectile(self.xexact[0],0.)
        self.bullet = Bullet(self.x_int,-self.l)
        
        self.bullet_color=(255,0,255)
        self.proj_color=(0,255,255)
        self.s_bullet=Rectangle(self.cv,self.bullet.pos(),10,10,self.bullet_color)
        self.s_proj=Ball(self.cv,self.projectile.pos(),5,self.proj_color)
   
        self.draw_objects()
    def draw_objects(self):
        """moves uppermost disc of source tower to top of destination tower."""
        for i in range(0,len(self.texact),int((len(self.texact)-1)/100.)):
            t=self.texact[i]
            t_shift=t-self.t0
            self.disptime(t) 
            self.projectile.x=self.xexact[i]
            self.projectile.y=0.0
            self.s_proj.move_to(self.projectile.pos(),self.speed)
            proj_coor=(self.projectile.x,self.projectile.y)
            self.bullet.x=self.x_int
            if t_shift>0 :
                self.bullet.y=-self.l+self.c*t_shift
                bullet_coor=(self.bullet.x,-self.bullet.y)
                self.dispbulletcoor(bullet_coor)
                self.s_bullet.move_to(self.bullet.pos(),self.speed)
            self.dispprojcoor(proj_coor)
        self.bullet.y=-self.l+self.c*(self.texact[-1]-self.t0)
        bullet_coor=(self.bullet.x,-self.bullet.y)
        self.dispbulletcoor(bullet_coor)
        self.s_bullet.move_to(self.bullet.pos(),self.speed)
        self.projectile.x=self.xexact[-1]
        self.projectile.y=0.0
        self.s_proj.move_to(self.projectile.pos(),self.speed)
        proj_coor=(self.projectile.x,self.projectile.y)
        self.dispprojcoor(proj_coor)
        self.disptime(self.texact[-1])
        error=abs(self.xexact[-1]-self.x_int)/self.x_int
        #print error
        self.disperror(error) 
class Draw:

    def display_bullet_coor(self, bullet_coor):
        """method to be passed to the Draw-Engine to  display bullet cooridnates"""
        self.bullet_coor_Lbl.configure(text = " bullet position:\n (%6.4f,%6.4f)" % bullet_coor)
    def display_proj_coor(self, proj_coor):
        self.proj_coor_Lbl.configure(text = " projectile position:\n (%6.4f,%6.4f)" % proj_coor)
    def display_time(self, r_time):
        self.time_Lbl.configure(text = " Time:\n %6.4f" % r_time)
        
    def display_error(self, error):
        self.error_Lbl.configure(text = "Error:\n {0:6.4%}".format(error))
        
    def __init__(self, exactsol, sol, speed=5):
        root = Tk()                            
        root.title("Object Interception")          
        root.wm_attributes("-topmost", 1)
        cv = Canvas(root,width=600,height=460) 
        cv.pack()
        tmp1,l,tmp2,x_int=sol
        fnt = ("Arial", 12, "bold")
        tmp1,xexact=exactsol

        attrFrame = Frame(root)
        self.bullet_coor_Lbl= Label( attrFrame, width = 20, padx=20, text = " bullet position:\n (%8.4f,%8.4f)" % (x_int,-l), anchor=CENTER,font = fnt, height = 2)
        self.proj_coor_Lbl=Label(attrFrame, width = 20, padx=20, text = " projectile position:\n (%8.4f,%8.4f)" %(0.0,0.0), anchor=CENTER, font = fnt, height = 2 )
        self.time_Lbl=Label(attrFrame, width = 20, padx=20, text = " Time:\n %6.4f" %(0.0), anchor=CENTER, font = fnt, height = 2 )
        self.error_Lbl=Label(attrFrame, width=20, padx=20, text= "Error:\n{0:6.2%}".format(0.0) ,font=fnt, anchor=CENTER,height=2)
        for widget in (self.bullet_coor_Lbl, self.proj_coor_Lbl,self.time_Lbl,self.error_Lbl):
            widget.pack(side=LEFT)
        attrFrame.pack(side=TOP)

        ctrlFrame = Frame(root) # contains Buttons to control the game 
        self.quitBtn = Button( ctrlFrame, width=11, text="OK", font=fnt,
                                state = NORMAL, padx=15, command = ctrlFrame.quit )
        self.quitBtn.pack(side=LEFT)

        ctrlFrame.pack(side=TOP)

       
        # setup of the scene
        x_axis= cv.create_line(  0,  400,  880, 400, fill='black')
        
        

        self.dEngine = DrawEngine(cv,speed, exactsol, sol,self.display_bullet_coor,self.display_proj_coor, self.display_time,self.display_error)
        
        root.mainloop()
        root.destroy()        
        
        

if __name__  == "__main__":
    pass
