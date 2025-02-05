
from langgraph.graph import END, StateGraph, START
from research_team import research_supervisor_node , search_node ,web_scraper_node
from supervisor_node import State
from models import GraphState




workflow = StateGraph(GraphState)

research_builder = StateGraph(State)
research_builder.add_node("supervisor", research_supervisor_node)
research_builder.add_node("search", search_node)
research_builder.add_node("web_scraper", web_scraper_node)

research_builder.add_edge(START, "supervisor")
research_graph = research_builder.compile()


