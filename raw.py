import pygame
class chess:

    def __init__(self):
        self.turn='w'
        self.running=True
        self.board=[
        ['R','N','B','Q','K','B','N','R'],
        ['P','P','P','P','P','P','P','P'],
        ['_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_'],
        ['_','_','_','_','_','_','_','_'],
        ['p','p','p','p','p','p','p','p'],
        ['r','n','b','q','k','b','n','r']
                    ]
        
        self.wpieces=['q','k','b','n','r','p']
        self.bpieces=['R','N','B','Q','K','P']

        #---pygame init :

        self.col=True
        pygame.init()

        WIDTH, HEIGHT = 800, 800

        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Chess")


        # ---
        self.font = pygame.font.SysFont(None, 48)
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.color1 = (0, 0, 0)


#---returns i and j for ij :
    def cal(self,k):
        i=k//10
        j=k%10
        return [i,j]


    def isblack(self,i,j):
        return(self.board[i][j] in self.bpieces) 
    
    def iswhite(self,i,j):
        return(self.board[i][j] in self.wpieces) 

    def tonum(self,i,j):
        return (i*10)+j
    
    def v(self,i,j):
        return i<8 and i>-1 and j<8 and j>-1



#--------function for each piece :
    #promotion not defined
    def wpawn(self,i,j):
        ret=[]

        if(self.v(i-1,j) and self.board[i-1][j]=='_'):
            ret.append(self.tonum(i-1,j))
        if(self.v(i-1,j-1) and self.isblack(i-1,j-1)):
            ret.append(self.tonum(i-1,j-1))
        if(self.v(i-1,j+1) and self.isblack(i-1,j+1)):
            ret.append(self.tonum(i-1,j+1))
        if(i==6):
            ret.append(self.tonum(i-2,j))
        return ret
        
    def wknight(self,i,j):
        ret=[]
        if(self.v(i-1,j-2) and self.board[i-1][j-2] not in self.wpieces):
            ret.append(self.tonum(i-1,j-2))

        if(self.v(i-1,j+2) and self.board[i-1][j+2] not in self.wpieces):
            ret.append(self.tonum(i-1,j+2))

        if(self.v(i-2,j-1) and self.board[i-2][j-1] not in self.wpieces):
            ret.append(self.tonum(i-2,j-1))

        if(self.v(i-2,j+1) and self.board[i-2][j+1] not in self.wpieces):
            ret.append(self.tonum(i-2,j+1))

        #

        if(self.v(i+1,j-2) and self.board[i+1][j-2] not in self.wpieces):
            ret.append(self.tonum(i+1,j-2))

        if(self.v(i+1,j+2) and self.board[i+1][j+2] not in self.wpieces):
            ret.append(self.tonum(i+1,j+2))

        if(self.v(i+2,j-1) and self.board[i+2][j-1] not in self.wpieces):
            ret.append(self.tonum(i+2,j-1))

        if(self.v(i+2,j+1) and self.board[i+2][j+1] not in self.wpieces):
            ret.append(self.tonum(i+2,j+1))

        return ret

    def wrook(self,i,j):                                
        ret=[]
        x=i
        y=j
        while( self.v(x+1,y) and self.board[x+1][y] not in self.wpieces):
            if(self.board[x+1][y]!='_'):
                ret.append(self.tonum(x+1,y))
                break
            ret.append(self.tonum(x+1,y))
            x=x+1
        
        x=i
        y=j

        while( self.v(x-1,y) and self.board[x-1][y] not in self.wpieces):
            if(self.board[x-1][y]!='_'):
                ret.append(self.tonum(x-1,y))
                break
            ret.append(self.tonum(x-1,y))
            x=x-1
        
        x=i
        y=j

        while( self.v(x,y-1) and self.board[x][y-1] not in self.wpieces):
            if(self.board[x][y-1]!='_'):
                ret.append(self.tonum(x,y-1))
                break
            ret.append(self.tonum(x,y-1))
            y=y-1


        x=i
        y=j

        while( self.v(x,y+1) and self.board[x][y+1] not in self.wpieces):
            if(self.board[x][y+1]!='_'):
                ret.append(self.tonum(x,y+1))
                break
            ret.append(self.tonum(x,y+1))
            y=y+1


        return ret

