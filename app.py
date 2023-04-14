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


 
if st.checkbox('Check Box'):
    st.write('checckata')

from PIL import Image
image = Image.open('mare.jpg')
st.image(image, caption='Mare mare!!!',width=860)

lang = st.radio(
    "What's your favorite programming language?",
    ('C++', 'Python'))
if lang == 'C++':
    st.write('You selected C++.')
else:
    st.write('You selected Python')

x1 = st.slider('Please inserisci lato1 rettangolo', 0, 100, 25)
x2 = st.slider('Please inserisci lato2 rettangolo', 0, 100, 35)

def area(l1:float,l2:float):
    a = l1*l2
    return a 

st.write("l'area rettangolo è ", area(x1,x2))

add_selectbox = st.sidebar.radio(
    "Please choose an option",
    ("Option 1", "Option 2", "Option 3")
)

import matplotlib.pyplot as plt 
from numpy.random import rand

fig = plt.figure(figsize=(18,10)) 
plt.scatter([1,2,3,4,5],[1,2,3,4,5])
st.pyplot(fig)

rn = st.slider('Please inserisci il numero dei punti da visualizzare', 0, 100, 88)
x = rand(rn)
y = rand(rn)
fig2 = plt.figure(figsize=(18,10)) 
plt.plot(x,y,'or')
st.pyplot(fig2)

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://www.coverstyl.com/cache/articles_160/o6-solid-light-blue2_1024_1024_1.webp");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 


     



 

 

