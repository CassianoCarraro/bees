FPS = 30
WINDOWWIDTH = 800
WINDOWHEIGHT = 600
MENUWIDTH = 200
GAMERECTWIDTH = WINDOWWIDTH - MENUWIDTH
CELLSIZE = 20
assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size."
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size."
CELLWIDTH = int(WINDOWWIDTH / CELLSIZE)
CELLHEIGHT = int(WINDOWHEIGHT / CELLSIZE)

#             R    G    B
WHITE     = (255, 255, 255)
BLACK     = (  0,   0,   0)
RED       = (255,   0,   0)
GREEN     = (  0, 255,   0)
DARKGREEN = (  0, 155,   0)
DARKGRAY  = ( 40,  40,  40)
LIGHTGRAY = (211, 211, 211)
BGCOLOR = BLACK

UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'

angles = (( 45,   0,  -45),
          ( 90,   0,  -90),
          (135, 180, -135))
