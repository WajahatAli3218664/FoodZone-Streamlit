import streamlit as st
import json
import os
from datetime import datetime

# Initialize session state for cart if it doesn't exist
if 'cart' not in st.session_state:
    st.session_state.cart = []
    
if 'order_confirmed' not in st.session_state:
    st.session_state.order_confirmed = False
    
if 'order_number' not in st.session_state:
    st.session_state.order_number = None

# Function to add item to cart
def add_to_cart(item_name, item_price):
    price_value = float(item_price.replace('$', ''))
    st.session_state.cart.append({
        "name": item_name,
        "price": price_value,
        "quantity": 1
    })
    st.toast(f"{item_name} added to cart!", icon="🛒")

# Function to view item details
def view_details(item_name, item_description, item_price, item_image):
    st.session_state.view_item = {
        "name": item_name,
        "description": item_description,
        "price": item_price,
        "image": item_image
    }

# Function to clear cart
def clear_cart():
    st.session_state.cart = []
    st.toast("Cart cleared!", icon="🗑️")

# Function to confirm order
def confirm_order():
    if len(st.session_state.cart) > 0:
        st.session_state.order_confirmed = True
        st.session_state.order_number = f"ORD-{datetime.now().strftime('%Y%m%d')}-{hash(str(st.session_state.cart))%1000:03d}"
        # In a real application, you'd save the order to a database here
    else:
        st.warning("Your cart is empty!")

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

.menu-category {
    margin-bottom: 30px;
    animation: fadeIn 1.5s ease-in-out;
}

@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes slideIn {
    from { transform: translateX(-50px); opacity: 0; }
    to { transform: translateX(0); opacity: 1; }
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.dish-card {
    border: 1px solid #333;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
    background-color: #1e1e1e;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    animation: slideIn 0.6s ease-out forwards;
    opacity: 0;
}

.dish-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 16px rgba(255, 111, 97, 0.2);
}

.dish-image {
    width: 100%;
    height: 150px;
    object-fit: cover;
    border-radius: 10px;
    margin-bottom: 10px;
}

.dish-name {
    font-size: 18px;
    font-weight: 600;
    color: #ff6f61;
    margin-bottom: 5px;
}

.dish-price {
    font-size: 16px;
    color: #00ddff;
    margin-bottom: 10px;
    font-weight: 500;
}

.dish-description {
    color: #cccccc;
    font-size: 14px;
    margin-bottom: 15px;
    line-height: 1.4;
}

.btn-primary {
    background-color: #00aaff;  /* Cyan color */
    color: white;
    padding: 8px 16px;
    border-radius: 5px;
    border: none;
    transition: background-color 0.3s ease, transform 0.3s ease;
    margin: 5px;
    cursor: pointer;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    display: inline-block;
    text-align: center;
}

.btn-primary:hover {
    background-color: #0088cc;
    transform: translateY(-2px);
}

.btn-secondary {
    background-color: #8a2be2;  /* Purple color */
    color: white;
    padding: 8px 16px;
    border-radius: 5px;
    border: none;
    transition: background-color 0.3s ease, transform 0.3s ease;
    margin: 5px;
    cursor: pointer;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    display: inline-block;
    text-align: center;
}

.btn-secondary:hover {
    background-color: #7722aa;
    transform: translateY(-2px);
}

.cart-container {
    background-color: #1e1e1e;
    border-radius: 10px;
    padding: 20px;
    margin-top: 20px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    animation: fadeIn 1s ease-in-out;
}

.cart-item {
    display: flex;
    justify-content: space-between;
    padding: 10px 0;
    border-bottom: 1px solid #333;
}

.btn-confirm {
    background-color: #4CAF50;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    transition: background-color 0.3s ease, transform 0.3s ease;
    margin-top: 15px;
    cursor: pointer;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    animation: pulse 2s infinite;
    width: 100%;
    display: block;
}

.btn-confirm:hover {
    background-color: #388E3C;
    transform: translateY(-2px);
}

