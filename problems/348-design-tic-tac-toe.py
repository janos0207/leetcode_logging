# https://leetcode.com/problems/design-tic-tac-toe/description/

# time O(N), space O(N^2)
class TicTacToe:
    def __init__(self, n: int):
        self.board = [[0] * n for _ in range(n)]
        self.n = n

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        if all(self.board[row][i] == player for i in range(self.n)) or \
                all(self.board[i][col] == player for i in range(self.n)):
            return player
        if row == col and all(self.board[i][i] == player for i in range(self.n)):
            return player
        if row + col == self.n-1 and all(self.board[i][self.n-i-1] == player for i in range(self.n)):
            return player
        return 0


# time O(1), space O(N)
class TicTacToe2:
    def __init__(self, n: int):
        self.n = n
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        p = 1 if player == 1 else -1
        self.rows[row] += p
        self.cols[col] += p
        if row == col:
            self.diagonal += p
        if row + col == self.n-1:
            self.anti_diagonal += p
        if abs(self.rows[row]) == self.n or abs(self.cols[col]) == self.n or \
                abs(self.diagonal) == self.n or abs(self.anti_diagonal) == self.n:
            return player
        return 0
