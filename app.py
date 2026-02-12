import streamlit as st
import time

# إعدادات الصفحة
st.set_page_config(page_title="Spotter Live", layout="centered")

# --- كود التحديث التلقائي الفعال ---
# هذا الجزء يجعل الصفحة تعيد تحميل نفسها كل 3 ثوانٍ تلقائياً
if "sleep_time" not in st.session_state:
    st.session_state.sleep_time = 3

st.title("🚗 Spotter Live Map")
st.write(f"Last Sync: {time.strftime('%H:%M:%S')}")

# نظام التحكم (Admin)
st.sidebar.header("Control Panel")
slot1 = st.sidebar.toggle('Parking Slot 1', value=True)
slot2 = st.sidebar.toggle('Parking Slot 2', value=False)

# عرض المواقف
col1, col2 = st.columns(2)

with col1:
    if slot1:
        st.error("### SLOT 1\nOCCUPIED")
    else:
        st.success("### SLOT 1\nFREE")

with col2:
    if slot2:
        st.error("### SLOT 2\nOCCUPIED")
    else:
        st.success("### SLOT 2\nFREE")

# أمر التحديث الإجباري
time.sleep(st.session_state.sleep_time)
st.rerun()
