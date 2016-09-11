import pygame, sys, time 
from pygame.locals import *
from pygame.sprite import *




#Ορισμός κάποιων χρωμάτων.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
DARKGREEN =(0, 51, 0)
BLUE = (0, 0, 255)
YELLOW=(255,255,0)
MAROON=(128, 0, 0)
SILVER=(192, 192, 192)
TEAL=(0, 128, 128)
RED =(255, 26, 26)



# Αναπαριστά ένα match. 
class Game():
    scoreFirst = 0
    scoreSecond = 0
    def __init__(self):
        Game.scoreFirst = 0 # Το σκορ του πρώτου παίχτη.
        Game.scoreSecond = 0 # Το σκορ του δεύτερου παίχτη.
    def printScore(self, surf,point,HORIZ=1000):  # Ανανεώνει το σκορ ανάλογα με το όρισμα point που έχει πάρει και εκτυπώνει το σκορ των παικτών στην οθόνη.
        if point == 1:
            Game.scoreFirst += 1
        elif point == 2:
            Game.scoreSecond += 1
        my_font = pygame.font.SysFont(None, 80)
        my_second_font = pygame.font.SysFont(None, 20)
        my_first_player = my_second_font.render('Player A', True, (0,0,0), (155,255,255))
        surf.blit(my_first_player , (HORIZ/2-200, 5))
        my_first_score = my_font.render (str(Game.scoreFirst), True, (0,0,0), (155,255,255))  
        surf.blit(my_first_score, (HORIZ/2-200, 20))
        my_second_player = my_second_font.render('Player B', True, (0,0,0), (155,255,255))
        surf.blit(my_second_player, (HORIZ/2+150, 5))
        my_second_score = my_font.render (str(Game.scoreSecond), True, (0,0,0), (155,255,255))  
        surf.blit(my_second_score, (HORIZ/2+150, 20))
        



# Η υποκλάση Ball μπάλα αναπαριστά μία μπάλα.
class Ball(Sprite):
    def __init__(self, createX, createY,speedX, speedY,\
                 dimX=32, dimY=32):
        Sprite.__init__(self)   
        self.rect=pygame.Rect(createX, createY, dimX, dimY)     # ορθογώνιο rect της κλάσης Ball  
        self.image=pygame.image.load('myred-ball.png')          # εικόνα image της κλάσης Ball
        
        self.speedX = speedX # Η ταχύτητα που θα έχει στο άξονα Χ η μπάλα κάποια συγκεκριμένη στιγμή.
        self.speedY = speedY # Η ταχύτητα που θα έχει στο άξονα Y η μπάλα κάποια συγκεκριμένη στιγμή.
        self.genSpeedX = speedX # Η γενική ταχύτητα που θα έχει στο άξονα Χ (δηλάδη η ταχύτητα που θα λαμβάνει η μπάλα μετά από ακινησία).
        self.genSpeedY = speedY # Η γενική ταχύτητα που θα έχει στο άξονα Υ (δηλάδη η ταχύτητα που θα λαμβάνει η μπάλα μετά από ακινησία).
    def move(self, surf,leftracketX,rightracketX,leftracketY,rightRacketY): #Aνανεώνει την θέση της μπάλας.
        self.rect.move_ip(self.speedX, self.speedY)
        surf.blit(self.image, self.rect)
        return(self.check_bounce(surf,leftracketX,rightracketX,leftracketY,rightRacketY)) # Επιστρέφει αυτό που θα επιστρέψει η check_bounce.

    def check_bounce(self,surf,leftracketX,rightracketX,leftracketY,rightracketY, horiz=1000, vert=600): #Ελέγχει αν η μπάλα είναι μέσα στο γήπεδο. 
        if self.rect.top<0 or self.rect.bottom>vert: # Σημαίνει ότι η μπαλά βρήκε σε κάποιον από τους πλαινούς τόιχους.
            self.speedY = -self.speedY
        if self.rect.left<0: # Εβαλε γκολ η δεξιά ρακέτα. Θα τοποθετηθεί μπροστά στην αριστερή ρακέτα και θα έχει μηδενική ταχύτητα.Επίσης θα επιστραφεί 2.
            self.rect.x=leftracketX+55
            self.rect.y=leftracketY+63
            self.speedX=0
            self.speedY=0
            self.rect.move_ip(0, 0)
            surf.blit(self.image, self.rect)
            playSound(1) #Παίζει έναν ήχο.
            pygame.time.wait(1000) #ΚΑΙΝΟΥΡΙΟ ΣΤΟΙΧΕΙΟ. 
            return 2
        if self.rect.right>horiz: # Εβαλε γκολ η αριστερη ρακέτα. Θα τοποθετηθεί μπροστά στην δεξία ρακέτα και θα έχει μηδενική ταχύτητα.Επίσης θα επιστραφεί 1.
            self.rect.x=rightracketX-55 
            self.rect.y=rightracketY+63
            self.speedX=0
            self.speedY=0
            self.rect.move_ip(0, 0)
            playSound(1)
            pygame.time.wait(1000)
            return 1
        return 0 #Θα επιστρεφεί μηδέν αν δεν έχει μπεί γκολ.


