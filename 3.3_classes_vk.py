from pprint import pprint
import requests
TOKEN = ''

user_id_1 = 9223488
user_id_2 = 124770632

# для отладки ошибок - строка #28

params = {
    'access_token': TOKEN,
    'v': 5.89,
}


class User:
    def __init__(self, user_id, token) -> None:
        self.token = token
        self.user_id = user_id

    def __and__(self, other_user) -> dict:
        params['source_uid'] = int(repr(self))
        params['target_uid'] = int(repr(other_user))
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params
        )
        # return response.json()
        return response.json()['response']

    def __repr__(self):
        self.user_id = str(self.user_id)
        return self.user_id

    def __str__(self) -> str:
        self.user_id = str(self.user_id)
        return f"https://vk.com/id{self.user_id}"


user1 = User(user_id_1, TOKEN)
user2 = User(user_id_2, TOKEN)

print(user1)

result = user1 & user2

print(f'Общие друзья у id{user_id_1} и id{user_id_2}:')
pprint(result)


# Вывод print(user) должен выводить ссылку на пользователя в VK
# Класс один, для каждого пользователя свой экземпляр
# __and__ (self, other_user):
# other_user - это другой экземпляр класса user
# далее идет логика получения общего списка друзей
# return mutual_user_lust

# from urllib.parse import urlencode

# OAUTH_URL = 'https://oauth.vk.com/authorize'
# OAUTH_PARAMS = {
#     'client_id': 7495257,  # id приложения
#     'display': 'page',  # page — форма авторизации в отдельном окне;
#     'scope': 'friends',  # права которые запрашиваем у юзера
#     'response_type': 'token',
#     'v': 5.89
# }
# print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))
