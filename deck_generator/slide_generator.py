import json

from deck_generator.presentation_generator import PresentationGenerator
from prompt_generator.generate_prompt import PromptGenerator
from prompt_generator.get_model_response import query_claude_bedrock, query_claude
from utility.get_keys import get_keys


class SlideGenerator:
    def __init__(self, input_data):
        self.topic = input_data.topic
        self.description = input_data.description
        self.num_slides = input_data.num_slides
        self.age_group = input_data.age_group
        self.include_diagrams = input_data.include_diagrams
        self.additional_instructions = input_data.additional_instructions
        self.model = input_data.model

    async def generate_slides(self):
        '''

        :param self:
        :return:
        '''
        # verify API keys
        print(f"Verifying key... before generating slide on {self.topic}")

        if self.model == "anthropic":
            anthropic_access_key, anthropic_secret_key = get_keys('anthropic')

        elif self.model == "aws":
            aws_access_key, aws_secret_key, aws_region = get_keys('aws')
        else:
            raise ValueError("Invalid model")

        print(f"Generating slides for topic: {self.topic}")
        prompt_gen = PromptGenerator(self.topic,
                             self.description,
                             self.num_slides,
                             self.age_group,
                             self.include_diagrams,
                             self.additional_instructions
                             )

        generated_prompt = prompt_gen.build_prompt()
        if self.model == "aws":
            response = query_claude_bedrock(generated_prompt, aws_access_key, aws_secret_key, aws_region)
        else:
            response = query_claude(generated_prompt, anthropic_access_key, anthropic_secret_key)

        # Remove "SLIDE_DATA:" and convert to dictionary
        try:
            # Find the index of '{' after 'SLIDE_DATA:'
            start_index = response.find('{', response.find(':'))
            # Extract the JSON part and convert it to a dictionary
            slide_data = json.loads(response[start_index:].strip())
            if self.include_diagrams:
                unsplash_access_key, unsplash_secret_key = get_keys('unsplash')
                presentation_generator = PresentationGenerator(unsplash_secret_key)
                # Call create_presentation method
                presentation_generator.create_presentation(slide_data, self.topic)
            else:
                presentation_generator = PresentationGenerator()
                presentation_generator.create_presentation(slide_data, self.topic)
        except json.JSONDecodeError as e:
            print(f"Error decoding JSON: {e}")









