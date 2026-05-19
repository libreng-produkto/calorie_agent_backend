from back_end.prompts.state import CalorieState
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode, tools_condition
from back_end.nodes.calorie_agent_node import CalorieAgent
from back_end.tools.tools import calorie_tools
from langchain.messages import HumanMessage
import base64
from pathlib import Path
import asyncio

def image_to_base64(image_path: str, mime_type: str = "image/png") -> str:
    """Convert an image file to base64 data URL."""
    path = Path(image_path)
    if not path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")
    
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    
    return f"data:{mime_type};base64,{b64}"

class CalorieGraph:
    def __init__(self):
        self.graph = None
        self.calorie_agent = None
    
    @classmethod
    async def create(cls):
        initialized = cls()
        await initialized.create_agent()
        initialized.build_graph()
        return initialized

    
    async def create_agent(self):
        self.calorie_agent = await CalorieAgent.create()
        return self.calorie_agent

    def build_graph(self):
        build = StateGraph(CalorieState)
        #
        build.add_node('calorie_agent',self.calorie_agent.run)
        build.add_node('tools',ToolNode(calorie_tools))
        #
        build.set_entry_point('calorie_agent')
        build.add_conditional_edges('calorie_agent',tools_condition,
            {
                "tools":"tools",
                "__end__":END
            }
        )
        build.add_edge('tools','calorie_agent')
        #
        self.graph = build.compile()
        return self.graph

if __name__ == "__main__":
    async def main():
        img_b64 = image_to_base64("/home/hz/CalorieAssistant/image.png","image/png")
        graph = await CalorieGraph.create()
        test_state = {
            "messages":[
                HumanMessage(
                    content=[
                    {
                        "type":"text",
                        "text":"I had this for breakfast."
                    },
                    {
                        "type":"image_url",
                        "image_url":{"url":img_b64}
                    }
                ]
                )
            ]
        }
        content = HumanMessage(
            content=[
                    {
                        "type":"text",
                        "text":"I had this for breakfast."
                    },
                    {
                        "type":"image_url",
                        "image_url":{"url":img_b64}
                    }
            ]
        )
        response = await graph.graph.ainvoke({'messages':[content]})
        for m in response['messages']:
            m.pretty_print()
    asyncio.run(main())
