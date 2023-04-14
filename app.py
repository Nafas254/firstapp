import streamlit as st
st.text('ciao ciao !!! ')
st.markdown('Streamlit is **_really_ cool**.')
st.markdown("This text is :green[colored ], and this is **:blue[colored]** and bold.")
st.markdown(":green[$\sqrt{x^3+y^2}=1$] is a Pythagorean identity. :pencil:")
st.title('This is a title')
st.title(':smile: A title with _italics_ :blue[colors] and emojis :smile:')
st.subheader('This is a subheader')
st.subheader('A subheader with _italics_ :blue[colors] and emojis :sunglasses:')
st.caption('This is a string that explains something above.')
st.caption('A caption with _italics_ :blue[colors] and emojis :sunglasses:')
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')
st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')
st.title('La mia prima App in python')

if st.button('Streamlit Button', help="Click here"):
    st.write('Hai cliccato')

from PIL import Image
 
if st.checkbox('Check Box'):
    st.write('checckata')

