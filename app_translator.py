import streamlit as st
from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

def translate_hindi_to_french(input_text):
    model = MBartForConditionalGeneration.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")
    tokenizer = MBart50TokenizerFast.from_pretrained("facebook/mbart-large-50-many-to-many-mmt")

    # Set source language to Hindi
    tokenizer.src_lang = "hi_IN"
    encoded_input = tokenizer(input_text, return_tensors="pt")

    # Generate translation
    generated_tokens = model.generate(
        **encoded_input,
        forced_bos_token_id=tokenizer.lang_code_to_id["hi_IN"]  # Target language French
    )

    # Decode and return translated text
    translated_text = tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)[0]
    return translated_text

def main():
    st.title("Hindi to French Translator")

    # Input text area
    input_text = st.text_area("Enter text in Hindi:", height=200)

    # Translate button
    if st.button("Translate"):
        if input_text:
            translated_text = translate_hindi_to_french(input_text)
            st.success("Corrected Text (Hindi):")
            st.text(translated_text)
        else:
            st.warning("Please enter some text to translate.")

if __name__ == "__main__":
    main()
