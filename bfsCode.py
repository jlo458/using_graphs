from collections import deque

# Understanding graphs and breadth-first search (bfs)
# Just playing around, nothing serious - shows friends of each person

def personIsSeller(person): 
  return person[-2:] == '.M'
     

graph = {} 
graph["me"] = ["Tom", "Dick", "Harry"] 
graph["Tom"] = ["Bob", "Dick"] 
graph["Dick"] = ["Peggy.M"] 
graph["Harry"] = ["Sue"]
graph["Bob"] = []
graph["Peggy.M"] = []
graph["Sue"] = [] 

search_queue = deque() 
search_queue += graph["me"] 
isSeller = False
searched = []

while search_queue: 
  person = search_queue.popleft() 
  if person not in searched:
    if personIsSeller(person): 
      print(person,' is a mango seller')
      isSeller = True 
  
    else: 
      search_queue += graph[person] 
      searched.append(person)

print(isSeller)
    
    
    
  
  


