// 2025-06-13 14:53
// 요약
// N 개의 정점 M 개의 단방향 간선
// N 개의 도시에 각각 면접자가 존재
// K 개의 도시에 면접장이 존재
// 각 도시의 면접자는 가장 가까운 도시로 이동
// 최소 거리인 면접장을 택해 이동할 때
// 가장 거리가 먼 도시에서 오는 면접자의 거리를 출력

// 제한
// 1초 256MB
// N 2~100,000
// M 1~500,000

// 풀이
// 각 N 개의 마을에서 출발해 K 개의 마을 중 하나에 도착해야 함
// 단방향이라 K 개의 마을에서 퍼뜨리는건 불가능?
// 어떤 마을 a 에서 다익스트라를 진행하면 K 인 마을을 만나는 시점..거기서는
//  a -> b 로 가는 정보를 줌
//  b -> a 인 정보로 저장(b 로 오는 a 의 거리)
// 역으로 K 인 마을에서 해당 마을로 들어오는 간선을 타고타고 가서 최단거리 인접 마을 구하기
// 다중 시작점 다익스트라 돌리고 각 마을의 거리 업데이트 하기
#include <iostream>
#include <algorithm>
#include <queue>
#include <unordered_map>

using namespace std;

long long INF = 1e18;

void dijkstra(long long dist[], unordered_map<int, unordered_map<int, int>> &adj_map, int k_cities[], int n, int k)
{
    priority_queue<pair<long long, int>, vector<pair<long long, int>>, greater<pair<long long, int>>> min_prio; // < distance, node >
    int cur, nxt;
    long long d, cost;

    for (int i = 0; i < k; i++)
    {
        min_prio.push({0, k_cities[i]});
        dist[k_cities[i]] = 0;
    }

    while (!min_prio.empty())
    {
        d = min_prio.top().first;
        cur = min_prio.top().second;
        min_prio.pop();

        if (dist[cur] < d)
            continue;

        for (auto &[nxt, cost] : adj_map[cur])
        {
            if (dist[nxt] > d + cost)
            {
                dist[nxt] = d + cost;
                min_prio.push({d + cost, nxt});
            }
        }
    }
}

int main()
{

    ios_base ::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    int N, M, K;
    cin >> N >> M >> K;
    unordered_map<int, unordered_map<int, int>> adj_map;
    int k_cites[K];
    long long dist[N + 1];
    fill(dist, dist + N + 1, INF);

    int u, v, c;
    for (int i = 0; i < M; i++)
    {
        cin >> u >> v >> c;
        if (adj_map[v].find(u) != adj_map[v].end())
        {
            adj_map[v][u] = min(adj_map[v][u], c);
        }
        else
        {
            adj_map[v][u] = c;
        }
    }
    for (int i = 0; i < K; i++)
    {
        cin >> k_cites[i];
    }

    dijkstra(dist, adj_map, k_cites, N, K);

    int output_node = 1;
    long long output_dist = 0;
    for (int i = 1; i < N + 1; i++)
    {
        if (dist[i] > output_dist)
        {
            output_dist = dist[i];
            output_node = i;
        }
        // cout << i << " " << dist[i] << "\n";
    }
    cout << output_node << "\n"
         << output_dist;
    return 0;
}