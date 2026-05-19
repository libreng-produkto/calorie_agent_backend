import os
import requests
import json
from dotenv import load_dotenv
from langchain.tools import tool

load_dotenv()

@tool
def calorie_db(query: str) -> str:
    """Query a single food item for nutritional information.

    Use this tool to look up calories and macros for ONE specific food item
    at a time. Format the query as a simple food + portion description.

    Args:
        query: A single food item with quantity. Examples:
            - "100g chicken breast"
            - "1 cup rice"
            - "2 slices of bread"
            - "egg" (defaults to ~50g)
            - "medium banana"

    Returns:
        JSON string containing:
        - name, calories, protein_g, fat_g, carbohydrate_g, fiber_g, serving_size

    Note:
        - Query ONE food item per call. Do NOT paste full meal descriptions.
        - Break complex meals into individual calls, then sum the totals.
        - If a portion is vague (e.g., "some rice"), estimate a reasonable serving.
    """
    api_url = "https://api.calorieninjas.com/v1/nutrition?query="
    try:
        response = requests.get(
            api_url+query,
            headers={
                'X-Api-Key':os.getenv('CALORIE_NINJA')
            }
        )
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            return f'Request Error'
    except Exception as e:
        return f'Error: {e}' 

calorie_tools = [calorie_db]

if __name__ == '__main__':
    query = '50g almonds'
    calorie = calorie_db(query=query)
    print(calorie)