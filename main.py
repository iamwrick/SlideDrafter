# main.py
import asyncio
import argparse
import time
from deck_generator import input_hanlder
from deck_generator.input_hanlder import UserInput
from deck_generator.slide_generator import SlideGenerator


def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate PowerPoint slides.')
    parser.add_argument('--topic', type=str, required=True, help='Topic of the presentation')
    parser.add_argument('--description', type=str, required=False, help='Description of the presentation')
    parser.add_argument('--num-slides', type=int, required=True, help='Number of slides')
    parser.add_argument('--age-group', type=str, required=True, help='Audience age group')
    parser.add_argument('--include-diagrams', type=bool, required=False, help='Include diagrams? (True/False)')
    parser.add_argument('--additional-instructions', type=str, required=False, help='Any additional information')
    parser.add_argument('--model', type=str, required=True, help='Include model choice')

    return parser.parse_args()


async def main():
    # Parse command-line arguments
    args = parse_arguments()
    user_input = UserInput(**vars(args))

    # Generate slides asynchronously
    slide_generator = SlideGenerator(user_input)
    await slide_generator.generate_slides()

if __name__ == "__main__":
    start_time = time.time()  # Record the start time
    asyncio.run(main())
    end_time = time.time()  # Record the end time
    elapsed_time = end_time - start_time
    print(f"Presentation created in {elapsed_time:.2f} seconds")

