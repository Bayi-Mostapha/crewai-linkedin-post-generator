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

try:
    with open('post.md', 'w') as md_file:
        pass
except FileNotFoundError:
    pass
except Exception as e:
    print(f"An error occurred: {e}")

print("enter your topic: ")
topic = input()
result = crew.kickoff(
    inputs = {'topic': topic}
)