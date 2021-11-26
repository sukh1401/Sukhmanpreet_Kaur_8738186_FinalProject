class TicTacToe:
    board = []

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

    # HandleTurn
    def handleTurn(self):
        """Prompts the player to choose a move for the game and determines the spot for the current player against the available spots for the game and fills the chosen spot otherwise alerts the user of the spot being already taken
        """
        pass

    # CheckIfGameOver
    def checkIfGameOver(self):
        """The game is over when all the available spots for the game are filled i.e a (tie), or when there is a continuous symbol of the same player across a column, row or diagonal i.e (win).
        """
        pass

    # CheckForWinner
    def checkForWinner(self):
        """Assigns the winner of the game in a row or column or diagonal
        """
        pass

    # CheckRowsWinner
    def checkRows(self):
        """Return the symbol of the winner of the game in a row

        Returns:
            str: returns symbol of the winner of the game in a row
        """
        pass

    # CheckColumnsWinner
    def checkColumns(self):
        """Return the symbol of the winner of the game in a column

        Returns:
            str: the symbol of the winner of the game in a column
        """
        pass

    # CheckDiagonalsWinner
    def checkDiagonals(self):
        """Return the symbol of the winner of the game in a diagonal

        Returns:
            str: the symbol of the winner of the game in a diagonal or None
        """
        pass

    # CheckForTie
    def checkForTie(self):
        """Updates the game state to over when all the available spots for the game are filled, and  there is no winner
        """
        pass

    # FlipPlayer
    def flipPlayer(self):
        """Assign a turn to the player depending on the player who has just played the game
        """
        pass


if __name__ == '__main__':
    app = TicTacToe()
    app.playGame()