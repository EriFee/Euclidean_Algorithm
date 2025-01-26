class EuclideanAlgorithm: #A class to encapsulate the Euclidean Algorithm for finding the GCD.

    def calculate_gcd(self, number_1: int, number_2: int) -> int: #Calculate the greatest common divisor of two positive integers.
        while number_2 != 0:  # Repeat until the second number becomes 0
            remainder = number_1 % number_2 # Find the remainder of number_1 divided by number_2
            number_1 = number_2 # Update number_1 to be the value of number_2
            number_2 = remainder # Update number_2 to be the remainder
        return number_1 # Return the GCD, which is stored in number_1 when the loop ends
    
    def get_user_input(self): #Get valid user input and calculate GCD.
        while True:
            try:
                # Get input from the user
                number_1 = int(input("Enter the first positive integer: "))
                number_2 = int(input("Enter the second positive integer: "))
                
                # Check if both numbers are positive
                if number_1 <= 0 or number_2 <= 0:
                    raise ValueError("Both numbers must be positive integers.")
                
                # Calculate and return the GCD
                gcd = self.calculate_gcd(number_1, number_2)
                print(f"The GCD of {number_1} and {number_2} is: {gcd}")
                break  # Exit the loop once the calculation is successful
                
            except ValueError:
                print("Please enter valid positive integers.")

