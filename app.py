import streamlit as st
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers

## Function to get response from LLAma 2 model
def getLLamaresponse(input_text, no_words, blog_style):
    # Calling the llama model
    llm = CTransformers(model="C:\\Users\\malviyak\\Documents\\kalpit\\python\\LLM\\llama-2-7b-chat.ggmlv3.q8_0.bin",
                        model_type='llama',
                        config={'max_new_tokens': 256,
                                'temperature': 0.01})
    
    ## Prompt Template
    template="""
        Write a blog for {blog_style} job profile for a topic {input_text}
        within {no_words} words.
            """
    
    # Creating a PromptTemplate with placeholders for input variables
    prompt = PromptTemplate(input_variables=["blog_style", "input_text", 'no_words'],
                            template=template)
    
    ## Generate the response from the LLama 2 model
    response = llm(prompt.format(blog_style=blog_style, input_text=input_text, no_words=no_words))
    print(response)  # Printing the response for debugging purposes
    return response

# Streamlit page configuration
st.set_page_config(page_title="Generate Blogs",
                    page_icon='🤖',
                    layout='centered',
                    initial_sidebar_state='collapsed')

# Header
st.header("Generate Blogs 🤖")

# Input fields
input_text = st.text_input("Enter the Blog Topic")

# Creating two columns for additional fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')

with col2:
    blog_style = st.selectbox('Writing the blog for', ('Researchers', 'Data Scientist', 'Common People'), index=0)

# Button to trigger blog generation
submit = st.button("Generate")

## Final response
if submit:
    # Displaying the generated response
    st.write(getLLamaresponse(input_text, no_words, blog_style))



