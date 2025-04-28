class TreeNode:
	def __init__(self):
		self.left = None
		self.data = None
		self.right = None


if __name__ == "__main__":
    numbers = [10, 15, 8, 3, 9]
    root = None

    node = TreeNode()
    node.data = numbers[0]
    root = node

    for number in numbers[1:]:
        node = TreeNode()
        node.data = number
        current = root
        while True:
            if number < current.data:
                if current.left is None:
                    current.left = node
                    break
                current = current.left  # move
            else:
                if current.right is None:
                    current.right = node
                    break
                current = current.right  # move

    print("BST 구성 완료")

    find_number = int(input())

    current = root
    while True:
        if find_number == current.data:
            print(f"{find_number}을(를) 찾았습니다")
            break
        elif find_number < current.data:
            if current.left is None:
                print(f"{find_number}이(가) 존재하지 않습니다")
                break
            current = current.left
        else:
            if current.right is None:
                print(f"{find_number}이(가) 존재하지 않습니다")
                break
            current = current.right