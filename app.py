import streamlit as st

# Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="🍕 FoodieZone",
    page_icon="🍴",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Global Styling
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Main Title
st.markdown('<h1 class="fadeIn">🍕 FoodieZone</h1>', unsafe_allow_html=True)

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["🏠 Home", "🍽️ Menu", "ℹ️ About", "📞 Contact"])

# Display Selected Page
if page == "🏠 Home":
    st.switch_page("pages/Home.py")
elif page == "🍽️ Menu":
    st.switch_page("pages/Menu.py")
elif page == "ℹ️ About":
    st.switch_page("pages/About.py")
elif page == "📞 Contact":
    st.switch_page("pages/Contact.py")
