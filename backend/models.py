

from typing import List

from typing_extensions import TypedDict
from langgraph.graph import  MessagesState

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes:
        question: question
        generation: LLM generation
        documents: list of documents
    """

    question: str
    generation: str
    documents: List[str]

class State(MessagesState):
    next: str
