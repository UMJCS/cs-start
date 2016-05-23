# Written by minjie 10109867 using python3
# The input to the program is a text file containing comments, the robot start pose and a 2D map.
# Comment lines begin with a dollar character ($) and should be ignored by your program.
# The first non-comment line of that text file encodes the start pose of the robot.
# Those are three integer numbers separated by spaces. They encode x, y and orientation of the start, in that order.
# For the purpose of this assignment the orientation is encoded as four integer values between 0 and 3.
# 0: positive in x-axis (east)
# 1: positive in y-axis (north)
# 2: negative in x-axis (west)
# 3: negative in y-axis (south)
# we can realize that the number and orientation have something in common
# and i can use it to simpily my program
#  '.' (a free cell) or 'X' (occupied cell = wall).
# The bottom left cell in the text file is located in the origin of the coordinate system (0, 0).
# The x-axis follows this line to the east (right) while the y-axis follows this column to the north (up).
# but the list after deling is opposite,so i use list to save the position
# the Algorithm is very simple
# The algorithm has two parts:
# 1) Find the Wall
# 2) Follow the Wall.
# Find Wall
# Go forward until you either:
#   Reach an exit
#   Have a wall to the left side
#   Have a wall in front of you
#     In this case turn right once
# Follow Wall
# Do until you reach an exit:
#   If no wall on your left:
#     Turn left
#     Step forward
#   Else if wall in front of you:
#     Turn right
#   Else:
#     Go forward
# Output:
# The program has to output all poses the robot drives through
# while following the left hand wall following algorithm (see below).
# The output starts with the start pose and ends with the end pose.
# All intermediate poses have to be displayed as well.
# Make sure that you do not print the same pose immediately again
# - with the exception if start and end pose are the same! The end pose is always outside of the map (we have exited the maze).
# The pose output has to have the following format:
# [[x, y], o]
# with x and y being the coordinates and o the orientation with the same encoding as the input.
# There is one space after each comma.
# Write each pose in a new line.
#######################################################
#The out function: using to print all the tem after deling
def out(position_tem_use):
    print(position_tem_use)
#######################################################
# #Then simulate all the acts of the robot
# 1.forward()
# 2.turnLeft()
# 3.turnRight()
# I use list deling to get the point which is having now
# and using it to change the position_tem_use to change
# and do the next step
# it's easy to simulate
# we should decide the orientation it owns and then using list to change
def forward(position_tem_use):
    if position_tem_use[1]==0:
        position_tem_use[0][0]+=1
    if position_tem_use[1]==1:
        position_tem_use[0][1]+=1
    if position_tem_use[1]==2:
        position_tem_use[0][0]-=1
    if position_tem_use[1]==3:
        position_tem_use[0][1]-=1
    return position_tem_use
#the relationship between 0-3 and the orientation makes it quick to turn left and ten right
#and don't need to decide the orientation first
def turnLeft(position_tem_use):
    if position_tem_use[1]==3:
        position_tem_use[1]=0
    else:
        position_tem_use[1]+=1
    return position_tem_use
def turnRight(position_tem_use):
    if position_tem_use[1]==0:
        position_tem_use[1]=3
    else:
        position_tem_use[1]-=1
    return position_tem_use
##########################################################
#Then It is required that you implement and use functions with the following name and according functionality:

# moves the provided pose one step forward
#1.forward(...)

# turns the provided pose left
#2.turnLeft(...)

# returns true if the cell in front of given pose is occupied
#3.isWallInFront(...)
# turnleft function is already done
# and the turnRight function is used in is isWallInFront function
# for if a robot find a wall infront it turn right at once
# The algorithm
##############################################################
# Follow Wall
# Do until you reach an exit:
#   If no wall on your left:
#     Turn left
#     Step forward
#   Else if wall in front of you:
#     Turn right
#   Else:
#     Go forward
def isWallInFront(position_tem_use):
    if position_tem_use[1]==2:
        if [position_tem_use[0][0]-1,position_tem_use[0][1]] in wall_position:
            return True
        else:
            return False
    if position_tem_use[1]==0:
        if [position_tem_use[0][0]+1,position_tem_use[0][1]] in wall_position:
            return True
        else:
            return False
    if position_tem_use[1]==3:
        if [position_tem_use[0][0],position_tem_use[0][1]-1] in wall_position:
            return True
        else:
            return False
    if position_tem_use[1]==1:
        if [position_tem_use[0][0],position_tem_use[0][1]+1] in wall_position:
            return True
        else:
            return False
