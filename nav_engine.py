import requests
import re


class NavEngine:
    def __init__(self, maps_key):
        self.key = maps_key
        self.url = "https://maps.googleapis.com/maps/api/directions/json"

    def get_step_directions(self, origin_lat_lon, destination):
        params = {
            'origin': origin_lat_lon,
            'destination': destination,
            'mode': 'walking',
            'key': self.key
        }

        res = requests.get(self.url, params=params).json()

        if res['status'] == 'OK':
            steps = res['routes'][0]['legs'][0]['steps']

            directions = []

            for step in steps:
                instruction = step['html_instructions']
                clean_instruction = re.sub(
                    '<[^<]+?>',
                    '',
                    instruction
                )
                directions.append(clean_instruction)

            return directions

        return ["Route calculation in progress..."]