

from langgraph import LangGraph, GraphNode
from tools import CalculatorTool, WebScraperTool, MockTool

class PlanAgent:
    def __init__(self):
        self.graph = LangGraph()

    def plan(self, query):
        
        tasks = query.split(" and ")
        for task in tasks:
            self.graph.add_node(GraphNode(task))  
        return tasks

class ToolAgent:
    def __init__(self, tool_retriever):
        self.tool_retriever = tool_retriever

    def solve_task(self, task):
        tool = self.tool_retriever.get_tool_for_task(task)
        return tool.use(task)

class FeedbackAgent:
    def refine_task(self, task, result):
        if "error" in result:
            
            return task + " (refined)"
        return task

class ToolRetriever:
    def get_tool_for_task(self, task):
        if "calculate" in task:
            return CalculatorTool()
        elif "fetch" in task:
            return WebScraperTool()
        else:
            return MockTool()
