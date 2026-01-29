from lib import Trie, OptimizedTrie
import sys, math


"""
TODO:
- 일단 lib.py의 Trie Class부터 구현하기
- main 구현하기

힌트: 한 글자짜리 자료에도 그냥 str을 쓰기에는 메모리가 아깝다...
"""


def main() -> None:
    # 구현하세요!

    n : int = int(input())
    trie : OptimizedTrie = OptimizedTrie()
    lis : list[str] = []
    for _ in range(n):
        lis.append(input())
    for s in sorted(lis):
        trie.push(s)
    ans : int = 1
    mod : int = 1_000_000_007

    modFac : list[int] = [1] * 10000
    for i in range(1, 10000):
        modFac[i] = modFac[i-1] * i%mod

    for i in range(len(trie)):
        ans *= modFac[trie[i].child_count + int(trie[i].is_end)]
        ans %= mod
    print(ans)
    return

if __name__ == "__main__":
    main()