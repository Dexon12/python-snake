import arcade
from random import *
from math import *
offsets = {"up":(0,20),"down":(0,-20),"left":(-20,0),"right":(20,0)}
class Window(arcade.Window):
    def __init__(self):
        super().__init__(800,800,"snake")
        self.snake = [[400,400],[420,400]]
        self.snake_dir = "up"
        self.speed = 0.1
        self.set_update_rate(self.speed)
        self.food_pos = self.random_position()
        self.stop = False
        self.score = 0
    def random_position(self):
        x = randint(50,750)
        y = randint(50,750)
        return(x,y)
    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.WHITE)
        for snake in self.snake:
            arcade.draw_rectangle_filled(snake[0],snake[1],20,20,arcade.color.BLACK)
        arcade.draw_circle_filled(self.food_pos[0],self.food_pos[1],10,arcade.color.RED)
        arcade.draw_text(f"Счет: {self.score}",50,750,arcade.color.BLACK,20)
    def find_distance(self,pos_1,pos_2):
        x1,y1 = pos_1
        x2,y2 = pos_2
        distance = sqrt((x2-x1)**2 + (y2 - y1)**2)
        return(distance)

    def collision(self):
        if self.find_distance(self.snake[-1],self.food_pos) < 20:
            self.food_pos = self.random_position()
            self.speed -= 0.005
            self.set_update_rate(self.speed)
            self.score += 1
            return True
        return False
    def on_key_press(self,key,modifiers):
        if key == arcade.key.W and self.snake_dir != "down":
            self.snake_dir = "up"
        if key == arcade.key.S and self.snake_dir != "up":
            self.snake_dir = "down"
        if key == arcade.key.D and self.snake_dir != "left":
            self.snake_dir = "right"
        if key == arcade.key.A and self.snake_dir != "right":
            self.snake_dir = "left"
    def update(self,delta_time):
        
        if self.stop == False:
            
            head = [0,0]
            head[0] = self.snake[-1][0] + offsets[self.snake_dir][0]
            head[1] = self.snake[-1][1] + offsets[self.snake_dir][1]
            if head in self.snake:
                self.stop = True
            self.snake.append(head)
            
            if self.collision() == False:
                self.snake.pop(0)
                
            if self.snake[-1][0] >= 800:
                self.snake[-1][0] = 0
            elif self.snake[-1][0] <= 0:
                self.snake[-1][0] = 800
            elif self.snake[-1][1] >= 800:
                self.snake[-1][1] = 0
            elif self.snake[-1][1] <= 0:
                self.snake[-1][1] = 800
      
        

window = Window()
arcade.run()


    
