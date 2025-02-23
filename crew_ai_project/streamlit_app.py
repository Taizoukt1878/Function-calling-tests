import sys
import streamlit as st
from logger import setup_logger
from chat_logs import run_and_log_crew

__import__('pysqlite3')
sys.modules['sqlite3'] = sys.modules.pop('pysqlite3')


def main():

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Initialize session state
    if 'current_tool' not in st.session_state:
        st.session_state.current_tool = "None"
    if 'last_update' not in st.session_state:
        st.session_state.last_update = None
    
    # Setup logger
    logger = setup_logger()
    
    # Header
    st.title("Crew AI Assistant 🤖")
    st.markdown("---")
    
    # Display current tool usage
    col1 = st.sidebar
    with col1:
        st.subheader("Current Tool")
        tool_placeholder = st.empty()

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
                tool_placeholder.write(st.session_state.current_tool)
                logger.info(f"Processing user input: {user_input}")
                response = run_and_log_crew(user_input)
                logger.info(f"Crew AI response: {response.raw}")
                print(response)
            # Display assistant response
            with st.chat_message("assistant"):
                st.markdown(response)
            st.session_state.chat_history.append({"role": "assistant", "content": response.raw})
            
        except Exception as e:
            logger.error(f"Error processing request: {str(e)}")
            st.error(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()