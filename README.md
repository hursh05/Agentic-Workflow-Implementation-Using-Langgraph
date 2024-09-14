# Agentic-Workflow-Implementation-Using-Langgraph
Overview
This repository contains the implementation of an agentic workflow using Langgraph. The project is designed to break down a user query into manageable sub-tasks using a PlanAgent and iteratively refine these sub-tasks (modify, delete, or add) with a ToolAgent. The workflow integrates feedback loops and reflection mechanisms to ensure task reliability and completion.

The main architecture is split into two loops:

Outer Loop: Handles task breakdown, refinement, and feedback iteration.
Inner Loop: Manages task execution using tool dispatch and retrieval.

Key Components
PlanAgent: Splits a complex user query into sub-tasks and manages their refinement (modification, deletion, and addition).
ToolAgent: Retrieves the appropriate tools (language models, APIs, etc.) to solve the sub-tasks.
Feedback and Reflection: The workflow implements feedback loops to refine the sub-tasks and improve accuracy and reliability.
Features
Task Breakdown: The PlanAgent splits user queries into a set of manageable sub-tasks.
Iterative Refinement: Modify, delete, or add sub-tasks based on feedback.
Tool Integration: Use ToolAgent to dispatch tools (e.g., Google Search, Jupyter notebooks, etc.) for solving sub-tasks.
Feedback Loop: Feedback from previous tasks is used to refine future iterations and improve reliability.
Langgraph Integration: The Langgraph framework is used to manage the agentic workflow
Setup
Prerequisites
Python 3.x
langgraph (Ensure the Langgraph module is correctly installed)
Other dependencies (can be installed via requirements.txt)
Installation
Clone the repository:
Install the required dependencies:
pip install -r requirements.txt
Langgraph Integration
This project uses Langgraph to manage the following functionalities:

Task Management: Using LangGraph to split complex queries into sub-tasks.
Tool Management: Retrieving tools based on task requirements and using ToolAgent to dispatch tasks to these tools.
Feedback & Reflection: Implementing feedback loops to refine and enhance task results based on performance, ensuring high reliability.
Key Components
1. PlanAgent
Responsible for breaking down the user query into sub-tasks. The current implementation splits tasks based on logical connectors in the query.

2. ToolAgent
Responsible for retrieving the appropriate tool for each task and executing the task. Tools like calculators and web scrapers are utilized.

3. FeedbackAgent
Monitors task execution and refines the tasks if errors or inefficiencies are detected.

4. LangGraph
Handles the creation and management of the task and tool graphs.

5. Streamlit Interface
Provides an interactive web interface for users to input queries and view results.
