class TreeNode(object):
    def __init__(self, val, info, seats):
        self.val = val
        self.info = info
        self.seats=seats
        self.left = None
        self.right = None
        self.height = 1

class AVL_Tree(object):
    def insert(self, root, key, info, seats):
        if not root:
            return TreeNode(key, info, seats)
        elif key < root.val:
            root.left = self.insert(root.left, key, info, seats)
        else:
            root.right = self.insert(root.right, key, info, seats)
        root.height = 1 + max(self.getHeight(root.left),
                           self.getHeight(root.right))
        balance = self.getBalance(root)
        # Case 1 - Left Left
        if balance > 1 and key < root.left.val:
            return self.rightRotate(root)
        # Case 2 - Right Right
        if balance < -1 and key > root.right.val:
            return self.leftRotate(root)
        # Case 3 - Left Right
        if balance > 1 and key > root.left.val:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        # Case 4 - Right Left
        if balance < -1 and key < root.right.val:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root) 
        return root
 
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left),
                         self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                         self.getHeight(y.right))
        return y
 
    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left),
                        self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                        self.getHeight(y.right))
        return y
 
    def getHeight(self, root):
        if not root:
            return 0
 
        return root.height
 
    def getBalance(self, root):
        if not root:
            return 0
 
        return self.getHeight(root.left) - self.getHeight(root.right)
 
    def preOrder(self, root):
        if not root:
            return
        print("-------------------------------------------------------------------------------------------")
        print("BOOKING ID: ", "{0} ".format(root.val), end="\n")
        print("SEATS BOOKED: ", root.seats, end="\n")
        print("-------------------------------------------------------------------------------------------")       
        self.preOrder(root.left)
        self.preOrder(root.right)

    def getMinValueNode(self, root):
        if root is None or root.left is None:
            return root
 
        return self.getMinValueNode(root.left)
        
    def delete(self, root, key, temp2):
        if not root:
            return root
 
        elif key < root.val:
            root.left = self.delete(root.left, key, temp2)
 
        elif key > root.val:
            root.right = self.delete(root.right, key, temp2)
 
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
 
            elif root.right is None:
                temp = root.left
                root = None
                return temp
 
            temp = self.getMinValueNode(root.right)
            temp2= root.seats
            root.seats=temp.seats
            root.info=temp.info
            root.val = temp.val
            root.right = self.delete(root.right, temp.val, temp2)
            
 
        if root is None:
            return root
        root.height = 1 + max(self.getHeight(root.left),
                            self.getHeight(root.right))
 
        balance = self.getBalance(root)
 
        # Case 1 - Left Left
        if balance > 1 and self.getBalance(root.left) >= 0:
            return self.rightRotate(root)
 
        # Case 2 - Right Right
        if balance < -1 and self.getBalance(root.right) <= 0:
            return self.leftRotate(root)
 
        # Case 3 - Left Right
        if balance > 1 and self.getBalance(root.left) < 0:
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
 
        # Case 4 - Right Left
        if balance < -1 and self.getBalance(root.right) > 0:
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
 
        #print(temp2)
        return [root, temp2]

    def searchNode(self, root, value):
        if root== None:
            return False
        if root.val == value:
            #=[]
            #temp=root.seats
            #print(root.seats)
            #print(temp)
            return True
        elif value < root.val:
            self.searchNode(root.left, value)
        elif value > root.val:
            self.searchNode(root.right, value)

    def returnList(self, root, value, temp):   
        if root.val == value:
            #=[]
            temp=root.seats
            #print(root.seats)
            print(temp)
            return root.seats
        elif value < root.val:
            self.returnList(root.left, value, temp)
            #print(temp)
        elif value > root.val:
            self.returnList(root.right, value, temp)
            #print(temp)
        print("test")
        return temp



    def updateTicket(self, root, value, temp):
        if root.val == value:
            for i in temp:
                #print(i)
                root.seats.remove(i)
            return True
        elif value < root.val:
            if root.left.val == value:
                return True
            else:
                self.updateTicket(root.left, value)
        elif value > root.val:
            if root.right.val == value:
                return True
            else:
                self.updateTicket(root.right, value)
        else:
            return False

    def viewSeats(self, root, value):
        #print("Seats booked under ", value)
        #print(root.seats)
        if root.val == value:
            print("Seats booked under ", value)
            #print(root.val)
            for i in root.seats:
                print(i, end= " ")
            return True
        elif value < root.val:
            self.viewSeats(root.left, value)
        elif value > root.val:
            self.viewSeats(root.right, value)
        else:
            return False

     
