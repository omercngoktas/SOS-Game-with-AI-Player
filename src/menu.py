
from board import Board
from minimax import Minimax_Alpha_Beta
from player import Player

def create_board():
    board_height = int(input("Please specify the board's height (1-10): "))
    board_width = int(input("Please specify the board's width (1-10): "))
    board = Board(board_height, board_width)
    board.create_board()
    board.print_board()
    return board

def display_welcome():
    print("Welcome to the Game!")

def display_menu():
    print("Please select an option:")
    print("1. Human vs AI")
    print("2. AI vs AI")
    print("3. Human vs Human")
    print("4. Exit")

def get_user_choice():
    choice = input("Enter your choice (1-4): ")
    return choice

def play_the_game():
    while True:
        board = create_board()
        minimax = Minimax_Alpha_Beta(board)
        display_menu()
        choice = get_user_choice()

        if choice == "1":
            print("You selected Human vs AI")
            ai_depth = int(input("Please specify the AI's depth (1-10): "))
            ai_type = input("Please specify the AI's type (max/min): ")
            ai_player = Player(ai_type, ai_depth, minimax, board)
            human_score = 0
            
            while not board.is_game_over():
                ai_player.play()
                board.print_board()
                if board.is_game_over(): break
                
                is_valid_move = False
                while not is_valid_move:
                    row = int(input("Please enter the row: "))
                    col = int(input("Please enter the column: "))
                    value = input("Please enter the value: ")
                    is_valid_move = board.check_if_move_is_valid(row, col)
                    if not is_valid_move:
                        print("Invalid move. Please try again.")
                
                gained_score = board.check_score_for_move(row, col, value)
                board.move(row, col, value)
                human_score += len(gained_score) if gained_score != None else 0
                board.print_board()
            
            ai_player_score = ai_player.get_score()
            if human_score == ai_player_score:
                print("It's a tie!")
                print(f"Human player score: {human_score}")
                print(f"AI ({ai_player.player_type}) player score: {ai_player_score}")
                
            else:
                print(f"Human player won!!!" if human_score > ai_player_score else f"AI ({ai_player.player_type}) player won!!!")
                print(f"Human player score: {human_score}")
                print(f"AI ({ai_player.player_type}) player score: {ai_player_score}")
            break
            
            
        elif choice == "2":
            print("You selected AI vs AI")
            ai_player1_depth = int(input("Please specify the AI-1's depth (1-10): "))
            ai_player1_type = input("Please specify the AI-1's type (max/min): ")
            ai_player1 = Player(ai_player1_type, ai_player1_depth, minimax, board)
            ai_player2_depth = int(input("Please specify the AI-2's depth (1-10): "))
            ai_player2_type = input("Please specify the AI-2's type (max/min): ")
            ai_player2 = Player(ai_player2_type, ai_player2_depth, minimax, board)
            while not board.is_game_over():
                ai_player1.play()
                board.print_board()
                if board.is_game_over():
                    break
                ai_player2.play()
                board.print_board()
            
            ai_player1_score = ai_player1.get_score()
            ai_player2_score = ai_player2.get_score()
            print(f"AI-1 ({ai_player1.player_type}) player score: {ai_player1_score}")
            print(f"AI-2 ({ai_player2.player_type}) player score: {ai_player2_score}")
            if ai_player1_score == ai_player2_score:
                print("It's a tie!")
                print(f"AI-1 ({ai_player1.player_type}) player score: {ai_player1_score}")
                print(f"AI-2 ({ai_player2.player_type}) player score: {ai_player2_score}")
            else:
                print(f"AI-1 ({ai_player1.player_type}) player won!!!" if ai_player1_score > ai_player2_score else f"AI-2 ({ai_player2.player_type}) player won!!!")
            break
            

        elif choice == "3":
            print("You selected Human vs Human")
            human1_score = 0
            human2_score = 0
            while not board.is_game_over():
                is_valid_move = False
                while not is_valid_move:
                    print("Human-1's turn:")
                    row = int(input("Please enter the row: "))
                    col = int(input("Please enter the column: "))
                    value = input("Please enter the value: ")
                    is_valid_move = board.check_if_move_is_valid(row, col)
                    if not is_valid_move:
                        print("Invalid move. Please try again.")
                
                gained_score = board.check_score_for_move(row, col, value)
                board.move(row, col, value)
                human1_score += len(gained_score) if gained_score != None else 0
                board.print_board()
                if board.is_game_over(): break
                
                is_valid_move = False
                while not is_valid_move:
                    print("Human-2's turn:")
                    row = int(input("Please enter the row: "))
                    col = int(input("Please enter the column: "))
                    value = input("Please enter the value: ")
                    is_valid_move = board.check_if_move_is_valid(row, col)
                    if not is_valid_move:
                        print("Invalid move. Please try again.")
                
                gained_score = board.check_score_for_move(row, col, value)
                board.move(row, col, value)
                human2_score += len(gained_score) if gained_score != None else 0
                board.print_board()
            
            print("Human-1 player score: " + str(human1_score))
            print("Human-2 player score: " + str(human2_score))
            if human1_score == human2_score:
                print("It's a tie!")
            else:
                print("Human-1 player won!!!" if human1_score > human2_score else "Human-2 player won!!!")
            
            break
            

        elif choice == "4":
            print("Exiting the game...")
            break

        else:
            print("Invalid choice. Please try again.")