# ΚΑΙΝΟΥΡΙΟ ΣΤΟΙΧΕΙΟ. Αναπαριστά ένα πολύ λεπτό rect που βρίσκεται πάνω στην ρακέτα και κουνιέται μαζί μ αυτήν ( το χρησιμοποιούμε για να μην έχουμε περίεργες
# συμπεριφορές όταν η ρακέτα έρχεται σε επαφή με την μπάλα από πλάγια). 
class MyRect(Rect):
    def __init__(self, createX, createY,\
                 dimX=1, dimY=125, speedY=5):
        self.rect=pygame.Rect(createX, createY, dimX, dimY)
        self.moveUp=False
        self.moveDown=False
        self.speedY=speedY

    def move(self, surf, vert=600): # Ανανέωση της θέσης.
        if self.moveUp and self.rect.top>0:
            self.rect.move_ip(0,-self.speedY)
        if self.moveDown and self.rect.bottom<vert:
            self.rect.move_ip(0,self.speedY)



# Aναπαριστά την ρακέτα ( υποκλάση της sprite ). 
class Raketa(Sprite):
    def __init__(self, createX, createY,rot,\
                 dimX=25, dimY=125, speedY=5):
        Sprite.__init__(self)
        self.rect=pygame.Rect(createX, createY, dimX, dimY)
        #Δημιουγία της λεπτής επιφάνειας πάνω από την ρακέτα.
        if rot==90:
            self.upSurf=MyRect(createX+dimX, createY) 
        else:
            self.upSurf=MyRect(createX, createY)
        self.image=pygame.image.load('raketa.png')
        self.image=pygame.transform.rotate(self.image,rot) # Περιστρέφει την ρακέτα. (τη αριστερή 90 μοίρες την δεξιά 270 μοίρες)
        self.transimage = pygame.transform.scale(self.image, (dimX, dimY))
        self.moveUp=False
        self.moveDown=False
        self.speedY=speedY

    def move(self, surf,isThe,my_ball,horiz=1000 ,vert=600):  #Mετακινει την ρακέτα.
        # Ελέγχει αν η μπάλα είναι σταματημένη μπροστά στην αριστερή ρακέτα και αυτή κουνηθέι της δίνει ταχύτητα. 
        if (self.moveUp or self.moveDown) and my_ball.speedX==0 and my_ball.speedY==0 and isThe=='left' and my_ball.rect.x<horiz/2:
            my_ball.speedX= -my_ball.genSpeedX
            my_ball.speedY= my_ball.genSpeedY
            my_ball.rect.move_ip(-my_ball.genSpeedX, my_ball.genSpeedY)
            surf.blit(self.image, self.rect)
        # Ελέγχει αν η μπάλα είναι σταματημένη μπροστά στην δεξιά ρακέτα και αυτή κουνηθέι της δίνει ταχύτητα.    
        if (self.moveUp or self.moveDown) and my_ball.speedX==0 and my_ball.speedY==0 and isThe=='right' and my_ball.rect.x>horiz/2:
            my_ball.speedX= my_ball.genSpeedX
            my_ball.speedY= my_ball.genSpeedY
            my_ball.rect.move_ip(my_ball.genSpeedX, my_ball.genSpeedY)
            surf.blit(self.image, self.rect)
            
        if self.moveUp and self.rect.top>0:
            self.upSurf.move(surf)
            self.rect.move_ip(0,-self.speedY)
        if self.moveDown and self.rect.bottom<vert:
            self.upSurf.move(surf)
            self.rect.move_ip(0,self.speedY)
        surf.blit(self.transimage, self.rect)



