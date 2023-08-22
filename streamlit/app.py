import streamlit as st
import json
from streamlit_lottie import st_lottie

st.set_page_config(page_title="my hackathon project",layout="wide")

def load_lottiefile(filepath:str):
    with open(filepath,"r") as f:
        return json.load(f)
lottie_variable1=load_lottiefile("1.json")   
lottie_variable2=load_lottiefile("2.json")  
lottie_variable3=load_lottiefile("3.json")  
lottie_variable4=load_lottiefile("4.json")   


st.subheader("hello everyone")
st.title("we are working on AI")
st.write("we are passionate coders")
# st.write("[click here to redirect to a link](paste any youtube link here)")


with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("COGNITIVE COMPUTIONG AND SOCIAL SENSING:GRAPH")
        st.write("##")
        st.write("##")
        st.write("##")

        st.write('''DESCRIPTION OF GRAPH '''
                 )
        if st.button("SHOW GRAPH"):
            st.write("write the function to display graph here")
    with right_column:
        st_lottie(lottie_variable1,height=700,key="catu")       
with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with right_column:
        st.header("COGNITIVE COMPUTIONG AND SOCIAL SENSING:FILE UPLOADING")
        st.write("##")
        st.write("##")
        st.write("##")

        docx_file=st.file_uploader("upload your txt file here",type=["txt","pdf","docx"])
        if st.button("process"):
            if docx_file is not None:
                if docx_file.type=="text/plain":
                    raw_text=str(docx_file.read(),"utf-8")
                    st.write(raw_text)
                    # text files data is stored in form of string in variable raw_text
     
    with left_column:
        st_lottie(lottie_variable2,height=700,key="catu2")              




with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with left_column:
        st.header("COGNITIVE COMPUTIONG AND SOCIAL SENSING:DROPDOWN MENU")
        st.write("##")
        st.write("##")
        st.write("##")
        st.selectbox("DropDownMenu",["option1","option2","option3"],index=0)
       
    with right_column:
        st_lottie(lottie_variable3,height=700,key="catu3")    




with st.container():
    st.write("---")
    left_column,right_column=st.columns(2)
    with right_column:
        st.header("COGNITIVE COMPUTIONG AND SOCIAL SENSING:ANALYSIS")
        st.write("##")
        st.write("##")
        st.write("##")

        st.write('''DESCRIPTION OF ANALYSIS'''
                 )
        if st.button("ANALYSE"):
            st.write("CALL ANALYSIS FUNCTION HERE")
    with left_column:
        st_lottie(lottie_variable4,height=700,key="catu4")            