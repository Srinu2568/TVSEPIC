from pydantic import BaseModel

class FeatureNote(BaseModel):
    Car	: int
    Location : int
    Year : int
    Kilometers_Driven : int
    Owner_Type : int
    Fuel_Type : int
    Power : float