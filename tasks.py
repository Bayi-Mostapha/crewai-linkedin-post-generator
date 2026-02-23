from crewai import Task
from tools import search_tool
from agents import researcher, synthesizer, content_generator

research_task = Task(
    description="Research and gather comprehensive information about '{topic}'. Find recent trends, developments, and insights from reputable sources. "
                "Focus on practical applications, industry impact, and future implications. "
                "Collect at least 5-7 key insights or findings.",
    expected_output="A detailed research report with key findings, trends, and insights about the topic, including sources and relevant statistics",
    tools=[search_tool],
    agent=researcher
)

syn_task = Task(
    description="Analyze and synthesize the research findings into a structured format. Identify key themes, patterns, and the most important takeaways. "
                "Organize the information logically and highlight the most compelling insights for a professional audience.",
    expected_output="A well-structured synthesis document with key themes, insights, and their implications organized in a clear, hierarchical format",
    tools=[],
    agent=synthesizer
)

content_task = Task(
    description="Create a compelling, professional LinkedIn post based on the synthesized research about '{topic}'. "
                "The post should be engaging, insightful, and suitable for a tech-savvy professional audience. "
                "Include a clear hook, key insights, and a call-to-action. Keep it between 300-500 words.",
    expected_output="A polished LinkedIn post that is engaging, professional, and ready to publish. Should include hooks, insights, and engagement elements",
    tools=[],
    agent=content_generator,
    async_execution=False,
    output_file='post.md'
)