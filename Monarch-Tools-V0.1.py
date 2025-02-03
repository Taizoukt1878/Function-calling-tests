import streamlit as st
import json
from openai import OpenAI
from tools import FUNC_TOOLS
from utils import fetch_results
import os
# from config import MARKET_DATA

TOOLS = FUNC_TOOLS


tool_call_cache = {}  # Caches results of (tool_name, arguments_as_string) -> result


def handle_user_input(user_input):
    """
    Runs an 'agent loop':
    1) Construct a conversation with system instructions + user input (+ optional previous steps).
    2) Ask the LLM what to do (which tools to call or produce a final answer).
    3) If LLM calls tools, execute them, append results, re-ask until LLM finalizes answer.
    4) Display reasoning steps in real-time using a placeholder.
    """
    # --- Prepare a placeholder to display reasoning in real-time ---
    reasoning_placeholder = st.empty()

    # System Prompt: Encourage multi-tool usage if relevant
    system_instructions = (
        "You are SPECTgent, a superpowerful AI who is sarcastic about crypto. "
        "You have access to multiple tools. For complex queries, call all relevant tools , don't add extra tools that aren't relevant "
        "Do not finalize your answer until you have used all the tools you need "
        "Once done, produce a professional, easy-to-understand final answer. No introductions. "
    )

    conversation = [
        {"role": "system", "content": system_instructions},
        {"role": "user", "content": user_input},
    ]

    # Create and configure your LLM client
    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=os.getenv(
            "OPENAI_API_KEY",
            "provide an API KEY",
        ),
    )

    max_iterations = 5
    iteration = 0

    # Use the spinner to show a circle loader while processing
    with st.spinner("Thinking..."):
        while iteration < max_iterations:
            iteration += 1

            # (Optional) Update the reasoning placeholder to show progress
            reasoning_placeholder.markdown(
                f"**Monarch Thinking:** Iteration {iteration} - Checking what to do next..."
            )

            # Ask the LLM for the next step
            chat_completion = client.chat.completions.create(
                model="meta/llama-3.1-70b-instruct",
                messages=conversation,
                tools=TOOLS,  # Make sure TOOLS is defined elsewhere
                tool_choice="auto",
                temperature=0.85,
                top_p=0.8,
                max_tokens=4096,
                stream=False,
            )

            response = chat_completion.choices[0].message
            print(response)
            # Show the LLM's immediate response as part of the reasoning
            reasoning_placeholder.markdown(
                "**Monarch Thinking:** Received instructions from the LLM..."
            )

            # Check if the LLM returned tool calls
            if hasattr(response, "tool_calls") and response.tool_calls:
                for tool_call in response.tool_calls:
                    tool_name = tool_call.function.name

                    # Attempt to parse arguments from JSON
                    try:
                        arguments = json.loads(tool_call.function.arguments)
                    except Exception:
                        arguments = tool_call.function.arguments

                    # Convert arguments to a JSON string (or any hashable form) for caching
                    args_str = json.dumps(arguments, sort_keys=True)

                    reasoning_placeholder.markdown(
                        f"**Monarch Thinking:** Calling tool `{tool_name}` with {arguments}..."
                    )

                    # Check cache first
                    if (tool_name, args_str) in tool_call_cache:
                        tool_result = tool_call_cache[(tool_name, args_str)]
                    else:
                        # If not in cache, fetch and store result
                        tool_result = fetch_results(tool_name, arguments)
                        tool_call_cache[(tool_name, args_str)] = tool_result
                    # New changes
                    if tool_name == "get_market_data":
                        # Wait for user to select market data to display
                        if (
                            "tokens" not in st.session_state
                            or not st.session_state["continue"]
                        ):
                            # st.session_state["selected_data"] = st.multiselect(
                            #     "Select market data to display:",
                            #     options=MARKET_DATA,  # The same logic will be used for the token names
                            #     #
                            # )
                            st.session_state["tokens"] = st.multiselect(
                                "Select tokens to display:",
                                options=[item["name"] for item in tool_result],
                            )

                            st.session_state["continue"] = False
                            st.button(
                                "Continue",
                                on_click=lambda: st.session_state.update(
                                    {"continue": True}
                                ),
                            )
                            return "Waiting for user input..."
                    else:
                        st.session_state["continue"] = (
                            False  # Reset for next possible input
                        )
                    # Add the tool's result so the LLM can see it on the next iteration
                    if "selected_data" in st.session_state:
                        # selected_data = st.session_state["selected_data"]
                        selected_tokens = st.session_state["tokens"]
                        conversation.append(
                            {
                                "role": "assistant",
                                "content": f"Tool '{tool_name}' returned: {json.dumps(tool_result)} only about the  tokens named: {selected_tokens}",
                            }
                        )
                    else:
                        conversation.append(
                            {
                                "role": "assistant",
                                "content": f"Tool '{tool_name}' returned: {json.dumps(tool_result)} ",
                            }
                        )

                # Loop again so the LLM can incorporate these results
                continue
            else:
                # If no tool calls, this should be the final answer
                final_text = response.content or ""
                final_text = final_text.strip()

                # Optionally convert single line breaks to double line breaks
                # so that Markdown renders paragraphs properly:
                final_text = final_text.replace("\n", "\n\n")

                # Clear the reasoning placeholder
                reasoning_placeholder.empty()
                # empty selected_data from session state
                if "tokens" in st.session_state:
                    # del st.session_state["selected_data"]
                    del st.session_state["tokens"]

                return final_text

        # If we exit the loop (too many iterations), return partial.
        reasoning_placeholder.empty()
        return "I'm sorry, I'm stuck in a loop. (No final answer was produced.)"


def main():
    st.title("Spectre AI - Monarch AI Agent")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    user_input = st.text_input("Ask me something:")
    print(user_input)
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        response = handle_user_input(user_input)  # <-- Your existing logic
        st.session_state.messages.append({"role": "bot", "content": response})

    # Display the conversation
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.write(f"**You:** {message['content']}")
        else:
            # Apply text cleanup for better formatting
            bot_text = message["content"].strip()
            # Convert single newlines to double newlines for paragraphs
            bot_text = bot_text.replace("\n", "\n\n")
            bot_text = bot_text.replace("$", "\\$")
            st.markdown(f"**Bot:** {bot_text}")


if __name__ == "__main__":
    main()
