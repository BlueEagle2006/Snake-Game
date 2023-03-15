import pygame;
import random,time;
pygame.init();
gd = pygame.display.set_mode((600,600))
pygame.display.set_caption('Snake Game');
def Oyun_Snake():
    def score(number):
        font = pygame.font.SysFont(None,30);
        text = font.render('Apples: '+str(number),True,(255,255,255))
        gd.blit(text,(0,0));
    def get_high_score():
        f0=open("high_score.txt","a");
        f0.close();
        f0=open("high_score.txt","r");
        f1=f0.read();
        f0.close();
        if len(f1)==0:
            f1=0;
            f0=open("high_score.txt","w");
            f0.write(str(f1));
            f0.close();
        return int(f1);
    def update_high_score(apples,highscore):
        if apples>highscore:
            f0=open("high_score.txt","w");
            f0.write(str(apples));
            f0.close();
    def high_score(number):
        font = pygame.font.SysFont(None,30);
        text = font.render('High Score: '+str(number),True,(255,255,255))
        gd.blit(text,(0,25));
    def snake(x,y,ax,ay,sp):
        pygame.draw.rect(gd,(0,0,0),[0,0,600,600]);
        pygame.draw.rect(gd,(255,0,0),[(ax*40),(ay*40),40,40]);
        pygame.draw.rect(gd,(225,200,0),[x,y,40,40]);
        for i in range(len(sp)):
            if i%2==0:
                pygame.draw.rect(gd,(255,255,0),[(sp[i]),(sp[i+1]),40,40]);
    def text_objects(text,font):
        textS=font.render(text,True,(255,255,255))
        return(textS)
    def pprint(text):
        LT = pygame.font.Font('freesansbold.ttf',40);
        Text = text_objects(text,LT)
        gd.blit(Text,(180,80))
        pygame.display.update();
    def game_loop():
        while True:
            sayi=0;
            x = 200;
            y = 240;
            b=1;
            xC=0;
            yC=0;
            ax=11;
            ay=6;
            Dur=0;
            gd.fill((255,255,255));
            pygame.draw.rect(gd,(0,0,0),[0,0,600,600]);
            pprint('Snake Game');
            time.sleep(1);
            pygame.draw.rect(gd,(0,0,0),[0,0,600,600]);
            pprint('by Can ER')
            time.sleep(1);
            sp=[160,240,120,240]
            Q = False;
            while not Q:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        Dur=1;
                if Dur==1:
                    break;
                snake(x,y,ax,ay,sp);
                score(sayi);
                update_high_score(sayi,get_high_score());
                high_score(get_high_score());
                pygame.display.update();
                key = pygame.key.get_pressed();
                if x==(ax*40) and y==(ay*40):
                    sayi+=1                
                    sp.append(sp[(len(sp)-1)-1])
                    sp.append(sp[(len(sp)-1)-3])
                    while True:
                        o=0;
                        ax=random.randrange(0,15)
                        ay=random.randrange(0,15)
                        for i in range(len(sp)):
                            if i%2==0:
                                if sp[i]==(ax*40) and sp[i+1]==(ay*40):
                                    o=1;
                                if x==(ax*40) and y==(ay*40):
                                    o=1;
                        if o==0:
                            break;
                if key[pygame.K_RIGHT] or key[pygame.K_d]:
                    if (xC)!=(-40):
                        xC=40;
                        yC=0;
                        time.sleep(0.001);
                        b=0;
                if key[pygame.K_LEFT] or key[pygame.K_a]:
                    if (xC)!=(40)and b==0:
                        xC=-40;
                        yC=0;
                        time.sleep(0.001);
                if key[pygame.K_UP] or key[pygame.K_w]:
                    if (yC)!=(40):
                        xC=0;
                        yC=-40;
                        time.sleep(0.001);
                        b=0;
                if key[pygame.K_DOWN] or key[pygame.K_s]:
                    if (yC)!=(-40):
                        xC=0;
                        yC=40;
                        time.sleep(0.001);
                        b=0;
                if b==0:
                    for i in range(len(sp)-1,-1,-1):
                        if i>=2 and i%2==0:
                            sp[i]=sp[i-2]
                            sp[i+1]=sp[i-1]
                    sp[0]=x;
                    sp[1]=y;
                x=x+xC;
                y=y+yC;
                p=0;
                for i in range(len(sp)):
                    if i%2==0:
                        if sp[i]==x and sp[i+1]==y:
                            p+=1;
                            break;
                if p==1:
                    time.sleep(1);
                    Q = True;
                if x<0:
                    x=560;
                if x>560:
                    x=0;
                if y<0:
                    y=560;
                if y>560:
                    y=0;
                time.sleep(0.08);
                pygame.display.update();
            if Dur==1:
                break;
    game_loop();
Oyun_Snake();
