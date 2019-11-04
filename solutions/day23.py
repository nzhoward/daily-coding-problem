def get_shortest_path(maze, start, end, dist, prev, visited):

    start_i = start[0]
    start_j = start[1]
    
    if start == end:
        return

    if start_i - 1 >= 0 and not maze[start_i - 1][start_j] and dist[start_i - 1][start_j] is None:
        dist[start_i - 1][start_j] = prev + 1
        
    if start_i + 1 < len(maze) and not maze[start_i + 1][start_j] and dist[start_i + 1][start_j] is None:
        dist[start_i + 1][start_j] = prev + 1
        
    if start_j - 1 >= 0 and not maze[start_i][start_j - 1] and dist[start_i][start_j - 1] is None:
        dist[start_i][start_j - 1] = prev + 1
        
    if start_j + 1 < len(maze[0]) and not maze[start_i][start_j + 1] and dist[start_i][start_j + 1] is None:
        dist[start_i][start_j + 1] = prev + 1
    
    if start_i - 1 >= 0 and not maze[start_i - 1][start_j] and not visited[start_i - 1][start_j]:
        visited[start_i - 1][start_j] = True
        get_shortest_path(maze, (start_i - 1, start_j), end, dist, dist[start_i - 1][start_j], visited)
    if start_i + 1 < len(maze) and not maze[start_i + 1][start_j] and not visited[start_i + 1][start_j]:
        visited[start_i + 1][start_j] = True
        get_shortest_path(maze, (start_i + 1, start_j), end, dist, dist[start_i + 1][start_j], visited)
    if start_j - 1 >= 0 and not maze[start_i][start_j - 1] and not visited[start_i][start_j - 1]:
        visited[start_i][start_j - 1] = True
        get_shortest_path(maze, (start_i, start_j - 1), end, dist, dist[start_i][start_j - 1], visited)
    if start_j + 1 < len(maze[0]) and not maze[start_i][start_j + 1] and not visited[start_i][start_j + 1]:
        visited[start_i][start_j + 1] = True
        get_shortest_path(maze, (start_i, start_j + 1), end, dist, dist[start_i][start_j + 1], visited)

    return dist, dist[end[0]][end[1]]


f = False
t = True

maze1 = [[f, f, f, f],
        [t, t, f, t],
        [f, f, f, f],
        [f, f, f, f]]

dist1 = [[None for i in range(len(maze1[0]))] for j in range(len(maze1))]
visited1 = [[False for i in range(len(maze1[0]))] for j in range(len(maze1))]
start1 = (3, 0)
end1 = (0, 0)

dist1[start1[0]][start1[1]] = 0
print(get_shortest_path(maze1, start1, end1, dist1, 0, visited1))


maze2 = [[f, f, f, f, f],
         [t, t, t, t, f],
         [f, f, f, f, f]]

dist2 = [[None for i in range(len(maze2[0]))] for j in range(len(maze2))]
visited2 = [[False for i in range(len(maze2[0]))] for j in range(len(maze2))]
start2 = (2, 0)
end2 = (0, 0)

dist2[start2[0]][start2[1]] = 0
print(get_shortest_path(maze2, start2, end2, dist2, 0, visited2))
