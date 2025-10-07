import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("🌊 파동 중첩 시각화")

# 슬라이더로 파동 설정
A1 = st.slider("파동1 진폭 A₁", 0.0, 2.0, 1.0)
A2 = st.slider("파동2 진폭 A₂", 0.0, 2.0, 1.0)
k = st.slider("파수 k", 1.0, 10.0, 5.0)
phi = st.slider("위상차 φ (도)", 0, 360, 0)

# 계산
x = np.linspace(0, 4*np.pi, 500)
y1 = A1 * np.sin(k*x)
y2 = A2 * np.sin(k*x + np.deg2rad(phi))
y_sum = y1 + y2

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y1, '--', label='파동1')
ax.plot(x, y2, '--', label='파동2')
ax.plot(x, y_sum, label='합성파', color='black')
ax.legend()
ax.set_xlabel("x (위치)")
ax.set_ylabel("y (변위)")
ax.set_title("두 파동의 중첩")
st.pyplot(fig)
