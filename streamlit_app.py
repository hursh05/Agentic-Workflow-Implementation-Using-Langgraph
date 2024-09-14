

import streamlit as st
from app import run_agentic_workflow

st.title("Agentic Workflow with Langgraph")
query = st.text_input("Enter your query")

if st.button("Submit"):
    if query:
        results = run_agentic_workflow(query)
        for result in results:
            st.write(result)
    else:
        st.write("Please enter a valid query.")
