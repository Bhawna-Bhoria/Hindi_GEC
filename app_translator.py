import streamlit as st
from googletrans import Translator

translator = Translator()

# Function to correct grammar in Hindi
def correct_grammar_hindi(text_to_check):
    test = translator.translate(text_to_check).text
    test2 = translator.translate(test, src='hi', dest='en').text
    result = translator.translate(test2, src='en', dest='hi').text
    return result

def main():
    st.title("Grammar Correction (Hindi)")

    # Header with developer details
    st.markdown(
        """
        Developed by **Bhawna Bhria** (M22MA003) under the guidance of **Dr. Gaurav Harit**.
        """
    )

    # Input text area
    input_text = st.text_area("Enter text to correct grammar (Hindi):", height=200)

    # Correct Grammar button
    if st.button("Correct Grammar"):
        if input_text:
            # Call function to correct grammar
            corrected_text = correct_grammar_hindi(input_text)
            # Display corrected text
            st.success("Corrected Text:")
            st.text(corrected_text)
        else:
            st.warning("Please enter some text to correct.")

if __name__ == "__main__":
    main()
