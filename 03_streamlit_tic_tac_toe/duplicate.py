import streamlit as st

def game_state(grid_size):
    if "board_size" not in st.session_state:
        st.session_state.board_size = grid_size
        st.session_state.board = [""] * (grid_size * grid_size)
        st.session_state.current_player = "X"
        st.session_state.game_over = False
        st.session_state.winner = None
        return
    
    if st.session_state.board_size != grid_size:
        st.session_state.board_size = grid_size
        st.session_state.board = [""] * (grid_size * grid_size)
        st.session_state.current_player = "X"
        st.session_state.game_over = False
        st.session_state.winner = None


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
    N = st.session_state.board_size
    board = st.session_state.board

    for row in range(N):
        cols = st.columns(N, gap="small")
        for col in range(N):
            index = row * N + col
            symbol = board[index]
            display_symbol = "❌" if symbol == "X" else ("⭕" if symbol == "O" else " ")
            with cols[col]:
                if st.button(display_symbol, key=f"cell_{index}", use_container_width=True):
                    if symbol == "" and not st.session_state.game_over:
                        board[index] = st.session_state.current_player
                        check_winner(size=N)
                        if not st.session_state.game_over:
                            switch_player()
                        st.rerun()
                    else:
                        st.warning("Cell already filled!")
                    

def check_winner(size=3):
    board = st.session_state.board
    N = size

    # -- rows --
    for r in range(N):
        row = [r * N + c for c in range(N)]
        values = [board[i] for i in row]
        if values[0] != "" and all(v == values[0] for v in values):
            st.session_state.game_over = True
            st.session_state.winner = values[0]
            return
        
    # -- columns --
    for c in range(N):
        col = [c + N * r for r in range(N)]
        values = [board[i] for i in col]
        if values[0] != "" and all(v == values[0] for v in values):
            st.session_state.game_over = True
            st.session_state.winner = values[0]
            return
        
    # -- main diagonal --
    diag1 = [i + (N + 1) for i in range(N)]
    values = [board[i] for i in diag1]
    if values[0] != "" and all(v == values[0] for v in values):
        st.session_state.game_over = True
        st.session_state.winner = values[0]
        return
    
    # -- anti-diagonal --
    diag2 = [(i + 1) + (N - 1) for i in range(N)]
    values = [board[i] for i in diag2]
    if values[0] != "" and all(v == values[0] for v in values):
        st.session_state.game_over = True
        st.session_state.winner = values[0]
        return
    
    # -- draw --
    if all(cell != "" for cell in board):
        st.session_state.game_over = True
        st.session_state.winner = "Draw"


def reset_game(grid_size):
    st.session_state.board_size = grid_size
    st.session_state.board = [""] * (grid_size * grid_size)
    st.session_state.current_player = "X"
    st.session_state.winner = None
    st.session_state.game_over = False


def switch_player():
    st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"



def main():
    st.title("Tic-Tac-Toe Game")

    grid_size = st.selectbox("Choose board size: ", [3, 4, 5], index=0)

    game_state(grid_size)
    display_board()


    if st.session_state.winner:
        if st.session_state.winner == "Draw":
            st.success("It's a draw")
        else:
            st.success(f"Player {st.session_state.winner} wins!")

    if st.button("Play Again"):
        reset_game(st.session_state.board_size)
        st.rerun()

    st.write("Current Player: ", st.session_state.current_player)


if __name__ == '__main__':
    main()