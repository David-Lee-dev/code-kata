from abc import abstractmethod, ABC
from typing import List


class Subject(ABC):
    @abstractmethod
    def subscribe(self, observer):
        pass

    @abstractmethod
    def unsubscribe(self, observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class Netflix(Subject):
    _price: int = 10000
    _subscribers: List[Observer] = []

    @property
    def price(self):
        return self._price

    @property
    def subscribers(self):
        return self._subscribers

    def subscribe(self, observer):
        self._subscribers.append(observer)
        print(f"{observer} 구독 시작")

    def unsubscribe(self, observer):
        self._subscribers.remove(observer)
        print(f"{observer} 구독 해지")

    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update(self)

    def increase(self):
        self._price += 10000
        self.notify()

    def decrease(self):
        print("가격 내렸어 돌아와줘 ㅠㅠ 10명이서 봐도 봐줄게")
        self._price -= 10000
        self.notify()


class UserA(Observer):
    def update(self, subject: Netflix):
        if subject.price > 50000:
            print(f"UserA: {subject.price} 너무 비싸!")
            subject.unsubscribe(self)
        else:
            print(f"UserA: {subject.price} 정도는 뭐...")
            if self not in subject.subscribers:
                subject.subscribe(self)


class UserB(Observer):
    def update(self, subject: Netflix):
        if subject.price > 20000:
            print(f"UserB: {subject.price} 너무 비싸!")
            subject.unsubscribe(self)
        else:
            print(f"UserB: {subject.price} 정도는 뭐...")
            if self not in subject.subscribers:
                subject.subscribe(self)


netflix = Netflix()
userA = UserA()
userB = UserB()

netflix.subscribe(userA)
netflix.subscribe(userB)

netflix.increase()
netflix.increase()
netflix.increase()
netflix.increase()
netflix.increase()

"""
subscribe 는 Subject가 아닌 Observer가 수행할 수 있다.
unsubscribe를 하는 순간 더 이상 Observer가 아니기 때문에 update를 수행하지 않는다.
고로 다시 subscribe를 하는 로직이 있더라도 Subject의 상태를 알 수 없어서 update를 수행하지 않는다.
"""
netflix.decrease()
netflix.decrease()
netflix.decrease()
netflix.decrease()
