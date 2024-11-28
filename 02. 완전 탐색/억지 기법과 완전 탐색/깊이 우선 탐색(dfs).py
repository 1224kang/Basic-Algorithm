def dfs(graph, start, visited ):
    if start not in visited:
        visited.add(start)
        print(start,end=' ')
        nbr=graph[start]-visited
        for v in nbr:
            dfs(graph,v,visited)
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



print('DFS : ', end='')
dfs(mygraph, "A", set() )
print()