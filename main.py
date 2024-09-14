from agents import CustomPlanAgent, CustomToolAgent, CustomFeedbackAgent, CustomToolRetriever


def run_agentic_workflow(query):

    plan_agent = CustomPlanAgent()
    tool_retriever = CustomToolRetriever()
    tool_agent = CustomToolAgent(tool_retriever)
    feedback_agent = CustomFeedbackAgent()

    tasks = plan_agent.plan(query)

    for task in tasks:
        result = tool_agent.solve_task(task)
        print(f"Result for task '{task}': {result}")

        refined_task = feedback_agent.refine_task(task, result)
        if refined_task != task:
            refined_result = tool_agent.solve_task(refined_task)
            print(f"Result for refined task '{refined_task}': {refined_result}")

if __name__ == "__main__":
    user_query = "fetch data and calculate sum"
    run_agentic_workflow(user_query)
