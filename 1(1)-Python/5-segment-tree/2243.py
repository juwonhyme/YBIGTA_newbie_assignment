from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


def main() -> None:
    # 구현하세요!
    n : int = int(input())
    tree : SegmentTree = SegmentTree(
        1_000_001, 
        lambda x, y : x + y, 
        0, 
        [0]*1_000_001
    )
    for _ in range(n):
        lis : list[int] = list(map(int, input().split()))
        if lis[0] == 1:
            s : int = 0
            e : int = 1_000_000
            while s + 1 < e:
                m : int = (s + e)//2
                count : int = tree.query(1, m)
                if count < lis[1]:
                    s = m 
                else:
                    e = m
            print(e)
            tree.mergeValue(e, -1)
        if lis[0] == 2:
            tree.mergeValue(lis[1], lis[2])
            
if __name__ == "__main__":
    main()