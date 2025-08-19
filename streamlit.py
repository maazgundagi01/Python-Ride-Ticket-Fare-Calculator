import streamlit as st

# Initialize session state variables
if 'step' not in st.session_state:
    st.session_state.step = 1
if 'height' not in st.session_state:
    st.session_state.height = None
if 'age' not in st.session_state:
    st.session_state.age = None
if 'photo_choice' not in st.session_state:
    st.session_state.photo_choice = None

# App title
st.title("🎢 Rollercoaster Ticket Calculator")
st.write("Welcome to the rollercoaster!")

# Step 1: Height
if st.session_state.step == 1:
    st.subheader("Step 1: Height Check")
    height = st.number_input("What is your height in cm?", min_value=0, max_value=300, value=120)

    if st.button("Submit Height"):
        st.session_state.height = height
        if height >= 120:
            st.session_state.step = 2
            st.rerun()
        else:
            st.session_state.step = "too_short"
            st.rerun()

# Step 2: Age (only if tall enough)
elif st.session_state.step == 2:
    st.success("You can ride the rollercoaster!")
    st.subheader("Step 2: Age")
    age = st.number_input("What is your age?", min_value=0, max_value=150, value=18)

    if st.button("Submit Age"):
        st.session_state.age = age
        st.session_state.step = 3
        st.rerun()

# Step 3: Photo service
elif st.session_state.step == 3:
    # Calculate ticket price
    age = st.session_state.age
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12

    st.info(f"Your ticket price is ${bill}")
    st.subheader("Step 3: Photo Service")
    photo_choice = st.radio(
        "Would you like a photo service for an extra $3?",
        ["Yes", "No"]
    )

    if st.button("Submit Photo Choice"):
        st.session_state.photo_choice = photo_choice
        st.session_state.step = 4
        st.rerun()

# Step 4: Final bill
elif st.session_state.step == 4:
    age = st.session_state.age
    photo_choice = st.session_state.photo_choice

    # Calculate prices
    if age <= 12:
        bill = 5
    elif age <= 18:
        bill = 7
    else:
        bill = 12

    photo_charge = 3 if photo_choice == "Yes" else 0
    total_bill = bill + photo_charge

    # Show summary
    st.subheader("🎫 Your Order Summary")
    st.write(f"**Height:** {st.session_state.height} cm ✅")
    st.write(f"**Age:** {age} years old")
    st.write(f"**Ticket:** ${bill}")

    if photo_choice == "Yes":
        st.write("**Photo Service:** ✅ You have chosen to opt-in for the photo service")
        st.write(f"**Photo Cost:** ${photo_charge}")
    else:
        st.write("**Photo Service:** ❌ You have chosen to skip the photo service")

    st.markdown("---")
    st.success(f"**Your total bill is: Ticket(${bill}) + Extra Charge(${photo_charge}) = ${total_bill}**")

    if st.button("Start Over"):
        # Reset all session state
        for key in ['step', 'height', 'age', 'photo_choice']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# Too short to ride
elif st.session_state.step == "too_short":
    st.error("Sorry, you have to grow taller before you can ride. Come back later!")
    st.info("Minimum height requirement: 120 cm")

    if st.button("Try Again"):
        # Reset session state
        for key in ['step', 'height', 'age', 'photo_choice']:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()