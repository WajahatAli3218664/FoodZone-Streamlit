# pages/4_📞_Contact.py
import streamlit as st

# Custom CSS for Animations and Styling
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

body {
    font-family: 'Poppins', sans-serif;
    background-color: #121212;
    color: #ffffff;
}

h1, h2, h3, h4, h5, h6 {
    color: #ff6f61;
}

.contact-section {
    padding: 20px;
    border-radius: 10px;
    background-color: #1e1e1e;
    margin-bottom: 20px;
    animation: fadeIn 2s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.fadeIn {
    animation: fadeIn 1.5s ease-in-out;
}

.stTextInput>div>div>input, .stTextArea>div>textarea {
    background-color: #2c2c2c;
    color: #ffffff;
    border: 1px solid #444;
    border-radius: 5px;
    padding: 10px;
}

.stTextInput>div>div>input:focus, .stTextArea>div>textarea:focus {
    border-color: #ff6f61;
    box-shadow: 0 0 5px rgba(255, 111, 97, 0.5);
}

.stButton>button {
    background-color: #ff6f61;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    transition: background-color 0.3s ease, transform 0.3s ease;
}

.stButton>button:hover {
    background-color: #ff3b2f;
    transform: translateY(-2px);
}

.success-message {
    padding: 15px;
    border-radius: 5px;
    background-color: #4CAF50;
    color: white;
    text-align: center;
    animation: slideIn 0.5s ease-in-out;
}

@keyframes slideIn {
    from { transform: translateY(-20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}
</style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<h1 class="fadeIn">📞 Contact Us</h1>', unsafe_allow_html=True)

# Contact Form Section
st.markdown("""
<div class="contact-section fadeIn">
    <h2>Get in Touch</h2>
    <p>
        Have questions or feedback? We'd love to hear from you! Fill out the form below, and we'll get back to you as soon as possible.
    </p>
</div>
""", unsafe_allow_html=True)

# Contact Form
with st.form("contact_form"):
    name = st.text_input("Name", placeholder="Enter your name")
    email = st.text_input("Email", placeholder="Enter your email")
    message = st.text_area("Message", placeholder="Type your message here...", height=150)
    submit = st.form_submit_button("Submit")

    if submit:
        st.markdown("""
        <div class="success-message">
            Thank you for contacting us! We will get back to you soon. 🎉
        </div>
        """, unsafe_allow_html=True)

# Additional Contact Info
st.markdown("""
<div class="contact-section fadeIn">
    <h2>📍 Our Location</h2>
    <p>
        Burns Road,<br>
        Karachi,Sindh, FC 75500<br>
        📞 +923242042329
    </p>
</div>
""", unsafe_allow_html=True)

# Social Media Links
st.markdown("""
<div class="contact-section fadeIn">
    <h2>🌐 Follow Us</h2>
    <p>
        Stay connected with us on social media for the latest updates and offers:
    </p>
    <p>
        <a href="https://www.facebook.com/Wajii10" target="_blank">Facebook</a> |
        <a href="https://twitter.com" target="_blank">Twitter</a> |
        <a href="https://www.linkedin.com/in/wajahat-ali-3189862b4/" target="_blank">Linkedin</a>
    </p>
</div>
""", unsafe_allow_html=True)
