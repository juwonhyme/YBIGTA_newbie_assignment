from __future__ import annotations

from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Callable


"""
TODO:
- SegmentTree 구현하기
"""


T = TypeVar("T")
U = TypeVar("U")


class SegmentTree(Generic[T, U]):
    """
    0-based non-recursive segment tree
    
    n : size 
    merge : function used when two child values are merged
    arr : initial array

    setValue(i, v) : set value of index i -> tree[x] = v
    mergeValue(i, v) : merge value of index i -> tree[x] = merge(tree[x], v)
    query(l, r) : return merge(tree[l] ... tree[r])

    """
    # 구현하세요!
    def __init__(
            self, 
            n : int, 
            merge : Callable[[T, T], T], 
            identity : T,
            arr : Optional[list[T]] = None
        ) -> None:
        """
        Docstring for __init__
        
        :param n: size of index ([0 .. n-1])
        :type n: int
        :param merge: function which merges two node
        :type merge: Callable[[T, T], T]
        :param identity: identity value (= null value)
                        0 (when merge function equals to +)
                        -INF (when merge function equals to max)
        :type identity: T
        :param arr: initial array, equals to [identity] * n
                    when it is not provided
        :type arr: Optional[list[T]]
        """
        self.n : int = n
        self.merge : Callable[[T, T], T] = merge
        self.identity = identity
        self.tree : list[T] = [self.identity] * (2*n)
        if arr != None:
            for i in range(n):
                self.tree[n+i] = arr[i]
            for i in range(n-1, -1, -1):
                self.tree[i] = self.merge(self.tree[i<<1], self.tree[i<<1|1])
    def mergeValue(self, x : int, v : T) -> None:
        """
        Docstring for mergeValue
        set tree[x] to merge(tree[x], v)
        """
        x += self.n
        self.tree[x] = self.merge(self.tree[x], v)
        while x > 1:
            self.tree[x>>1] = self.merge(self.tree[x], self.tree[x^1])
            x >>= 1
    def setValue(self, x : int, v : T) -> None:
        """
        Docstring for setValue
        set tree[x] to v
        """
        x += self.n 
        self.tree[x] = v 
        while x > 1:
            self.tree[x>>1] = self.merge(self.tree[x], self.tree[x^1])
            x >>= 1
    def query(self, l : int, r : int) -> T:
        """
        Docstring for query
        returns merge(tree[l] .. tree[r])
        """
        l, r = l+self.n, r+self.n+1
        res : T = self.identity
        while l < r:
            if l&1:
                res = self.merge(res, self.tree[l])
                l += 1
            if r&1:
                r -= 1
                res = self.merge(res, self.tree[r])
            l >>= 1 
            r >>= 1 
        return res


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