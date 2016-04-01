import networkx as nx

def gen_graph(words):
	from string import ascii_lowercase as lowercase
	G = nx.Graph(name="word ladder")
	charMap = dict((c,lowercase.index(c))for c in lowercase)
	def genWords(word):
		for i in range(len(word)):
			left, c, right = word[0:i], word[i], word[i+1:]
			index = charMap[c]
			for char in lowercase[index+1:]:
				yield left + char + right
	gen = ((word, cand)for word in sorted(words)
		for cand in genWords(word) if cand in words)
	G.add_nodes_from(words)
	for word, cand in gen:
		G.add_edge(word, cand)
	return G

def make_graph():
	fh = open('words4.dat','r')
	words = set()
	for line in fh.readlines():
		line = line.decode()
		if line.startswith('*'):
			continue
		w = str(line[0:4])
		words.add(w)
	return gen_graph(words)

if __name__ == '__main__':
	from networkx import *
	G = make_graph()
	for (source, target) in [('cold','warm'),
							('love','hate')]:
		print("Shortest path between %s and %s is"%(source,target))
		try:
			sp=shortest_path(G, source, target)
			for n in sp:
				print(n)
		except nx.NetworkXNoPath:
			print("None")

