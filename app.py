import streamlit as st
import time

# إعدادات تجعل التطبيق سريعاً جداً وخفيفاً على الموبايل
st.set_page_config(page_title="Spotter OS", layout="wide")

# كود التحديث التلقائي (السر في السرعة)
if 'last_update' not in st.session_state:
    st.session_state.last_update = time.time()

# تحديث الصفحة كل ثانية واحدة فقط
st.empty() 

st.title("🚗 Spotter Live Map")
st.write(f"Last Sync: {time.strftime('%H:%M:%S')}")

# محاكاة المواقف
with st.sidebar:
    st.header("Admin Dashboard")
    a1 = st.toggle('Slot A1', value=True)
    a2 = st.toggle('Slot A2', value=False)

col1, col2 = st.columns(2)
with col1:
    if a1:
        st.error("### A1\nOCCUPIED")
    else:
        st.success("### A1\nFREE")

with col2:
    if a2:
        st.error("### A2\nOCCUPIED")
    else:
        st.success("### A2\nFREE")

# يخبر المتصفح أن يعيد التحميل بعد ثانية واحدة
time.sleep(1)
st.rerun()
