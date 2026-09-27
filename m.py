import streamlit as st

st.title("🧮 เกมแก้สมการ")

# ----------------------------------------------------
# 1. กำหนดค่าเริ่มต้นใน session_state
# ----------------------------------------------------
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""
if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""
if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""
if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""
if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""


# ----------------------------------------------------
# 2. ฟังก์ชันเริ่มเกมใหม่
# ----------------------------------------------------
def reset_game():
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.session_state.is_ended = False


# ----------------------------------------------------
# 3. ฟังก์ชันแสดงผลคะแนน
# ----------------------------------------------------
@st.dialog("📊 สรุปผลการเล่นเกม")
def show_result_dialog(ans1, ans2, ans3, ans4, ans5):
    st.balloons()

    score = 0

    # แปลงคำตอบเป็นข้อความและตัดช่องว่าง
    answers = [
        ans1.strip(),
        ans2.strip(),
        ans3.strip(),
        ans4.strip(),
        ans5.strip()
    ]

    # คำตอบที่ถูกต้อง
    correct_answers = ["12", "25", "9", "6", "8"]

    # ตรวจคำตอบทั้ง 5 ข้อ
    for i in range(5):
        if answers[i] == correct_answers[i]:
            st.success(f"✅ ข้อ {i + 1}: ถูกต้อง")
            score += 1
        else:
            st.error(
                f"❌ ข้อ {i + 1}: ไม่ถูกต้อง "
                f"(คำตอบที่คุณตอบ: {answers[i]})"
            )

    # แสดงคะแนน
    st.info(f"🏆 ได้คะแนนรวม: {score} / 5 คะแนน")

    if score == 5:
        st.success("🎉 ยอดเยี่ยม! แก้สมการได้ครบทุกข้อ")
    elif score >= 3:
        st.warning("👍 ทำได้ดี! ลองทบทวนข้อที่ผิดอีกครั้ง")
    else:
        st.error("💪 ลองฝึกแก้สมการเพิ่มเติมนะ!")


# ----------------------------------------------------
# 4. ปุ่มเริ่มเล่นเกม
# ----------------------------------------------------
st.button(
    "🎮 เริ่มเล่นเกม",
    on_click=reset_game
)

st.divider()


# ----------------------------------------------------
# 5. แสดงโจทย์สมการ
# ----------------------------------------------------
st.subheader("📝 จงหาค่า x จากสมการ")
st.write("💡 ให้กรอกเฉพาะคำตอบ เช่น ถ้า x = 12 ให้กรอก `12`")


# ข้อ 1
st.write("### ข้อ 1")
st.write("จงหาค่า x จากสมการ  x + 8 = 20")
ans1 = st.text_input(
    "คำตอบข้อ 1",
    value=st.session_state.ans1_val
)


# ข้อ 2
st.write("### ข้อ 2")
st.write("จงหาค่า x จากสมการ  x - 15 = 10")
ans2 = st.text_input(
    "คำตอบข้อ 2",
    value=st.session_state.ans2_val
)


# ข้อ 3
st.write("### ข้อ 3")
st.write("จงหาค่า x จากสมการ  3x = 27")
ans3 = st.text_input(
    "คำตอบข้อ 3",
    value=st.session_state.ans3_val
)


# ข้อ 4
st.write("### ข้อ 4")
st.write("จงหาค่า x จากสมการ  2x + 6 = 18")
ans4 = st.text_input(
    "คำตอบข้อ 4",
    value=st.session_state.ans4_val
)


# ข้อ 5
st.write("### ข้อ 5")
st.write("จงหาค่า x จากสมการ  5x - 10 = 30")
ans5 = st.text_input(
    "คำตอบข้อ 5",
    value=st.session_state.ans5_val
)


# ----------------------------------------------------
# 6. อัปเดตคำตอบลง session_state
# ----------------------------------------------------
st.session_state.ans1_val = ans1
st.session_state.ans2_val = ans2
st.session_state.ans3_val = ans3
st.session_state.ans4_val = ans4
st.session_state.ans5_val = ans5


# ----------------------------------------------------
# 7. ปุ่มส่งคำตอบ
# ----------------------------------------------------
if st.button("📥 ส่งคำตอบ"):
    st.session_state.is_ended = True
    st.rerun()


# ----------------------------------------------------
# 8. แสดง Dialog ผลลัพธ์
# ----------------------------------------------------
if st.session_state.get("is_ended", False):
    show_result_dialog(
        ans1,
        ans2,
        ans3,
        ans4,
        ans5
    )


st.divider()

st.write("นายธรรศ พานเพชรสุขุม เลขที่ 13 ม.4/4")
