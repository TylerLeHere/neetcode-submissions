class Node:
     def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:


    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # Mapping the key to the node

        #Before having any values in our cache, we want to have a couple of dummy pointer to tell us what are the most recent and least recent values that we added
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        #We want this nodes to be connected together because if we are putting a new node, we want to put it in the middle between left and right. We can do that with some pointer stuff

        self.left.next = self.right
        self.right.prev = self.left

        #Left is going to help us find the least recently used
        #Right is going to be the most recently used

    #Remove from linked list
    def remove(self, node):
        #Node is going to be the middle node, get the previous and next
        prevNode = node.prev
        nextNode = node.next

        prevNode.next = node.next
        nextNode.prev = node.prev
        #Now node longer in between


    #Insert to the right most position
    def insert(self, node):
        #Insert the node at the most right position, 
        prevNode = self.right.prev
        nextNode = self.right
        prevNode.next = nextNode.prev = node
        node.next, node.prev = nextNode, prevNode


    def get(self, key: int) -> int:
        #If the key exists, the key in our cache, we can return that value
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val # Return the node, to get the value just .val
        
        #Every time we get the value, we want to update it to the most recent, going to write a couple of helper function, like remove and insert

        #If it does not exist, return -1
        return -1
        

        

    def put(self, key: int, value: int) -> None:
        #If we have the key already in the cache, that means the node already existed, before we want to insert into our list, we want to remove it
        if key in self.cache:
            self.remove(self.cache[key])
        
        self.cache[key] = Node(key, value)
                #We have a double linked list, so make sure to insert it in our linked list

        self.insert(self.cache[key])

        #make sure if it exceeds capacity as well
        if len(self.cache) > self.cap:
            #Remove, delete or evict the least recently used
            #Remove from the linked list, and delete the LRU from the hashmap. Why we have the left, tells us what is least recently used
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]


        
