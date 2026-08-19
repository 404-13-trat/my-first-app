import streamlit as st

#ส่วนที่ 1 หัวข้อหน้าเว็บ (Title สีแดง)
st.markdown("# :red [ คำนวณค่าดัชนีมวลกาย BMI]")
st.write("กรอกข้อมูลนํ้าหนักและส่วนสูงของคุณ เพื่อเช็กสุขภาพเบื้องต้น")

#ส่วนที่ 2 สร้างช่องรับค่านํ้าหนัก และ ส่วนสูง
weight = st.number_input("กรอกนํ้าหนักของคุณ (กิโลกรัม):", min_value=1.0, value=1.0)
height_cm = st.number_input("กรอกนํ้าหนักของคุณ (เซนติเมตร):", min_value=1.0, value=1.0)
