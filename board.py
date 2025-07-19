import pygame
import sys


class show:
    def __init__(self):

        self.col=True
        pygame.init()
        WIDTH, HEIGHT = 800, 800

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")

        self.running = True



        self.font = pygame.font.SysFont(None, 48)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)

        self.color1 = (0, 0, 0)


        self.board=[
        ['R','N','B','Q','K','B','N','R'],
        ['P','P','P','P','P','P','P','P'],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        [' ',' ',' ',' ',' ',' ',' ',' '],
        ['p','p','p','p','p','p','p','p'],
        ['r','n','b','q','k','b','n','r']
                    ]
    
        symb = {
        'K': '♔',  'Q': '♕',  'R': '♖',  'B': '♗',  'N': '♘',  'P': '♙',  # white
        'k': '♚',  'q': '♛',  'r': '♜',  'b': '♝',  'n': '♞',  'p': '♟',  # black
        '_': '_',  ' ': '·',   None: 'none'                                        # empty
    }


        self.ft=[]


    def color(self):
        if(self.col):
            self.col=False
            return [0,100,0]
        else:
            self.col=True
            return [255,255,255]

    def showgrid(self):
        


        for i in range(0,800,100):
            self.col= not self.col
            for j in range(0,800,100):

                pygame.draw.rect(self.screen, self.color(), (i, j, 100, 100,))

    def plotp(self):
            

        for i in range(0,800,100):
            for j in range(0,800,100):

                x=int(i/100)
                y=int(j/100)
                print(x," ",y)
                text_surface = self.font.render(self.board[x][y], True, self.color1)
                self.screen.blit(text_surface, (j+30, i+30))
                


    def run(self):
        while self.running:
        
            # Event handling
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print("2")
                    self.ft.append(event.pos)
                
                
            self.screen.fill((30, 30, 30))
            s1.showgrid()
            self.plotp()
            pygame.display.flip()

         

s1 = show() 


s1.run()

pygame.quit()

sys.exit()
      
        











