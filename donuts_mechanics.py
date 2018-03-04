# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 18:51:52 2018

@author: KORA
"""
import random

class Donut_M:
    def __init__(self):
        self.egg_d = 200*0.05*4
        self.egg_r = self.egg_d/2
        self.donuts_grid()
        self.donuts_number = 10
        self.initial_position()
        self.to_draw = []
        
    def donuts_grid(self):
        
        self.empty_grid_list = []
        self.full_grid_list = []
        
        for x in range(1, int(1300/self.egg_d)-2):
            for y in range(1, int(700/self.egg_d)-2):
                posx_center = x*self.egg_d + self.egg_d
                posy_center = y*self.egg_d + self.egg_d
                my_tuple = (posx_center, posy_center)
                self.empty_grid_list += [my_tuple]            
      
        
    def initial_position(self):
        for i in range(self.donuts_number):
            self.put_donut()
            
            
    def put_donut(self):
        point = random.choice(self.empty_grid_list)
        #self.empty_grid_list.remove(point)
        self.full_grid_list += [point]
        return point
  
    
    def change_donut_pos(self, donut_coordinates):
        self.empty_grid_list += [donut_coordinates]
        #self.full_grid_list.remove(donut_coordinates)
        point = self.put_donut()
        return point
    
    
    def check_click(self, click_x, click_y, running_sprites):
#        for donut_coordinates in self.full_grid_list:
#            if self.check_hit(click_x, click_y, donut_coordinates):
#                new_point = self.change_donut_pos(donut_coordinates)
#                where_it_was = donut_coordinates
#                return [new_point, where_it_was]
#        return 0
        for spriteobj in running_sprites:
            x, y = spriteobj.position
            donut_coordinates = (x, y)
            if self.check_hit(click_x, click_y, donut_coordinates):
                new_point = self.change_donut_pos(donut_coordinates)
                #where_it_was = donut_coordinates
                return [new_point, spriteobj]
        return 0
                
     
        
    def check_hit(self, click_x, click_y, donut_coordinates):
        donut_x, donut_y = donut_coordinates
        #print(donut_coordinates)
        #print((donut_x - click_x)**2 + (donut_y - click_y)**2, self.egg_r**2)
        if ( donut_x - click_x+20)**2 + (donut_y - click_y)**2 <= (self.egg_r+20)**2:
            
            return True
        else:
            return False

        
        
        
        
        
if __name__ == "__main__":
    f = Donut_M()
    #print(f.full_grid_list)