#--------------ends here


    def possiblemoves(self,i,j,turn):
        
        if(self.board[i][j]==' '):
                return []
        

        if(turn=='w'):
            if(self.board[i][j]=='p'):
                return self.wpawn(i,j)
            elif(self.board[i][j]=='q'):
                return self.wqueen(i,j)
            elif(self.board[i][j]=='r'):
                return self.wrook(i,j)
            elif(self.board[i][j]=='n'):
                return self.wknight(i,j)
            elif(self.board[i][j]=='b'):
                return self.wbishop(i,j)
            elif(self.board[i][j]=='k'):
                return self.wking(i,j)
        else:
            if(self.board[i][j]=='p'):
                return self.bpawn(i,j)
            elif(self.board[i][j]=='q'):
                return self.bqueen(i,j)
            elif(self.board[i][j]=='r'):
                return self.brook(i,j)
            elif(self.board[i][j]=='n'):
                return self.bknight(i,j)
            elif(self.board[i][j]=='b'):
                return self.bbishop(i,j)
            elif(self.board[i][j]=='k'):
                return self.bking(i,j)
            

    def move(self,frm,to,turn):

        
        [i,j]=self.cal(frm)
        [x,y]=self.cal(to)

        pmoves=self.possiblemoves(i,j,turn) or []
        
        if( to not in pmoves):

            print("Not a valid move , try again")
            return False


        self.board[x][y]=self.board[i][j]
        self.board[i][j]='_'
        self.showgrid()
        self.plotp()
        pygame.display.flip()
        return True




    def takemove(self,turn):
        print(turn," move move 00 to 45 : ")
        begin=int(input())

        [i,j]=self.cal(begin)
        
        if(self.v(i,j)):

            pm=self.possiblemoves(i,j,'w')
            if(len(pm)==0):
                return [-2,-2]

            print(self.symb[self.board[i][j]],pm)

            end=int(input())
        else:
            return [-1,-1]

        return [begin,end]
 
    def run(self):

        tofrom=[]
        self.showgrid()
        self.plotp()
        pygame.display.flip()
        while(self.running):
            
            
            for event in pygame.event.get():
            # Handle quit
                if event.type == pygame.QUIT:
                    self.running = False

                # Detect mouse tap (mouse button down event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:  # Left click

                        tofrom.append(event.pos)

                        frm=tofrom[0][1]//100*10 + tofrom[0][0]//100
                        
                        print(tofrom[0][1]//100*10 + tofrom[0][0]//100)

                        fx=tofrom[0][1]//100
                        fy=tofrom[0][0]//100

                        pm=self.possiblemoves(fx,fy,'w')

                        print(pm)

                        self.showgrid()
                        self.plotp()
                        pygame.display.flip()


                        if(len(tofrom)>=2 and len(pm)>0):

                            tx=tofrom[1][1]//100
                            ty=tofrom[1][0]//100

                            tofrom=[]

                            to=tx*10 + ty
                            

                            if(self.turn=='w'):
                                                                    
                                    self.move(frm,to,'w')
                                    self.showboard()

                                
                                

                            else:
                                [i,j]=self.takemove("Black")
                                
                                if(i==-2):
                                    print("no postion to move")

                                elif(i==-1):
                                    print("wrong input , try again : ")
                                else:


                                    x=self.move(i,j,'w')
                                    self.showboard()
                                    if(x):
                                        self.turn='w'

        pygame.quit()


    symb = {
        'K': '♔',  'Q': '♕',  'R': '♖',  'B': '♗',  'N': '♘',  'P': '♙',  # white
        'k': '♚',  'q': '♛',  'r': '♜',  'b': '♝',  'n': '♞',  'p': '♟',  # black
        '_': ' ',  ' ': '·',   None: 'none'                                        # empty
    }


    def showboard(self):
        # Header
        print("\n    0  1  2  3  4  5  6  7")
        print("  ──────────────────────────")
        
        for rank in range(0,8):
            row = self.board[rank]
            print(f"{rank} │", end=" ")
            for square in row:
                glyph = self.symb.get(square, '_')
                print(glyph, end="  ")
            print(f"│ {8 - rank}")
        
        # Footer
        print("  ──────────────────────────")
        print("    a  b  c  d  e  f  g  h\n")



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
                if self.board[x][y]  == '_':
                    txt=' '
                else:
                    txt=self.board[x][y] 
                text_surface = self.font.render(txt , True, self.color1)
                self.screen.blit(text_surface, (j+30, i+30))
                

b1=chess()
print("Hello")
b1.showgrid()
b1.showboard()
b1.run()

