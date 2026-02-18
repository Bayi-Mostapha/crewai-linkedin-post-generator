import os
from crewai import Agent, LLM

llm = LLM(
    model="mistral/mistral-large-latest",
    api_key=os.getenv("MISTRAL_API_KEY")
)

researcher = Agent(
    llm = llm,
    role="Senior Tech Research Analyst",
    goal="Find and extract high-quality, recent, and relevant information about the given topic",
    backstory=("You are an experienced tech research analyst with deep expertise in technology trends and software development. "
               "You have years of experience finding and analyzing high-quality information from reliable sources. "
               "Your strength lies in identifying the most relevant and recent insights on complex technical topics."),
    tools=[],
    verbose=True,
    allow_delegation=False
)

synthesizer = Agent(
    llm = llm,
    role="Research Synthesizer",
    goal="structure and synthesize the given info",
    backstory=("You are a skilled information architect with expertise in organizing complex research findings. "
               "You excel at identifying patterns, connections, and key insights from raw information. "
               "Your structured approach transforms scattered data into coherent, actionable knowledge."),
    tools=[],
    verbose=True,
    allow_delegation=False
)

content_generator = Agent(
    llm = llm,
    role="LinkedIn Content Formatter",
    goal="generate a high-quality professional post about the topic, based on the info given",
    backstory=("You are a seasoned LinkedIn content creator and thought leader in technology. "
               "You specialize in crafting compelling, professional posts that engage and inspire the tech community. "
               "Your content is known for balancing insights with accessibility, always driving meaningful conversations."),
    tools=[],
    verbose=True,
    allow_delegation=False
)