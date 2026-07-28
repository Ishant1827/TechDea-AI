from dotenv import load_dotenv
import os
import streamlit as st
import google.generativeai as genai

# Load .env file
load_dotenv()

# API Configuration
api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    st.error("❌ GOOGLE_API_KEY not found!")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-3.6-flash")

# ===========================
# Page Configuration
# ===========================
st.set_page_config(
    page_title="TechDea AI Assistant",
    page_icon="🤖",
    layout="wide"
)

# ===========================
# Sidebar
# ===========================
with st.sidebar:
    st.title("TechDea")
    st.write("Welcome to our AI Customer Support.")

    st.markdown("---")

    st.subheader("Capabilities")
    st.write("Projects Information")
    st.write("Pricing")
    st.write("Customer Support")
    st.write("Business Queries")

    st.markdown("---")

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ===========================
# Main Page
# ===========================
st.title("TechDea AI Assistant")
st.caption("Ask us anything about our projects or services.")

# ===========================
# Chat History
# ===========================
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ===========================
# Chat Input
# ===========================
prompt = st.chat_input("Type your questions here...")

if prompt:

    st.session_state.messages.append(
        {"role": "user", "content": prompt}
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):

            try:

                business_prompt = f"""

You are TechDea AI, the official AI assistant of TechDea.

About TechDea:
- TechDea is an IT company that provides software development and technology solutions.
- We develop:
  • Business Websites
  • E-Commerce Websites
  • Web Applications
  • Mobile Applications (Android & iOS)
  • AI Chatbots
  • Custom Software
  • ERP & CRM Systems
  • API Integration
  • Cloud Deployment
  • UI/UX Design
  • Automation Solutions

Training Services:
- Python
- Java
- C & C++
- Web Development
- Full Stack Development
- Data Structures & Algorithms
- Artificial Intelligence & Machine Learning
- Data Science
- SQL & Database
- Interview Preparation
- Live Projects & Internship Training

Rules:
1. Be professional, friendly and helpful.
2. Answer questions only related to TechDea and its services.
3. If the user asks about software development or training, explain our services clearly.
4. If the user asks for pricing, explain that pricing depends on project requirements and ask for project details.
5. If the question is very technical, outside TechDea's services, or you are not confident about the answer, politely refer the user to our support team.

Support Contact:
📧 contact.techdea@gmail.com
📞 +91 9369907885

Always end difficult conversations with:
"For more detailed assistance, please contact our team at contact.techdea@gmail.com or call +91 9369907885."

Customer Question:
{prompt}
"""

                response = model.generate_content(business_prompt)
                reply = response.text

            except Exception as e:
                reply = f"❌ Error: {e}"

        st.markdown(reply)

    st.session_state.messages.append(
        {"role": "assistant", "content": reply}
    )

# ===========================
# Footer
# ===========================
st.markdown("---")
st.caption("© 2026 TechDea | AI Customer Support")