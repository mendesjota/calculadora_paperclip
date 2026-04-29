import streamlit as st

def main():
    st.title("Calculadora Simples")
    
    # Initialize session state
    if 'display' not in st.session_state:
        st.session_state.display = '0'
    if 'first_number' not in st.session_state:
        st.session_state.first_number = None
    if 'operation' not in st.session_state:
        st.session_state.operation = None
    if 'waiting_for_second_number' not in st.session_state:
        st.session_state.waiting_for_second_number = False
    
    # Display
    st.text_input("Display", value=st.session_state.display, key="display_input", disabled=True)
    
    # Button layout
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button('7'):
            button_clicked('7')
        if st.button('4'):
            button_clicked('4')
        if st.button('1'):
            button_clicked('1')
        if st.button('C'):
            clear_display()
    
    with col2:
        if st.button('8'):
            button_clicked('8')
        if st.button('5'):
            button_clicked('5')
        if st.button('2'):
            button_clicked('2')
        if st.button('0'):
            button_clicked('0')
    
    with col3:
        if st.button('9'):
            button_clicked('9')
        if st.button('6'):
            button_clicked('6')
        if st.button('3'):
            button_clicked('3')
        if st.button('='):
            calculate_result()
    
    with col4:
        if st.button('+'):
            set_operation('+')
        if st.button('-'):
            set_operation('-')
        if st.button('*'):
            set_operation('*')
        if st.button('/'):
            set_operation('/')

def button_clicked(value):
    if st.session_state.waiting_for_second_number:
        st.session_state.display = value
        st.session_state.waiting_for_second_number = False
    else:
        if st.session_state.display == '0':
            st.session_state.display = value
        else:
            st.session_state.display += value

def clear_display():
    st.session_state.display = '0'
    st.session_state.first_number = None
    st.session_state.operation = None
    st.session_state.waiting_for_second_number = False

def set_operation(op):
    if st.session_state.display:
        st.session_state.first_number = float(st.session_state.display)
        st.session_state.operation = op
        st.session_state.waiting_for_second_number = True

def calculate_result():
    if st.session_state.first_number is not None and st.session_state.operation is not None:
        second_number = float(st.session_state.display)
        if st.session_state.operation == '+':
            result = st.session_state.first_number + second_number
        elif st.session_state.operation == '-':
            result = st.session_state.first_number - second_number
        elif st.session_state.operation == '*':
            result = st.session_state.first_number * second_number
        elif st.session_state.operation == '/':
            if second_number == 0:
                st.session_state.display = 'Erro'
                st.session_state.waiting_for_second_number = False
                return
            result = st.session_state.first_number / second_number
        
        # Format result to remove unnecessary decimal places
        if result == int(result):
            st.session_state.display = str(int(result))
        else:
            st.session_state.display = str(result)
        
        st.session_state.waiting_for_second_number = False
        st.session_state.operation = None

if __name__ == "__main__":
    main()