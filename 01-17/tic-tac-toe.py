wins = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

for pozice in wins:
    jedna, dva, tri = pozice
    board="  X X X  "
    if board[jedna - 1] == board[dva - 1] and board[jedna - 1] == board[tri - 1] and board[jedna - 1] != " ":
        print("victory, vyhrál", board[jedna - 1])
        break # nebo return pokud chci ukončit funkci

def funkce():
    a = 5

funkce()

print(a)