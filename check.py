import sys
import os

# Add the project directory to sys.path
sys.path.append(os.path.abspath(r"D:/project/agentic_workflow"))

# Now import LangGraph from the langgraph module
from langgraph import LangGraph

# Test LangGraph functionality
lg = LangGraph()
lg.some_method()


from langgraph import LangGraph  # Import LangGraph

lg = LangGraph()
lg.some_method()


# Import LangGraph from langgraph (which uses the __init__.py)
from langgraph import LangGraph

# Initialize and use LangGraph
lg = LangGraph()
lg.some_method()
