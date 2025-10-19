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
    cols = st.columns(3)

    for i in range(9):
        col_index = i % 3
        row_index = i // 3

        with cols[col_index]:
            if st.button(st.session_state.board[i] or " ", key=f"cell_{i}"):
                if st.session_state.board[i] == "" and not st.session_state.game_over:
                    st.session_state.board[i] = st.session_state.current_player
                    switch_player()

def check_winner():
    winning_comb = [
        ## rows
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        ## columns
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        ## diagonals
        [0, 4, 8],
        [2, 4, 6],
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


def switch_player():
    st.session_state.current_player = "0" if st.session_state.current_player == "X" else "X"



def main():
    st.title("Tic-Tac-Toe Game")

    game_state()
    display_board()

    if st.session_state.winner:
        if st.session_state.winner == "Draw":
            st.success("It's a draw")
        else:
            st.success(f"Player {st.session_state.winner} wins!")



    st.write("Current Player: ", st.session_state.current_player)


if __name__ == '__main__':
    main()