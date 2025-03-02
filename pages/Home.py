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
    color: #61a5ff;
}

.product-card {
    border: 1px solid #333;
    border-radius: 10px;
    padding: 15px;
    margin: 10px;
    background-color: #1e1e1e;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.product-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(76, 175, 80, 0.2);
}

.product-card h3, .product-card p {
    color: #ffffff;
}

.equal-image {
    width: 100%;
    height: 200px;
    object-fit: cover;
    border-radius: 10px;
    transition: transform 0.3s ease;
}

.equal-image:hover {
    transform: scale(1.05);
}

@keyframes fadeIn {
    from { opacity: 0; }
    to { opacity: 1; }
}

.fadeIn {
    animation: fadeIn 1.5s ease-in-out;
}

.animated-section {
    margin-top: 30px;
    text-align: center;
    animation: slideIn 1s ease-in-out;
}

@keyframes slideIn {
    from { transform: translateY(20px); opacity: 0; }
    to { transform: translateY(0); opacity: 1; }
}

.food-slider {
    display: flex;
    overflow-x: auto;
    gap: 20px;
    padding: 20px;
    margin: 20px 0;
}

.food-slider img {
    width: 200px;
    height: 150px;
    border-radius: 10px;
    object-fit: cover;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.food-slider img:hover {
    transform: scale(1.05);
    box-shadow: 0 8px 16px rgba(76, 175, 80, 0.3);
}

.food-icons {
    display: flex;
    justify-content: space-around;
    flex-wrap: wrap;
    margin: 20px 0;
}

.food-icons img {
    width: 80px;
    height: 80px;
    margin: 10px;
    transition: transform 0.3s ease;
}

.food-icons img:hover {
    transform: scale(1.2);
}

.quote-section {
    padding: 20px;
    background-color: #1e1e1e;
    border-radius: 10px;
    margin: 20px 0;
    animation: fadeIn 2s ease-in-out;
}

.quote-section p {
    font-style: italic;
    color: #61a5ff;
    font-size: 18px;
}

.footer {
    padding: 20px;
    background-color: #1e1e1e;
    text-align: center;
    border-top: 1px solid #333;
    margin-top: 50px;
    animation: slideIn 1s ease-in-out;
}

.footer p, .footer a {
    color: #ffffff;
    font-size: 14px;
    text-decoration: none;
    transition: color 0.3s ease;
}

.footer a:hover {
    color: #61a5ff;
}
</style>
""", unsafe_allow_html=True)

# Page Title
st.markdown('<h1 class="fadeIn">🍕 Welcome to FoodieZone!</h1>', unsafe_allow_html=True)
st.write("Your one-stop destination for delicious food.")

# Featured Dishes
st.write("## 🍴 Featured Dishes")
cols = st.columns(3)

dishes = [
    {"name": "Margherita Pizza", "image": "https://cdn.shopify.com/s/files/1/0274/9503/9079/files/20220211142754-margherita-9920_5a73220e-4a1a-4d33-b38f-26e98e3cd986.jpg?v=1723650067", "description": "Classic Italian pizza with fresh mozzarella and basil."},
    {"name": "Burger", "image": "https://www.seriouseats.com/thmb/P0opRA7Movx8bqIAjXQHo7y6VeU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/20230525-SEA-Wagyu-Burger-Amanda-Suarez-hero-54009c50b715486892bbed7a0edc829c.jpg", "description": "Juicy beef burger with cheese and veggies."},
    {"name": "Pasta", "image": "https://foodhub.scene7.com/is/image/woolworthsltdprod/Easy-chicken-and-bacon-pasta?wid=1300&hei=1300&fmt=png-alpha", "description": "Creamy Alfredo pasta with grilled chicken."},
]

for idx, dish in enumerate(dishes):
    with cols[idx % 3]:
        st.markdown(f"""
        <div class="product-card fadeIn">
            <img class="equal-image" src="{dish['image']}" alt="{dish['name']}">
            <h3>{dish['name']}</h3>
            <p>{dish['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# Interactive Food Slider
st.markdown("""
<div class="animated-section">
    <h2>🍴 Explore Our Menu</h2>
    <div class="food-slider">
        <img src="https://rakskitchen.net/wp-content/uploads/2021/09/gulab-jamun.jpg" alt="Gulab Jamun">
        <img src="https://www.ndtv.com/cooks/images/Haleem%282%29.jpg" alt="Haleem">
        <img src="https://media.istockphoto.com/id/1313085999/photo/fried-vegetable-spring-rolls-with-sweet-chili-and-soya-sauce-on-wooden-board.jpg?s=612x612&w=0&k=20&c=OM1OfrBS7D4666h9eZtztqFmQW0Ch15bcMcNbYhUBIo=" alt="Haleem">
        <img src="https://www.apnachef.com/wp-content/uploads/2023/12/chicken-biryani-50-people-wide.jpg" alt="Biryani">
        <img src="https://www.chocolatesandchai.com/wp-content/uploads/2022/04/Al-Baik-Chicken-Recipe-h5.jpg" alt="Al Baik Chicken">
        <img src="https://cdn.shopify.com/s/files/1/0570/2113/6986/files/Shahi_Nihari_Tin_-_Chicken_Nihari_-_Chicken_Nihari_Can_-_Tin_Packed_-_Net_Weight_800_Grams_Canned_-_Ready_To_Eat_-_Tasty_Food_04289dfa-6a83-4639-8fb6-4e3796ea0c54.jpg?v=1661857769" alt="Nihari">
    </div>
</div>
""", unsafe_allow_html=True)

# Animated Food Icons
st.markdown("""
<div class="animated-section">
    <h2>🍴 Quick Bites</h2>
    <div class="food-icons">
        <img src="https://cdn-icons-png.flaticon.com/512/706/706164.png" alt="Pizza Icon">
        <img src="https://cdn-icons-png.flaticon.com/512/5787/5787100.png" alt="Burger Icon">
        <img src="https://cdn-icons-png.flaticon.com/512/5787/5787134.png" alt="Pasta Icon">
        <img src="https://cdn-icons-png.flaticon.com/512/5787/5787140.png" alt="Biryani Icon">
        <img src="https://cdn4.iconfinder.com/data/icons/arabic-culture-flat/72/Untitled-2-29-512.png" alt="Tikka Icon">
        <img src="https://cdn-icons-png.freepik.com/512/5375/5375249.png" alt="Ice Cream Icon">
    </div>
</div>
""", unsafe_allow_html=True)

# Food Quotes
st.markdown("""
<div class="quote-section">
    <p>"Good food is the foundation of genuine happiness."</p>
    <p>"Life is short, eat dessert first."</p>
    <p>"Food is not just eating energy, it's an experience."</p>
</div>
""", unsafe_allow_html=True)

# Footer
st.markdown("""
<div class="footer">
    <p>© 2025 FoodieZone. All rights reserved.</p>
    <p>Created with ❤️ by <a href="#" target="_blank">Wajahat Ali</a></p>
    <p>"Good food is the foundation of genuine happiness."</p>
</div>
""", unsafe_allow_html=True)
