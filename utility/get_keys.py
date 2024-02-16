import json
import pkg_resources


def get_keys(environment):
    file_path = pkg_resources.resource_filename(__name__, '../configuration/api_keys.json')
    with open(file_path, 'r') as file:
        config = json.load(file)
    if environment == 'aws':
        return config['aws']['access_key'], config['aws']['secret_key'], config['aws'].get('aws_region', None)
    elif environment == 'anthropic':
        return config['anthropic']['access_key'], config['anthropic']['secret_key']
    elif environment == 'unsplash':
        return config['unsplash']['access_key'], config['unsplash']['secret_key']
    else:
        raise ValueError("Invalid environment")
