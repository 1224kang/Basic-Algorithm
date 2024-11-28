import queue


def bfs(graph, start):
    visited={start}
    que=queue.Queue()
    que.put(start)
    while not que.empty():
        v=que.get()
        print(v,end=' ')
        nbr=graph[v]-visited
        for u in nbr:
            visited.add(u)
            que.put(u)
    return None



mygraph = dict()
n=int(input())

for i in range(n):
    edge=input().strip()
    node1,node2=edge.split()

    if node1 not in mygraph:
        mygraph[node1]=set()
    mygraph[node1].add(node2)

    if node2 not in mygraph:
        mygraph[node2]=set()
    mygraph[node2].add(node1)


print('BFS : ', end='')
bfs(mygraph, "A")
print()
