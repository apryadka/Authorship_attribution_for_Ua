import pickle
import streamlit as st
import base64
import sklearn

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-repeat: no-repeat;
        background-size: auto;
        background-position: center;
        background-repeat: no-repeat;
        background-size: cover;
    }}
    
    </style>
    """,
    unsafe_allow_html=True
    )

def templeate_style():
    add_bg_from_local('./img/bg.jpg') 
    hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            div.stButton > button:first-child {
                display block;
                width: 100%;
                background-color: rgb(204, 49, 49);
                color: #fff;
            }
            </style>
            """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def main():
    templeate_style()
    model_file = open('./model/LogisticRegression.pckl','rb')
    model = pickle.load(model_file)
    model_file.close()
    
    with st.container():
        st.markdown("<h2 style='text-align: center; color: black;'> Визначення авторства українських текстів</h2>", unsafe_allow_html=True)
        # st.title('Визначення авторства українських текстів')
        input = st.text_area(label='Напишіть фрагмент тексту')

    with st.container():
        col1, col2  = st.columns(2)
        with col1:
            button_clicked = st.button('Роспізнати автора')  
        if button_clicked:
            if len(input) < 1:
                st.text('Напишіть фрагмент тексту')
            else:
                if len(input.split(' ')) < 3:
                    st.text('Текст закороткий мінімум 3 слова')
                else:
                    result = model.predict([input])
                    st.text(f'Можливо це :  {result[0]}')

        with col2:
            button_authors = st.button('Наявні автори') 
            if button_authors:
                for author in model.classes_:
                    st.text(author)

if __name__ == "__main__":
    main()
