from lib import SegmentTree
import sys


"""
TODO:
- 일단 SegmentTree부터 구현하기
- main 구현하기
"""


class Pair(tuple[int, int]):
    """
    힌트: 2243, 3653에서 int에 대한 세그먼트 트리를 만들었다면 여기서는 Pair에 대한 세그먼트 트리를 만들 수 있을지도...?
    """
    def __new__(cls, a: int, b: int) -> 'Pair':
        return super().__new__(cls, (a, b))

    @staticmethod
    def default() -> 'Pair':
        """
        기본값
        이게 왜 필요할까...?
        """
        return Pair(0, 0)

    @staticmethod
    def f_conv(w: int) -> 'Pair':
        """
        원본 수열의 값을 대응되는 Pair 값으로 변환하는 연산
        이게 왜 필요할까...?
        """
        return Pair(w, 0)

    @staticmethod
    def f_merge(a: 'Pair', b: 'Pair') -> 'Pair':
        """
        두 Pair를 하나의 Pair로 합치는 연산
        이게 왜 필요할까...?
        """
        return Pair(*sorted([*a, *b], reverse=True)[:2])

    def sum(self) -> int:
        return self[0] + self[1]


def main() -> None:
    # 구현하세요!
    n : int = int(input())
    A : list[int] = [0] + list(map(int, input().split()))
    tree : SegmentTree = SegmentTree(
        n+1, 
        Pair.f_merge,
        Pair.default(),
        [Pair.f_conv(A[i]) for i in range(n+1)]
    )
    m : int = int(input())
    for _ in range(m):
        line = list(map(int, input().split()))
        query : int = line[0]
        if query == 1:
            i, v = line[1:]
            tree.setValue(i, Pair.f_conv(v))
        if query == 2:
            l, r = line[1:]
            print(Pair.sum(tree.query(l, r)))

if __name__ == "__main__":
    main()