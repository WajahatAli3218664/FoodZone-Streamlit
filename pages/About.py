# pages/About.py
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

.about-section {
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

.team-member {
    text-align: center;
    margin: 20px;
    padding: 15px;
    border-radius: 10px;
    background-color: #2c2c2c;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.team-member:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(255, 111, 97, 0.2);
}

.team-member img {
    width: 150px;
    height: 150px;
    border-radius: 50%;
    object-fit: cover;
    margin-bottom: 10px;
}

.food-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
    margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<h1 class="fadeIn">ℹ️ About Us</h1>', unsafe_allow_html=True)

# About Section
st.markdown("""
<div class="about-section fadeIn">
    <h2>Welcome to FoodieZone!</h2>
    <p>
        At FoodieZone, we believe that food is not just a necessity but an experience. Our journey began with a simple idea: to bring the best flavors from around the world to your plate. Whether you're craving a classic Margherita Pizza, a juicy Burger, or creamy Alfredo Pasta, we've got you covered.
    </p>
    <p>
        Our team of passionate chefs and food enthusiasts work tirelessly to ensure that every dish we serve is a masterpiece. We source the freshest ingredients and use traditional cooking techniques to deliver an unforgettable dining experience.
    </p>
</div>
""", unsafe_allow_html=True)

# Team Section
st.markdown('<h2 class="fadeIn">👨‍🍳 Our Team</h2>', unsafe_allow_html=True)
cols = st.columns(3)

team_members = [
    {"name": "Chef John", "role": "Head Chef", "image": "https://www.allrecipes.com/thmb/J3HVpKCDkXviLrRVRdceOPgSJrQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/fm20-chef-johnshelves-1244-60493c5b1013405ab9caf19d8be329df.jpg"},
    {"name": "Chef Maria", "role": "Pastry Chef", "image": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTLYjxgKpRQoYlV2a7aBSgpLeecvJ6Y2b5_hA&s"},
    {"name": "Chef Zakir", "role": "Sous Chef", "image": "https://reviewit.pk/wp-content/uploads/2013/12/ZQ.jpg"},
]

for idx, member in enumerate(team_members):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="team-member fadeIn">
            <img src="{member['image']}" alt="{member['name']}">
            <h3>{member['name']}</h3>
            <p>{member['role']}</p>
        </div>
        """, unsafe_allow_html=True)

# Food Images Section
st.markdown('<h2 class="fadeIn">🍴 Our Specialties</h2>', unsafe_allow_html=True)
food_images = [
    "https://images.immediate.co.uk/production/volatile/sites/30/2024/12/Chicken-Karahi-847828f.jpg?resize=768,574",
    "https://defencebakery.in/cdn/shop/files/Chocolate_Strawberry_Pastry_b93c804a-afce-4c0c-8ffd-e440d728dfb8.jpg?v=1722671054",
    "https://www.kitchenathoskins.com/wp-content/uploads/2023/07/chicken-tikka-13.jpg",
]

cols = st.columns(3)
for idx, image in enumerate(food_images):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="fadeIn">
            <img class="food-image" src="{image}" alt="Food Image {idx + 1}">
        </div>
        """, unsafe_allow_html=True)

# More About Us
st.markdown("""
<div class="about-section fadeIn">
    <h2>Our Mission</h2>
    <p>
        Our mission is to create a culinary experience that delights your senses and brings people together. We strive to innovate while staying true to the traditions that make food so special.
    </p>
    <h2>Why Choose Us?</h2>
    <ul>
        <li>🍕 Fresh, high-quality ingredients</li>
        <li>🍔 Passionate and experienced chefs</li>
        <li>🍝 A diverse menu to satisfy all tastes</li>
        <li>🍰 A commitment to excellence in every dish</li>
    </ul>
</div>
""", unsafe_allow_html=True)