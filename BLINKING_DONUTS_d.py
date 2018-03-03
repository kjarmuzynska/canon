''' board for game '''

import sys
import os
#sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from primitives import Circle, Line, Polygon, Pixel, Base
import cocos
import numpy as np
import math
import time
import random 
from cocos.actions import *
from donuts_mechanics import Donut_M
import pygame
from cocos.audio.pygame.mixer import Sound
from cocos.audio.pygame import mixer
#from cocos.actions.base_actions.IntervalAction import *
#from window_designer import My_Window

class TBoard(cocos.layer.Layer):
    is_event_handler = True

    def __init__(self):
        
        super( TBoard, self ).__init__()
        self.schedule( self.step )
        self.DM = Donut_M()
        self.sprites_list = dict()
        self.points = 0
        self.draw_initiation()
        self.good_song = Sound("sounds/good.wav")
        self.bad_song = Sound("sounds/bad.wav")
        
        
    
    def draw_initiation(self):
        for donut_coordinates in self.DM.full_grid_list:
            self.draw_donut(donut_coordinates)
            
            
    def draw_donut(self, donut_coordinates):
        #random picture
        picture_number = random.randint(1, 6)  
        center_x, center_y = donut_coordinates
        path = 'images/p%s.png' % (picture_number)
        sprite = cocos.sprite.Sprite(path) 
        sprite.scale = 0.05*4 #10 pikseli * cos
        sprite.position = center_x, center_y
        self.add(sprite, z = 1 )
        my_name = 'p%s' % (picture_number)
        print(my_name, 'position at', center_x, center_y) 
        dict_key = 'a(%s,%s)' %(center_x, center_y)
        self.sprites_list[dict_key] = sprite
        
        
    
    def step(self,dt):
        pass


    def onClicked(self):

        hitted = self.DM.check_click(self.posx, self.posy)
        #print('hitted', hitted)
        if hitted:
            print('trafiono')
            self.good_song.play()
            center_x, center_y = hitted[1]
            dict_key = 'a(%s,%s)' %(center_x, center_y)
            print('gdzie', dict_key)
            to_kill = self.sprites_list[dict_key]
            print('kill', to_kill)
            self.remove(self.sprites_list[dict_key])
            self.draw_donut(hitted[0])
        else:
            print('pudlo')
            self.bad_song.play()
                
    def on_mouse_press (self, x, y, buttons, modifiers):
        try:
            self.posx, self.posy = cocos.director.director.get_virtual_coordinates (x, y)

            self.onClicked()

        except Exception as e:
            print(e)        
        
        
class Board_Runner:
    def run(self):
        cocos.director.director.init(width=1300, height=700)
        mixer.init()
        
    	# We create a new layer, an instance of HelloWorld
    
        hello_layer = TBoard()
        #menu_layer = My_Menu()
    
    	# A scene that contains the layer hello_layer
        main_scene = cocos.scene.Scene(hello_layer)#, menu_layer)
    
    	# And now, start the application, starting with main_scene
        cocos.director.director.run(main_scene)
        
    
    	# or you could have written, without so many comments:
    #	  director.run( cocos.scene.Scene( HelloWorld() ) )

        
if __name__ == "__main__":
    Board_Runner().run()
	# director init takes the same arguments as pyglet.window
    