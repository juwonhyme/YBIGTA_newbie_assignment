from dataclasses import dataclass, field
from typing import TypeVar, Generic, Optional, Iterable


"""
TODO:
- Trie.push 구현하기
- (필요할 경우) Trie에 추가 method 구현하기
"""


T = TypeVar("T")


@dataclass
class TrieNode(Generic[T]):
    body: Optional[T] = None
    children: list[int] = field(default_factory=lambda: [])
    is_end: bool = False


class Trie(list[TrieNode[T]]):
    """
    Trie (implementation by using list)
    """
    def __init__(self) -> None:
        super().__init__()
        self.append(TrieNode(body=None))

    def push(self, seq: Iterable[T]) -> None:
        """
        seq: T의 열 (list[int]일 수도 있고 str일 수도 있고 등등...)

        action: trie에 seq을 저장하기
        """
        # 구현하세요!

        cur : int = 0
        for c in seq:
            child_exist = False 
            for nxt in reversed(self[cur].children):
                if self[nxt].body == c:
                    child_exist = True 
                    cur = nxt 
                    break
            if not child_exist:
                self[cur].children.append(len(self))
                cur = len(self)
                self.append(TrieNode(body=c))
        self[cur].is_end = True

@dataclass 
class OptimizedTrieNode(Generic[T]):
    body : int = 0
    child_count : int = 0
    last_child : int = 0
    is_end : bool = False

class OptimizedTrie(list[OptimizedTrieNode[T]]):
    """
    Optimized Trie (Offline Trie)
    need sort before using push(), only for boj 3080 (to prevent TLE/MLE)
    This code only changes logic, actually it is possible to implement this
        whole class in original TrieNode/Trie structure. but I thought 
        separating two classes would be more clear.
    """
    def __init__(self) -> None:
        super().__init__()
        self.append(OptimizedTrieNode(body = -1))

    def push(self, seq: Iterable[str]) -> None:
        cur : int = 0 
        for c in seq:
            flag : bool = True 
            if self[cur].child_count == 0:
                flag = False 
            elif self[self[cur].last_child].body != ord(c)-ord('A'):
                flag = False 
            if flag:
                cur = self[cur].last_child 
            else:
                self[cur].child_count += 1
                self[cur].last_child = len(self)
                cur = self[cur].last_child
                self.append(OptimizedTrieNode(body = ord(c)-ord('A')))
        self[cur].is_end = True