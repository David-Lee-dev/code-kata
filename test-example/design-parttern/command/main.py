from abc import ABC, abstractmethod

database = {}


class Order:
    def __init__(self, user, product):
        self.user = user
        self.product = product


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass


class OrderCommand(Command):
    def __init__(self, order):
        self._order = order

    def execute(self):
        user = self._order.user
        database[user] = {
            'product': self._order.product,
            'status': '결제 대기 중'
        }

        print(f'{user}가 {database[user]["product"]}를 주문')


class PaymentCommand(Command):
    def __init__(self, order):
        self._order = order

    def execute(self):
        user = self._order.user
        data = database.get(user)

        if not data:
            print(f'{user}는 주문 내역이 없습니다.')
            return

        if data['status'] == '결제 완료':
            print(f'{user}는 이미 결제가 완료되었습니다.')
            return

        data['status'] = '결제 완료'
        print(f'{user}가 {data["product"]}를 결제')


class RefundCommand(Command):
    def __init__(self, order):
        self._order = order

    def execute(self):
        user = self._order.user
        data = database.get(user)

        if not data:
            print(f'{user}는 주문 내역이 없습니다.')
            return

        if data['status'] == '결제 대기 중':
            print(f'{user}는 아직 결제가 완료되지 않았습니다.')
            return

        data['status'] = '환불 완료'
        print(f'{user}가 {data["product"]}를 환불')


class OrderService:
    def __init__(self):
        self._commands = {}

    def set_command(self, key, command):
        self._commands[key] = command

    def serve(self, key):
        command = self._commands.get(key)
        if command is None:
            print(f'{key}는 유효하지 않은 명령어입니다.')
            return

        command.execute()


if __name__ == '__main__':
    order = Order('이주현', '애플 워치 8')

    service = OrderService()
    service.set_command('order', OrderCommand(order))
    service.set_command('payment', PaymentCommand(order))
    service.set_command('refund', RefundCommand(order))

    service.serve('order')
    service.serve('payment')
    service.serve('refund')

    print(database)
