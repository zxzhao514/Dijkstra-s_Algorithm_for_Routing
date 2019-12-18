## Project III Dijkstra’s Algorithm for Routing

#### Jason Zhao 4405 3635

### Project Description

In networks, a node needs to find out the shortest path to the rest in the same network. The weights associated with links are also referred as costs. In this project, it is simply the distance. Dijkstra’s algorithm is commonly used to server this purpose for network routing, Google Maps and shortest path for robotics.

### Algorithms

```pseudocode
1:	function Dijkstra(Graph, source):
2:	for each vertex v in Graph:	// Initialization
3:	dist[v] := infinity	// initial distance from source to vertex v 
4:	previous[v] := undefined	// Previous node in optimal path from source
5:	dist[source] := 0	// Distance from source to source
6:	Q := the set of all nodes in Graph	// all nodes in the graph are unoptimized - thus are in Q
7:	while Q is not empty:	// main loop
8:	u := node in Q with smallest dist[ ]
9:	remove u from Q
10:	for each neighbor v of u:	// where v has not yet been removed from Q.
11:	alt := dist[u] + dist_between(u, v)
12:	if alt < dist[v]	// Relax (u,v)
13:	dist[v] := alt
14:	previous[v] := u
15:	return previous[ ]
```

### Source Code

```python
import numpy as np
from numpy import Infinity, sqrt, argmin
from numpy.random import randint
from matplotlib.pyplot import figure, plot, text

def dijkstra(graph, src):

    if graph is None:
        return None
    nodes = [i for i in range(len(graph))]  # obtain all the original nodes
    visited = []  # minimum distance list
    if src in nodes:
        visited.append(src)
        nodes.remove(src)
    else:
        return None
    distance = {src: 0}  # record distance between source node and each node
    for i in nodes:
        distance[i] = graph[src][i]  # initialization
    # print(distance)
    path = {src:{src:[]}}  # distance the route
    k = pre = src
    while nodes:
        mid_distance=float('inf')
        for v in visited:
            for d in nodes:
                new_distance = graph[src][v]+graph[v][d]
                if new_distance < mid_distance:
                    mid_distance = new_distance
                    graph[src][d] = new_distance  # updating the distance
                    k=d
                    pre=v
        distance[k]=mid_distance  # minimal route
        path[src][k]=[i for i in path[src][pre]]
        path[src][k].append(k)

        visited.append(k)
        nodes.remove(k)
        print(visited, nodes)
    return distance, path

  
  if __name__ == '__main__':

    # Data Preparing & Plotting
    N = 100
    x1 = randint(10, 90, size=N)
    y1 = randint(10, 90, size=N)
    ind = [i for i, v in enumerate(x1) if v < 40 or v > 60]
    # let x, y br lists with elements whose values are under 40 or over 60
    x, y = x1[ind], y1[ind]
    N = len(x)

    # set first and last elements of x and y as 0 and 100
    x[0], x[-1] = 0, 100
    y[0], y[-1] = 0, 100

    fig = figure(1, figsize=(16, 16))
    plot(x, y, 'ko', ms=16)
    plot(x[0], y[0], 'bs', ms=18)
    plot(x[-1], y[-1], 'bs', ms=18)

    # This is to show the source node and last node of the program
    for i in range(N):
        if i == 0:
            text(x[i], y[i] + 2, 'S', fontsize=16)
        elif i == N - 1:
            text(x[i], y[i] + 2, 'D', fontsize=16)
        else:
            text(x[i], y[i] + 2, str(i), fontsize=16)

    graph_list = [x, y]

    distance, path = dijkstra(graph_list, 0)
    print(distance, path)
    
```

### Program Outputs

hop = 40

![hop = 40](/Users/zixuanzhao/Downloads/Dijkstra-s_Algorithm_for_Routing-master/hop = 40.png)

hop = 50

![hop = 50](/Users/zixuanzhao/Downloads/Dijkstra-s_Algorithm_for_Routing-master/hop = 50.png)

hop = 60

![hop = 60](/Users/zixuanzhao/Downloads/Dijkstra-s_Algorithm_for_Routing-master/hop = 60.png)

hop = 70

![hop = 40](/Users/zixuanzhao/Downloads/Dijkstra-s_Algorithm_for_Routing-master/hop = 70.png)

hop = 80

![hop = 40](/Users/zixuanzhao/Downloads/Dijkstra-s_Algorithm_for_Routing-master/hop = 80.png)