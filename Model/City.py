#!/bin/python3
"""
This module contains the City class, which is a subclass of BaseModel.
"""

from Model.BaseModel import BaseModel
from Model.Country import Country


class City(BaseModel):
	"""
	This class represents a city.
	"""

	def __init__(self, name, Country):
		"""
		Initializes a new instance of the City class.

		Args:
			name (str): The name of the city.
			country (str): The country where the city is located.
		"""
		super().__init__()
		self.name = name
		self.country = Country
		self.places = [] # List of places in the city.
		Country.add_city(self)
	
	def add_place(self, place):
		"""
		Adds a place to the city.

		Args:
			place (Place): The place to add.
		"""
		self.places.append(place)

	def __str__(self):
		"""
		Returns a string representation of the City object.

		Returns:
			str: The string representation of the City object.
		"""
		return f"City: {self.name}"
