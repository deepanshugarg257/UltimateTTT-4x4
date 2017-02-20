# 0 -> empty ; 1-> X ; 2->O
#player 1 -1
from __future__ import print_function
import copy

class Player1:

    def __init__(self):
        self.termVal = 100
        self.limit = 3
        self.count = 0

    def heuristic(self,old_move):
        return (50,old_move)

    def dfs(self,board,old_move,flag,depth):
        if(board.find_terminal_state()[0] == flag):
            return (self.termVal,old_move)
        if(board.find_terminal_state()[0] == 'x' or board.find_terminal_state()[0] == 'o'):
            return (-1*self.termVal,old_move)
        if(board.find_terminal_state()[0] == 'NONE' or depth > self.limit):
            return self.heuristic(old_move)
        cells = board.find_valid_move_cells(old_move)
        nodeVal = -5*self.termVal
        toMark = [-1,-1]
        for chosen in cells :
            # print(chosen)
            new = 'x'
            if(flag == 'x'):
                new = 'o'
            tmp = copy.deepcopy(board.block_status)
            board.update(old_move,chosen,flag)
            tmp1 = self.dfs(board,chosen,new,depth+1)
            if(nodeVal<tmp1[0]):
                nodeVal = tmp1[0]
                toMark[0] = chosen[0]
                toMark[1] = chosen[1]
            board.board_status[chosen[0]][chosen[1]] = '-'
            board.block_status = copy.deepcopy(tmp)
            del(tmp)
        return (nodeVal,toMark)

    def move(self,board,old_move,flag):
        print("hey")
        self.count+=1
        print("entering the move for ",self.count)
        toret = self.dfs(board,old_move,flag,1)[1]
        print(toret)
        return toret[0],toret[1]
