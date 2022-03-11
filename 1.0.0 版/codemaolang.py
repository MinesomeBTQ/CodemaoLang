# Codemao Lang - v1.0.0
# 作者: BT.Q
# 官网: http://tobtq.top
# 文档: http://tobtq.top/codemao
# 反馈: http://tobtq.top/feedback
#
# codemaoLang 是一个为编程猫api打造的高度包装的Python库
# 目前支持功能:
#   1.使用账号与密码登录用户，修改和获取用户信息
#   2.使用ID获取用户信息（包括公开信息、代表作信息、荣誉信息、作品列表、收藏作品列表、关注列表、粉丝列表）
#   3.生成随机昵称
#
# 免责声明：请合理使用codemaoLang，如果因为使用不当对您和编程猫社区造成损失，本开发者不承担任何法律责任
#

import requests
import json

__version__ = '1.0.0'


class UserError(Exception):
    ...


def post(url: str, data=None):
    if data is None:
        data = {}
    try:
        return requests.post('https://api.codemao.cn' + url, data=json.dumps(data),
                             headers={
                                 "Content-Type": "application/json",
                                 "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; ) '
                                               'AppleWebKit/537.36 (KHTML, like Gecko) '
                                               'Chrome/81.0.4044.138 Safari/537.36'
                             }
                             )
    except json.JSONDecodeError:
        return None


def get(url: str, cookies=None):
    if cookies is None:
        cookies = {}
    try:
        return requests.get('https://api.codemao.cn' + url,
                            headers={
                                "Content-Type": "application/json",
                                "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; ) '
                                              'AppleWebKit/537.36 (KHTML, like Gecko) '
                                              'Chrome/81.0.4044.138 Safari/537.36'
                            },
                            cookies=cookies
                            )
    except json.JSONDecodeError:
        return None


def patch(url: str, data=None, cookies=None):
    if cookies is None:
        cookies = {}
    if data is None:
        data = {}
    try:
        return requests.patch('https://api.codemao.cn' + url, data=json.dumps(data),
                              headers={
                                  "Content-Type": "application/json",
                                  "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; ) '
                                                'AppleWebKit/537.36 (KHTML, like Gecko) '
                                                'Chrome/81.0.4044.138 Safari/537.36'
                              },
                              cookies=cookies
                              )
    except json.JSONDecodeError:
        return None


