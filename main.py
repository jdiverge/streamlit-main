from multiprocessing import Condition
from operator import truth
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

left_column, right_culumn = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_culumn.write('ここは右カラム')

expander1 = st.expander('問合せ1')
expander1.write('問い合わせ1の回答')
expander2 = st.expander('問合せ2')
expander2.write('問い合わせ2の回答')
expander3 = st.expander('問合せ3')
expander3.write('問い合わせ3の回答')

# text = st.text_input(
#     'あなたの趣味を教えてください。',
# )

# 'あなたの趣味は、', text, 'です。'

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition

# if st.checkbox('Show Image'):
#     img = Image.open('001.jpg')
#     st.image(img, caption='Jun', use_column_width=True)

