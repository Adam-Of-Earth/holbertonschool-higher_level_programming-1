"""Tests for the square object model"""


import importlib
import models.base
import models.rectangle
import models.square
import unittest


Square = models.square.Square


class SquareTests (unittest.TestCase):
    """Tests for the square object model"""

    def setUp(self):
        """Refresh the Square before each test"""

        importlib.reload(models.base)
        importlib.reload(models.rectangle)
        importlib.reload(models.square)

    def test_Validator(self):
        """Tests validator method"""

        s = Square(1, 2, 1)
        msg = "width must be an integer"
        with self.subTest():
            with self.assertRaises(TypeError, msg=msg):
                Square("5")
        with self.subTest():
            with self.assertRaises(TypeError, msg=msg):
                s.size = "5"
        with self.subTest():
            with self.assertRaises(TypeError, msg=msg):
                Square([3])
        with self.subTest():
            with self.assertRaises(TypeError, msg=msg):
                s.size = [3]
        msg = "width must be > 0"
        with self.subTest():
            with self.assertRaises(ValueError, msg=msg):
                Square(0)
        with self.subTest():
            with self.assertRaises(ValueError, msg=msg):
                s.size = 0
        with self.subTest():
            with self.assertRaises(ValueError, msg=msg):
                Square(-1)
        with self.subTest():
            with self.assertRaises(ValueError, msg=msg):
                s.size = -1

    def test_TooFewArgs(self):
        """Test for too few args"""

        msg = "__init__() missing 1 required positional argument: 'size'"
        with self.assertRaises(TypeError, msg=msg):
            Square()

    def test_InitTooManyArgs(self):
        """Giving too many arguments to the constructor"""

        msg = "__init__() got an unexpected keyword argument 'ids'"
        with self.assertRaises(TypeError, msg=msg):
            Square(5, id=20)
        msg = "__init__() takes from 2 to 5 positional arguments but " \
                  "6 were given"
        with self.assertRaises(TypeError, msg=msg):
            Square(1, 2, 3, 4, 5)

    def test_SizeUpdate(self):
        """Changing the size and seeing if it changes with and height"""

        s = Square(3)
        with self.subTest():
            self.assertEqual(s.width, 3)
        with self.subTest():
            self.assertEqual(s.height, 3)
        s.size = 30
        with self.subTest():
            self.assertEqual(s.width, 30)
        with self.subTest():
            self.assertEqual(s.height, 30)

    def test_ToStr(self):
        """Converting squares to a string"""

        s = Square(1, 2, 3)
        msg = "[Square] (1) 2/3 - 1"
        with self.subTest():
            self.assertEqual(str(s), msg)
        s.x = 10
        s.y = 20
        msg = "[Square] (1) 10/20 - 1"
        with self.subTest():
            self.assertEqual(str(s), msg)
        s = Square(5, 6, 7, 8)
        msg = "[Square] (8) 6/7 - 5"
        with self.subTest():
            self.assertEqual(str(s), msg)
        s.size = 30
        msg = "[Square] (8) 6/7 - 30"
        with self.subTest():
            self.assertEqual(str(s), msg)

    def test_ToDict(self):
        """Converting the object to a dictionary"""

        s = Square(3, 10, 4, "square")
        d = {"id": "square", "size": 3, "x": 10, "y": 4}
        self.assertEqual(s.to_dictionary(), d)

    def test_Update(self):
        """Updating attributes using the update method"""

        s = Square(1, 2, 3)
        arguments = (
            ("id", "id"), ("size", 20), ("x", 30), ("y", 40), ("extra", 0)
        )
        d = s.to_dictionary()
        for i in range(len(arguments)):
            args = arguments[:i + 1]
            if i < len(arguments) - 1:
                d.update(args)
            with self.subTest():
                s.update(*(val for _, val in args))
                self.assertEqual(s.to_dictionary(), d)
        s.update("new", width=5)
        d["id"] = "new"
        with self.subTest():
            self.assertEqual(s.to_dictionary(), d)
        s.update("new", 1, 2, 3, 4)
        d = s.to_dictionary()
        for i in range(len(arguments)):
            args = arguments[:i + 1]
            if i < len(arguments) - 1:
                d.update(args)
            with self.subTest():
                s.update(**dict(args))
                self.assertEqual(s.to_dictionary(), d)
