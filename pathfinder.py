import numpy as np

maze_array = [[0, 0, 0, 0, 0],
              [0, 0,-1,-1, 0],
              [0, 0, 0,-1, 0],
              [0, 0,-1,-1, 0],
              [0, 0, 0, 0, 0]]

def find_walls(maze_array: list)->list:
    wall_list = list()
    for x in range(np.size(maze_array,0)):
        for y in range(np.size(maze_array,1)):
            if(maze_array[x][y] == -1):
                wall_list.append(tuple((x,y)))
    return wall_list                

#Also finds diagonal elements(The bot cannot move diagnoally)
def find_neighbours(maze_array: list,coord: tuple,walls: list)->list:
    neighbour_list = list()
    for x in range(-1,2):
        for y in range (-1,2):
            new_coord = tuple((coord[0]+x,coord[1]+y))
            if (new_coord == coord
                or new_coord[0]<0
                or new_coord[1]<0
                or new_coord[0] > (np.size(maze_array,0)-1)
                or new_coord[1] > (np.size(maze_array,1)-1)
                or new_coord in walls):
                continue
            else:
                neighbour_list.append(new_coord)
    return neighbour_list                


#this function does not return diagonal coordinates    
def find_neighbours(coord: tuple, maze_array: list)->list:
    walls = find_walls(maze_array)
    neighbour_list = list()
    neighbour_list_unique = list()
    neighbour_list.append(tuple((coord[0]-1,coord[1])))
    neighbour_list.append(tuple((coord[0],coord[1]-1)))
    neighbour_list.append(tuple((coord[0],coord[1]+1)))
    neighbour_list.append(tuple((coord[0]+1,coord[1])))
    for neighbour_coord in neighbour_list:
        if (neighbour_coord not in walls
        and neighbour_coord[0]>=0
        and neighbour_coord[1]>=0
        and neighbour_coord[0] < (np.size(maze_array,0))
        and neighbour_coord[1] < (np.size(maze_array,1))):
            neighbour_list_unique.append(neighbour_coord)
    return neighbour_list_unique            
      
def unique_list(array: list)->list:
    temp_list = list()
    for element in array:
        if element not in temp_list:
            temp_list.append(element)
    return temp_list            
        
def path_find(maze_array: list, start: tuple)->list:
    stack = list()
    history = list()
    stack.append(start)
    distance_array = maze_array
    count = 0
    while(stack):
        neighbours = []
        not_repeated_neighbours = []
        for coord in stack:
            history.append(coord)
            distance_array[coord[0]][coord[1]] = count
            neighbours.extend(find_neighbours(coord,maze_array))
        for coord in neighbours:
            if coord not in history:
                not_repeated_neighbours.append(coord)
        stack = not_repeated_neighbours                                             
        count +=1
    return distance_array                


if __name__=="__main__":
    start = (2,2)
    print(np.array(maze_array))
    print("---"*20)
    distance_array = path_find(maze_array,start)
    print(np.array(distance_array))






        
    
