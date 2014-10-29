


import TreeNode
from pickle import *
from BoardNode import *

class Tree():
    #Root Node points to start of tree
    __RootNode = None
    
    #Pointer to Current Node
    __CurrentNode = None
    
    #Working Node
    __WorkingNode = None

    #Set Working to Current
    def GoToCurrentState():
        if (__CurrentNode):
            __WorkingNode = __CurrentNode
            return 0
        else:
            return -1
    #Finds a node that matches a passed in board
    def Find(board):
        if found:
            return node
        else:
            return 0
        
    #Returns list Working's known states and associated stats
    def KnownOptions():
        if (__WorkingNode and __WorkingNode.KnownMovesTaken):
            r = []
            i = 0
            for node in __WorkingNode.KnownMovesTaken:
                r[i] = []
                r[i][0] = node.BoardState 
                r[i][1] = node.NumberOfTimesReached
                r[i][2] = node.NumberOfTimesWhiteWon
                r[i][3] = node.NumberOfTimesDraw
                r[i][4] = node.GameHistory
                i += 1
            return 0
        else:
            return -1

    #Sets Working/Current to Root node
    def ResetState():
        if (__RootNode):
            __WorkingNode = __CurrentNode = __RootNode
            return 0
        else:
            return -1

    #Moves current to wherever NewBoard is or will be
    def UpdateBoard(NewBoard):
        
        return

    def MoveWorkingNode(BoardStat):
        return

    #Initilizes tree's root node with starting board
    def __init__(self):
        #treefile = open('tree.dat','rb')
        #tree = load(treefile)
            
        '''        
        with open("tree.dat") as (f, err):
            if err:
                tree = {}
            else:
                tree = load(f)
           '''
        return

    #updates tree dictionary with statistics
    def update():
        #for BoardNode in gamePath:
            #tree[fen] = 
        return
        
    #adds a boardNode object into the dictionary    
    def addBoardNode(fen):
        b1 = [0,0,0,0]
        data1 = {fen: b1}
        #data1 = {'a': [1, 2.0, 3, 4],'b': [1,2,3],'c': None}
        #selfref_list = [1, 2, 3]
        #selfref_list.append(selfref_list)

        output = open('tree.dat', 'wb')

        # Pickle dictionary using protocol 0.
        dump(data1, output)

        # Pickle the list using the highest protocol available.
        #pickle.dump(selfref_list, output, -1)

        output.close()
        
        return
        
        
    #saves tree dictionary to file
    def save():

        '''
        with open("tree.dat") as (f, err):
            if err:
                print("Can not save data to tree.dat")
            else:
                dump(f)
                '''
        return
        
 



       