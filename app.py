import streamlit as st
from dotenv import load_dotenv
import os
from groq import Groq
from PIL import Image
import base64

# -----------------------------------
# Load environment variables
# -----------------------------------

load_dotenv()

# -----------------------------------
# Create Groq client
# -----------------------------------

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


# -----------------------------------
# Encode image to Base64
# -----------------------------------

def encode_image(image_file):

    image_bytes = image_file.getvalue()

    return base64.b64encode(image_bytes).decode("utf-8")


# -----------------------------------
# Get response from Groq
# -----------------------------------

def get_response(question, image_file):

    image_base64 = encode_image(image_file)

    response = client.chat.completions.create(

        model="qwen/qwen3.6-27b",

        messages=[
            {
                "role": "system",

                "content": """
                You are an AI assistant specialized in invoice analysis.

                Analyze the uploaded invoice image and answer the
                user's question accurately.

                Extract information such as:

                - Invoice number
                - Invoice date
                - Vendor name
                - Customer name
                - Products or services
                - Quantity
                - Price
                - Tax
                - Total amount

                If the requested information is not present in the
                invoice, clearly say that it is not available.
                """
            },

            {
                "role": "user",

                "content": [

                    {
                        "type": "text",
                        "text": question
                    },

                    {
                        "type": "image_url",

                        "image_url": {
                            "url": f"data:image/jpeg;base64,{image_base64}"
                        }
                    }
                ]
            }
        ],

        temperature=0.2,

        max_completion_tokens=1024
    )

    return response.choices[0].message.content


# ===================================
# Streamlit UI
# ===================================

st.title("🤖 AI Vision Chatbot")

st.header("Invoice Analysis and Question Answering")


# -----------------------------------
# User question
# -----------------------------------

input_text = st.text_input(
    "Ask a question about the invoice:"
)


# -----------------------------------
# Upload invoice
# -----------------------------------

uploaded_file = st.file_uploader(
    "Upload Invoice",
    type=["png", "jpg", "jpeg"]
)


# -----------------------------------
# Display uploaded image
# -----------------------------------

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Invoice",
        use_container_width=True
    )


# -----------------------------------
# Submit button
# -----------------------------------

submit_button = st.button("Submit")


# -----------------------------------
# Process request
# -----------------------------------

if submit_button:

    if uploaded_file is None:

        st.warning(
            "Please upload an invoice image."
        )

    elif not input_text:

        st.warning(
            "Please enter a question."
        )

    else:

        try:

            with st.spinner("Analyzing invoice..."):

                answer = get_response(
                    input_text,
                    uploaded_file
                )

            st.subheader("🤖 AI Response")

            st.write(answer)

        except Exception as e:

            st.error(f"Error: {e}")