#Створи власний Шутер!
#galaxy.jpg
from pygame import*
from random import randint, choice
from time import time as timer
#self
win_h = 700
win_w = 800
win = display.set_mode((win_w, win_h))
display.set_caption("OverRun")
fps = 60
clock = time.Clock()



velocity = 0
roady = 0
roadx = 0
    
    
    
    
class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, w, h, speed):
        super().__init__()
        self.image = transform.scale(image.load(img), (w,h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
     
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 3:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_h - 90:
            self.rect.y += self.speed
        if keys[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if keys[K_d] and self.rect.x < win_w - 70:
            self.rect.x += self.speed
        
            
        


bg = transform.scale(image.load("road.jpg"), (win_w, win_h))


lost = 0
class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y +=self.speed
        if self.rect.y > win_h:
            self.rect.x = choice([win_w-380, win_w-260, 190, 300])
            self.rect.y = -60
    
    def set_speed(self, speed):
        self.speed = speed
        
            
            
        
        

            
#TODO images
player_img = "player_c.png"
Car_img = "Car.png"
truck_img = "truck.png"
minitruck_img = "Mini_truck.png"
taxi_img = "taxi.png"
bullet_img = "bullet.png"
asteroid_img = "asteroid.png"




#TODO music
mixer.init()
mixer.music.load('music.mp3')
mixer.music.play()
volume_value = 0.1
mixer.music.set_volume(volume_value)


mixer.music.set_volume(volume_value)




#TODO fonts 
font.init()
text_1 = font.SysFont("Arial", 30)
text_2 = font.SysFont("Arial", 72 )
text_win = text_2.render("YOU WIN!", 1,(0,255,0))
text_lose = text_2.render("You Crashed!", 1, (150,0,0))



#TODO sprites
player = Player(player_img, 415, win_h-200, 75, 140, 10)






keys = key.get_pressed()

#TODO groups
max_enemy = 4
max_enemy2 = 4
rights = sprite.Group()
for i in range(1,max_enemy):
    right = Enemy(choice([Car_img,truck_img, minitruck_img, taxi_img]), choice([win_w-380, win_w-275]), -50, 75, 140, randint(5,10))
    rights.add(right)
    




lefts = sprite.Group()
for i in range(1,max_enemy2):
    left = Enemy(choice([Car_img,truck_img, minitruck_img, taxi_img]), choice([190, 300]), -400, 75, 150, randint(7,12))
    lefts.add(left)




restart = False
player_speed = player.speed
distance = 0
goal = 5000
clock = time.Clock()
FPS = 60
game = True
finish = False
velocity = 12




while game:
    win.blit(bg, (roadx, roady))
    win.blit(bg, (roadx, roady - 700))
    if roady >= 700:
        roady = 0
    roady = roady + velocity
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_e:
                restart = True
                
            if e.key == K_i:
                goal = 999999
                
                
                
            if e.key == K_w:
                player_speed = player.speed *2
                
                velocity = 19
                for right in rights:
                    right.set_speed(randint(10,20))
                for left in lefts:
                    left.set_speed(randint(12,21))
                    
        elif e.type == KEYDOWN:
            if e.key == K_s:
                player_speed = player.speed /2
                velocity = 0
                for right in rights:
                    right.set_speed(randint(1,4))
                for left in lefts:
                    left.set_speed(randint(3,6))
                    
        elif e.type == KEYUP:
            if e.key == K_w or e.key == K_s:
                player_speed = player.speed
                velocity = 12
                for right in rights:
                    right.set_speed(randint(5,10))
                for left in lefts:
                    left.set_speed(randint(7,12))
                    
    
                
                
                
                
            
                
            
    if not finish and not restart:
        rights.update()
        rights.draw(win)
        lefts.update()
        lefts.draw(win)
        
        
        
        
        
    
        
 
        
            
        player.update()
        player.reset()     
        rights.draw(win)
        lefts.draw(win)
        
        
        
        text_tip2 = text_1.render(f"Tip: avoid other cars", 1,(255,255,255), (80,80,80))
        text_tip1 = text_1.render(f"Tip: don't drive of the road", 1,(255,255,255), (80,80,80))
        text_c = text_1.render(f"Press 'E' to restart", 1,(255,255,255), (80,80,80))
        text_i = text_1.render(f"Press 'I' fot endless mode", 1,(255,255,255), (150,150,150))
        text_goal = text_1.render(f"Goal: "+str(goal/1000), 1,(255,255,255), (150,150,150))
        text_dis = text_1.render(f"Current distance: "+str(distance /1000) +" km" , 1,(255,255,255), (150,150,150))
        win.blit(text_goal, (10,20))
        win.blit(text_dis, (10,50))
        win.blit(text_i, (10,650))
        
        
        
        if player.rect.x >= 615:
            distance = 0
            distance = distance
            win.blit(text_i, (10,650))
            win.blit(text_lose, (215,215))
            win.blit(text_c, (300,340))
            win.blit(text_tip1, (255,300))
            display.update()
            finish = True

            
            
            
        if player.rect.x <= 100:
            distance = 0
            distance = distance
            win.blit(text_i, (10,650))
            win.blit(text_lose, (215,215))
            win.blit(text_c, (300,340))
            win.blit(text_tip1, (255,300))
            display.update()
            finish = True

            
        
            
        if (sprite.spritecollide(player, rights, True)
            or sprite.spritecollide(player, lefts, True)):
                
                distance = 0
                distance = distance
                win.blit(text_i, (10,650))
                win.blit(text_lose, (215,215))
                win.blit(text_c, (300,340))
                win.blit(text_tip2, (290,300))
                display.update()
                finish = True
                
                
                
            
            
           
            
        
            
        
        
            
        if distance > goal:
            finish = True
            goal += 5000
            win.blit(text_win, (250,200))
            win.blit(text_c, (290,290))
            
        distance += player_speed    
        display.update()
        time.delay(50)
    else:
        distance = 0
        player.rect.x = 415
        player.rect.y = win_h-200
        if restart:
            
            
        
            for right in rights:
                right.kill()
            for left in lefts:
                left.kill()
            
            for i in range(1,max_enemy):
                right = Enemy(choice([Car_img,truck_img, minitruck_img, taxi_img]), choice([win_w-380, win_w-275]), -50, 75, 140, randint(5,10))
                rights.add(right)
            for i in range(1,3):
                left = Enemy(choice([Car_img,truck_img, minitruck_img, taxi_img]), choice([190, 300]), -400, 75, 150, randint(7,12))
            rights.add(right)
            finish = False
            restart = False
            
    
    