# ΚΑΙΝΟΥΡΙΟ ΣΤΟΙΧΕΙΟ. Αναπαριστά ένα εμπόδιο ( υποκλάση της Rect ).
class Barrier(Rect):
    def __init__(self, surf , createX, createY, color ,dimX=2, dimY=50):
        Rect.__init__(self, createX, createY, dimX, dimY)
        self.color=color # Του δίνει χρώμα.
        pygame.draw.rect(surf, color, self, 0)
    def updateBarrier(self, surf): # Ανανεώνει την θέση του.
        pygame.draw.rect(surf, self.color, self, 0)
    def barrierBevavior(self,surf,my_ball): # Συμπεριφορά του εμποδίου ( δεν κάνει κάτι ).
        pass



# ΚΑΙΝΟΥΡΙΟ ΣΤΟΙΧΕΙΟ. Αναπαριστά ένα 'μαγικό' εμπόδιο ( υποκλάση της Barrier ).  
class MagicBarrier(Barrier):
    def __init__(self, surf , createX, createY, color ,dimX=1, dimY=50):
        super().__init__(surf , createX, createY, color ,dimX=1, dimY=50)

    #Επέκταση μεθόδου - Πολυμορφισμός.
    def barrierBevavior(self,surf,my_ball): # Συμπεριφορά του εμποδίου. Αλλάζει την κατεύθυνση της μπάλας στον άξονα Y (Μπερδέυει τον αντίπαλο).
        my_ball.speedY=-my_ball.speedY
        my_ball.rect.move_ip(my_ball.speedX, my_ball.speedY)
        

# ΚΑΙΝΟΥΡΙΟ ΣΤΟΙΧΕΙΟ. Αναπαριστά ένα 'κακό' εμπόδιο ( υποκλάση της Barrier ).
class BadBarrier(Barrier):
    def __init__(self, surf , createX, createY, color ,dimX=1, dimY=50):
        super().__init__(surf , createX, createY, color ,dimX=1, dimY=50)

    #Επέκταση μεθόδου - Πολυμορφισμός.
    def barrierBevavior(self,surf,my_ball): # Συμπεριφορά του εμποδίου. Αλλάζει την κατεύθυνση της μπάλας στον άξονα X (To γυρνάει προς τα πίσω).
        playSound(2) # παίζει έναν ήχο.
        my_ball.speedX= -my_ball.speedX
        my_ball.rect.move_ip(my_ball.speedX,my_ball.speedY)




# ΚΑΙΝΟΥΡΙΟ ΣΤΟΙΧΕΙΟ. Αναπαριστά ένα κουμπί ( υποκλάση της Rect ).
class Button(Rect):
   def __init__(self, text, rectcoord,default_color,hover_color): # Αρχικοποιέι τις διάφορες τιμές του κουμπιού.
      self.text = text
      self.is_hover = False
      self.rectcoord=rectcoord
      self.default_color = default_color
      self.hover_color = hover_color
      self.font_color = (0, 0, 0)
      Rect.__init__(self, rectcoord)


      
   def label(self,screen): # Βάζει το κείμενο στο κουμπί.
      font = pygame.font.Font(None, 22)
      text = font.render(self.text, True, self.font_color)
      my_textRect=text.get_rect()
      my_textRect.centerx = self.centerx        
      my_textRect.centery = self.centery
      screen.blit(text,  my_textRect )


      
   def color(self): # Επιστρέχει το κατάλληλο χρώμα ανάλογα με το αν το ποντίκι είναι πάνω από το κουμπί ή όχι.
      if self.is_hover:
         return self.hover_color
      else:
         return self.default_color
        
   def draw(self, screen, mouse): # Aνανεώνει το κουμπί πάνω στην αντίστοιχη οθόνη.
      pygame.draw.rect(screen, self.color(), self)
      self.label(screen)
      self.check_hover(mouse)
      
      
   def check_hover(self, mouse): # Ελέγχει αν το ποντικί είναι πάνω από το κουμπί.
      if self.collidepoint(mouse):
         self.is_hover = True 
      else:
         self.is_hover = False









