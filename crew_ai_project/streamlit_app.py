import streamlit as st
from crew_setup import crew
from logger import setup_logger
import sys

__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')

def main():

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    
    # Setup logger
    logger = setup_logger()
    
    # Header
    st.title("Crew AI Assistant 🤖")
    st.markdown("---")
    
    # Chat interface
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Input field
    user_input = st.chat_input("Ask something...")
    
    if user_input:
        # Display user message
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        
        # Get Crew AI response
        try:
            with st.spinner("Thinking..."):
                logger.info(f"Processing user input: {user_input}")
                response = crew.kickoff(inputs={"user_input": user_input})
                print(response)
            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response})
            
        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()