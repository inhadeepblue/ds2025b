class Graph:
	def __init__ (self, size):
		self.graph = [[0 for _ in range(size)] for _ in range(size)]


class DisjointSet:  # 크루스칼 알고리즘을 위한 유틸리티 클래스
	def __init__(self, n):
		self.parent = [i for i in range(n)]

	def find(self, x):
		if self.parent[x] != x:
			self.parent[x] = self.find(self.parent[x])
		return self.parent[x]

	def union(self, x, y):
		x_root = self.find(x)
		y_root = self.find(y)
		if x_root != y_root:
			self.parent[y_root] = x_root
			return True
		return False


def print_graph(g) :
	print(' ', end = ' ')
	for v in range(len(g.graph)) :
		print(name_ary[v], end =' ')
	print()
	for row in range(len(g.graph)) :
		print(name_ary[row], end =' ')
		for col in range(len(g.graph)) :
			print(f"{g.graph[row][col]:2d}", end=' ')
		print()
	print()


g1 = None
name_ary = ['인천', '서울', '강릉', '대전', '광주', '부산']
incheon, seoul, gangneung, daejeon, gwangju, busan = 0, 1, 2, 3, 4, 5

graph_size = 6
g1 = Graph(graph_size)
g1.graph[incheon][seoul] = 10; g1.graph[incheon][gangneung] = 15
g1.graph[seoul][incheon] = 10; g1.graph[seoul][gangneung] = 40; g1.graph[seoul][daejeon] = 11; g1.graph[seoul][gwangju] = 55
g1.graph[gangneung][incheon] = 15; g1.graph[gangneung][seoul] = 40; g1.graph[gangneung][daejeon] = 12
g1.graph[daejeon][seoul] = 11; g1.graph[daejeon][gangneung] = 12; g1.graph[daejeon][gwangju] = 20; g1.graph[daejeon][busan] = 30
g1.graph[gwangju][seoul] = 55; g1.graph[gwangju][daejeon] = 20; g1.graph[gwangju][busan] = 28
g1.graph[busan][daejeon] = 30; g1.graph[busan][gwangju] = 28

print('도시 간 도로 건설을 위한 전체 연결도')
print_graph(g1)

edge_ary = []
for i in range(graph_size) :
	for j in range(graph_size) :
		if g1.graph[i][j] != 0 :
			edge_ary.append([g1.graph[i][j], i, j])
print(edge_ary)

edge_ary.sort()  # 오름차순
print(edge_ary)


ds = DisjointSet(graph_size)
mst_edges = list()
mst_cost = 0

for cost, s, e in edge_ary:
	if ds.union(s, e):
		mst_edges.append((cost, s, e))
		mst_cost = mst_cost + cost


mst_graph = Graph(graph_size)
for cost, s, e in mst_edges:
	mst_graph.graph[s][e] = cost
	mst_graph.graph[e][s] = cost


print('최소 비용 계산')
print_graph(mst_graph)
print(f"최소 비용 :  {mst_cost}")

print('\nMST 간선 목록')
for cost, u, v in mst_edges:
	print(f"{name_ary[u]} --- {name_ary[v]} : {cost}")