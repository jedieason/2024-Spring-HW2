liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

def uniswap_trade(source_amount, pl_source, pl_dis):
    new_source_balance = pl_source + source_amount
    new_dis_balance = pl_source * pl_dis / new_source_balance
    dis_received = pl_dis - new_dis_balance
    return dis_received

def dfs(current_token, balance, path, visited_edges, best):
    if current_token == 'tokenB' and len(path) > 1 and balance > best[1]:
        best[0] = f"path: {'->'.join(path)}, tokenB balance={balance:.6f}"
        best[1] = balance
        return True
    
    found = False
    for (source, dis), (source_to_dis, dis_to_source) in liquidity.items():
        if source == current_token:
            if (source, dis) not in visited_edges:
                new_balance = uniswap_trade(balance, source_to_dis, dis_to_source)
                visited_edges.add((source, dis))
                found = dfs(dis, new_balance, path + [dis], visited_edges, best) or found
                visited_edges.remove((source, dis))
        elif dis == current_token:
            if (dis, source) not in visited_edges:
                new_balance = uniswap_trade(balance, dis_to_source, source_to_dis)
                visited_edges.add((dis, source))
                found = dfs(source, new_balance, path + [source], visited_edges, best) or found
                visited_edges.remove((dis, source))
    return found

i_balance = 5
i_token = 'tokenB'
i_path = [i_token]
visited_edges = set()
best_path = [None, -float('inf')]

if not dfs(i_token, i_balance, i_path, visited_edges, best_path):
    print("No profitable path found.")
else:
    print(best_path[0])
