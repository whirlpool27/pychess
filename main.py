import constant

def createBoard():
  board = []
  pawn = "P "*8
  white_pieces = "R N B Q K B N R"
  white_pawns = pawn.strip()
  black_pieces = white_pieces.lower()
  black_pawns = pawn.strip().lower()

  board.append(black_pieces.split(" "))
  board.append(black_pawns.split(" "))
  for i in range(4):
    board.append([" "]*8)
  board.append(white_pawns.split(" "))
  board.append(white_pieces.split(" "))

  return board

def display(board):
  print(" : %s"%("a b c d e f g h".split(" ")))
  print("-"*43)
  for index, pieces in enumerate(board):
    row = 8 - index
    print("%s: %s"%(row, pieces))

if __name__ == '__main__':
  board = createBoard()
  display(board)


  