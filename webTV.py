import requests
import json
import streamlit as st
st.set_page_config(page_title="web của tôi" , page_icon=":tada:",layout="wide")
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .css-1rs6os {visibility: hidden;}
            .css-17ziqus {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
with st.container():
    st.write("---")
    left_column , right_column = st.columns(2)
    with left_column:
        st.subheader("chào , tôi là quân :wave:")
        st.title("một học sinh đến từ Vietnam")
        st.write("Tôi đam mê tìm cách sử dụng Python để ngày càng hiệu quả hơn")
        st.write("[learn more>](https://www.youtube.com/channel/UC3opf8J6aPKbP4EZj892rwQ)")
with st.container():
    st.write("---")
    left_column , right_column = st.columns(2)
    with left_column:
         st.header("việc tôi làm")
         st.write("##")
         st.write("""
         Trên kênh YouTube của mình, tôi đang tạo các hướng dẫn cho những người:
         - đang tìm cách tận dụng sức mạnh của Python trong công việc hàng ngày của họ.
         - đang làm việc với Excel và tự nhận thấy rằng - "phải có một cách tốt hơn." """ 
         )
         st.write("[learn more>](https://www.youtube.com/channel/UC3opf8J6aPKbP4EZj892rwQ)")
with st.container():
    st.write("---")
    st.header("liên lạc với tôi")
    st.write('##')
    contact_form = """
    <form action="https://formsubmit.co/quanpham122007@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
    <input type="text" name="name" placeholder ="tên của bạn" required>
    <input type="email" name="email" placeholder="email của bạn" required>
    <textarea name="message" placeholder="Chi tiết về vấn đề của bạn"></textarea>
    <button type="submit">Send</button>
</form>
"""
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
left_column , right_column = st.columns(2)
with left_column :
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
