import collections
from collections import Iterable, Iterator

# collections.namedtuple会产生一个继承自tuple的子类，与tuple不同的是，它可以通过名称访问元素
# 以下创建了一个名为"Card"的类，该类有两个属性"rank"和"suit"
Card = collections.namedtuple('Card', ['rank', 'suit'])


class PokerCard:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


poker = PokerCard()
print(poker)
print(len(poker))  # 调用__len__方法
print(poker[0])  # 调用__getitem__方法

# 仅仅是实现了__getitem__方法, pockercard 就可以使用for遍历,但不属于可迭代对象或者迭代器
print(isinstance(poker, Iterator))
print(isinstance(poker, Iterable))
for card in poker[:5]:
    print(card)


