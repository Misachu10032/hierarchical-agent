from IPython.display import Image, display
from typing import List

from langgraph.graph import END, StateGraph, START

from models import State

from writing_team import doc_writing_node, doc_writing_supervisor_node, chart_generating_node, note_taking_node


# Create the graph here
paper_writing_builder = StateGraph(State)
paper_writing_builder.add_node("supervisor", doc_writing_supervisor_node)
paper_writing_builder.add_node("doc_writer", doc_writing_node)
paper_writing_builder.add_node("note_taker", note_taking_node)
paper_writing_builder.add_node("chart_generator", chart_generating_node)

paper_writing_builder.add_edge(START, "supervisor")
paper_writing_graph = paper_writing_builder.compile()


