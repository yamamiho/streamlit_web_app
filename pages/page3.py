import streamlit as st

#textbox
st.subheader("textbox")
with st.form(key="profile_form"): #こうするとボタンを押すまでリロードされない。カーソルを話してもリロードされない
    
    name = st.text_input("名前")
    #select box #ラジオボックスならst.radiobox()
    born_category = st.selectbox(
        "出身",
        ("西日本","東日本","その他")
    )

    #複数選択
    hobby = st.multiselect(
        "趣味",
        ("sports","book","music","other")
    )


    submit_btn = st.form_submit_button("送信")

    if submit_btn:
        st.text(f"ようこそ！{name}さん")
        st.text(f"出身：{born_category}")
        st.text(f"趣味：{', '.join(hobby)}")