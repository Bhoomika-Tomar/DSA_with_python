class Node:
    def __init__ (self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self, cap):
        #code here
        self.capacity = cap
        #USING DICTIONARY FOR KEY-VALUE PAIRS
        self.cache = { }
        self.head = Node (-1, -1)
        self.tail = Node (-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def remove (self, node):
        prevnode = node.prev
        nextnode = node.next
        prevnode.next = nextnode
        nextnode.prev = prevnode
        
    def add (self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key not in self.cache:
            return -1
            
        node = self.cache [key]
        self.remove (node)
        self.add (node)
        return node.value
    
        
    #Function for storing key-value pair.   
    def put(self, key, value):
        #code here
        if key in self.cache:
            node = self.cache[key]
            self.remove (node)
            del self.cache[key]
            
        #CAPACITY IS FULL, REMOVE LRU NODE
        if len(self.cache) == self.capacity:
            lru_node = self.tail.prev
            del self.cache [lru_node.key]
            self.remove (lru_node)
            
        #ADD A NEW NODE
        newnode = Node(key, value)
        self.add (newnode)
        self.cache [key] = newnode
            
