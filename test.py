
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
        # 更新两个节点集合
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