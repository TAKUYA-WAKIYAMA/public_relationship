"""
Source:
https://buildersbox.corp-sansan.com/entry/2021/04/15/110000

"""

import streamlit as st
import spacy
from dframcy import DframCy




@st.cache(allow_output_mutation=True)
def load_model():
    """毎回モデルのロードをしていると時間がかかるため、キャッシュしておく"""
    nlp = spacy.load("ja_ginza")
    dframcy = DframCy(nlp)
    return dframcy

def highlight_ner_row(x):
    color = ""
    if x.entity != "O":
        color = "background-color: skyblue;"
    return [color for _ in x]

def main():
    st.title("固有表現抽出")
    text = st.text_area('テキストを入力し、Ctrl+Enterで解析結果を表示します。', max_chars=510)
    dframcy = load_model()
    doc = dframcy.nlp(text)
    # df_anno = dframcy.to_dataframe(doc).style.apply(highlight_ner_row, axis=1)
    df_anno = dframcy.to_dataframe(doc)

    st.table(df_anno)


if __name__ == "__main__":
    main()