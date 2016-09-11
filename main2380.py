#Μουστάκας Αριστείδης  ΑΕΜ: 2380

#Κάνω import την βιβλιοθήκη μου.
from mylib2380 import * 


pygame.init()

#Αρχικοποιώ το ρολόι, δηλώνω το ύψος και το πλάτος της οθόνης και την αρχικοποιώ με τα κατάλληλα ορίσματα.    
my_clock = pygame.time.Clock()


HORIZ=1000
VERT=600
my_screen = pygame.display.set_mode((HORIZ, VERT), 0, 32)
pygame.display.set_caption('Pong')



#Βρόγχος του παιχνιδιού.

while True:
    #Δημιουργώ 2  κουμπιά (αντικείμενα τύπου button).
    btn = Button('Play in nornal mode', (330,500,150,55) ,RED,MAROON)
    btn2 = Button('Play in fast mode', (550,500,150,55) , RED,MAROON)
    p=True
    #Bρόγχος που αναπαριστά την αρχική οθόνη του παιχνιδιού και έχει μέσα και τα 2 κουμπιά.
    while p:
        welcome_screen(my_screen,btn,btn2,my_clock)
        #ΚΑΙΝΟΥΡΙΟ ΣΤΟΙΧΕΙΟ. Παίρνω την θέση που βρίσκεται αυτήν την στιγμή το ποντίκι.
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():    
            if ev.type == QUIT:
                pygame.quit()                
                sys.exit()
            elif ev.type == MOUSEBUTTONDOWN:
                #Αν πατηθεί το πρώτο κουμπί ( ξεκινάει το παιχνίδι σε normal mode ) ορίζω σαν ταχύτητα της μπάλας στο άξονα x το -3 και στον y τo 2.
                #Επίσης κάνω το p=false δηλαδή τελειώνει ο βρόγχος που αναπαριστά την αρχική οθόνη.
                if btn.collidepoint(mouse):
                     p=False
                     ballSpX=-3
                     ballSpY=2
                elif btn2.collidepoint(mouse):#Αν πατηθεί το πρώτο κουμπί ( ξεκινάει το παιχνίδι σε fast mode ) ορίζω σαν ταχύτητα
                     p=False                # της μπάλας στο άξονα x το -4 και στον y τo 3. Επίσης κάνω το p=false δηλαδή τελειώνει ο βρόγχος που αναπαριστά την αρχική οθόνη. 
                     ballSpX=-4
                     ballSpY=3
        
        pygame.display.update()









    
    my_screen.fill(GREEN)
    # Δημιουργώ ένα αντικείμενο ball και το τοποθετώ στην θέση (HORIZ-50, VERT-50) και ξεκινάει με αρχική ταχύτητα ballSpX, ballSpY που έχουν πάρει τιμή
    # από τα κουμπιά της αρχικής οθόνης.
    my_ball = Ball(HORIZ-50, VERT-50, ballSpX, ballSpY)
    #Δημιουργώ 2 ρακέτες. Την πρώτη (δεξιά ρακέτα) την τοποθετώ στην θέση (HORIZ*9/10, VERT/2) και την περιστρέφω 270 μοίρες και την δεύτερη (αριστερή ρακέτα)
    # στην θέση (HORIZ*1/10, VERT/2) με περιστροφή 90 μοίρες.
    first_rak = Raketa(HORIZ*9/10, VERT/2,rot=270) 
    second_rak = Raketa(HORIZ*1/10, VERT/2,rot=90)

    #Δημιουργώ τα 10 αντικείμενα εμπόδια που βρίσκονται στην μέση.Το 3ο και το 9ο είναι MagicΒarrier αντικείμενα (κόκκινο χρώμα) , το 6 BadBarrier (μαύρο χρώμα)
    #και τα υπόλοιπα απλά Barrier αντικείνα (λευκό χρώμα).
    barrierList=[ Barrier(my_screen,HORIZ/2 - 3 , 60*i , WHITE) if i==0 or i==1 or i==3 or i==4 or i==6 or i==7 or i==9 \
                  else MagicBarrier(my_screen,HORIZ/2 - 3 , 60*i , RED) if i==2 or i==8 else BadBarrier(my_screen,HORIZ/2 - 3 , 60*i , BLACK)  for i in range(10)]


    
    p=True
    #Δημιουργώ ένα αντικείμενο Game
    game=Game()


    #Ο βρόγχος του παιχνιδιού.
    while p:
        for ev in pygame.event.get():    
            if ev.type == QUIT:
                pygame.quit()                
                sys.exit()


    # Ανάλογα με το ποιο πλήκτρο πατήθει παίρνουν τιμή true οι αντίστοιχες ιδιότητες των αντικειμένων first_rak και second_rak και οι αντίστοιχες επιφάνειες
    # first_rak.upSurf και second_rak.upSurf που βρίσκονται στο πάνω μέρος τους.
            if ev.type == KEYDOWN:
                if ev.key == K_UP:
                    first_rak.moveUp = True
                    first_rak.upSurf.moveUp=True
                if ev.key == K_DOWN:
                    first_rak.moveDown = True
                    first_rak.upSurf.moveDown=True
                if ev.key == K_w:
                    second_rak.moveUp = True
                    second_rak.upSurf.moveUp=True
                if ev.key == K_s:
                    second_rak.moveDown = True
                    second_rak.upSurf.moveDown=True
                if ev.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if ev.type == KEYUP:
                if ev.key == K_UP:
                    first_rak.moveUp = False
                    first_rak.upSurf.moveUp=False
                if ev.key == K_DOWN:
                    first_rak.moveDown = False
                    first_rak.upSurf.moveDown=False
                if ev.key == K_w:
                    second_rak.moveUp = False
                    second_rak.upSurf.moveUp=False
                if ev.key == K_s:
                    second_rak.moveDown = False
                    second_rak.upSurf.moveDown=False






        # Η λογική του παιχνιδιού.
        my_screen.fill(GREEN)
        for bar in barrierList: #Καλώ την updateBarrier για όλα τα Barrier ώστε να ανανεωθούν στην οθόνη.
            bar.updateBarrier(my_screen)

        # Καλώ την my_ball.move ώστε να ανανεωθεί η θέση της πάντας. Μου επιστρέφετε 0 αν δεν έχει μπει Goal 1 αν έχει βάλει Goal η αριστερή ρακέτα και 2 αν
        # έχει βάλει goal η δεξιά ρακέτα.
        point=my_ball.move(my_screen,second_rak.rect.x,first_rak.rect.x,second_rak.rect.y,first_rak.rect.y)
        first_rak.move(my_screen,'right',my_ball) # Ανανεώνεται η θέση της δεξίας ρακέτας.
        second_rak.move(my_screen,'left',my_ball) # Ανανεώνεται η θέση της αριστερής ρακέτας.
        game.printScore(my_screen,point)        # Εκτυπώνεται το τρέχον score.

        
        for bar in barrierList:     # Ελέγχω αν η my_ball χτύπησει πάνω σε κάποιο εμπόδιο καλείται η barrierBevavior για το συγκεκριμένο Barrier όπου θα  
            if my_ball.rect.colliderect(bar):   # ενεργοποιήσει την συμπεριφορά του συγκεκριμένου εμποδίου.
                bar.barrierBevavior(my_screen,my_ball)



        #Ελέγχει αν η μπάλα συγκρουστεί με το rectangle upSurf που είναι μια πολύ λεπτή επιφάνει στο μπροστινίο μέρος της ρακέτας και αλλάζει την κατεύθυνση της μπάλας.
        if my_ball.rect.colliderect(first_rak.upSurf.rect) or my_ball.rect.colliderect(second_rak.upSurf.rect):
            playSound(0) # ΚΑΙΝΟΥΡΙΟ ΣΤΟΙΧΕΙΟ. Παίζει ένας ήχος.
            my_ball.speedX= -my_ball.speedX
            my_ball.move(my_screen,second_rak.rect.x,first_rak.rect.x,second_rak.rect.y,first_rak.rect.y)


            
        if game.scoreFirst==11: # Aν ο πρώτος παίχτης μαζέψει 11 πόντους το παιχνίδι λήγει και γίνεται false ο βρόγχος του παιχνιδιου.
            winner='Player A'
            p=False
        elif game.scoreSecond==11:  # Aν ο δεύτερος παίχτης μαζέψει 11 πόντους το παιχνίδι λήγει και γίνεται false ο βρόγχος του παιχνιδιου.
            winner='Player B'
            p=False
        pygame.display.update() # ανανέωση της οθόνης.
        my_clock.tick(120)







    #Δημιουργώ 2  κουμπιά (αντικείμενα τύπου button).
    btn = Button('Play again', (330,500,150,55) ,RED,MAROON)
    btn2 = Button('Exit', (550,500,150,55) , RED,MAROON)
    pygame.display.update()
    p=True
    #Bρόγχος που αναπαριστά την αρχική οθόνη του παιχνιδιού και έχει μέσα και τα 2 κουμπιά.
    while p:
        last_screen(my_screen,btn,btn2,my_clock,winner,str(game.scoreFirst)+" - "+str(game.scoreSecond))
        mouse = pygame.mouse.get_pos()
        for ev in pygame.event.get():
            if ev.type == QUIT:
                pygame.quit()                
                sys.exit()
            if ev.type == MOUSEBUTTONDOWN:
                #Αν πατηθεί το πρώτο κουμπί κάνω το p=false δηλαδή τελειώνει ο βρόγχος που αναπαριστά την τελική οθόνη και ουσιαστικά ξαναγυρνάω στο μεγάλο βρόγχο
                # while (δηλαδή θα εμφανιστεί η αρχική οθόνη ).
                if btn.collidepoint(mouse):
                    p=False
                elif btn2.collidepoint(mouse): #Αν πατηθεί το πρώτο κουμπί κάνω το p=false δηλαδή τελειώνει ο βρόγχος που αναπαριστά την τελική οθόνη και
                    p=False                     # και τερματίζει η εφαρμογή.
                    pygame.quit()
                    sys.exit()
  


    
