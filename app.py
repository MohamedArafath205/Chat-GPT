import streamlit as st
import openai


st.set_page_config(page_title="Chat GPT", page_icon=":tada:", layout="wide")

# ---- Header ----

st.subheader("""
            HI :wave:, 
            I am Mohamed Arafath an AIML student at SRM Institue of Science and Technology. 
            I am a Jack of all cards! 
            I know Machine Learning and Intrested to learn more about web developement""")
st.title("This is my [GitHub](https://github.com/MohamedArafath205) follow me!")

title = st.text_input("Ask me anything...")


openai.api_key = "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"


response = openai.Completion.create(
  model="text-davinci-003",
  prompt=title,
  temperature=0,
  max_tokens=60,
  top_p=1,
  frequency_penalty=0.5,
  presence_penalty=0
)
if st.button('Enter'):
    st.success(response.choices[0].text)