class user:
    def __init__(self, identity: str, password: str):
        self.identity, self.password = identity, password
        self.ifLogon = False
        self.__data = {}
        data = post(
            '/tiger/v3/web/accounts/login',
            data={
                "identity": identity,
                "password": password,
                "pid": "65edCTyg"
            }
        )
        self.__cookies = data.cookies
        data = data.json()
        try:
            if data['error_number'] == 2:
                raise UserError('用户不存在或者密码错误')

        except KeyError:
            ...
        self.__data = data
        auth, user_info = data['auth'], data['user_info']
        self.auth.data = auth
        self.auth.token = auth['token']
        self.auth.phone_number = auth['phone_number']
        self.auth.email = auth['email']
        self.auth.has_password = auth['has_password']
        self.auth.is_weak_password = auth['is_weak_password']
        self.__data = user_info
        self.id = user_info['id']
        self.nickname = user_info['nickname']
        self.avatar_url = user_info['avatar_url']
        self.fullname = user_info['fullname']
        self.birthday = user_info['birthday']
        self.sex = user_info['sex']
        self.qq = user_info['qq']
        self.description = user_info['description']
        data = get('/api/user/info', cookies=self.__cookies).json()['data']['userInfo']
        try:
            if data['code'] == 2002:
                raise UserError('用户未登录')
        except KeyError:
            ...
        self.info.data = data
        self.info.id = data['id']
        self.info.nickname = data['nickname']
        self.info.avatar = data['avatar']
        self.info.email = data['email']
        self.info.gold = data['gold']
        self.info.qq = data['qq']
        self.info.real_name = data['real_name']
        self.info.sex = data['sex']
        self.info.username = data['username']
        self.info.description = data['description']
        self.info.doing = data['doing']
        self.info.level = data['level']
        self.ifLogon = True
        self.__log('登录成功')

    __data: dict = {}
    id: int
    nickname: str
    avatar_url: str
    fullname: str
    birthday: int
    sex: int
    qq: str
    description: str

    class auth:
        data: dict = {}
        token: str
        phone_number: str
        email: str
        has_password: bool
        is_weak_password: bool

    def __log(self, value: str):
        if self.id:
            print(f'{self.id}: {value}')

    def logout(self):
        post('/tiger/v3/web/accounts/logout')
        self.ifLogon = False
        self.__data = {}
        self.__log('退出登录成功')
        self.auth.data = self.auth.token = self.auth.phone_number = self.auth.email = self.auth.has_password = \
            self.auth.is_weak_password = self.__data = self.id = self.nickname = self.avatar_url = \
            self.fullname = self.birthday = self.sex = self.qq = self.description = self.info.data = self.info.id = \
            self.info.nickname = self.info.avatar = \
            self.info.email = self.info.gold = self.info.qq = self.info.real_name = self.info.sex = \
            self.info.description = self.info.level = ...
        self.__cookies = ''

    def __set(self, key: str, value):
        try:
            data = patch('/tiger/v3/web/accounts/info', {key: value}, self.__cookies)
            if data.json()['error_number'] == 0:
                raise UserError('用户未登录')
            elif data.json()['error_number'] == 5:
                raise UserError('输入格式错误')
            else:
                raise UserError('未知错误')
        except json.JSONDecodeError:
            self.reload()
            self.__log(f'设置{key}为{value}成功')

    setNickname = lambda self, nickname: self.__set('nickname', nickname)
    setFullname = lambda self, fullname: self.__set('fullname', fullname)
    setDescription = lambda self, description: self.__set('description', description)
    setSex = lambda self, sex: self.__set('sex', sex)
    setBirthday = lambda self, birthday: self.__set('birthday', birthday)
    setAvatar_url = lambda self, avatar_url: self.__set('avatar_url', avatar_url)

    def setPassword(self, password: str):
        try:
            data = patch('/tiger/v3/web/accounts/password', {
                "old_password": self.password,
                "password": password,
                "confirm_password": password
            }, self.__cookies)
            if data.json()['error_number'] == 0:
                raise UserError('用户未登录')
            elif data.json()['error_number'] == 5:
                raise UserError('输入格式错误')
            else:
                print(data)
                raise UserError('未知错误')
        except json.JSONDecodeError:
            self.__log(f'设置新密码成功')

    def messages(self) -> list[dict[str: str, str: str], dict[str: str, str: str], dict[str: str, str: str]]:
        data = get('/web/message-record/count', cookies=self.__cookies)
        return data.json()

    class info:
        data: dict = {}
        id: str
        nickname: str
        avatar: str
        email: str
        gold: int
        qq: str
        real_name: str
        sex: str
        description: str
        level: int

    def reload(self):
        self.__init__(self.identity, self.password)


