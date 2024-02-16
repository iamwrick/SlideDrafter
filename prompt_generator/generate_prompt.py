class PromptGenerator:
    def __init__(self, topic, description=None, slide_count=None, audience_age_group=None, include_diagrams=False, additional_instructions=None):
        self.topic = topic
        self.description = description
        self.audience_age_group = audience_age_group
        self.slide_count = slide_count
        self.include_diagrams = include_diagrams
        self.additional_instructions = additional_instructions

    def build_prompt(self):
        prompt = "\n\nHuman: "

        prompt += f"Please create a {self.slide_count} slide PowerPoint presentation on the topic of {self.topic}. "
        if self.description:
            prompt += f"{self.description}"

        prompt += """
              For each slide, provide the information in a Python dictionary containing keys for: 
              - 'title' (5 words maximum)
              - 'intro' (1 sentence overview)  
              - 'content' (up to 250 chars of text, facts, examples)
              - 'takeaway' 
              - 'image'(placeholder image filename or path without actual files) 
              """

        prompt += f"""  
              - Focus on the presentation and actionable solutions tailored for an audience age group {self.audience_age_group},
              - Use bullet points, numbered lists, or other formatting techniques to organize information clearly.
              - Left align text and use high contrast colors. 
              - Ensure a logical flow between slides building concepts from introduction to conclusions.
              """

        example_slide = {
            "title": "Poverty Causes Hunger",
            "intro": "One of the main factors driving world hunger is extreme poverty.",
            "content": "Text elaborating on how poverty traps communities in hunger...",
            "takeaway": "Alleviating poverty is key to reducing world hunger long-term.",
            "image": "poverty image"
        }

        prompt += f"""  
              Respond with a JSON formatted string containing a 'slides' dictionary key mapping to a list of {self.slide_count} slide dictionaries.
              Each slide dictionary should match the format shown in the above example slide.
              """

        prompt += """  
              - Do not include any other descriptive text or formatting.
              - Respond only with the JSON string containing the slide data.
              - Make sure to start response with 'SLIDE_DATA:' delimiter before the JSON string.
              """
        prompt += f"""
              - Please make sure you follow the {self.additional_instructions} carefully
              """

        prompt += f"\n\nAssistant: "

        return prompt



