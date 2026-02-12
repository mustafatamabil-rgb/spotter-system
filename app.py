import streamlit as st
import time

# إعداد الصفحة
st.set_page_config(page_title="Spotter Live", layout="centered")

st.title("🚗 Spotter Live Map")

# زر تحديث يدوي للموبايل (عشان تضغط عليه ويحدث فوراً)
if st.button('🔄 Refresh Now (اضغط للتحديث)'):
    st.rerun()

st.write(f"Last Sync: {time.strftime('%H:%M:%S')}")

# نظام التحكم
st.sidebar.header("Admin Panel")
s1 = st.sidebar.toggle('Parking 1', value=True)

if s1:
    st.error("### SLOT 1: OCCUPIED")
else:
    st.success("### SLOT 1: FREE")

# كود التحديث التلقائي (الذي يحاول العمل في الخلفية)
time.sleep(2)
st.rerun()

