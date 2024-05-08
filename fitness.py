import requests


def calculate_calories_burned(exercise, time, weight):
    """
    Calculate calories burned from an exercise based on MET values.

    :param exercise: str, type of exercise performed
    :param minutes: float, duration of the exercise in minutes
    :param weight: float, weight of the person in kilograms
    :return: float, calories burned
    """
    