import asyncio
from langchain_openrouter import ChatOpenRouter
from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain.agents.structured_output import ToolStrategy
from langchain.messages import AIMessage
from langgraph.types import Command
from langchain.messages import SystemMessage
from back_end.prompts.calorie_agent_prompt import CALORIE_AGENT_SYSTEM_PROMPT
from back_end.prompts.response_digest import CalorieAgentResponse
from dotenv import load_dotenv
from typing import Literal
from back_end.tools.tools import calorie_tools
load_dotenv()

class CalorieAgent:
    def __init__(self):
        self.llm = None
        self.system_prompt = SystemMessage(content=CALORIE_AGENT_SYSTEM_PROMPT)
    
    @classmethod
    async def create(cls):
        initialized = cls()
        await initialized.make_agent()
        return initialized

    async def make_agent(self):
        self.llm = create_agent(model=ChatOpenRouter(
            model='openai/gpt-5.4-mini',
            temperature=0.3
        ),tools=calorie_tools,system_prompt=CALORIE_AGENT_SYSTEM_PROMPT, response_format=ToolStrategy(CalorieAgentResponse)
        )
        return self.llm
    
    async def run(self,state)->Command[Literal['tools','__end__']]:
        response = await self.llm.ainvoke({"messages": state['messages']})
        return Command(
            update={
                'messages':[response['messages'][-1]],
                'structured_response':response.get('structured_response')
            }
        )

if __name__ == '__main__':
    async def main():
        agent = await CalorieAgent.create()
        response = await agent.llm.ainvoke({'messages':'Hi so I ate a one piece chicken joy with rice from jollibee with coke and small fries on the side.'})
        for m in response['messages']:
            m.pretty_print()
        # print(response)
        print(response['structured_response'])
        return response
    asyncio.run(main())
