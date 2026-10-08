import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Restaurant Bill Generator",
    page_icon="🍽️",
    layout="centered"
)

st.title("🍽️ Restaurant Bill Generator")
st.subheader("Create Your Delicious Bill 😋")

menu = {
    "🍕 Pizza": 250,
    "🍔 Burger": 150,
    "🍟 French Fries": 100,
    "🌮 Tacos": 180,
    "🍝 Pasta": 200,
    "🍗 Chicken Biryani": 280,
    "🥤 Soft Drink": 60,
    "☕ Coffee": 80,
    "🍨 Ice Cream": 120
}

st.sidebar.header("🍴 Select Food Items")

selected_items = {}

for item, price in menu.items():
    quantity = st.sidebar.number_input(
        f"{item} - ₹{price}",
        min_value=0,
        max_value=20,
        value=0,
        step=1
    )

    if quantity > 0:
        selected_items[item] = {
            "price": price,
            "quantity": quantity
        }

st.sidebar.header("💰 Offers")

discount_percent = st.sidebar.slider(
    "Discount (%)",
    min_value=0,
    max_value=30,
    value=0
)

gst_percent = st.sidebar.slider(
    "GST (%)",
    min_value=0,
    max_value=18,
    value=5
)

if st.button("🧾 Generate Bill", use_container_width=True):

    if not selected_items:
        st.warning("⚠️ Please select at least one food item.")
    else:
        subtotal = 0

        st.success("✅ Bill Generated Successfully!")

        st.markdown("---")
        st.subheader("🧾 RESTAURANT BILL")

        st.write(
            f"**Date:** {datetime.now().strftime('%d-%m-%Y %I:%M %p')}"
        )

        st.markdown("---")

        col1, col2, col3, col4 = st.columns(4)

        col1.markdown("**Item**")
        col2.markdown("**Qty**")
        col3.markdown("**Price**")
        col4.markdown("**Total**")

        for item, details in selected_items.items():

            price = details["price"]
            quantity = details["quantity"]
            total = price * quantity

            subtotal += total

            col1, col2, col3, col4 = st.columns(4)

            col1.write(item)
            col2.write(quantity)
            col3.write(f"₹{price}")
            col4.write(f"₹{total}")

        st.markdown("---")

        discount_amount = subtotal * discount_percent / 100
        amount_after_discount = subtotal - discount_amount

        gst_amount = amount_after_discount * gst_percent / 100

        grand_total = amount_after_discount + gst_amount

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Subtotal:**")
            st.write("**Discount:**")
            st.write("**Amount After Discount:**")
            st.write("**GST:**")
            st.write("**Grand Total:**")

        with col2:
            st.write(f"₹{subtotal:.2f}")
            st.write(f"- ₹{discount_amount:.2f}")
            st.write(f"₹{amount_after_discount:.2f}")
            st.write(f"₹{gst_amount:.2f}")
            st.success(f"### ₹{grand_total:.2f}")

        st.markdown("---")

        st.info("🙏 Thank you for dining with us! Visit Again ❤️")

        st.balloons()