class another:
    def __init__(self, user_id):
        self.user_id = user_id
        self.__data = {}
        data = get('/api/user/info/detail/' + str(user_id)).json()
        if data['code'] == 404:
            raise UserError('您访问的资源不存在')
        __user = data['data']['userInfo']['user']
        work = data['data']['userInfo']['work']
        self.__data = data
        self.info.data = __user
        self.info.id = __user['id']
        self.info.nickname = __user['nickname']
        self.info.sex = __user['sex']
        self.info.description = __user['description']
        self.info.doing = __user['doing']
        self.info.preview_work_id = __user['preview_work_id']
        self.info.level = __user['sex']
        self.work.data = work
        self.work.id = work['id']
        self.work.name = work['name']
        self.work.preview = work['preview']
        data = get('/creation-tools/v1/user/center/honor?user_id=' + str(user_id)).json()
        try:
            if data['error_code']:
                raise UserError(data['error_message'])
        except:
            ...
        self.honor.data = data
        self.honor.attention_status = data['attention_status']
        self.honor.block_total = data['block_total']
        self.honor.re_created_total = data['re_created_total']
        self.honor.attention_total = data['attention_total']
        self.honor.fans_total = data['fans_total']
        self.honor.collected_total = data['collected_total']
        self.honor.liked_total = data['liked_total']
        self.honor.view_times = data['view_times']
        self.honor.author_level = data['author_level']
        self.honor.is_official_certification = data['is_official_certification']
        self.honor.subject_id = data['subject_id']
        self.honor.work_shop_name = data['work_shop_name']
        self.honor.work_shop_level = data['work_shop_level']
        self.honor.like_score = data['like_score']
        self.honor.collect_score = data['collect_score']
        self.honor.fork_score = data['fork_score']
        data = get(f'/creation-tools/v1/user/center/work-list?user_id={str(user_id)}&offset=1&limit=200').json()
        self.works.data = data
        for __item in range(len(data['items'])):
            self.works.items += [self.works().getItem(__item)]
        data = get(f'/creation-tools/v1/user/center/collect/list?user_id={str(user_id)}&offset=1&limit=200').json()
        self.collections.data = data
        for __item in range(len(data['items'])):
            self.collections.items += [self.collections().getItem(__item)]
        data = get(f'/creation-tools/v1/user/followers?user_id={str(user_id)}&offset=1&limit=200').json()
        self.followers.data = data
        for __item in range(len(data['items'])):
            self.followers.items += [self.followers().getItem(__item)]
        data = get(f'/creation-tools/v1/user/fans?user_id={str(user_id)}&offset=1&limit=200').json()
        self.fans.data = data
        for __item in range(len(data['items'])):
            self.fans.items += [self.fans().getItem(__item)]
        self.__log('获取信息成功')

    class info:
        data: dict = {}
        id: int
        nickname: str
        avatar: str
        sex: int
        description: str
        doing: str
        preview_work_id: int
        level: int

    class work:
        data: dict = {}
        id: int
        name: str
        preview: str

    class honor:
        data: dict = {}
        attention_status: bool
        block_total: int
        re_created_total: int
        attention_total: int
        fans_total: int
        collected_total: int
        liked_total: int
        view_times: int
        author_level: int
        is_official_certification: int
        subject_id: int
        work_shop_name: str
        work_shop_level: int
        like_score: int
        collect_score: int
        fork_score: int

    class works:
        data: dict = {}
        items: list = []

        def getItem(self, number: int):
            class item:
                def __init__(self, data: dict):
                    self.data = data
                    self.id: int = data['id']
                    self.type: int = data['type']
                    self.work_name: str = data['work_name']
                    self.preview: str = data['preview']
                    self.view_times: int = data['view_times']
                    self.collect_times: int = data['collect_times']
                    self.liked_times: int = data['liked_times']
                    self.parent_id: int = data['parent_id']
                    self.fork_enable: bool = data['fork_enable']
                    self.fork_times: int = data['fork_times']
                    self.publish_time: int = data['publish_time']
                    self.description: str = data['description']

            return item(self.data['items'][number - 1])

    class collections:
        data: dict = {}
        items: list = []

        def getItem(self, number: int):
            class item:
                def __init__(self, data: dict):
                    self.data = data
                    self.id: int = data['id']
                    self.name: str = data['name']
                    self.preview: str = data['preview']
                    self.user_id: int = data['user_id']
                    self.nickname: str = data['nickname']
                    self.avatar_url: str = data['avatar_url']
                    self.views_count: int = data['views_count']
                    self.likes_count: int = data['likes_count']
                    self.collections_count: int = data['collections_count']
                    self.is_deleted: bool = data['is_deleted']
                    self.publish_time: int = data['publish_time']
                    self.work_type: int = data['work_type']
                    self.description: str = data['description']

            return item(self.data['items'][number - 1])

    class followers:
        data: dict = {}
        items: list = []

        def getItem(self, number: int):
            class item:
                def __init__(self, data: dict):
                    self.data = data
                    self.id: int = data['id']
                    self.nickname: str = data['nickname']
                    self.avatar_url: str = data['avatar_url']
                    self.n_works: int = data['n_works']
                    self.total_likes: int = data['total_likes']
                    self.is_followed: bool = data['is_followed']
                    self.description: str = data['description']

            return item(self.data['items'][number - 1])

    class fans:
        data: dict = {}
        items: list = []

        def getItem(self, number: int):
            class item:
                def __init__(self, data: dict):
                    self.data = data
                    self.id: int = data['id']
                    self.nickname: str = data['nickname']
                    self.avatar_url: str = data['avatar_url']
                    self.total_likes: int = data['total_likes']
                    self.is_followed: bool = data['is_followed']
                    self.description: str = data['description']

            return item(self.data['items'][number - 1])

    def __log(self, value: str):
        if self.info.id:
            print(f'{self.info.id}: {value}')

    def reload(self):
        self.__init__(self.user_id)


def random_nickname():
    return get('/api/user/random/nickname').json()['data']['nickname']
