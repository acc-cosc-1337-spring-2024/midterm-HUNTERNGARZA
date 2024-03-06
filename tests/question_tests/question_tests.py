#write function tests here, don't add input('') statements here!
import unittest

#follow this example to add questions b, c, and d for testing including their functions
from src.question_a.question_a import test_config, get_sum_of_evens
from src.question_b.question_b import get_random_number
from src.question_c.question_c import is_prime

class Test_Config(unittest.TestCase):

    def test_question_a_config(self):
        self.assertEqual(True, test_config())

    def test_get_sum_of_evens(self):
        self.assertEqual(get_sum_of_evens(11), 30)
        self.assertEqual(get_sum_of_evens(10), 30)
        self.assertEqual(get_sum_of_evens(8), 20)

    def test_get_random_number(self):
        number = get_random_number()
        self.assertTrue(0 < number and number < 6)

    def test_is_prime(self):
        self.assertFalse(is_prime(4))
        self.assertTrue(is_prime(5))
        self.assertTrue(is_prime(11))
