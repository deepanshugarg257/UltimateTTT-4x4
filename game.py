# 0 -> empty ; 1-> X ; 2->O
#player 1 -1
from __future__ import print_function
import copy

class Player1:

    def __init__(self):
        self.termVal = 100
        self.limit = 4

    def heuristic(self,old_move):
        return (50,old_move)

    def dfs(self,board,old_move,flag,depth):
        # print("old move : ",old_move)
        if(board.find_terminal_state()[0] == flag):
            print("returning move" , old_move)
            return (self.termVal,old_move)
        elif(board.find_terminal_state()[0] == 'x' or board.find_terminal_state()[0] == 'o'):
            print("returning move elif 1 " , old_move)
            return (-1*self.termVal,old_move)
        elif(depth > self.limit or board.find_terminal_state()[0] == 'NONE'):
            print("returning move elif 2 " , old_move)
            return self.heuristic(old_move)
        cells = board.find_valid_move_cells(old_move)
        print ("cells ", cells)
        #random.shuffle(cells)
        nodeVal = (-1*self.termVal,old_move)
        print("len of cells" , len(cells))
        for chosen in cells :
            print("chosen ",chosen)
            new = 'x'
            if(flag == 'x'):
                new = 'o'
            tmp = copy.deepcopy(board.block_status)
            board.update(old_move,chosen,flag)
            # print("hi")
            tmp1 = self.dfs(board,chosen,new,depth+1)
            if(nodeVal[0]<tmp1[0]):
                nodeVal[0] = tmp1[0]
                nodeVal[1] = chosen
                # print("updating at level ",level," with ",tmp1)
            board.board_status[chosen[0]][chosen[1]] = '-'
            board.block_status = copy.deepcopy(tmp)
            del(tmp)
        return nodeVal

    def move(self,board,old_move,flag):
        print("hey")
        returnval = self.dfs(board,old_move,flag,1)[1]
        print ("final ", returnval)
        return returnval
