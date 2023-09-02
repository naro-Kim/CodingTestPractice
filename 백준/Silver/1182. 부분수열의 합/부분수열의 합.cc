#include <iostream>
using namespace std;

int n, s; // s == sum condition
int cnt = 0; // cnt = number of subsequence that satisfies the condition
int arr[22];

void dfs(int idx, int sum) // 인자 idx는 현재 탐색중인 arr의 인덱스, sum은 해당 인덱스까지 부분 수열의 합
{
	// n번째 수까지 탐색 끝
	if (idx == n) {
		if (sum == s) cnt++;
		return; // 재귀 종료 조건
	}
	// 재귀를 통해 sum을 계속 더해나간다.
	dfs(idx + 1, sum);
	dfs(idx + 1, sum+arr[idx]);
}

int main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
	
	cin >> n >> s;
	for (int i = 0; i < n; i++)
	{
		cin >> arr[i];
	}
	dfs(0, 0); // dfs로 조건을 만족하는 부분집합 갯수를 센다.
	if (s == 0) cnt--; // 공집합은 cnt를 빼준다.
	cout << cnt;
	return 0;
}