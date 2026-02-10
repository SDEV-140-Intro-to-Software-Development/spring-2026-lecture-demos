def print_human_head():
	print("o   o")
	print("  >  ")

def print_monkey_head():
	print("( o o )")
	print("  \"  ")

def print_figure(face):
	face()
	print("  |")
	print("--|--")

choice = int(input('Enter 1=monkey, 2=human: '))
if choice == 1:
	print_figure(print_monkey_head)
elif choice == 2:
	print_figure(print_human_head)
