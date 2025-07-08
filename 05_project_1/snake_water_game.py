"""
let water(w) = -1
let snake(s) = 1
let gun(g) = 0 
"""

computer = -1
yourStr = input("Enter your choice {water:w, snake:s, gun:g}  :")
gameDir = { "w": -1, "s": 1, "g":0 }
you = gameDir[yourStr]

if(computer == you):
    print('It\'s  a draw')
else:    
    if( computer == -1 and you == 0):
        print('You loose')
    elif( computer == -1 and you == 1 ):
        print('You Win')
