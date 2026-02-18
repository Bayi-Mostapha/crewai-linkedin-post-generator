from crewai import Crew, Process
from agents import researcher, synthesizer, content_generator
from tasks import research_task, syn_task, content_task

crew = Crew(
    agents = [researcher, synthesizer, content_generator],
    tasks = [research_task, syn_task, content_task],
    process = Process.sequential,
    memory = True,
    cache = True,
    max_rpm = 100,
    share_crew = True
)

result = crew.kickoff(
    inputs = {'topic': 'data engineers in 2026'}
)