.btn-clear {
    background-color: #f44336;
    color: white;
    padding: 10px 20px;
    border-radius: 5px;
    border: none;
    transition: background-color 0.3s ease, transform 0.3s ease;
    margin-top: 15px;
    cursor: pointer;
    font-family: 'Poppins', sans-serif;
    font-weight: 500;
    width: 100%;
    display: block;
}

.btn-clear:hover {
    background-color: #d32f2f;
    transform: translateY(-2px);
}

.order-confirmation {
    background-color: #1e1e1e;
    border: 2px solid #4CAF50;
    border-radius: 10px;
    padding: 20px;
    margin-top: 20px;
    text-align: center;
    animation: fadeIn 1s ease-in-out;
}

.order-number {
    font-size: 24px;
    color: #4CAF50;
    font-weight: bold;
    margin: 10px 0;
}

/* Delay animation for each dish card */
.dish-card:nth-child(1) { animation-delay: 0.1s; }
.dish-card:nth-child(2) { animation-delay: 0.2s; }
.dish-card:nth-child(3) { animation-delay: 0.3s; }
.dish-card:nth-child(4) { animation-delay: 0.4s; }
.dish-card:nth-child(5) { animation-delay: 0.5s; }
.dish-card:nth-child(6) { animation-delay: 0.6s; }

/* Keep Streamlit buttons visible for functionality but make them less prominent */
.stButton > button {
    visibility: visible !important;
    position: relative;
    z-index: 1;
}

/* Style for custom buttons container */
.btn-container {
    display: flex;
    justify-content: space-between;
    margin-top: 10px;
}

