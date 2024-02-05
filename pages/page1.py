import streamlit as st

st.subheader("code")

st.text("streamlit を用いたwebアプリ作成テスト中\n"
        "参考 : https://www.youtube.com/watch?v=4nsTce1Oce8")

code ="""
import streamlit as st

st.title("miho_memo")
st.caption("This is a test apprication for miho")

st.subheader("streamlit")

code = '''
print("hello world!")
'''

st.code(code, language="python")
"""

st.code(code, language="python")
st.text("hello world!")