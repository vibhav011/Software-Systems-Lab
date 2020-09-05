class Node(object):
	"""
	Node contains two objects - a left and a right child, both may be a Node or both None,
	latter representing a leaf
	"""
	def __init__(self, left=None, right=None):
		super(Node, self).__init__()
		self.left = left
		self.right = right

	def __str__(self):
		"""
		Default inorder print
		"""
		if self.left is None and self.right is None:
			return "(   )"
		else:
			return "( " + str(self.left) + " " + str(self.right) + " )"

	def __eq__(self, other):
		if self.left is None and self.right is None:
			return other.left is None and other.right is None
		elif other.left is None and other.right is None:
			return False
		else:
			return self.left == other.left and self.right == other.right


def mirrorTree(node):
	if node.left is None:
		return node
	mirrorTree(node.left)
	mirrorTree(node.right)
	node.left, node.right = node.right, node.left
	return node


def allTrees(n):
	if n == 0:
		return [Node()]
	final = []
	for i in range(n):
		left = allTrees(i)
		right = allTrees(n-1-i)
		ans = [Node(l, r) for l in left for r in right]
		final += ans
	return final


def allSymTrees(n):
	trees = allTrees(n)
	final = [tree for tree in trees if tree == mirrorTree(tree)]
	return final


if __name__ == '__main__':
	for x in allSymTrees(int(input())):
		print(x)
	node = Node(Node(Node(), Node()), Node())
	print(node)
