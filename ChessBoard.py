import numpy as np
import matplotlib.pyplot as plt

#creating a 8x8 matrix with zeros
ChessBoard=np.zeros((8,8))

#initializing 1 to the chessboard
ChessBoard[1::2,0::2]=1
ChessBoard[0::2,1::2]=1
plt.imshow(ChessBoard,cmap="binary")
plt.show()
