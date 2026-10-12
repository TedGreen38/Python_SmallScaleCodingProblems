


class LogicModel:
    """Base class for models that encapsulate application logic."""

    # Returns the sum of the model's data
    def return_sum(self, valueA: int, valueB: int) -> int:
        """Return the sum of the model's data."""
        return valueA + valueB

    # Returns the number of ways to climb n stairs, taking 1 or 2 steps at a time
    def count_stairs(self, n: int) -> int:
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            return self.count_stairs(n - 1) + self.count_stairs(n - 2)

    # Returns boolean value indicating whether the string is a palindrome
    def palindromic(self, s: str) -> bool:

        cleaned = ''.join(c.lower() for c in s if c.isalnum())
        return cleaned == cleaned[::-1]

    # Returns the square of the input number
    def square_num(self, n: int) -> int:
        return n * n