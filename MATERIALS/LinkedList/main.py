from linked_list import LinkedList

def main():
	my_list = LinkedList()

	my_list.append(2)
	my_list.append(3)
	my_list.append(6)
	my_list.append(8)

	print(my_list)

	my_list.reverse()

	print(my_list)


if __name__ == "__main__":
	main()
