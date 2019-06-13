#!/usr/bin/python3
"""Tests for Rectangle class"""


import contextlib
import importlib
import io
import models.base
import models.rectangle
import unittest


Rectangle = models.rectangle.Rectangle


class RectangleTests(unittest.TestCase):
    """Tests for Rectangle class"""

    def setUp(self):
        """Refresh Rectangle module for each test"""

        importlib.reload(models.base)
        importlib.reload(models.rectangle)

    def test_Area(self):
        """Compare width and height to result of area method"""

        r = Rectangle(10, 5)
        with self.subTest():
            self.assertEqual(r.area(), 50)
        r.width = 3
        r.height = 7
        with self.subTest():
            self.assertEqual(r.area(), 21)

    def test_Display(self):
        """Test the display module"""

        out = io.StringIO()
        r = Rectangle(4, 6)
        result = "####\n####\n####\n####\n####\n####\n"
        with self.subTest():
            with contextlib.redirect_stdout(out):
                r.display()
            self.assertEqual(out.getvalue(), result)
        out.truncate(0)
        out.seek(0)
        r.width = 2
        r.height = 3
        r.x = 3
        r.y = 2
        result = "\n\n   ##\n   ##\n   ##\n"
        with self.subTest():
            with contextlib.redirect_stdout(out):
                r.display()
            self.assertEqual(out.getvalue(), result)

    def test_TooFewArgs(self):
        """Test for too few args to init"""

        msg = "__init__() missing 1 required positional argument: 'height'"
        with self.assertRaises(TypeError, msg=msg):
            Rectangle(1)

    def test_TooManyArgs(self):
        """Test for too many args to init"""

        msg = "__init___() takes from 3 to 6 positional arguments but 7" \
            "were given"
        with self.assertRaises(TypeError, msg=msg):
            Rectangle(1, 2, 3, 4, 5, 6)
