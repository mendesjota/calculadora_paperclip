import streamlit as st

st.set_page_config(page_title="Calculadora", page_icon="🧮", layout="centered")

st.markdown("""
<style>
    .stButton > button {
        width: 100%;
        height: 60px;
        font-size: 24px;
        font-weight: bold;
        border-radius: 10px;
        margin: 5px 0;
        transition: all 0.2s;
    }
    .stButton > button:hover {
        transform: scale(1.05);
    }
    .number-btn > button {
        background-color: #f0f2f6;
        color: #31333F;
        border: 1px solid #e0e0e0;
    }
    .number-btn > button:hover {
        background-color: #e0e0e0;
    }
    .operator-btn > button {
        background-color: #ff4b4b;
        color: white;
    }
    .operator-btn > button:hover {
        background-color: #ff3333;
    }
    .clear-btn > button {
        background-color: #ff8c00;
        color: white;
    }
    .equals-btn > button {
        background-color: #4CAF50;
        color: white;
    }
    .equals-btn > button:hover {
        background-color: #45a049;
    }
    .display-box {
        background-color: #1e1e1e;
        color: white;
        padding: 20px;
        border-radius: 15px;
        text-align: right;
        font-size: 36px;
        font-family: monospace;
        margin-bottom: 20px;
    }
    .title {
        text-align: center;
        color: #31333F;
        margin-bottom: 30px;
    }
</style>
""", unsafe_allow_html=True)

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
    st.markdown('<h1 class="title">🧮 Calculadora Simples</h1>', unsafe_allow_html=True)
    
    if 'display' not in st.session_state:
        st.session_state.display = '0'
    if 'first_number' not in st.session_state:
        st.session_state.first_number = None
    if 'operation' not in st.session_state:
        st.session_state.operation = None
    if 'waiting_for_second_number' not in st.session_state:
        st.session_state.waiting_for_second_number = False
    
    st.markdown(f'<div class="display-box">{st.session_state.display}</div>', unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown('<div class="number-btn">', unsafe_allow_html=True)
        if st.button('7'):
            button_clicked('7')
        if st.button('4'):
            button_clicked('4')
        if st.button('1'):
            button_clicked('1')
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="clear-btn">', unsafe_allow_html=True)
        if st.button('C'):
            clear_display()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="number-btn">', unsafe_allow_html=True)
        if st.button('8'):
            button_clicked('8')
        if st.button('5'):
            button_clicked('5')
        if st.button('2'):
            button_clicked('2')
        if st.button('0'):
            button_clicked('0')
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col3:
        st.markdown('<div class="number-btn">', unsafe_allow_html=True)
        if st.button('9'):
            button_clicked('9')
        if st.button('6'):
            button_clicked('6')
        if st.button('3'):
            button_clicked('3')
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="equals-btn">', unsafe_allow_html=True)
        if st.button('='):
            calculate_result()
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col4:
        st.markdown('<div class="operator-btn">', unsafe_allow_html=True)
        if st.button('+'):
            set_operation('+')
        if st.button('-'):
            set_operation('-')
        if st.button('*'):
            set_operation('*')
        if st.button('/'):
            set_operation('/')
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()