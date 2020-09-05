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
	left = mirrorTree(node.left)
	right = mirrorTree(node.right)
	return Node(right, left)


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
	if n%2 == 0:
		return []
	trees = allTrees(n//2)
	mirrors = [mirrorTree(tree) for tree in trees]
	final = [Node(tree, mirror) for tree in trees for mirror in mirrors]
	return final


if __name__ == '__main__':
	x = allSymTrees(int(input()))
	node = Node(Node(Node(), Node()), Node())