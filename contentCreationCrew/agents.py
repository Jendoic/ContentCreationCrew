from crewai import Agent 
from crewai_tools import SerperDevTool
import os
from dotenv import load_dotenv
load_dotenv()


os.getenv("OPENAI_API_KEY")
search_tool = SerperDevTool()



# Topic Researcher Agent
topicResearcher = Agent(
    role='Topic Researcher',
    goal='Identify trending topics and relevant keywords in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "You are a diligent researcher, always on the lookout for the latest trends and topics."
    ),
    tools=[search_tool],
    allow_delegation=True
)

# Content Writer Agent
contentWriter = Agent(
    role='Content Writer',
    goal='Write engaging articles or blog posts based on researched topics',
    verbose=True,
    memory=True,
    backstory=(
        "You are a creative writer, skilled in crafting engaging and informative content."
    ),
    tools=[search_tool],
    allow_delegation=False
)

# SEO Specialist Agent
seoSpecialist = Agent(
    role='SEO Specialist',
    goal='Optimize content for search engines and ensure it reaches a wide audience',
    verbose=True,
    memory=True,
    backstory=(
        "You are an SEO expert, knowledgeable in optimizing content to rank well in search engines."
    ),
    tools=[search_tool],
    allow_delegation=False
)
