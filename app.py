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

# Sidebar Styling
st.sidebar.markdown("""
    <style>
        .sidebar-container {
            background-color: #1E1E1E;
            padding: 15px;
            border-radius: 10px;
        }
        .sidebar-title {
            font-size: 26px;
            font-weight: bold;
            color: #FF5733;
            text-align: center;
            margin-bottom: 20px;
        }
        .sidebar-item {
            font-size: 18px;
            font-weight: bold;
            color: #ffffff;
            background-color: #333;
            padding: 12px;
            border-radius: 8px;
            margin: 8px 0;
            text-align: center;
            transition: 0.3s;
        }
        .sidebar-item:hover {
            background-color: #FF5733;
            color: #fff;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# Navigation Heading
st.sidebar.markdown('<div class="sidebar-title">📍 Explore FoodieZone</div>', unsafe_allow_html=True)

# Navigation Menu
page = st.sidebar.radio("", ["🏠 Home", "🍽️ Menu", "ℹ️ About", "📞 Contact"])

# Display Selected Page
if page == "🏠 Home":
    st.switch_page("pages/Home.py")
elif page == "🍽️ Menu":
    st.switch_page("pages/Menu.py")
elif page == "ℹ️ About":
    st.switch_page("pages/About.py")
elif page == "📞 Contact":
    st.switch_page("pages/Contact.py")
