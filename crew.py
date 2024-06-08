from crewai import Crew, Process
from contentCreationCrew.tasks import researchTask, writeTask, seoTask
from contentCreationCrew.agents import topicResearcher, contentWriter, seoSpecialist

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Forming the Content Creation Crew
crew = Crew(
    agents=[topicResearcher, contentWriter, seoSpecialist],
    tasks=[researchTask, writeTask, seoTask],
    process=Process.sequential
)
@app.route('/contentCreationAgency', methods=['POST'])
def contentCreationAgency():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No topic provided'}), 400
    topic = data['topic']
    if not topic:
        return jsonify({'error': 'No topic provided'}), 400
    result = crew.kickoff(inputs={'topic': topic})
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)




