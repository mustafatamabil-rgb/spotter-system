import streamlit as st
import time

# إعدادات الصفحة للسيرفر العالمي
st.set_page_config(page_title="Spotter Live", layout="wide")

# كود التحديث الإجباري (Force Refresh)
if "last_heartbeat" not in st.session_state:
    st.session_state.last_heartbeat = time.time()

st.title("🚗 Spotter Live Map")
st.write(f"Server Sync Time: {time.strftime('%H:%M:%S')}")

# لوحة التحكم (ستظهر لك في الرابط العالمي)
with st.sidebar:
    st.header("Admin Control")
    s1 = st.toggle('Slot 1 Status', value=True)
    s2 = st.toggle('Slot 2 Status', value=False)

col1, col2 = st.columns(2)
with col1:
    if s1:
        st.error("### SLOT 1\nOCCUPIED")
    else:
        st.success("### SLOT 1\nFREE")

with col2:
    if s2:
        st.error("### SLOT 2\nOCCUPIED")
    else:
        st.success("### SLOT 2\nFREE")

# السر هنا: يخبر المتصفح (موبايل أو لابتوب) أن يعيد التحميل كل ثانية
time.sleep(1)
st.rerun()