def isWallToLeft(position_tem_use):
    if position_tem_use[1]==2:
        if [position_tem_use[0][0],position_tem_use[0][1]-1] in wall_position:
            return True
        else:
            return False
    if position_tem_use[1]==0:
        if [position_tem_use[0][0],position_tem_use[0][1]+1] in wall_position:
            return True
        else:
            return False
    if position_tem_use[1]==3:
        if [position_tem_use[0][0]+1,position_tem_use[0][1]] in wall_position:   #(x+1,y)
            return True
        else:
            return False
    if position_tem_use[1]==1:
        if [position_tem_use[0][0]-1,position_tem_use[0][1]] in wall_position:
            return True
        else:
            return False
import sys,copy
words=sys.stdin.readlines()
# Using stdin.readlines make it better to deal with all the lines
################################################################
# Make tems and parameter
position_tem_use=[]
position_tem=[]
wall_position=[]
maze_high=-1
step=0
width=0
#################################################################
# divide all lines in words
# if $ in lines it means should be ignored
# if X and . in lines means it is a maze
# else is the position numbers
for line in words:
    if line[0]=='$':
        pass
    elif line[0]==' ' or line[0]=='\n':
        pass
    elif line[0]!='X' and line[0]!='.':
        for i in line.split(' '):
            position_tem.append(int(i.replace('\n','')))
        position_tem=[[position_tem[0],position_tem[1]],position_tem[2]]
#Make list the same as output
# And make it easy to change and judge
    else:
        maze_high+=1
        width=len(line)
        for comd in range(width):
         #   print(line)
            if line[comd]=='X':
                wall_position.append([comd,maze_high])

for position_tem_use in wall_position:
    position_tem_use[1]=maze_high-position_tem_use[1]
##################################
# The judgement of exit is the x,y of the position
# above 0 and less than the maze_high and maze_width
def Exit(position_tem_use):
    if position_tem_use[0][0]<0 or position_tem_use[0][0]>width-1 or position_tem_use[0][1]<0 or position_tem_use[0][1]>maze_high:
        return True
    else:
        return False
#find all the position of the wall
#and easy for judge if is/not a wall in front or at left or at right side
##########################################################
position_tem_use=position_tem
out(position_tem_use)
############################################################
# if the start position is  outside the maze
#print the end position and quit
if Exit(position_tem_use)==True :
    out(position_tem_use)
#if the start position is inside the maze
# the Algorithm
# Find Wall
# Go forward until you either:
#   Reach an exit
#   Have a wall to the left side
#   Have a wall in front of you
#     In this case turn right once
else:
    while isWallToLeft(position_tem_use)==False and Exit(position_tem_use)==False:
         #   print('in0')
        if isWallInFront(position_tem_use)==True:
          #      print('in1')
            position_tem_use=turnRight(position_tem_use)
            out(position_tem_use)
        else:
           #     print('in2')
            position_tem_use=forward(position_tem_use)
            out(position_tem_use)
# The algorithm
# Follow Wall
# Do until you reach an exit:
#   If no wall on your left:
#     Turn left
#     Step forward
#   Else if wall in front of you:
#     Turn right
#   Else:
#     Go forward
while Exit(position_tem_use)==False and step<500:
# Do until you reach an exit:
#   If no wall on your left:
#     Turn left
#     Step forward
    if isWallToLeft(position_tem_use)==False:
        position_tem_use=turnLeft(position_tem_use)
        out(position_tem_use)
        position_tem_use=forward(position_tem_use)
        out(position_tem_use)
        step+=2
#   If no wall on your left:
#     Turn left
#     Step forward
    elif isWallInFront(position_tem_use)==True:
        position_tem_use=turnRight(position_tem_use)
        out(position_tem_use)
        step+=1
#   Else if wall in front of you:
#     Turn right
    else:
        position_tem_use=forward(position_tem_use)
        out(position_tem_use)
        step+=1
#   Else:
#     Go forward
########################################################
#   End








