import streamlit as st  #streamlit run CostDecoder.py

# Mapping of numbers to letters
number_to_letter = {
    '0': 'O',
    '1': 'A',
    '2': 'B',
    '3': 'C',
    '4': 'D',
    '5': 'E',
    '6': 'F',
    '7': 'G',
    '8': 'H',
    '9': 'I'
}

# Reverse mapping from letters to numbers (for decoding)
letter_to_number = {v: k for k, v in number_to_letter.items()}



# Title of the app
st.title("Cost-Coder")

#info about tool

st.title('Make your product cost secret.')


# Initialize session state to store the multiplier
if 'multiplier' not in st.session_state:
    st.session_state['multiplier'] = 3.5  # Default value

# User selects either to Create Code or Decode
option = st.radio("Choose an option:", ("Create Code", "Decode"))

if option == "Create Code":
    st.header("Create Code")
    
    # Input for the number to encode
    number = st.number_input("Enter a number:", value=0)
    
    # Input for optional multiplier (default is 3.5)
    user_multiplier = st.number_input("Enter a multiplier (optional):", value=0.0, min_value=0.0, step=0.1)
    
    # If the user hasn't entered a multiplier, use the default (3.5)
    if user_multiplier == 0:
        multiplier = 3.5
    else:
        multiplier = user_multiplier

    # Store the multiplier in session state
    st.session_state['multiplier'] = multiplier
    
    if st.button("Generate Code"):
        # Step 1: Multiply the number by the preset or user multiplier
        multiplied_number = number * multiplier
        
        # Convert the multiplied number to an integer to avoid floating-point characters
        multiplied_number_str = str(int(multiplied_number))
        
        # Step 2: Convert the number to letters using the mapping
        encoded_string = ''.join([number_to_letter[digit] for digit in multiplied_number_str])
        
        # Display the encoded result
        st.write(f"Your Code is: {encoded_string}")

elif option == "Decode":
    st.header("Decode Code")
    
    # Input for the coded form to decode
    coded_form = st.text_input("Enter the coded form:").upper()
    
    # Use the saved multiplier from session state
    multiplier = st.session_state['multiplier']
    
    if st.button("Decode"):
        try:
            # Step 1: Reverse the mapping (letters back to numbers)
            decoded_number_str = ''.join([letter_to_number[letter] for letter in coded_form])
            
            # Step 2: Convert the decoded string back to a number
            decoded_number = int(decoded_number_str)
            
            # Step 3: Divide the decoded number by the stored multiplier
            original_number = decoded_number / multiplier
            
            # Display the decoded result
            st.write(f"Your Decoded Value is: {original_number}")
        except KeyError:
            st.error("Invalid coded form. Please ensure you entered valid letters corresponding to the encoded format.")
