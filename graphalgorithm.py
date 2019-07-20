def find_path(graph, start, end, path=[]):
    path += [start]
    print('Path Awal', path)
    if start == end:
        return path
    if start not in graph:
        return None
    for node in graph[start]:
        print('Node sekarang %s dari Start %s' % (node, start))
        if node not in path:
            print('Path Kedua', node)
            newpath = find_path(graph, node, end, path)
            print('Newpath = ', newpath)
            if newpath: return newpath
    return None


def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    print('Path Awal', path)
    if start == end:
        return [path]
    if start not in graph:
        return []
    paths = []
    for node in graph[start]:
        print('Node sekarang %s dari Start %s' % (node, start))
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            print('Newpaths = ', newpaths)
            for newpath in newpaths:
                paths.append(newpath)
    print('Semua Path', paths)
    return paths


def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    print('Path Awal =', path)
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None

    for node in graph[start]:
        print('Node sekarang %s dari Start %s' % (node, start))
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            print('Newpath = ', newpath)
            if newpath:
                if not shortest or len(newpath) < len(shortest):
                    shortest = newpath
    print('Path Terpendek = ', shortest)
    return shortest


def find_longest_path(graph, start, end, path=[]):
    path = path + [start]
    print('Path Awal', path)
    if start == end:
        return path
    if start not in graph:
        return None
    longest = None

    for node in graph[start]:
        print('Node sekarang %s dari Start %s' % (node, start))
        if node not in path:
            newpath = find_longest_path(graph, node, end, path)
            print('Newpath = ', newpath)
            if newpath:
                if not longest or len(newpath) > len(longest):
                    longest = newpath
    print('Path Terpanjang = ', longest)
    return longest


graph = {'A': ['B', 'C'],
         'B': ['C', 'D'],
         'C': ['D'],
         'D': ['C'],
         'E': ['F'],
         'F': ['C']}
print('============ Mencari path =============')
print('Hasil akhir', find_path(graph, 'A', 'C'))
print('============ Mencari semua path ============')
print('hasil akhir semua path', find_all_paths(graph, 'A', 'C'))
print('============ Mencari path terpendek ============')
print('hasil akhir path terpendek', find_shortest_path(graph, 'A', 'C'))
print('============ Mencari path terpanjang ============')
print('hasil akhir path terpanjang', find_longest_path(graph, 'A', 'C'))


