import os
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
  # os.system('cls')
  print(" : %s"%("a b c d e f g h".split(" ")))
  print("-"*43)
  for index, pieces in enumerate(board):
    row = 8 - index
    print("%s: %s"%(row, pieces))

def isValidMove(board, origin, end):
  origin_row = constant.row[origin[1]]
  origin_column = constant.column[origin[0]]
  origin_piece = board[origin_row][origin_column]
  end_row = constant.row[end[1]] 
  end_column = constant.column[end[0]]
  end_piece = board[end_row][end_column]
  row_diff = origin_row - end_row
  column_diff = end_column - origin_column
  white_pieces = "P R N B Q K".split(" ")
  black_pieces = "p r n b q k".split(" ")

  # Check if white moves is valid
  if origin_piece == 'P':
    # move forward
    # can only move 2 blocks
    if row_diff > 0 and row_diff <= 2 and column_diff < 2:
      if row_diff == 2 and column_diff == 1:
        return False
      elif row_diff == 1 and column_diff == 1 and (end_piece == " " or end_piece in white_pieces):
        return False
      elif row_diff == 2 and origin_row != constant.row["2"]:
        return False
      elif row_diff == 1 and column_diff == 0 and end_piece != " ":
        return False
      return True
    else:
      return False
  elif origin_piece == 'R':
    if (abs(row_diff) > 0 and abs(column_diff) > 0) or end_piece in white_pieces:
      return False
    else:
      if row_diff == 0:
        if column_diff > 0:
          index = origin_column + 1
          while index < end_column:
            if board[origin_row][index] != " ":
              return False
            index += 1
        else:
          index = origin_column - 1
          while index > end_column:
            if board[origin_row][index] != " ":
              return False
            index -= 1
      else: # column diff == 0
        if row_diff > 0:
          index = origin_row - 1
          while index > end_row:
            if board[index][origin_column] != " ":
              return False
            index -= 1
        else:
          index = origin_row + 1
          while index < end_row:
            if board[index][origin_column] != " ":
              return False
            index += 1
  return True

def move(board, origin, end):
  origin_piece = board[constant.row[origin[1]]][constant.column[origin[0]]]
  
  if isValidMove(board, origin, end):
    board[constant.row[origin[1]]][constant.column[origin[0]]] = " "
    board[constant.row[end[1]]][constant.column[end[0]]] = origin_piece
  else:
    print("Invalid move!")

  return

if __name__ == '__main__':
  board = createBoard()
  display(board)

  while True:
    userInput = input().lower()
    if userInput == "q":
      exit()
    else:
      moveInput = userInput.split("-")
      move(board,moveInput[0], moveInput[1])
      display(board)




  