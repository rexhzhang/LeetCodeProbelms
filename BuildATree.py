from collections import deque


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BuildTree(object):

    def __init__(self, data: list):
        self.data = iter(data)
    

    def build(self):
        try:
            val = next(self.data)
        except:
            return

        if val == None:
            return None

        node = TreeNode(val)
        node.left = self.build()
        node.right = self.build()
        
        return node
    
    def printTree(self, node):
        q = deque([node])
        print(q)
        while q:
            if len(set(q)) == 1 and '#' in set(q):
                break 
            
            new_q= deque([])
            print_queue = []
            while q:
                node = q.popleft()
                if node == '#':
                    print_queue.append('#')
                    new_q.append('#')
                    new_q.append('#')
                else:

                    print_queue.append(node.val)

                    if node.left and node.right:
                        new_q.append(node.left)
                        new_q.append(node.right)
                        
                    elif node.left :
                        new_q.append(node.left)
                        new_q.append('#')
                    elif node.right:
                        new_q.append('#')
                        new_q.append(node.right)
            
            print(print_queue)

            q = new_q
                        
                    


