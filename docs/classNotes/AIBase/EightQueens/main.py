import numpy as np           # 提供维度数组与矩阵运算
import copy                  # 从copy模块导入深度拷贝方法
from board import Chessboard

# 基于棋盘类，设计搜索策略
class Game:
    def __init__(self, show = True):
        """
        初始化游戏状态.
        """

        self.chessBoard = Chessboard(show)
        self.solves = []
        self.gameInit()

    # 重置游戏
    def gameInit(self, show = True):
        """
        重置棋盘.
        """

        self.Queen_setRow = [-1] * 8
        self.chessBoard.boardInit(False)

    ##############################################################################
    ####                请在以下区域中作答(可自由添加自定义函数)                 ####
    ####              输出：self.solves = 八皇后所有序列解的list                ####
    ####             如:[[0,6,4,7,1,3,5,2],]代表八皇后的一个解为                ####
    ####           (0,0),(1,6),(2,4),(3,7),(4,1),(5,3),(6,5),(7,2)            ####
    ##############################################################################
    #                                                                            #

    def storeChessBoard(self):
        """
        Store the current chessboard state.
        """

        return copy.deepcopy(self.chessBoard.chessboardMatrix), copy.deepcopy(self.chessBoard.queenMatrix), copy.deepcopy(self.chessBoard.unableMatrix), copy.deepcopy(self.chessBoard.printMatrix)

    def backtrack(self, row, solution):
        """
        Backtracking search for Eight Queens Problem.
        """
        
        if row == 8:
            self.solves.append(solution[:])
            return

        for col in range(8):

            if col == 0:
                nowChessBoardMatrix, nowQueenMatrix, nowUnableMatrix, nowPrintMatrix = self.storeChessBoard()
            
            self.chessBoard.chessboardMatrix = copy.deepcopy(nowChessBoardMatrix)
            self.chessBoard.queenMatrix = copy.deepcopy(nowQueenMatrix)
            self.chessBoard.unableMatrix = copy.deepcopy(nowUnableMatrix)
            self.chessBoard.printMatrix = copy.deepcopy(nowPrintMatrix)
            if self.chessBoard.setQueen(row, col, False):
                solution[row] = col
                self.backtrack(row + 1, solution)
                
    def run(self, row=0):
        """
        Eight Queens Problem.
        """
        if row < 0:
            return
        
        solution = [-1] * 8

        self.backtrack(row, solution)

    #                                                                            #
    ##############################################################################
    #################             完成后请记得提交作业             #################
    ##############################################################################

    def showResults(self, result):
        """
        结果展示.
        """

        self.chessBoard.boardInit(False)
        for i,item in enumerate(result):
            if item >= 0:
                self.chessBoard.setQueen(i,item,False)

        self.chessBoard.printChessboard(False)

    def get_results(self):
        """
        输出结果(请勿修改此函数).
        return: 八皇后的序列解的list.
        """

        self.run()
        return self.solves
    
    def printCurrentBoard(self, Board):
        '''
        Print the current chessboard.
        '''

        for i in range(9):
            for j in range(9):
                if i+j==0:
                    print('  ', end='')
                elif (i==0 and j!=8) or j==0 :
                    print(str(Board[i][j])+' ', end='')
                elif i==0 and j==8:
                    print(str(Board[i][j])+' ')
                elif j!=8:
                    print(self.MyTrans(Board[i][j])+' ', end='')
                else:
                    print(self.MyTrans(Board[i][j])+' ')

    def MyTrans(self, x):
        '''
        棋盘绘制字符转换
        '''

        return{0:'-',-1:'x',1:'o'}.get(x)

if __name__ == "__main__":
    game = Game()
    solutions = game.get_results()
    print('There are {} results.'.format(len(solutions)))
    game.showResults(solutions[0])
