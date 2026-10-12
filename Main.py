from LogicModel import LogicModel


def main():
	print("Hello, world!")
	logic_model = LogicModel()
	print("Sum:", logic_model.return_sum(5, 10))
	print("Ways to climb stairs:", logic_model.count_stairs(5))
	print("Is 'racecar' a palindrome?", logic_model.palindromic("racecar"))
	print("Is 'hello' a palindrome?", logic_model.palindromic("hello"))
	print("Square of 5:", logic_model.square_num(5))

if __name__ == "__main__":
	main()
