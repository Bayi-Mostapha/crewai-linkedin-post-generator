import os
from crewai_tools import EXASearchTool

exa_api_key = os.getenv('EXA_API_KEY')
if not exa_api_key:
    raise ValueError("EXA_API_KEY environment variable is not set. Please set your Exa API key.")

search_tool = EXASearchTool(api_key=exa_api_key)