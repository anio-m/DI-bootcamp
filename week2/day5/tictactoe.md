<!-- winning_combinations = [
[(0,0),(0,1),(0,2)],
[(1,0),(1,1),(1,2)],
[(2,0),(2,1),(2,2)],
[(0,0),(1,0),(2,0)],
[(0,1),(1,1),(2,1)],
[(0,2),(1,2),(2,2)],
[(0,0),(1,1),(2,2)],
[(0,2),(1,1),(2,0)],
] -->

winning_combinations = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))

---

# game()

- "welcome to the game"
- call displayBoard
  --> maybe a global variable to use it in all the functions
  <!-- board = [
  ["x", "", ""]
  ["x", "o", "o"]
  ["x", "", ""]
  ] -->

    <!-- maybe other way -->

  board_x = ["x", "", "", "x", "x", "x", "", "", ""]

  board_o = ["", "o", "", "", "", "", "", "", ""]

  <!-- board = ["x", "x", "o", "o", "x", "x", "o", "x", "x"] -->

- play the game 9 times, and check if the turn is even or oddd
  if even --> X plays
  if odd --> O plays

- ask the user for his answer
  --> need a while
  --> save the answer in the board only if not empty
  --> if not empty, choose again

- call displayBoard() again
- call check_combination()

---

# displayBoard()

- print the board using a loop

---

# check_combination

- check if a combination in the board is the same as a winning combination - and check if its same the same symbol
- if it's same symbol + same combinaison --> inform the winner

---

--> create other functions if necessary

<!-- board = {
0 : "x",
1 : "o",
2 : "",

} -->
