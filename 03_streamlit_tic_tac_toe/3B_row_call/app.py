import streamlit as st

## Functions ##

def game_state():
    if "board" not in st.session_state:
        st.session_state.board = [""] * 9
    
    if "current_player" not in st.session_state:
        st.session_state.current_player = "X"

    if "winner" not in st.session_state:
        st.session_state.winner = None

    if "game_over" not in st.session_state:
        st.session_state.game_over = False




## Main ##

def main():
    print("""This will be one of the next mini projects aside from the image color identifier. 
        Will do in the future after my thesis defense""")



if __name__ == '__main__':
    main()