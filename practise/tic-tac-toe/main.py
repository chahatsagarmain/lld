import sys
from board_builder import BoardBuilder
from strategy import DefaultStrategy

def main():
    print("====================================")
    print("       WELCOME TO TIC TAC TOE       ")
    print("====================================")
    
    # 1. Get Board Size
    n = 3
    while True:
        try:
            n_input = input("Enter board size (default 3, minimum 3): ").strip()
            if not n_input:
                break
            n = int(n_input)
            if n >= 3:
                break
            else:
                print("Board size must be at least 3. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            
    # 2. Get Player 1 Symbol
    char_first = "X"
    while True:
        char_input = input("Player 1, choose your symbol (X or O, default X): ").strip().upper()
        if not char_input:
            break
        if char_input in {"X", "O"}:
            char_first = char_input
            break
        else:
            print("Invalid symbol. You must choose 'X' or 'O'.")
            
    char_second = "O" if char_first == "X" else "X"
    print(f"Player 2 symbol automatically set to: {char_second}")
    
    # 3. Build Board and Strategy
    builder = BoardBuilder()
    builder.set_board_size(n)
    builder.set_player_char(1, char_first)
    builder.set_player_char(2, char_second)
    
    board = builder.build_board()
    strategy = DefaultStrategy()
    
    # 4. Start Game
    try:
        board.start_game(strategy)
    except KeyboardInterrupt:
        print("\n\nGame interrupted. Goodbye!")
        sys.exit(0)

if __name__ == "__main__":
    main()
