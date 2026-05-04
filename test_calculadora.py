import pytest
from calculadora import button_clicked, clear_display, set_operation, calculate_result

class MockSessionState(dict):
    def __getattr__(self, key):
        return self.get(key)
    
    def __setattr__(self, key, value):
        self[key] = value
    
    def __delattr__(self, key):
        self.pop(key, None)

def setup_session_state():
    """Setup mock session state for tests"""
    import streamlit as st
    if not hasattr(st, 'session_state') or not isinstance(st.session_state, MockSessionState):
        st.session_state = MockSessionState({
            'display': '0',
            'first_number': None,
            'operation': None,
            'waiting_for_second_number': False
        })

def test_button_clicked():
    """Testa a função button_clicked"""
    import streamlit as st
    setup_session_state()
    
    # Testa adicionando um número quando display é '0'
    st.session_state.waiting_for_second_number = False
    st.session_state.display = '0'
    button_clicked('5')
    assert st.session_state.display == '5'
    
    # Testa adicionando outro número
    button_clicked('3')
    assert st.session_state.display == '53'
    
    # Testa quando está esperando o segundo número
    st.session_state.waiting_for_second_number = True
    st.session_state.display = '5'
    button_clicked('7')
    assert st.session_state.display == '7'
    assert st.session_state.waiting_for_second_number == False

def test_clear_display():
    """Testa a função clear_display"""
    import streamlit as st
    setup_session_state()
    
    # Define estado inicial
    st.session_state.display = '123'
    st.session_state.first_number = 10
    st.session_state.operation = '+'
    st.session_state.waiting_for_second_number = True
    
    clear_display()
    
    assert st.session_state.display == '0'
    assert st.session_state.first_number is None
    assert st.session_state.operation is None
    assert st.session_state.waiting_for_second_number == False

def test_set_operation():
    """Testa a função set_operation"""
    import streamlit as st
    setup_session_state()
    
    # Define estado inicial
    st.session_state.display = '15'
    st.session_state.first_number = None
    st.session_state.operation = None
    st.session_state.waiting_for_second_number = False
    
    set_operation('+')
    
    assert st.session_state.first_number == 15.0
    assert st.session_state.operation == '+'
    assert st.session_state.waiting_for_second_number == True

def test_calculate_result_addition():
    """Testa a função calculate_result com adição"""
    import streamlit as st
    setup_session_state()
    
    # Define estado inicial
    st.session_state.display = '10'
    st.session_state.first_number = 5.0
    st.session_state.operation = '+'
    st.session_state.waiting_for_second_number = True
    
    calculate_result()
    
    assert st.session_state.display == '15'
    assert st.session_state.waiting_for_second_number == False
    assert st.session_state.operation is None

def test_calculate_result_subtraction():
    """Testa a função calculate_result com subtração"""
    import streamlit as st
    setup_session_state()
    
    # Define estado inicial
    st.session_state.display = '5'
    st.session_state.first_number = 10.0
    st.session_state.operation = '-'
    st.session_state.waiting_for_second_number = True
    
    calculate_result()
    
    assert st.session_state.display == '5'
    assert st.session_state.waiting_for_second_number == False
    assert st.session_state.operation is None

def test_calculate_result_multiplication():
    """Testa a função calculate_result com multiplicação"""
    import streamlit as st
    setup_session_state()
    
    # Define estado inicial
    st.session_state.display = '3'
    st.session_state.first_number = 4.0
    st.session_state.operation = '*'
    st.session_state.waiting_for_second_number = True
    
    calculate_result()
    
    assert st.session_state.display == '12'
    assert st.session_state.waiting_for_second_number == False
    assert st.session_state.operation is None

def test_calculate_result_division():
    """Testa a função calculate_result com divisão"""
    import streamlit as st
    setup_session_state()
    
    # Define estado inicial
    st.session_state.display = '2'
    st.session_state.first_number = 8.0
    st.session_state.operation = '/'
    st.session_state.waiting_for_second_number = True
    
    calculate_result()
    
    assert st.session_state.display == '4'
    assert st.session_state.waiting_for_second_number == False
    assert st.session_state.operation is None

def test_calculate_result_division_by_zero():
    """Testa a função calculate_result com divisão por zero"""
    import streamlit as st
    setup_session_state()
    
    # Define estado inicial
    st.session_state.display = '0'
    st.session_state.first_number = 10.0
    st.session_state.operation = '/'
    st.session_state.waiting_for_second_number = True
    
    calculate_result()
    
    assert st.session_state.display == 'Erro'
    assert st.session_state.waiting_for_second_number == False
    # Nota: A operação NÃO é resetada para None em caso de divisão por zero
    # Esta é uma decisão de design da implementação original
    assert st.session_state.operation == '/'

def test_calculate_result_float_formatting():
    """Testa a função calculate_result com formatação de float"""
    import streamlit as st
    setup_session_state()
    
    # Define estado inicial
    st.session_state.display = '5'
    st.session_state.first_number = 10.0
    st.session_state.operation = '/'
    st.session_state.waiting_for_second_number = True
    
    calculate_result()
    
    # 10/5 = 2.0 -> deve ser exibido como '2'
    assert st.session_state.display == '2'
    
    # Teste com resultado não inteiro
    st.session_state.display = '3'
    st.session_state.first_number = 10.0
    st.session_state.operation = '/'
    st.session_state.waiting_for_second_number = True
    
    calculate_result()
    
    # 10/3 = 3.333... -> deve ser exibido como float
    assert st.session_state.display == '3.3333333333333335'

if __name__ == "__main__":
    pytest.main([__file__])