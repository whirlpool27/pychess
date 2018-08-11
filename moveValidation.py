import constant

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
      return True
    else:
      return False
  elif origin_piece == 'R':
    if (abs(row_diff) > 0 and abs(column_diff) > 0):
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
  elif origin_piece == 'N':
    print(row_diff, column_diff)
    if not((abs(row_diff) == 2 and abs(column_diff) == 1) or (abs(row_diff) == 1 and abs(column_diff) == 2)):
      return False
  return True