import sys
input = sys.stdin.readline

class ListNode():
    def __init__(self, value):
        self.value = value
        self.nexts = {}
        
rooms = {}
preys = []

n = int(input())
for i in range(n):
    preys.append(list(input().split())[1:])

    
for prey in preys:
    if prey[0] in rooms:
        node = rooms[prey[0]]
    else:
        node = ListNode(prey[0])
        rooms[prey[0]] = node

    for i in range(1, len(prey)):
        if prey[i] in node.nexts:
            node = node.nexts[prey[i]]
        else:
            new_node = ListNode(prey[i])
            node.nexts[prey[i]] = new_node
            node = new_node

def dfs(node, depth, ret=[]):
    if len(node.nexts)==0:
        ret.append('-'*depth*2 + node.value)
    else:
        ret.append('-'*depth*2 + node.value)
        keys = list(node.nexts.keys())
        keys.sort()
        for key in keys:
            dfs(node.nexts[key], depth+1, ret=ret)
            
answers = []
keys = list(rooms.keys())
keys.sort()
for key in keys:
    ret = []
    dfs(rooms[key], 0, ret=ret)
    answers.append(ret)        

for answer in answers:
    print(*answer, sep="\n")