from back_end.graph import CalorieGraph
from back_end.graph import image_to_base64
from langchain.messages import HumanMessage

class AgentService:
    def __init__(self):
        self.graph = None
    
    async def initialize(self):
        if self.graph is None:
            self.graph = await CalorieGraph.create()
    
    async def process(self, message:str, images: list = None):
        await self.initialize()

        content = [{"type":"text","text": message}]
        if images:
            for img_path in images:
                b64 = image_to_base64(img_path)
                content.append({
                    "type":"image_url",
                    "image_url":{"url":b64}
                })
        
        state = {"messages": [HumanMessage(content=content)]}
        
        result = await self.graph.graph.ainvoke(state)
        return result.get('structured_response')

agent_service = AgentService()