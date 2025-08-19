import streamlit as st

# App title
st.title("🎢 Rollercoaster Ticket Calculator")
st.write("Welcome to the rollercoaster!")

# Height input
height = st.number_input("What is your height in cm?", min_value=0, max_value=300, value=120)

# Check if tall enough to ride
if height >= 120:
    st.success("You can ride the rollercoaster!")

    # Age input
    age = st.number_input("What is your age?", min_value=0, max_value=150, value=18)

    # Calculate ticket price based on age
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12

    st.info(f"Your ticket price is ${bill}")

    # Photo service option
    photo_answer = st.radio(
        "Would you like a photo service for an extra $3?",
        ["No", "Yes"]
    )

    # Calculate photo charge
    photo_charge = 3 if photo_answer == "Yes" else 0

    if photo_answer == "Yes":
        st.write("✅ You have chosen to opt-in for the photo service")
    else:
        st.write("❌ You have chosen to skip the photo service")

    # Display total bill
    total_bill = bill + photo_charge

    st.markdown("---")
    st.subheader("💰 Bill Summary")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Ticket", f"${bill}")
    with col2:
        st.metric("Photo Service", f"${photo_charge}")
    with col3:
        st.metric("Total", f"${total_bill}", delta=f"+${photo_charge}" if photo_charge > 0 else None)

    st.success(f"Your total bill is ${total_bill}")

else:
    st.error("Sorry, you have to grow taller before you can ride. Come back later!")
    st.info("Minimum height requirement: 120 cm")