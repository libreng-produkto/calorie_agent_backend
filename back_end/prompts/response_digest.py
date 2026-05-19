from typing import TypedDict, List

class FoodNutrients(TypedDict):
    name: str
    calories: float
    carbs: float
    protein: float
    fat: float
    fiber: float
    serving: int
    cholesterol: float
    sugar: float
    potassium: float

class CalorieAgentResponse(TypedDict):
    items: List[FoodNutrients]
