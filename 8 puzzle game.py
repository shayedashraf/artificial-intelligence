# -*- coding: utf-8 -*-

# I have put a comment on where you need to write the code. 
import copy
import queue
import math

initial_state = [[1, 5, 4],
                 [8, 2, -1],
                 [3, 7, 6]]

final_state = [[-1, 1, 2],
               [3, 4, 5],
               [6, 7, 8]]


class State(object):  # don't change this class
    def __init__(self, matrix):
        self.matrix = matrix
        self.f = 0
        self.g = 0
        self.h = 0

    def __lt__(self, other):
        return self.f < other.f

    def __repr__(self):
        return str(self.matrix[0]) + "\n" + str(self.matrix[1]) + "\n" + str(self.matrix[2])


def create_child(parent_state, move):
    i = 0
    j = 0
    found = False
    
    matrix = copy.deepcopy(parent_state)
    for i in range(0, 3):
        for j in range(0, 3):
            if parent_state[i][j] == -1:
                r=i
                c=j
                found = True
                break
        if found:
            break

    if move == "left":
        # write code for the left move from the parent state and return the new matrix;
        # check whether it's a valid move. for invalid move return -1
        if c-1==-1 :
          return -1
        matrix[r][c] ,matrix[r][c-1] = matrix[r][c-1] , matrix[r][c]
        #print(matrix)

        return matrix
        

    if move == "right":
        # write code for the right move from the parent state and return the new matrix;
        # check whether it's a valid move. for invalid move return -1
        if c+1==3: 
          return -1
        matrix[r][c] ,matrix[r][c+1] = matrix[r][c+1] , matrix[r][c]
        #print(matrix)
        return matrix
        

    if move == "up":
        # write code for the up move from the parent state and return the new matrix;
        # check whether it's a valid move. for invalid move return -1
        if r-1==-1:
          return -1
        matrix[r][c] ,matrix[r-1][c] = matrix[r-1][c] , matrix[r][c]
        #print(matrix)
 
        return matrix
        

    if move == "down":
        # write code for the down move from the parent state and return the new matrix;
        # check whether it's a valid move. for invalid move return -1
        if r+1==3:
          return -1
        matrix[r][c] ,matrix[r+1][c] = matrix[r+1][c] , matrix[r][c]
        #print(matrix)
     
        return matrix
        


def heuristic1(current_matrix):
    distance = 0
    # write code for calculating heuristic one: misplaced tiles and return the calculated value
    
    for i in range(0, 3):
      for j in range(0, 3): 
        if final_state[i][j] != current_matrix[i][j] :
          distance+=1
    
    return distance


def heuristic2(current_matrix):
    #distance = 0
    # write code for heuristic two: sum of euclidean distances
    h2 =0
    for i in range(0, 3):
      for j in range(0, 3): 
        if current_matrix[i][j] != -1 :
          if current_matrix[i][j]==1:
            h2+=math.sqrt(((i-0)**2) +((j-1)**2) )
          elif current_matrix[i][j]==2:
            h2+=math.sqrt( ((i-0)**2) +((j-2)**2))
          elif current_matrix[i][j]==3:
            h2+=math.sqrt( ((i-1)**2) +((j-0)**2))
          elif current_matrix[i][j]==4:
            h2+=math.sqrt( ((i-1)**2) +((j-1)**2))
          elif current_matrix[i][j]==5:
            h2+=math.sqrt( ((i-1)**2) +((j-2)**2))
          elif current_matrix[i][j]==6:
            h2+=math.sqrt( ((i-2)**2) +((j-0)**2))
          elif current_matrix[i][j]==7:
            h2+=math.sqrt( ((i-2)**2) +((j-1)**2))
          else:
            h2+=math.sqrt( ((i-2)**2) +((j-2)**2))
          
    return h2
    #return distance

def isGoal(matrix):
    for i in range(0,3):
        for j in range(0,3):
            if matrix[i][j] != final_state[i][j]:
                return False
    return True

def findh(choice) :
  unexplored = queue.PriorityQueue()  # step 1: declaring an open list
  explored = []  # step 2: declaring a closed list
  state_list=[]   #this list will be used for checking whether new matrix is or was already in the open list or not 

  # step 3: inserting initial state to the open list

  current_state = State(initial_state)
  current_state.g = 0
  if choice==1:
    current_state.h = heuristic1(current_state.matrix)
  elif choice==2 :
    current_state.h = heuristic2(current_state.matrix)
  current_state.f = current_state.g + current_state.h
  
  unexplored.put(current_state, current_state.f)
  state_list.append(current_state)

  # step 4: while open list is not empty

  while not unexplored.empty():
    # write code for step 4(a) and 4(b): pop the state with minimum f using unexplored.get()
    current_state = unexplored.get()
    possible_movements = ["up", "left", "down", "right"]

    # complete code for step 4(c)
    for move in possible_movements:
      # check if the number of move exceeds 31. If it is, the given state is not considered solvable
      if current_state.g > 31:
          print("can't solve")
          return -1
      
      # step 4(c)(i): write code for checking if the new_matrix is the goal_state and if it is, print the number of moves
      check = isGoal(current_state.matrix)
      if check== True:
        #print(current_state.matrix)
        #print("no of moves using h1 : ", current_state.f)
        return current_state.f

      new_matrix = create_child(current_state.matrix, move)
      
      if new_matrix == -1:
        continue

      #if new_matrix != -1:
      new_state=State(new_matrix)
      if choice==1:
        new_state.h= heuristic1(new_state.matrix)
      elif choice==2 :
        new_state.h= heuristic2(new_state.matrix)
      new_state.g=current_state.g+1
      new_state.f = new_state.g + new_state.h
      
      state_list.append(new_state)
      
      #if new_matrix != -1:
          # write code for step 4(c)(ii) and 4(c)(v). step 4(c)(iv) is not needed in this problem. why? 
          #every arg value 1
      
      #print("wrong tiles left : ", new_matrix.h,"  f:",new_matrix.f)

      in_unexplored_list= False
      
      for state in state_list:
        if state.matrix == new_state.matrix :
          if state.f < new_state.f:
              in_unexplored_list= True
      if in_unexplored_list==True :
        continue
        
      unexplored.put(new_state, new_state.f)
      #for loop end
    explored.append(current_state)  #all possible child has been created
  #while loop end
#function end

def inputMatrix():
  for i in range(0,3):
    for j in range(0,3):
      num = int(input()) 
      
      if num!=0 and num>=-1 and num<=8 : 
        initial_state[i][j]=num
      else :
        print("enter new matrix again: ")
        return -1
  
  return 1      


#main
print("Give your initial state")
print("blank space= -1 and values must be within 1 to 8. Don't repeat same values.")
if inputMatrix() ==1 :
  print(initial_state)
  h1=findh(1)
  if h1 != -1:
    print("using h1 no of moves:", h1)
  h2=findh(2)
  if h2 != -1:
    print("using h2 no of moves:", h2)
