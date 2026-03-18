# json.dumps e json.loads com strings + typing.TypedDict
# Ao converter de Python para JSON:
# Python........JSON
# dict          object
# list, tuple   array
# str           string
# int, float    number
# True          true
# False         false
# None          null

import json
from typing import TypedDict

# from pprint import pprint


# tipando  "string_json"
class Movie(TypedDict):
    title: str
    original_title: str
    is_movie: bool
    imdb_rating: float
    year: int
    characters: list[str]
    budget: None


string_json = """
{
  "title": "O senhor dos Anéis: A Sociedade do Anel",
  "original_title": "The Lord og the Rings: The Fellowship of the Ring",
  "is_movie": true,
  "imdb_rating": 8.8,
  "year": 2001,
  "characters": ["Frodo", "Sam", "Gandalf", "Legolas", "Boromir"],
  "budget": null
}
"""

movie: Movie = json.loads(string_json)  # carregando o json
# pprint(movie)
# print(movie["title"])
# print(movie["characters"][0])
# print(movie["year"] + 25)

json_string = json.dumps(movie, ensure_ascii=False, indent=2)
print(json_string)
