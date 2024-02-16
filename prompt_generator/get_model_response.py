import anthropic
import json
import anthropic_bedrock
import pkg_resources
from anthropic_bedrock import AnthropicBedrock
from anthropic import Anthropic, HUMAN_PROMPT, AI_PROMPT


def query_claude_bedrock(prompt, access_key, secret_key, region):
    print("inside query_claude_bedrock...")
    client = AnthropicBedrock(
        aws_access_key=access_key,
        aws_secret_key=secret_key,
        aws_region=region,
    )
    completion = client.completions.create(
        model="anthropic.claude-v2:1",
        max_tokens_to_sample=2048,
        prompt=prompt,
    )
    return completion.completion


def query_claude(prompt, access_key, secret_key):
    print("inside query_claude...")
    '''

    :param prompt:
    :param secret_key:
    :return:
    '''
    anthropic = Anthropic(
        api_key=secret_key,
    )

    completion = anthropic.completions.create(
        model="claude-2",
        max_tokens_to_sample=2048,
        prompt=f"{HUMAN_PROMPT} {prompt} {AI_PROMPT}",
    )
    return completion.completion


