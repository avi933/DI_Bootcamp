theBoard = {'1-1': ' ', '1-2': ' ', '1-3': ' ',
            '2-1': ' ', '2-2': ' ', '2-3': ' ',
            '3-1': ' ', '3-2': ' ', '3-3': ' '}


def win():
  if theBoard['1-1'] == theBoard['1-2'] == theBoard['1-3'] != ' ':
    return True
  if theBoard['2-1'] == theBoard['2-2'] == theBoard['2-3'] != ' ':
    return True
  if theBoard['3-1'] == theBoard['3-2'] == theBoard['3-3'] != ' ':
    return True
  if theBoard['1-1'] == theBoard['2-1'] == theBoard['3-1'] != ' ':
    return True
  if theBoard['1-2'] == theBoard['2-2'] == theBoard['3-2'] != ' ':
    return True
  if theBoard['1-3'] == theBoard['2-3'] == theBoard['3-3'] != ' ':
    return True
  if theBoard['1-1'] == theBoard['2-2'] == theBoard['3-3'] != ' ':
    return True
  if theBoard['1-3'] == theBoard['2-2'] == theBoard['3-3'] != ' ':
    return True
  return False
  



def printBoard(board):
    print("******************")
    print("*  " + board['1-1'] + '  |  '+board['1-2']+'  | '+board['1-3'] + "  *")
    print('* --- + --- + ---*')
    print("*  "+board['2-1'] + '  |  '+board['2-2']+'  | ' + board['2-3']+"  *")
    print("* --- + --- + ---*")
    print("*  "+board['3-1'] + '  |  '+board['3-2']+'  | ' + board['3-3']+"  *")
    print("******************")
printBoard(theBoard)
for x in range(9):
  t = input("enter position in form 1-1 or 3-2 \n")
  if theBoard[t] == " ":
     theBoard[t] = "x" if x%2 ==0 else "o"
  else:
     print("Space already occupied, try another space \n")  
  printBoard(theBoard)
  if  win() :
    print("you won")
    break
else: 
  print("It's a tie")