/* Fix for overlapping elements */
div[data-testid="column"] {
    z-index: 0;
}
</style>
""", unsafe_allow_html=True)

# Page layout with two columns
col1, col2 = st.columns([2, 1])

with col1:
    # Page Title
    st.markdown('<h1 style="animation: fadeIn 1.5s ease-in-out;">🍽️ Our Menu</h1>', unsafe_allow_html=True)
    
    # Menu Categories with Dishes, Images, and Prices with proper descriptions
    menu = {
        "🍟 Starters": [
            {
                "name": "French Fries", 
                "price": "$5.99",
                "description": "Crispy golden fries served with a choice of tangy ketchup or creamy garlic mayo. Perfect for sharing or as a side dish.",
                "image": "https://static.toiimg.com/thumb/54659021.cms?imgsize=275086&width=800&height=800"  # Add your image URL here
            },
            {
                "name": "Garlic Bread", 
                "price": "$4.99",
                "description": "Freshly baked bread slices topped with our signature garlic butter and herbs, toasted to perfection with a hint of parmesan cheese.",
                "image": "https://www.sipandfeast.com/wp-content/uploads/2022/07/garlic-bread-recipe-snippet.jpg"  # Add your image URL here
            },
            {
                "name": "Spring Rolls", 
                "price": "$6.99",
                "description": "Delicate crispy rolls filled with vegetables, glass noodles, and aromatic herbs. Served with sweet chili dipping sauce.",
                "image": "https://saltedmint.com/wp-content/uploads/2024/01/Vegetable-Spring-Rolls-4-500x375.jpg"  # Add your image URL here
            },
        ],
        "🍕 Main Course": [
            {
                "name": "Margherita Pizza", 
                "price": "$12.99",
                "description": "Classic Italian pizza with San Marzano tomato sauce, fresh mozzarella, basil leaves, and extra virgin olive oil on our handmade thin crust.",
                "image": "https://cdn.shopify.com/s/files/1/0274/9503/9079/files/20220211142754-margherita-9920_5a73220e-4a1a-4d33-b38f-26e98e3cd986.jpg?v=1723650067"  # Add your image URL here
            },
            {
                "name": "Burger", 
                "price": "$9.99",
                "description": "Juicy 100% Angus beef patty topped with melted cheddar, crisp lettuce, tomato, caramelized onions, and our special sauce in a toasted brioche bun.",
                "image": "https://www.seriouseats.com/thmb/P0opRA7Movx8bqIAjXQHo7y6VeU=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/20230525-SEA-Wagyu-Burger-Amanda-Suarez-hero-54009c50b715486892bbed7a0edc829c.jpg"  # Add your image URL here
            },
            {
                "name": "Pasta", 
                "price": "$11.99",
                "description": "Al dente fettuccine tossed in a rich and creamy sauce with sautéed mushrooms, grilled chicken, and topped with fresh parsley and parmesan.",
                "image": "https://foodhub.scene7.com/is/image/woolworthsltdprod/Easy-chicken-and-bacon-pasta?wid=1300&hei=1300&fmt=png-alpha"  # Add your image URL here
            },
        ],
        "🍰 Desserts": [
            {
                "name": "Chocolate Cake", 
                "price": "$7.99",
                "description": "Decadent triple-layer chocolate cake with dark chocolate ganache frosting, served with a scoop of vanilla bean ice cream.",
                    "image": "https://www.hersheyland.com/content/dam/hersheyland/en-us/recipes/recipe-images/2-hersheys-perfectly-chocolate-chocolate-cake-recipe-hero.jpg"
                },
            {
                "name": "Ice Cream", 
                "price": "$4.99",
                "description": "Premium handcrafted ice cream in your choice of flavors: vanilla bean, rich chocolate, strawberry, or seasonal special. Served with wafer sticks.",
                "image": "https://www.sugarhero.com/wp-content/uploads/2023/07/doughnut-ice-cream-sundae-square-1-featured-image.jpg"  # Add your image URL here
            },
            {
                "name": "Cheesecake", 
                "price": "$8.99",
                "description": "Creamy New York style cheesecake with a buttery graham cracker crust, topped with fresh berry compote and a mint garnish.",
                "image": "https://www.simplyrecipes.com/thmb/QAY2WlJ6xMQMY6vrLVrlgZe7sfk=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Simply-Recipes-Perfect-Cheesecake-LEAD-6-97a8cb3a60c24903b883c1d5fb5a69d3.jpg"  # Add your image URL here
            },
        ],
    }
    
    # Display Menu with Interactive Buttons - Fixed approach
    for category, dishes in menu.items():
        st.markdown(f'<h2 class="menu-category">{category}</h2>', unsafe_allow_html=True)
        
        for i, dish in enumerate(dishes):
            dish_id = f"{category.split()[1]}_{i}".lower()  # Create unique ID for each dish
            
            # Use custom image URL or fallback to placeholder
            img_url = dish.get('image', f"/api/placeholder/{300 + i*10}/{200 + i*5}")
            
            # Display dish card
            st.markdown(f"""
            <div class="dish-card" id="{dish_id}">
                <img class="dish-image" src="{img_url}" alt="{dish['name']}">
                <div class="dish-name">{dish['name']}</div>
                <div class="dish-price">{dish['price']}</div>
                <div class="dish-description">{dish['description']}</div>
            </div>
            """, unsafe_allow_html=True)
            
            # Use direct Streamlit buttons for functionality
            col_add, col_view = st.columns(2)
            with col_add:
                if st.button(f"Add to Cart", key=f"add_{dish_id}"):
                    add_to_cart(dish['name'], dish['price'])
                    st.rerun()
                    
            with col_view:
                if st.button(f"View Details", key=f"view_{dish_id}"):
                    view_details(dish['name'], dish['description'], dish['price'], dish.get('image', f"/api/placeholder/{300 + i*10}/{200 + i*5}"))
                    st.rerun()
            
            # Add custom styling for the buttons
            st.markdown(f"""
            <style>
            button[key="add_{dish_id}"] {{
                background-color: #00aaff !important;
                color: white !important;
                border: none !important;
                padding: 0.5rem 1rem !important;
                border-radius: 5px !important;
                width: 100% !important;
                font-weight: 500 !important;
            }}
            
            button[key="view_{dish_id}"] {{
                background-color: #8a2be2 !important;
                color: white !important;
                border: none !important;
                padding: 0.5rem 1rem !important;
                border-radius: 5px !important;
                width: 100% !important;
                font-weight: 500 !important;
            }}
            </style>
            """, unsafe_allow_html=True)

with col2:
    # Cart Display
    st.markdown('<h2 style="animation: fadeIn 1.5s ease-in-out;">🛒 Your Cart</h2>', unsafe_allow_html=True)
    
    if st.session_state.order_confirmed:
        # Order Confirmation Display
        st.markdown(f"""
        <div class="order-confirmation">
            <h3>Order Confirmed! ✅</h3>
            <p>Thank you for your order.</p>
            <div class="order-number">{st.session_state.order_number}</div>
            <p>Your food will be ready shortly.</p>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("Place New Order"):
            st.session_state.cart = []
            st.session_state.order_confirmed = False
            st.session_state.order_number = None
            st.rerun()
    
    else:
        # Cart Items Display
        if len(st.session_state.cart) > 0:
            st.markdown('<div class="cart-container">', unsafe_allow_html=True)
            
            total = 0
            for item in st.session_state.cart:
                st.markdown(f"""
                <div class="cart-item">
                    <span>{item['name']} x{item['quantity']}</span>
                    <span>${item['price']:.2f}</span>
                </div>
                """, unsafe_allow_html=True)
                total += item['price'] * item['quantity']
            
            st.markdown(f"""
            <div class="cart-item" style="font-weight: bold; border-bottom: none;">
                <span>Total</span>
                <span>${total:.2f}</span>
            </div>
            </div>
            """, unsafe_allow_html=True)
            
            # Cart Buttons - Direct Streamlit approach
            col_confirm, col_clear = st.columns(2)
            with col_confirm:
                if st.button("Confirm Order", key="confirm_order_btn"):
                    confirm_order()
                    st.rerun()
                
                # Style the button
                st.markdown("""
                <style>
                button[key="confirm_order_btn"] {
                    background-color: #4CAF50 !important;
                    color: white !important;
                    border: none !important;
                    padding: 0.6rem 1rem !important;
                    border-radius: 5px !important;
                    width: 100% !important;
                    font-weight: 500 !important;
                }
                </style>
                """, unsafe_allow_html=True)
                
            with col_clear:
                if st.button("Clear Cart", key="clear_cart_btn"):
                    clear_cart()
                    st.rerun()
                
                # Style the button
                st.markdown("""
                <style>
                button[key="clear_cart_btn"] {
                    background-color: #f44336 !important;
                    color: white !important;
                    border: none !important;
                    padding: 0.6rem 1rem !important;
                    border-radius: 5px !important;
                    width: 100% !important;
                    font-weight: 500 !important;
                }
                </style>
                """, unsafe_allow_html=True)
        
        else:
            st.info("Your cart is empty. Add some delicious items!")
    
    # Item Detail View (if selected)
    if 'view_item' in st.session_state:
        item = st.session_state.view_item
        st.markdown('<h3 style="margin-top: 30px;">Item Details</h3>', unsafe_allow_html=True)
        
        # Use the image from the item or fallback to placeholder
        img_url = item.get('image', "/api/placeholder/400/250")
        
        st.markdown(f"""
        <div class="dish-card">
            <img class="dish-image" src="{img_url}" alt="{item['name']}">
            <div class="dish-name">{item['name']}</div>
            <div class="dish-price">{item['price']}</div>
            <div class="dish-description">{item['description']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Direct button for adding from detail view
        if st.button("Add to Cart", key=f"detail_add_{item['name'].lower().replace(' ', '_')}"):
            add_to_cart(item['name'], item['price'])
            st.rerun()
        
        # Style the button
        st.markdown(f"""
        <style>
        button[key="detail_add_{item['name'].lower().replace(' ', '_')}"] {{
            background-color: #00aaff !important;
            color: white !important;
            border: none !important;
            padding: 0.6rem 1rem !important;
            border-radius: 5px !important;
            width: 100% !important;
            font-weight: 500 !important;
        }}
        </style>
        """, unsafe_allow_html=True)