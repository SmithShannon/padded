import pygame, os

dirname = os.path.dirname

class Room:
    def __init__(self):
        self.tiles = [10][10]

    def isSolved(self):
        return True

    def refresh (self):
        return tiles

class Tile:
    def __init__(self,image):
        self.image = image

    def refresh (self):
        return self.image

    def onTap (self,event):
        return True

class Sign(Tile):
    def __init__(self,text):
        super.__init__(self,pygame.image.load("signpost"))

    def onTap (self):
        text

class Totem(Tile):
    def __init__(self,images,symbols,neighbours):
        super.__init__(self,images[0])
        self.state = 0
        self.totems = symbols
        self.images = images
        self.neighbours = neighbours

    def onTap (self,event):
        self.state += 1
        for neighbour in neighbours:
            neighbour.onTap()

    def getState (self):
        return self.totems[self.state%len(totems)]

pygame.init()

class Room1(Room):
    def __init__ (self):
        super.__init__(self)
        

white = (255,255,255)

x=1000
y=1000

display_surface = pygame.display.set_mode((x,y))

floor = pygame.image.load("floor.png")
hWall = pygame.image.load("wall.png")
vWall = pygame.transform.rotate(hWall,90)
nwCorner = pygame.image.load("corner.png")
swCorner = pygame.transform.rotate(nwCorner,90)
seCorner = pygame.transform.rotate(swCorner,90)
neCorner = pygame.transform.rotate(seCorner,90)

doorN = pygame.image.load("closed_door.png")
doorW = pygame.transform.rotate(doorN,90)
doorS = pygame.transform.rotate(doorW,90)
doorE = pygame.transform.rotate(doorS,90)

openDN = pygame.image.load("open_door.png")
openDW = pygame.transform.rotate(openDN,90)
openDS = pygame.transform.rotate(openDW,90)
openDE = pygame.transform.rotate(openDS,90)

totemM = pygame.image.load("totem_M.png")
totemR = pygame.image.load("totem_R.png")

bed = pygame.image.load("bed.png")

while True:
    display_surface.blit(nwCorner,(0,0))
    display_surface.blit(swCorner,(0,900))
    display_surface.blit(seCorner,(900,900))
    display_surface.blit(neCorner,(900,0))
    for h in range(1,9):
        display_surface.blit(hWall,(0,h*100))
        display_surface.blit(hWall,(900,h*100))
        display_surface.blit(vWall,(h*100,0))
        display_surface.blit(vWall,(h*100,900))
    for r in range(1,9):
        for c in range(1,9):
            display_surface.blit(floor,(r*100,c*100))
    display_surface.blit(doorN,(500,0))
    display_surface.blit(doorW,(0,500))
    display_surface.blit(doorS,(400,900))
    display_surface.blit(doorE,(900,400))

    display_surface.blit(openDN,(400,0))
    display_surface.blit(openDW,(0,400))
    display_surface.blit(openDS,(500,900))
    display_surface.blit(openDE,(900,500))
    
    display_surface.blit(totemM,(500,500))
    display_surface.blit(totemR,(400,400))
    display_surface.blit(bed,(700,800))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        pygame.display.update()
        
