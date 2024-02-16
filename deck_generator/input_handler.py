from pydantic import BaseModel, Field


class UserInput(BaseModel):
    topic: str = Field(..., title="Topic", description="Enter the topic")
    description: str = Field(..., title="Description", description="Enter the description")
    num_slides: int = Field(..., gt=0, title="Number of Slides", description="Enter the number of slides")
    age_group: str = Field(..., title="Age group of the audience", description="Enter the age group of target audience")
    include_diagrams: bool = Field(..., title="Include Diagrams", description="Include diagrams? (True/False)")
    additional_instructions: str = Field(..., title="additional instructions", description="Enter if there are any additional instructions")
    model: str = Field(..., title="Model Name per config", description="Enter the model name")

    @classmethod
    def get_user_input(cls):
        topic = input(f"{cls.__annotations__['topic'].description}: ")
        description = input(f"{cls.__annotations__['description'].description}: ")
        age_group = input(input(f"{cls.__annotations__['age_group'].description}: "))
        num_slides = int(input(f"{cls.__annotations__['num_slides'].description}: "))
        include_diagrams = bool(input(f"{cls.__annotations__['include_diagrams'].description}: ").capitalize() == "True")
        additional_instructions = input(f"{cls.__annotations__['additional_instructions'].additional_instructions}: ")
        model = input(f"{cls.__annotations__['model'].model}: ")

        return cls(topic=topic, description=description, age_group=age_group, num_slides=num_slides, include_diagrams=include_diagrams, additional_instructions=additional_instructions, model=model)
