import streamlit as st
import subprocess
import os
from pathlib import Path

st.set_page_config(page_title="Career Guidance", layout="centered")

st.title("Career Guidance")
st.write("Enter your queries and click **Submit** to get guidance")

prompt = st.text_area(
    "Your prompt",
    placeholder="Please enter your query here",
    height=160
)

if st.button("Submit"):
    if not prompt or not prompt.strip():
        st.warning("Please enter the prompt")
    else:
        with st.spinner("Calling you guidance agent"):
            env = os.environ.copy()
            env["PROMPT"] = prompt

            python_executable = os.environ.get("PYTHON_EXECUTABLE", "python")
            main_py = Path(__file__).with_name("main.py")
            
            try:
                process = subprocess.run(
                    [python_executable, str(main_py)],
                    capture_output=True,
                    text=True,
                    env=env,
                    timeout=120
                )
            except:
                st.error("Some error occured!")
            else:
                output_markdown = process.stdout.strip()
                if output_markdown:
                    st.subheader("Agent Response:")
                    st.markdown(output_markdown)
