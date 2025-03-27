#!/usr/bin/python
# -*- coding: utf-8 -*-

from Game import Game
from Class9 import Class9


class Level(Game, Class9):
    def __init__(self):
        self.window; Surface = None
        self.name = None
        self.entity_list = None

    def run(self, ):
        pass
