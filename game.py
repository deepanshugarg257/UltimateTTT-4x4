# 0 -> empty ; 1-> X ; 2->O
#player 1 -1

from __future__ import print_function
import random

class Player1:
    size = 2
    termVal = 1000
    limit = 5
    board = [[[[0]*size for i in range(size)] for j in range(size)] for k in range(size)]

    def ifComp(x,y):
        a = (size*x+y)
        if(a or -a in compBlocks):
            return 1
        return 0


    def check(x,y,i,j,player,compBlocks):
        count[x][y]+=1
        if(count[x][y]==size*size)
            compBlocks.append((size*x+y)*player)
        flag = player*(size*2)
        if(i==j):
            for tmp in xrange(size):
                flag -= (board[x][y][tmp][tmp]) + player
        if(flag==0):
            compBlocks.append((size*x+y)*player)
            return
        flag = player*(size*2)
        if(i+j==size-1):
            for tmp in xrange(size):
                flag -= (board[x][y][tmp][size-1-tmp]) + player
        if(flag==0):
            compBlocks.append(((size*x+y)*player)*player)
            return
        flag = player*(size*2)
        for tmp in xrange(size):
            flag -= (board[x][y][i][tmp]) + player
        if(flag==0):
            compBlocks.append(((size*x+y)*player)*player)
            return
        flag = player*(size*2)
        for tmp in xrange(size):
            flag -= (board[x][y][tmp][j]) + player
        if(flag==0):
            compBlocks.append(((size*x+y)*player)*player)
            return

    def checkTerminate(compBlocks):
        row = [0 for i in xrange(size)]
        column = [0 for i in xrange(size)]
        diagnol1,diagnol2 = 0,0

        for block in compBlocks:
            tmp1 = block/size
            tmp2 = block%size
            row[tmp1]+=1
            column[tmp2]+=1
            if(tmp1==tmp2):
                diagnol1+=1
            if(tmp1+tmp2 == size-1)
                diagnol2+=1
        if(4 in row or 4 in column or diagnol1 == 4 or diagnol2 == 4):
            return termVal
        return 0

    def heuristic():
        return termVal/2

    def getPosMoves():
        

    def dfs(player, x, y, depth, compBlocks, alpha, beta):

        if (depth <= 0)
            return heuristic()

        a = checkTerminate(compBlocks)
        if(a!=0):
            return a*player

        if(depth > limit)
            return heuristic()

        nodeVal = -1*player*termVal
        # if(BlockComp(x,y)):
        #     for i in xrange(size):
        #         for j in xrange(size):
        #             if(!BlockComp(i,j)):
        #                 nodeVal = player*max(player*val,player*dfs(player,i,j,depth,compBlocks)
        #The move should be randomly chosen among the allowed moves to get the average runtime.
        posMoves = getPosMoves()
        random.shuffle(posMoves)
        nodeVal = -1*player*termVal

        # for i in xrange(size):
        #     for j in xrange(size):
        #         if(board[x][y][i][j]==0):
        #             board[x][y][i][j] = player
        #             check(x,y,i,j,player)
        #             nodeVal = player*max(player*val,player*dfs(0-player,i,j,depth+1,compBlocks))
        #             board[x][y][i][j] = 0

        #Posmoves will have the x*(size)+y
        for move in posMoves:
            board[move/size][move%size] = player


        return nodeVal


dfs(1,size/2,size/2,1,[])
