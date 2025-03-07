import streamlit as st

from callBedRock import call_bedrock_service # Import function from callBedRock.py
 # Load image
image_path = "CertExLogo.png" 

# Create a two-column layout
col1, col2 = st.columns([2, 8])

# Initialize session state variables
#if "user_input" not in st.session_state:
#    st.session_state.user_input = ""

# Function to clear input after submission
def clear_text():
    #st.session_state.user_input = ""  # Reset input
    st.session_state.my_text = st.session_state.widget
    st.session_state.widget = ""

############# Streamlit UI #############
# Display image in the first column
with col1:
    st.image(image_path, width=500)  # Adjust width as needed

# Display header in the second column
with col2:
    st.title("Check my certs")

#user_input = st.text_area("Enter your prompt:", key="widget", on_change=clear_text)
st.text_area("Enter your prompt:", key="widget", on_change=clear_text)
user_input = st.session_state.get('my_text', '')

if st.button("Generate Response"):
    if user_input.strip():
        output = call_bedrock_service(user_input)
        st.write(f"🙋🏻‍♂️🙋‍♀️ **Query:** {user_input}")
        st.write("### Response:")
        st.write(f"🤖 **Bot:** {output}")        
    else:
        st.warning("Please enter a prompt!")












 