import streamlit as st

def button_clicked(value):
    """
    Handle button clicks for number inputs.
    
    Args:
        value (str): The value of the button clicked (0-9)
    """
    if st.session_state.waiting_for_second_number:
        # If we're waiting for the second number, replace the display
        st.session_state.display = value
        st.session_state.waiting_for_second_number = False
    else:
        # Otherwise, append to the current display
        if st.session_state.display == '0':
            st.session_state.display = value
        else:
            st.session_state.display += value

def clear_display():
    """
    Clear the calculator display and reset all stored values.
    """
    st.session_state.display = '0'
    st.session_state.first_number = None
    st.session_state.operation = None
    st.session_state.waiting_for_second_number = False

def set_operation(op):
    """
    Store the selected operation and first number.
    
    Args:
        op (str): The mathematical operation (+, -, *, /)
    """
    if st.session_state.display:
        st.session_state.first_number = float(st.session_state.display)
        st.session_state.operation = op
        st.session_state.waiting_for_second_number = True

def calculate_result():
    """
    Calculate the result based on the stored operation and numbers.
    Handles division by zero and formats the result appropriately.
    """
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

def main():
    """
    Main function to run the Streamlit calculator application.
    """
    st.title("Calculadora Simples")
    
    # Initialize session state variables if they don't exist
    if 'display' not in st.session_state:
        st.session_state.display = '0'
    if 'first_number' not in st.session_state:
        st.session_state.first_number = None
    if 'operation' not in st.session_state:
        st.session_state.operation = None
    if 'waiting_for_second_number' not in st.session_state:
        st.session_state.waiting_for_second_number = False
    
    # Display the calculator screen (read-only)
    st.text_input("Display", value=st.session_state.display, key="display_input", disabled=True)
    
    # Create button layout using columns
    col1, col2, col3, col4 = st.columns(4)
    
    # First column: 7, 4, 1, C (Clear)
    with col1:
        if st.button('7'):
            button_clicked('7')
        if st.button('4'):
            button_clicked('4')
        if st.button('1'):
            button_clicked('1')
        if st.button('C'):
            clear_display()
    
    # Second column: 8, 5, 2, 0
    with col2:
        if st.button('8'):
            button_clicked('8')
        if st.button('5'):
            button_clicked('5')
        if st.button('2'):
            button_clicked('2')
        if st.button('0'):
            button_clicked('0')
    
    # Third column: 9, 6, 3, = (Equals)
    with col3:
        if st.button('9'):
            button_clicked('9')
        if st.button('6'):
            button_clicked('6')
        if st.button('3'):
            button_clicked('3')
        if st.button('='):
            calculate_result()
    
    # Fourth column: +, -, *, / (Operations)
    with col4:
        if st.button('+'):
            set_operation('+')
        if st.button('-'):
            set_operation('-')
        if st.button('*'):
            set_operation('*')
        if st.button('/'):
            set_operation('/')

if __name__ == "__main__":
    main()