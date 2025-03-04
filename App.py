import streamlit as st
import random

def generate_email(recipient_name, event_details, special_instructions):
    greetings = [
        f"Dear {recipient_name},",
        f"Hello {recipient_name},",
        f"Hi {recipient_name},",
    ]
    
    event_detail_options = [
        f"We are excited to invite you to {event_details['event_name']} on {event_details['event_date']} at {event_details['event_time']}.",
        f"You are cordially invited to {event_details['event_name']} on {event_details['event_date']} at {event_details['event_time']}.",
        f"Join us for {event_details['event_name']} on {event_details['event_date']} at {event_details['event_time']}.",
    ]
    
    special_instruction_options = [
        f"Please note that {special_instructions}.",
        f"Important: {special_instructions}.",
        f"Don't forget: {special_instructions}.",
    ]
    
    closings = [
        "Best regards,",
        "Sincerely,",
        "Thank you,",
    ]
    
    greeting = random.choice(greetings)
    event_detail = random.choice(event_detail_options)
    special_instruction = random.choice(special_instruction_options)
    closing = random.choice(closings)
    
    email = f"""
{greeting}

{event_detail}

{special_instruction}

{closing}
[Your Name]
"""
    
    return email

st.title("Personalized Email Generator")
recipient_name = st.text_input("Enter the recipient's name:")
event_name = st.text_input("Enter the event name:")
event_date = st.text_input("Enter the event date:")
event_time = st.text_input("Enter the event time:")
special_instructions = st.text_area("Enter any special instructions:")

if st.button("Generate Email"):
    event_details = {
        "event_name": event_name,
        "event_date": event_date,
        "event_time": event_time,
    }
    email = generate_email(recipient_name, event_details, special_instructions)
    st.subheader("Generated Email:")
    st.text_area("", email, height=200)
