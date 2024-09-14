

class CustomToolRetriever:
    """ToolRetriever selects the correct tool to handle the sub-task."""
    def get_tool_for_task(self, task):
        if "calculate" in task:
            return CalculatorTool()
        elif "fetch" in task:
            return WebScraperTool()
        return MockTool()

class CalculatorTool:
    """Simulates a calculator tool."""
    def use(self, task):
        return "Calculated result"

class WebScraperTool:
    """Simulates a web scraping tool."""
    def use(self, task):
        return "Fetched data from the web"

class MockTool:
    """Fallback tool for tasks that don't match any specific category."""
    def use(self, task):
        return "Processed task using mock tool"
    