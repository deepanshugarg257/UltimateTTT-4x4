# 0 -> empty ; 1-> X ; 2->O
#player 1 -1
from __future__ import print_function
import copy
import random

class Player1:

    def __init__(self):
        self.termVal = 100
        self.limit = 5
        self.count = 0

    def heuristic(self, old_move):
        return (50, old_move)

    def alphaBeta(self, board, old_move, flag, depth, alpha, beta):
        # Assuming 'x' to be the maximising player
        
        if(board.find_terminal_state()[0] == 'x'):
            return (self.termVal, old_move)
        
        if(board.find_terminal_state()[0] == 'o'):
            return (-1*self.termVal, old_move)
        
        if(board.find_terminal_state()[0] == 'NONE' or depth > self.limit):
            return self.heuristic(old_move)
        
        cells = board.find_valid_move_cells(old_move)
        random.shuffle(cells)
        #print (cells)
        
        if (flag == 'x'):
            
            nodeVal = -5*self.termVal, (-1,-1)
            new = 'o'
            tmp = copy.deepcopy(board.block_status)
            
            for chosen in cells :
                board.update(old_move, chosen, flag)
                tmp1 = self.alphaBeta(board, chosen, new, depth+1, alpha, beta)
                board.board_status[chosen[0]][chosen[1]] = '-'
                board.block_status = copy.deepcopy(tmp)
                
                if(nodeVal[0] < tmp1[0]):
                    nodeVal = tmp1[0], chosen
                    alpha = max(alpha, nodeVal[0])
                    if beta <= alpha :
                        break
                del(tmp1)
            del(tmp)
                
            return nodeVal


        if (flag == 'o'):
            
            nodeVal = 5*self.termVal, (-1,-1)
            new = 'x'
            tmp = copy.deepcopy(board.block_status)
            
            for chosen in cells :
                board.update(old_move, chosen, flag)
                tmp1 = self.alphaBeta(board, chosen, new, depth+1, alpha, beta)
                board.board_status[chosen[0]][chosen[1]] = '-'
                board.block_status = copy.deepcopy(tmp)
                
                if(nodeVal[0] > tmp1[0]):
                    nodeVal = tmp1[0], chosen
                    beta = min(beta, nodeVal[0])
                    if beta <= alpha :
                        break
                del(tmp1)
            del(tmp)
                
            return nodeVal


    def move(self, board, old_move, flag):
        print("hey")
        self.count += 1
        print("entering the move for ", self.count)
        toret = self.alphaBeta(board, old_move, flag, 1, -1000, 1000)[1]
        print("toret",toret)
        return toret[0], toret[1]
