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