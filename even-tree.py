#!/bin/python


from pprint import pprint


def get_input():
    nodec, edgec = raw_input().strip().split()
    nodec = int(nodec)
    edgec = int(edgec)
    edges = list()
    for i in xrange(edgec):
        edges.append([int(n) for n in raw_input().strip().split()])
    return nodec, edgec, edges


def get_root_node(edges):
    child_nodes = [e[0] for e in edges]
    parent_nodes = [e[1] for e in edges]
    # print 'parents'
    # pprint(parent_nodes)
    for p in parent_nodes:
        if p not in child_nodes:
            return p, child_nodes, parent_nodes


def count_children(t, n):
    for k, v in t.items():
        if n is k:
            return len(v)

def get_order(tree):
    max_len = int()
    order = list()
    for k, v in tree.items():
        if len(v) > max_len:
            max_len = len(v)
    for i in xrange(max_len):
        for k, v in tree.items():
            if len(v) == i+1:
                # add to stack
                order.append(k)
    return order


def count_parents(tree):
    c = list()
    for v in tree.values():
        c += v
    for node in c:
        print 'child:', node
        # if node in tree.keys():
            # tree['c' + node] =

def create_tree(c, p, r, e):
    tree = dict()
    tree[r] = [x[0] for x in e if x[1] is r]
    for pnode in set(p):
        tree[pnode] = list()
        for x in e:
            if pnode is x[1]:
                tree[pnode].append(x[0])
    child_count = dict()
    for node in set(c):
        if c in p:
            child_count[node] = len(tree[node])
        if node in c:
            # print 'do something'
            pass
    tree['cc'] = child_count
    return tree


def cut_branches(tree, p):
    pprint(tree)
    cuts = int()
    for node in set(p):
        if (len(tree[node]) + 1) % 2 == 0:
            cuts += 1
            print 'cutting off:', node, tree[node]
        else:
            print 'parent:', node, 'can not be cut'
    return cuts - 1


def main():
    nodec, edgec, edges = get_input()
    r, c, p = get_root_node(edges)
    tree = create_tree(c, p, r, edges)
    count_parents(tree)
    # print cut_branches(tree, p)


if __name__ == '__main__':
    main()
