from crewai import Task 
from crewai_tools import SerperDevTool

from contentCreationCrew.agents import topicResearcher, contentWriter, seoSpecialist

search_tool = SerperDevTool()




# Topic Research Task
researchTask = Task(
    description=(
        "Identify the latest trending topics and relevant keywords in {topic}. "
        "Focus on high search volume and relevance to the target audience. "
        "Provide a list of top 5 trending topics with their respective keywords."
    ),
    expected_output='A list of top 5 trending topics with keywords.',
    tools=[search_tool],
    agent=topicResearcher,
)

# Content Writing Task
writeTask = Task(
    description=(
        "Write an engaging and informative article on one of the trending topics identified. "
        "Ensure the content is original, well-structured, and provides value to the reader."
    ),
    expected_output='A 4-paragraph article on a trending topic.',
    tools=[search_tool],
    agent=contentWriter,
    async_execution=False,
    output_file='article.md'
)

# SEO Optimization Task
seoTask = Task(
    description=(
        "Optimize the written article for SEO. Focus on keyword usage, meta descriptions, "
        "internal linking, and readability. Publish the article once optimized."
    ),
    expected_output='An SEO-optimized article ready for publication.',
    tools=[search_tool],
    agent=seoSpecialist,
    async_execution=False,
    output_file='optimized_article.md'
)
