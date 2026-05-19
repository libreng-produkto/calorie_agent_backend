from back_end.graph import CalorieGraph
from back_end.graph import image_to_base64
from langchain.messages import HumanMessage
import base64

class AgentService:
    def __init__(self):
        self.graph = None
    
    async def initialize(self):
        if self.graph is None:
            self.graph = await CalorieGraph.create()
    
    async def process(self, message:str, image_data: bytes = None):
        await self.initialize()

        content = [{"type":"text","text": message}]
        if image_data:
            b64 = f"data:image/png;base64,{base64.b64encode(image_data).decode()}"
            content.append({"type":"image_url","image_url":{"url":b64}})

        state = {"messages": [HumanMessage(content=content)]}
        
        result = await self.graph.graph.ainvoke(state)
        return result.get('structured_response',{}).get('items')

agent_service = AgentService()