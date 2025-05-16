class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} # map key ->  [ <- Node -> ]

        #left=LRU, right=most recent (dummy nodes just to instantly get which is LRU and MostRecent)
        self.left, self.right = Node(0,0), Node(0,0)
        self.left.next, self.right.prev = self.right, self.left

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
    # insert node at right
    def insert(self, node):
        prev, nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.next, node.prev = nxt, prev

    def get(self, key: int) -> int:
        if key in self.cache:
            # TODO: update most recent
            # 1st: remove it from cache
            self.remove(self.cache[key])
            # 2nd: reinsert it at the Rightmost
            self.insert(self.cache[key])

            #                     .val bcz self.cache is "key ->  [ <-Node-> ]", 
            return self.cache[key].val
            # to get [ <-Node-> ]'s value
        return -1

    def put(self, key: int, value: int) -> None:
        # to make sure that the VALUE is this new updated put(key,value) one
        # we remove if existing same KEY 
        if key in self.cache:
            self.remove(self.cache[key])
        # then we point the cache to this Node
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])

        # but now we worry about capacity
        if len(self.cache) > self.cap:
            # we remove from the list and delete the LRU from the hashmap
            # so now we just get Left -> [Node]...[..]
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]



        

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)