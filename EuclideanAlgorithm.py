class EuclideanAlgorithm: #A class to encapsulate the Euclidean Algorithm for finding the GCD.

    def calculate_gcd(self, number_1: int, number_2: int) -> int: #Calculate the greatest common divisor of two positive integers.
        while number_2 != 0:  # Repeat until the second number becomes 0
            remainder = number_1 % number_2 # Find the remainder of number_1 divided by number_2
            number_1 = number_2 # Update number_1 to be the value of number_2
            number_2 = remainder # Update number_2 to be the remainder
        return number_1 # Return the GCD, which is stored in number_1 when the loop ends