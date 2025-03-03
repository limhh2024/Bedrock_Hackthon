import streamlit as st
from callBedRock import call_bedrock_service # Import function from callBedRock.py
 # Load image
image_path = "certExLogo.png" 

# Create a two-column layout
col1, col2 = st.columns([2, 8]) 

############# Streamlit UI #############
#st.title("Certificate Details Chatbot")

# Display image in the first column
with col1:
    st.image(image_path, width=500)  # Adjust width as needed

# Display header in the second column
with col2:
    st.title("Check my certs")

user_input = st.text_area("Enter your prompt:")

if st.button("Generate Response"):
    if user_input:
        output = call_bedrock_service(user_input)
        st.write("### Response:")
        st.write(output)
    else:
        st.warning("Please enter a prompt!")