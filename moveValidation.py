import constant

# TEMPORARY FILE TO GET ALGORITHM, WILL TURN THIS INTO "INTERFACE"
# AND CREATE EACH PIECES INTO DIFFERENT FILE OF IMPLEMENTED INTERFACE

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
  if end_piece in white_pieces:
    return False
  if origin_piece == 'P':
    # move forward
    # can only move 2 blocks
    if row_diff > 0 and row_diff <= 2 and column_diff < 2:
      if row_diff == 2 and column_diff == 1:
        return False
      elif row_diff == 1 and column_diff == 1 and (end_piece == " "):
        return False
      elif row_diff == 2 and origin_row != constant.row["2"]:
        return False
      elif row_diff == 1 and column_diff == 0 and end_piece != " ":
        return False
    else:
      return False
  elif origin_piece == 'R':
    if (abs(row_diff) > 0 and abs(column_diff) > 0):
      return False
    else:
      if row_diff == 0:
        if column_diff > 0:
          i = origin_column + 1
          while i < end_column:
            if board[origin_row][i] != " ":
              return False
            i += 1
        else:
          i = origin_column - 1
          while i > end_column:
            if board[origin_row][i] != " ":
              return False
            i -= 1
      else: # column diff == 0
        if row_diff > 0:
          i = origin_row - 1
          while i > end_row:
            if board[i][origin_column] != " ":
              return False
            i -= 1
        else:
          i = origin_row + 1
          while i < end_row:
            if board[i][origin_column] != " ":
              return False
            i += 1
  elif origin_piece == 'N':
    if not((abs(row_diff) == 2 and abs(column_diff) == 1) or (abs(row_diff) == 1 and abs(column_diff) == 2)):
      return False
  elif origin_piece == 'B':
    if not(abs(row_diff) == abs(column_diff)):
      return False
    
    if row_diff > 0:
      if column_diff > 0:
        i = origin_row - 1
        j = origin_column + 1
        while i > end_row:
          if board[i][j] != " ":
            return False
          i -= 1
          j += 1
      else:
        i = origin_row - 1
        j = origin_column - 1
        while i > end_row:
          if board[i][j] != " ":
            return False
          i -= 1
          j -= 1
      
    if row_diff < 0:
      if column_diff > 0:
        i = origin_row + 1
        j = origin_column + 1
        while i < end_row:
          if board[i][j] != " ":
            return False
          i += 1
          j += 1
      else:
        i = origin_row + 1
        j = origin_column - 1
        while i < end_row:
          if board[i][j] != " ":
            return False
          i += 1
          j -= 1
      
  elif origin_piece == 'Q':
    if not(abs(row_diff) == abs(column_diff)) and not(row_diff == 0 or column_diff == 0):
      return False
    
    if row_diff > 0:
      if column_diff > 0:
        i = origin_row - 1
        j = origin_column + 1
        while i > end_row:
          if board[i][j] != " ":
            return False
          i -= 1
          j += 1
      elif column_diff < 0:
        i = origin_row - 1
        j = origin_column - 1
        while i > end_row:
          if board[i][j] != " ":
            return False
          i -= 1
          j -= 1
      else:
        i = origin_row - 1
        while i > end_row:
          print (board[i][origin_column] != " ")
          if board[i][origin_column] != " ":
            print(i, end_row)
            return False
          i -= 1
    if row_diff < 0:
      i = origin_row + 1
      if column_diff > 0:        
        j = origin_column + 1
        while i < end_row:
          if board[i][j] != " ":
            return False
          i += 1
          j += 1
      elif column_diff < 0:
        j = origin_column - 1
        while i < end_row:
          if board[i][j] != " ":
            return False
          i += 1
          j -= 1
      else: # column_diff == 0
        while i < end_row:
          if board[i][origin_column] != " ":
            return False
          i += 1
    else: # row_diff == 0
      if column_diff > 0:
        i = origin_column + 1
        while i < end_column:
          if board[origin_row][i] != " ":
            return False
          i += 1
      elif column_diff < 0:
        i = origin_column - 1
        while i > end_column:
          if board[origin_row][i] != " ":
            return False
          i -= 1

  return True