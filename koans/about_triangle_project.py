#!/usr/bin/env python
# -*- coding: utf-8 -*-

from runner.koan import *

# You need to write the triangle method in the file 'triangle.py'
from .triangle import *


class AboutTriangleProject(Koan):

    def test_equilateral_triangles_have_equal_sides(self):
        self.assertEqual('Equilateral', triangle(2, 2, 2))
        self.assertEqual('Equilateral', triangle(10, 10, 10))

    def test_isosceles_triangles_have_exactly_two_sides_equal(self):
        self.assertEqual('Isosceles', triangle(3, 4, 4))
        self.assertEqual('Isosceles', triangle(4, 3, 4))
        self.assertEqual('Isosceles', triangle(4, 4, 3))
        self.assertEqual('Isosceles', triangle(10, 10, 2))

    def test_scalene_triangles_have_no_equal_sides(self):
        self.assertEqual('Scalene', triangle(3, 4, 5))
        self.assertEqual('Scalene', triangle(10, 11, 12))
        self.assertEqual('Scalene', triangle(5, 4, 2))
