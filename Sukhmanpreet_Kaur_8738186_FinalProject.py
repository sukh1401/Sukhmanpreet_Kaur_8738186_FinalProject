class TicTacToe:
    """
    A class used to represent a TicTacToe game

    ...

    Attributes
    ----------
    gameStillGoing : bool, default True
        a boolean variable indicating whether the game is still on
    currentPlayer : str, default X
        the symbol of the current player that is playing the game
    winner : str, default None
        the symbol of the winner of the game
    board : list, default spots with "-"
        the board showing the available spots for the game

    Methods
    -------
    display_board()
        Displays the available spots for the game and the already filled spots with symbols of the players if already played.
    playGame()
        Main method to run the game until the game is over
    handleTurn()
        Prompts the player to choose a move for the game and determines the spot for the current player against the available spots for the game and fills the chosen spot
    checkIfGameOver()
        The game is over when all the available spots for the game are filled, or when there is a continuous symbol of the same player across a column, row or diagonal otherwise its a tie.
    checkForWinner()
        Assigns the sysmbol of the winner of the game in a row or column or diagonal
    checkRows()
        Return the symbol of the winner of the game in a row
    checkColumns()
        Return the symbol of the winner of the game in a column
    checkDiagonals()
        Return the symbol of the winner of the game in a diagonal
    checkForTie()
        Updates the game state to over when all the available spots for the game are filled, and  there is no winner
    flipPlayer()
        Assign a turn to the player depending on the player who has just played the game

    """
    board = []
    gameStillGoing = True
    winner=None
    currentPlayer = "X"

    def __init__(self):
         self.board = [
            "-", "-", "-",
            "-", "-", "-",
            "-", "-", "-"
        ]

    # Display Board
    def displayBoard(self):
        """Displays the available spots for the game and the already filled spots with symbols of the players if already played.
        """
        print("|", self.board[0], "|", self.board[1], "|", self.board[2], "|")
        print("|", self.board[3], "|", self.board[4], "|", self.board[5], "|")
        print("|", self.board[6], "|", self.board[7], "|", self.board[8], "|")

    # PlayGame
    def playGame(self):
        """Main method to run the game until the game is over.
        """
        # display board
        self.displayBoard()
        # We will keep the game on play as long as the the state of the gameStillGoing variable is True
        while self.gameStillGoing:
            # handleTurns for the player i.e the spot the player wants to fill
            self.handleTurn()
            # check if the game is over
            self.checkIfGameOver()
            # flip Players turns
            self.flipPlayer()
        # handle logic when the game is over if there is a winner print who the winner is otherwise print a Tie
        if self.winner == "X" or self.winner == "O":
            print(f"{self.winner} won.")
        else:
            print("Tie.")


    # HandleTurn
    def handleTurn(self):
        """Prompts the player to choose a move for the game and determines the spot for the current player against the available spots for the game and fills the chosen spot otherwise alerts the user of the spot being already taken
        """
        # Print who the player's turn is
        print(f"{self.currentPlayer}'s turn")
        # Prompt the player for the position for the spot
        position = input("Choose a position from 1-9:")
        valid = False
        # As long as the player chooses an already filled position or a position value not in the given range, alert the player and prompt again
        while not valid:
            while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                position = input("Innvalid Input! Choose a position from 1-9:")
            position = int(position)-1
            # if the position is in the range, then check if the spot is not filled set valid True to exit the loop for prompting for the position
            if self.board[position] == "-":
                valid = True
            else:
                print("Spot already filled. Go again")
        # the position is okay, fill the board with the player's symbol at that position and display the updated board.
        self.board[position] = f"{self.currentPlayer}"
        self.displayBoard()

    # CheckIfGameOver
    def checkIfGameOver(self):
        """The game is over when all the available spots for the game are filled i.e a (tie), or when there is a continuous symbol of the same player across a column, row or diagonal i.e (win).
        """
        self.checkForWinner()
        self.checkForTie()

    # CheckForWinner
    def checkForWinner(self):
        """Assigns the winner of the game in a row or column or diagonal
        """
        # check rows
        rowWinner = self.checkRows()
        # check columns
        columnWinner = self.checkColumns()
        # check diagonals
        diagonalsWinner = self.checkDiagonals()
        if rowWinner:
            self.winner = rowWinner
        elif columnWinner:
            self.winner = columnWinner
        elif diagonalsWinner:
            self.winner = diagonalsWinner
        else:
            self.winner = None

    # CheckRowsWinner
    def checkRows(self):
        """Return the symbol of the winner of the game in a row

        Returns:
            str: returns symbol of the winner of the game in a row
        """
        row1 = self.board[0] == self.board[1] == self.board[2] != "-"
        row2 = self.board[3] == self.board[4] == self.board[5] != "-"
        row3 = self.board[6] == self.board[7] == self.board[8] != "-"
        if row1 or row2 or row3:
            self.gameStillGoing = False
        if row1:
            return self.board[0]
        elif row2:
            return self.board[3]
        elif row3:
            return self.board[6]
        else:
            return

    # CheckColumnsWinner
    def checkColumns(self):
        """Return the symbol of the winner of the game in a column

        Returns:
            str: the symbol of the winner of the game in a column
        """
        column1 = self.board[0] == self.board[3] == self.board[6] != "-"
        column2 = self.board[1] == self.board[4] == self.board[7] != "-"
        column3 = self.board[2] == self.board[5] == self.board[8] != "-"
        if column1 or column2 or column3:
            self.gameStillGoing = False
        if column1:
            return self.board[0]
        elif column2:
            return self.board[3]
        elif column3:
            return self.board[6]
        else:
            return

    # CheckDiagonalsWinner
    def checkDiagonals(self):
        """Return the symbol of the winner of the game in a diagonal

        Returns:
            str: the symbol of the winner of the game in a diagonal or None
        """
        diagonal1 = self.board[0] == self.board[4] == self.board[8] != "-"
        diagonal2 = self.board[6] == self.board[4] == self.board[2] != "-"
        if diagonal1 or diagonal2:
            self.gameStillGoing = False
        if diagonal1:
            return self.board[0]
        elif diagonal2:
            return self.board[2]
        else:
            return

    # CheckForTie
    def checkForTie(self):
        """Updates the game state to over when all the available spots for the game are filled, and  there is no winner
        """
        if "-" not in self.board:
            self.gameStillGoing = False
        return

    # FlipPlayer
    def flipPlayer(self):
        """Assign a turn to the player depending on the player who has just played the game
        """
        if self.currentPlayer == 'X':
            self.currentPlayer = 'O'
        else:
            self.currentPlayer = 'X'


if __name__ == '__main__':
    app = TicTacToe()
    app.playGame()