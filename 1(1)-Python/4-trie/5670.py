from lib import Trie
import sys


"""
TODO:
- 일단 Trie부터 구현하기
- count 구현하기
- main 구현하기
"""


def count(trie: Trie, query_seq: str) -> int:
    """
    trie - 이름 그대로 trie
    query_seq - 단어 ("hello", "goodbye", "structures" 등)

    returns: query_seq의 단어를 입력하기 위해 버튼을 눌러야 하는 횟수
    """
    pointer : int = 0
    cnt : int = 0

    for element in query_seq:
        if len(trie[pointer].children) > 1 or trie[pointer].is_end:
            cnt += 1

        new_index : int = -1

        for nxt in trie[pointer].children:
            if trie[nxt].body == element:
                new_index = nxt 
                break

        pointer = new_index

    return cnt + int(len(trie[0].children) == 1)


def main() -> None:
    # 구현하세요!

    while True:
        try:
            n : int = int(input())
            lis : list[str] = []
            trie : Trie = Trie()
            for _ in range(n):
                lis.append(input())
                trie.push(lis[-1])
            sum : int = 0
            for s in lis:
                sum += count(trie, s)
            print(f'{sum / n :.2f}')
        except EOFError:
            break


if __name__ == "__main__":
    main()