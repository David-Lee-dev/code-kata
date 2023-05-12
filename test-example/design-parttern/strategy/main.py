class UserDataFilter:
    def expose(self):
        pass

class UserDataService:
    def __init__(self, dataFilter: UserDataFilter):
        self._dataFilter = dataFilter

    @property
    def dataFilter(self) -> UserDataFilter:
        """
        어떤 dataFilter가 주입?될 지 모른다.
        Duck 객체를 생성할 때 주입된 dataFilter에 따라 생성된 UserDataService 객체의 동작이 달리진다.
        """
        return self._dataFilter

    @dataFilter.setter
    def behavior(self, dataFilter):
        self._dataFilter = dataFilter


    def service(self):
        """
        UserDataService 클래스는 해당 메서드가 최종적으로 어떤 동작을 할지에 대해 관여하지 않는다.
        주입된 dataFilter에 따라서 해당 메서드의 동작이 달라진다.
        """
        self._dataFilter.expose()


class MyDataFilter(UserDataFilter):
    def expose(self):
        user_data = {
            "id": "1",
            "nickname": "test",
            "age": "30",
            "email": "test@gmail.com",
            "only_for_me": "secret",
        }
        print(user_data)


class AnotherUserDataFilter(UserDataFilter):
    def expose(self):
        user_data = {
            "id": "1",
            "nickname": "test",
            "email": "test@gmail.com",
        }
        print(user_data)


user_service1 = UserDataService(MyDataFilter())
user_service1.service()

user_service2 = UserDataService(AnotherUserDataFilter())
user_service2.service()
