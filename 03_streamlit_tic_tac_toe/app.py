import streamlit as st

def game_state():
    if "board" not in st.session_state:
        st.session_state.board = [""] * 9
    
    if "current_player" not in st.session_state:
        st.session_state.current_player = "X"

    if "winner" not in st.session_state:
        st.session_state.winner = None

    if "game_over" not in st.session_state:
        st.session_state.game_over = False

def display_board():
    st.markdown(
        """
        <style>
        div[data-testid="column"] > div > button {
            height: 100px;
            width: 100px;
            font-size: 40px;
            font-weight: bold;
            }
        </style>
        """, unsafe_allow_html=True
    )

    for row in range(3):
        cols = st.columns(3, gap="small")
        for col in range(3):
            index = row * 3 + col
            symbol = st.session_state.board[index]
            display_symbol = "❌" if symbol == "X" else ("⭕" if symbol == "O" else " ")
            with cols[col]:
                if st.button(display_symbol, key=f"cell_{index}"):
                    if symbol == "" and not st.session_state.game_over:
                        st.session_state.board[index] = st.session_state.current_player
                        check_winner()
                        if not st.session_state.game_over:
                            switch_player()
                    else:
                        st.warning("Cell already filled!")
                    

def check_winner():
    winning_comb = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  ## rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  ## columns
        [0, 4, 8], [2, 4, 6]              ## diagonals
    ]
    board = st.session_state.board

    for combo in winning_comb:
        a, b, c = combo
        if board[a] != "" and board[a] == board[b] == board[c]:
            st.session_state.winner = board[a]
            st.session_state.game_over = True
            return
        
    if "" not in board:
        st.session_state.winner = "Draw"
        st.session_state.game_over = True

def reset_game():
    st.session_state.board = [""] * 9
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.game_over = False


def switch_player():
    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"



def main():
    st.title("Tic-Tac-Toe Game")

    game_state()
    display_board()

    if st.session_state.winner:
        if st.session_state.winner == "Draw":
            st.success("It's a draw")
        else:
            st.success(f"Player {st.session_state.winner} wins!")

    if st.button("Play Again"):
        reset_game()

    st.write("Current Player: ", st.session_state.current_player)


if __name__ == '__main__':
    main()