# Αναπαριστά την αρχική οθόνη που καλώς ορίζει τον παίχτη,περιέχει κάποιες πληροφορίες για το παιχνίδι ( σε ποιο σκορ λήγει, ποια πλήκτρα χρησιμοποιεί ο κάθε
# παίκτης ) και έχει 2 κουμπιά (ένα κουμπί 'play in normal mode' και ένα κουμπί 'play in fast mode').
def welcome_screen(surf,btn,btn2,my_clock):
    # Συντεταγμένες κέντρου της surf 
    surfcentX = surf.get_rect().centerx
    surfcentY = surf.get_rect().centery

    surf.fill(GREEN)
    redrect=pygame.draw.rect(surf, RED, (surfcentX-400, surfcentY-150, 800, 300), 0)
    my_basicFont = pygame.font.SysFont(None, 80)
    my_secFont = pygame.font.SysFont(None, 55)  
    my_text = my_basicFont.render\
              ("Welcome to 'The Pong Game'.", True, BLACK)  
    my_textRect = my_text.get_rect()         
    my_textRect.centerx = surfcentX          
    my_textRect.centery = surfcentY
    surf.blit(my_text, my_textRect)
    my_text = my_secFont.render('The game ends at 11 points.', True, DARKGREEN)  
    my_textRect = my_text.get_rect()         
    my_textRect.centerx = surfcentX          
    my_textRect.centery = surfcentY+50
    surf.blit(my_text, my_textRect)
    my_thirdFont = pygame.font.SysFont(None, 30)
    my_text =  my_thirdFont.render('created by Aristeidis Moustakas.', True, SILVER)  
    my_textRect = my_text.get_rect()         
    my_textRect.bottomright = surf.get_rect().bottomright  
    surf.blit(my_text, my_textRect)
    my_text =  pygame.font.SysFont(None, 25).render("Player A plays with the 'W' and 'S' keys.", True, SILVER)  
    my_textRect = my_text.get_rect()         
    my_textRect.bottomleft = redrect.bottomleft  
    surf.blit(my_text, my_textRect)
    my_text =  pygame.font.SysFont(None, 25).render("Player B plays with the up and down keys.", True, SILVER)  
    my_textRect = my_text.get_rect()         
    my_textRect.bottomright = redrect.bottomright   
    surf.blit(my_text, my_textRect)
    mouse = pygame.mouse.get_pos()
    btn.draw(surf, mouse)
    btn2.draw(surf, mouse)
    pygame.display.update()
    my_clock.tick(60)


# Αναπαριστά την τελική οθόνη που ανακοινώνει τον νικητή, τα τελικά αποτελέσματα και έχει 2 κουμπιά (ένα κουμπί 'play again' και ένα κουμπί 'exit').
def last_screen(surf,btn,btn2,my_clock,winner,fscore):
    surfcentX = surf.get_rect().centerx
    surfcentY = surf.get_rect().centery
    surf.fill(GREEN)
    pygame.draw.rect(surf, RED, (surfcentX-400, surfcentY-150, 800, 300), 0)
    my_basicFont = pygame.font.SysFont(None, 65)
    my_text = my_basicFont.render("The winner is "+winner+" and ", True, BLACK)  
    my_textRect = my_text.get_rect()         
    my_textRect.centerx = surfcentX          
    my_textRect.centery = surfcentY
    surf.blit(my_text, my_textRect)
    my_text = my_basicFont.render('the final score is '+fscore, True, BLACK)  
    my_textRect = my_text.get_rect()         
    my_textRect.centerx = surfcentX          
    my_textRect.centery = surfcentY+40
    surf.blit(my_text, my_textRect)
    mouse = pygame.mouse.get_pos()
    btn.draw(surf, mouse)
    btn2.draw(surf, mouse)
    pygame.display.update()
    my_clock.tick(60)



# ΚΑΙΝΟΥΡΙΟ ΣΤΟΙΧΕΙΟ. Παίζει έναν ήχο (με την χρήση της mixer). Αν πάρει σαν όρισμα 0 παίζει τον ήχο σύγκρουσης με την ρακέτα, αν πάρει σαν όρισμα το 1 παίζει
# τον ήχο του γκολ και αν πάρει το 2 τον ήχο ότι βρήκε στο badBarrier.
def playSound(i):
    songs = ['pingpong_song.mp3', 'ispoint.mp3','thefail.mp3']
    pygame.mixer.music.load(songs[i])
    pygame.mixer.music.play(0)
