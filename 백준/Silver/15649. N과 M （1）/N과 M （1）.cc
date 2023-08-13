#include <bits/stdc++.h>
using namespace std;
#include <iostream>
using namespace std;

int n, m; // m == depth
int arr[9] = { 0, };
bool visited[9] = { 0, };

void dfs(int cnt)
{
	//탐색 끝
	if (cnt == m) 
	{
		for (int i = 0; i < m; i++) cout << arr[i] << ' ';
		cout << '\n';
	}
	//탐색 진행중
	for (int i = 1; i <= n; i++) // 1<= m <=  n <= 8이므로 index를 1부터 시작한다.
	{
		if (!visited[i])
		{
			visited[i] = true;
			arr[cnt] = i;
			dfs(cnt+1);
			visited[i] = false; // visited 해제
		}
	}
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> n >> m;
	dfs(0);
	return 0;
}
