
from crewai.flow.flow import Flow, start, listen
from litellm import completion  # Replace with your preferred LLM API client

class TopicOutlineFlow(Flow):


    @start()
    def generate_topic(self):
        # Prompt the LLM to generate a blog topic.
        response = completion(
            model= "gemini/gemini-2.0-flash-exp",
            messages=[{
                "role": "user",
                "content": "Generate a creative blog topic for 2025."
            }]
        )
        topic = response["choices"][0]["message"]["content"].strip()
        print(f"Generated Topic: {topic}")
        return topic

    @listen(generate_topic)
    def generate_outline(self, topic):
        # Now chain the output by using the topic in a follow-up prompt.
        response = completion(
            model= "gemini/gemini-2.0-flash-exp",
            messages=[{
                "role": "user",
                "content": f"Based on the topic '{topic}', create a detailed outline for a blog post."
            }]
        )
        outline = response["choices"][0]["message"]["content"].strip()
        print("Generated Outline:")
        print(outline)
        return outline
    @listen(generate_outline)
    def save_outline(self, outline):
        with open("outline.txt", "w") as f:
            f.write(outline)

def kickoff():
    flow = TopicOutlineFlow()
    final_outline = flow.kickoff()
    print("Final Output:")
    print(final_outline)
