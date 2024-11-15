
BSIZ = 3 # board side size

ST_PLAYER = 4 # stones per player

# Define the colors we will use in RGB format
BLACK =   (  0,   0,   0)
GRAY =    (150, 150, 150) 
WHITE =   (255, 255, 255)
# Chosen so that they are still friendly to colorblind people:
BLUISH =  ( 26, 133, 255)
REDDISH = (212,  17,  89)
PLAYER_COLOR = (BLUISH, REDDISH) 

# Define the game window width and height and the slot size and separation in pixels
SLOT = 100        # squares size
SEP = 20          # squares separation
ROOM = SLOT + SEP # extra room at sides 
HEIGHT = BSIZ * SLOT + (BSIZ + 1) * SEP + ROOM # room for 3 squares with margin and internal separators and extra below
WIDTH = HEIGHT + ROOM              # extra at both sides
RAD = SLOT / 3                     # circle radius

NO_PLAYER = -1
