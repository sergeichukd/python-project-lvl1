#!usr/bin/env python3

from brain_games.games import engine

from brain_games.games import even
from brain_games.games import calc
from brain_games.games import gcd
from brain_games.games import progression
from brain_games.games import prime


def run_even():
    engine.run(even)


def run_calc():
    engine.run(calc)


def run_gcd():
    engine.run(gcd)


def run_progression():
    engine.run(progression)


def run_prime():
    engine.run(prime)
