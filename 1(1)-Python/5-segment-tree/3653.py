from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    # 구현하세요!
    T = int(input())
    for _ in range(T):
        n, _ = map(int, input().split())
        pos : list[int] = [n-i+1 for i in range(n+1)]
        tree : SegmentTree = SegmentTree(
            200_001, 
            lambda x, y : x+y, 
            0, 
            [1 if 1 <= i and i <= n else 0 for i in range(200_001)]
        )
        pos_mx : int = n
        for x in map(int, input().split()):
            print(tree.query(pos[x]+1, pos_mx), end = ' ')
            tree.mergeValue(pos[x], -1)
            pos_mx += 1
            pos[x] = pos_mx 
            tree.mergeValue(pos[x], 1)
        print('')

if __name__ == "__main__":
    main()