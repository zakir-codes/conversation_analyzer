import streamlit as st
import httpx

st.set_page_config(page_title="Sales Analyzer", layout="wide")

st.title("Sales Analyzer")
st.caption("POC Frontend - Streamlit")

backend_base_url = "http://localhost:8000"


@st.cache_data(ttl=10)
def fetch_health() -> dict:
    try:
        with httpx.Client(timeout=2.0) as client:
            r = client.get(f"{backend_base_url}/health")
            r.raise_for_status()
            return r.json()
    except Exception as exc:  # noqa: BLE001
        return {"status": f"error: {exc}"}


col1, col2 = st.columns(2)
with col1:
    st.subheader("Backend Health")
    health = fetch_health()
    st.json(health)

with col2:
    st.subheader("Links")
    st.markdown("- Backend docs: http://localhost:8000/docs")


