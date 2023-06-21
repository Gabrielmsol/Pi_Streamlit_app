from Ramanujan import Pi
import streamlit as st
import textwrap


# Text Structure:

Title = '''Ramanujan's pi Approximation '''
Section = '''Who was Ramanujan?'''
text = 'Ramanujan, known as Srinivasa Ramanujan, was a brilliant Indian\n' \
       'mathematician who lived from 1887 to 1920.\n' \
       'He is widely regarded as one of the greatest mathematical\n' \
       'prodigies in history, making significant contributions\n' \
       'to the field of mathematics despite having no formal\n' \
       'training in the subject.\n' \
       "Ramanujan's extraordinary talent and intuitive insights\n" \
       'led him to discover numerous groundbreaking results in\n' \
       'areas such as number theory, mathematical analysis, and infinite series.\n' \
       'His work has had a profound and lasting impact on various branches\n' \
       'of mathematics, influencing the work of many renowned mathematicians.\n' \
       "Ramanujan's genius was recognized by the British mathematician G.H. Hardy,\n" \
       'who invited him to study at the University of Cambridge in England.\n' \
       'During his short life, Ramanujan produced an extensive body of mathematical\n' \
       'work that continues to inspire and fascinate mathematicians to this day.\n' \
       'His legacy serves as a testament to the power of human intellect and the\n' \
       'boundless potential of mathematical exploration.'
Section2 = 'What is the is the approximation? '
latex = r'\displaystyle{ \pi = \frac{9801}' \
        r'{ 2\ \sqrt{2}\ \sum_{n=0}^{\infty} \frac{(4n)!\ (1103+26390n)}{(n!)^4\ 396^{4n}} } }'

# end of text Structure


# Functions for streamlit

def question_box():

    with st.form('key1'):
        p = st.number_input('Please enter how many decimal places you want to do calculations with:', value=0, step=1, format="%d")
        n = st.number_input('Please also enter how many iterations of our approximation you want to use:', value=0, step=1, format="%d")
        st.form_submit_button('Calculate!')

    return p, n


def calculate_pi(p, n):

    if p == 0 or n == 0:
        return
    else:
        pi, Error = Pi(p, n)
        st.text(textwrap.fill(str(pi), width=80))
        st.text(Error)


# end Streamlit Functions


# Site structure

st.title(Title)
st.subheader(Section)
st.text(text)
st.subheader(Section2)
st.latex(latex)
p, n = question_box()
calculate_pi(p, n)

# end Site structure
