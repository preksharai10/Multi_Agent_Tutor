import streamlit as st
import requests


API_URL = "http://localhost:8000/ask"  

st.set_page_config(page_title="Multi-Agent Tutor", layout="centered")


if "history" not in st.session_state:
    st.session_state["history"] = []

st.title("🎓 Multi-Agent Tutor")
st.markdown("Ask me anything related to **Math**, **Physics**, or **Chemistry**!")

with st.form(key="query_form"):
    user_query = st.text_area("Your Question", height=100, placeholder="e.g., What is 2 + 2?")
    submit_btn = st.form_submit_button("Get Answer")

# Input validation
if submit_btn:
    if not user_query.strip():
        st.warning(" Please enter a question.")
    elif len(user_query.strip()) < 3:
        st.warning(" Question too short. Please enter a valid question.")
    else:
        with st.spinner("Thinking..."):
            try:
                response = requests.post(API_URL, json={"question": user_query.strip()})
                if response.status_code == 200:
                    answer = response.json().get("response", "No response returned.")
                    st.session_state["history"].append((user_query.strip(), answer))
                    st.success(" Answer:")
                    st.markdown(f"> {answer}")
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
            except Exception as e:
                st.error(f" Failed to reach backend: {e}")

# Display conversation history
if st.session_state["history"]:
    st.markdown("---")
    st.subheader(" Conversation History")
    for i, (q, a) in enumerate(reversed(st.session_state["history"]), 1):
        st.markdown(f"**{i}. Question:** {q}")
        st.markdown(f"  **Answer:** {a}")
