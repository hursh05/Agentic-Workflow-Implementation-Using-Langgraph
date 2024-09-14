
from agents import PlanAgent, ToolAgent, FeedbackAgent, ToolRetriever

def run_agentic_workflow(query):
    plan_agent = PlanAgent()
    tool_retriever = ToolRetriever()
    tool_agent = ToolAgent(tool_retriever)
    feedback_agent = FeedbackAgent()

    tasks = plan_agent.plan(query)
    results = []

    for task in tasks:

        result = tool_agent.solve_task(task)
        results.append(f"Result for task '{task}': {result}")

        refined_task = feedback_agent.refine_task(task, result)
        if refined_task != task:
            refined_result = tool_agent.solve_task(refined_task)
            results.append(f"Result for refined task '{refined_task}': {refined_result}")

    return results

if __name__ == "__main__":
    user_query = "fetch data and calculate sum"
    results = run_agentic_workflow(user_query)
    for result in results:
        print(result)
