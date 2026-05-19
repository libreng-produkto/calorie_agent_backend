from typing import TypedDict, List, Annotated, Any
from langgraph.graph.message import add_messages
from langchain.messages import AnyMessage

class CalorieState(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]
    structured_response: Any