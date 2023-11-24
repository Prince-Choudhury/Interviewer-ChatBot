import streamlit as st
from dotenv import load_dotenv
from langchain.llms import OpenAI
import time
from PIL import Image  
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts.chat import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
import base64

# Set page configuration
st.set_page_config(
    page_title="Interviewer ChatBot",
    page_icon=Image.open("logo.png"),
    layout="wide",
)

# Add custom CSS for styling
app_css = """
    body {
        background-color: #f0f0f0;
    }
    .container {
        display: flex;
        align-items: center;
    }
    .logo-text {
        font-weight: bold;
        font-size: 40px;
        margin-left: 10px;
        color: #4e8cff; /* Set your desired color */
    }
    .logo-img {
        margin-right: 20px;
    }
    .col-container {
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .iframe-container {
        overflow: hidden;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .question-container {
        padding: 20px;
        margin-top: 10px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
"""

# Apply custom CSS
st.markdown(f'<style>{app_css}</style>', unsafe_allow_html=True)

# App Heading
st.markdown(
    """
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{0}" width=70 height=70>
        <p class="logo-text">CareerForge 🚀 Interview Assistant</p>
    </div>
    """.format(base64.b64encode(open("logo.png", "rb").read()).decode()),
    unsafe_allow_html=True,
)

# Load environment variables
load_dotenv()

def main():
    # Initialize chats
    if "currentChat" not in st.session_state:
        st.session_state.currentChat = []
        st.session_state.count = 0

        # Initialize OpenAI language model
        llm = OpenAI()

        # Define the prompt template
        prompt_template_name = PromptTemplate(
            input_variables=['input'],
            template='''You are an interviewer, interviewing the user for a junior level job role. 
                You should start the interview by asking the user's 
                name and the specific job role they have applied for if they haven't mentioned. 
                Always address the user by the name they specify. If the user hasn't mentioned the job role, 
                ask for the job role until it hasn't been given by the user. You should ask one question at a time. 
                You should stop the interview after 5 questions 
                Your should let the user know that their interview is over and thank the user for 
                their time and tell them that you will let them know the results of the soon via mail. 
                Give the user a feedback of the interview only if the user asks and it should be at the end of the interview.

                {input}
                '''
        )

        # Initialize conversation memory
        st.session_state.memory = ConversationBufferWindowMemory(input_key='input')

        # Initialize language model chain
        st.session_state.chain = LLMChain(llm=llm, prompt=prompt_template_name, memory=st.session_state.memory)

    # Sidebar content
    with st.sidebar:
        # Add a different chatbot symbol (emoji) next to the title
        st.title('Interviewer Chatbot 🤵')

        # Add a short and engaging tagline for your application
        st.markdown('Your Intelligent Interviewer chatbot')

        # Add a horizontal rule for separation
        st.markdown('---')

        # Add additional information or links if needed
        st.markdown('Built with ❤️ by [Prince Choudhury](https://www.linkedin.com/in/prince-choudhury26/)')

        # Optionally, provide a link to your GitHub repository
        st.markdown('[GitHub Repo](https://github.com/Prince-Choudhury)')

        # Create a button to exit and start a new interview
        if st.button('Exit and start new interview'):
            st.session_state.currentChat = []
            st.session_state.count = 0

    # Display chat messages from history on app rerun
    for message in st.session_state.currentChat:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    if user_input := st.chat_input("What would you like to discuss today?"):
        if st.session_state.count == 0:
            st.session_state.intro = user_input
        if st.session_state.count == 1:
            st.session_state.job = user_input
        st.session_state.count = st.session_state.count + 1

        # Add user message to chat history
        st.session_state.currentChat.append({"role": "user", "content": user_input})

        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(user_input)

        if st.session_state.count >= 2:
            # Display assistant response in chat message container
            with st.chat_message("assistant"):
                message_placeholder = st.empty()
                full_response = ""

                if st.session_state.count == 2:
                    response = st.session_state.chain(
                        {"input": f"Welcome! As the interviewer for the role '{st.session_state.intro}', introduce yourself and ask the candidate about their job preferences. Begin the interview process."})
                if st.session_state.count > 2:
                    if st.session_state.count == 6:
                        response = st.session_state.chain(
                            {"input": f"The candidate's response to the previous question was: '{user_input}'. You can now conclude the interview and provide feedback based on the conversation."})
                    else:
                        response = st.session_state.chain(
                            {"input": f"The candidate's response to the previous question was: '{user_input}'. Now, provide a thoughtful response and proceed to the next interview question."})

                assistant_response = response['text']

            # Add assistant response to chat history
            st.session_state.currentChat.append({"role": "assistant", "content": assistant_response})


    if st.session_state.count == 0:
        st.session_state.currentChat.append(
            {"role": "assistant",
             "content": "Hello! I am the Professional Interviewer Chatbot. I'm here to help you practice interviews in your chosen domain. Please provide a brief introduction :"})
        with st.chat_message("assistant"):
            st.markdown(
                "Hello! I am the Professional Interviewer Chatbot. I'm here to help you practice interviews in your chosen domain. Please provide a brief introduction :")

    if st.session_state.count == 1:
        st.session_state.currentChat.append(
            {"role": "assistant", "content": "What job role are you looking for?"})
        with st.chat_message("assistant"):
            st.markdown("What job role are you looking for?")


if __name__ == '__main__':
    main()
