#!/usr/bin/env python
# coding: utf-8

# In[1]:


from dotenv import load_dotenv


# In[2]:


load_dotenv()


# In[4]


# In[5]:


import streamlit as st
import os
from PIL import Image  # Avoid using the variable name 'Image' to prevent conflicts
import pathlib
import google.generativeai as genai  # type: ignore


# In[6]:


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# In[7]:


model = genai.GenerativeModel(model_name="gemini-1.5-flash")


# In[8]:


def gemini_response(input_text, image, prompt):
    response = model.generate_content([input_text, image[0], prompt])
    return response.text


# In[9]:


def input_image_details(uploaded_file):
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


# In[10]:


st.set_page_config(page_title="Medical Report Extraction")

st.header("MEDGEM")


# In[11]:


user_input = st.text_input("Input Prompt: ", key="input")

# Upload the file
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

# Initialize the Image variable
image = None


# In[12]:


if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)  # Display image with PIL

submit = st.button("Tell me about the invoice")

input_prompts = """Analyze the attached image of the medical report/blood test report. 
Give me answer based on my questions based on provided image answered must be correct. Give health advice if asked otherwise dont "
"""


# In[13]:


if submit:
    try:
        image_data = input_image_details(uploaded_file)
        response = gemini_response(user_input, image_data, input_prompts)  # Call the correct function
        st.subheader("The Response is")
        st.write(response)
    except FileNotFoundError as e:
        st.error(f"Error: {e}")
    except Exception as e:
        st.error(f"An unexpected error occurred: {e}")


# In[ ]:




