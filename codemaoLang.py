# Codemao Lang - v1.1.0
# 作者: BT.Q
# 官网: http://tobtq.top
# 文档: http://tobtq.top/codemao
# 反馈: http://tobtq.top/feedback
# 示例：http://tobtq.top/article?name=Codemao%20Lang%20%E5%AE%9E%E6%88%98%E7%A4%BA%E4%BE%8B
#
# codemaoLang 是一个为编程猫api打造的高度包装的Python库
# 目前支持功能:
#   1.使用账号与密码登录用户，修改和获取用户信息，以及在论坛发帖、回帖、回复等
#   2.使用ID获取用户信息（包括公开信息、代表作信息、荣誉信息、作品列表、收藏作品列表、关注列表、粉丝列表）
#   3.生成随机昵称
#   4.获取论坛所有面板的信息
#   5.使用ID获取指定帖子的信息
#   6.使用ID获取指定工作室的信息
#
# 免责声明：请合理使用codemaoLang，如果因为使用不当对您和编程猫社区造成损失，本开发者不承担任何法律责任
#

from typing import Union

import requests
import json

__version__ = '1.1.0'


class UserError(Exception):
    ...


def _post(url: str, data=None, cookies=None):
    if cookies is None:
        cookies = {}
    if data is None:
        data = {}
    return requests.post('https://api.codemao.cn' + url, data=json.dumps(data),
                         headers={
                             "Content-Type": "application/json",
                             "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; ) '
                                           'AppleWebKit/537.36 (KHTML, like Gecko) '
                                           'Chrome/81.0.4044.138 Safari/537.36'
                         },
                         cookies=cookies
                         )


def _get(url: str, cookies=None):
    if cookies is None:
        cookies = {}
    return requests.get('https://api.codemao.cn' + url,
                        headers={
                            "Content-Type": "application/json",
                            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; ) '
                                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                                          'Chrome/81.0.4044.138 Safari/537.36'
                        },
                        cookies=cookies
                        )


def _patch(url: str, data=None, cookies=None):
    if cookies is None:
        cookies = {}
    if data is None:
        data = {}
    return requests.patch('https://api.codemao.cn' + url, data=json.dumps(data),
                          headers={
                              "Content-Type": "application/json",
                              "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; ) '
                                            'AppleWebKit/537.36 (KHTML, like Gecko) '
                                            'Chrome/81.0.4044.138 Safari/537.36'
                          },
                          cookies=cookies
                          )


def _delete(url: str, data=None, cookies=None):
    if cookies is None:
        cookies = {}
    if data is None:
        data = {}
    return requests.delete('https://api.codemao.cn' + url, data=json.dumps(data),
                           headers={
                               "Content-Type": "application/json",
                               "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; ) '
                                             'AppleWebKit/537.36 (KHTML, like Gecko) '
                                             'Chrome/81.0.4044.138 Safari/537.36'
                           },
                           cookies=cookies
                           )


class board:
    boards: list = []
    for item in _get('/web/forums/boards/simples/all').json()['items']:
        class board:
            def __init__(self, data):
                self.data: dict = data
                self.id: str = data['id']
                self.name: str = data['name']
                self.icon_url: str = data['icon_url']
                self.is_hot: str = data['is_hot']

        boards += [board(item)]

    def getBoardById(self, board_id: Union[str, int]):
        data = _get('/web/forums/boards/' + str(board_id)).json()

        class board_:
            def __init__(self, data_):
                try:
                    if data_['error_name'] == 'Not Found':
                        raise UserError('模块不存在')
                except KeyError:
                    ...
                self.data: dict = data_
                self.id: str = data_['id']
                self.name: str = data_['name']
                self.description: str = data_['description']
                self.icon_url: str = data_['icon_url']
                self.is_hot: bool = data_['is_hot']
                self.n_posts: int = data_['n_posts']
                self.n_discussions: int = data_['n_discussions']

        return board_(data)

    def getBoardByName(self, board_name: str):
        __data = None
        success = False
        for i_ in self.boards:
            if i_.name == board_name:
                __data = _get('/web/forums/boards/' + i_.id).json()
                success = True
        if not success:
            raise UserError('模块不存在')

        class board_:
            def __init__(self, data_):
                self.data: dict = data_
                self.id: str = data_['id']
                self.name: str = data_['name']
                self.description: str = data_['description']
                self.icon_url: str = data_['icon_url']
                self.is_hot: bool = data_['is_hot']
                self.n_posts: int = data_['n_posts']
                self.n_discussions: int = data_['n_discussions']

        return board_(__data)


class user:
    def __init__(self, identity: str, password: str):
        self.identity, self.password = identity, password
        self.ifLogon = False
        self.__data = {}
        data = _post(
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
        data = _get('/api/user/info', cookies=self.__cookies).json()['data']['userInfo']
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
        _post('/tiger/v3/web/accounts/logout')
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
            data = _patch('/tiger/v3/web/accounts/info', {key: value}, self.__cookies)
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
            data = _patch('/tiger/v3/web/accounts/password', {
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

    def messages(self):
        _data = _get('/web/message-record/count', cookies=self.__cookies).json()

        class ret:
            data = {
                "comment_reply": _data[0]['count'],
                "like_fork": _data[1]['count'],
                "system": _data[2]['count']
            }
            comment_reply = _data[0]['count']
            like_fork = _data[1]['count']
            system = _data[2]['count']

        return ret
    
    def reply_work(self,id,content = '作品不错哟'):
        data = _post('/creation-tools/v1/works/{}/comment'.format(id),
                data = {'content':content},
                cookies = self.__cookies).json()
        try:
            xxxx = data['error_code']
            raise UserError('评论作品失败')
        except KeyError:
            self.__log('在作品{}发布评论成功'.format(id))
            return data['id']

    def like_work(self,id):
        data = _post('/nemo/v2/works/{}/like'.format(id),
                cookies = self.__cookies,
                data = {})
        
        self.__log('在作品{}点赞成功'.format(id))
            

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

    def post(self, title: str, content: str, board_name: str, studio_id: str = None):
        if len(title) < 5 or len(title) > 50:
            raise UserError('标题长度必须在5-50字之间')
        if len(content) < 10:
            raise UserError('内容长度必须不小于10字')
        i_ = board().getBoardByName(board_name)
        data = _post(f'/web/forums/boards/{i_.id}/posts',
                     data={
                         "title": title,
                         "content": content,
                         "studio_id": studio_id
                     },
                     cookies=self.__cookies
                     ).json()
        try:
            if data['error_code'] == 'Param-Invalid@Common':
                raise UserError('请求参数验证失败')
        except KeyError:
            self.__log(f'在论坛{i_.name}板块发布帖子成功')
            return data['id']

    def del_post(self, post_id: Union[str, int]):
        data = None
        try:
            data = _delete('/web/forums/posts/' + str(post_id), cookies=self.__cookies).json()
        except json.JSONDecodeError:
            self.__log(f'删除帖子成功')
        try:
            del data['error_code']
            raise UserError(data['error_message'])
        except TypeError:
            ...
        except KeyError:
            raise UserError('出现异常，请重试')

    def reply_post(self, post_id: Union[str, int], content: str):
        data = _post(f'/web/forums/posts/{str(post_id)}/replies',
                     data={"content": content},
                     cookies=self.__cookies).json()
        try:
            del data['error_code']
            raise UserError(data['error_message'])
        except KeyError:
            self.__log('回帖成功')
            return data['id']

    def reply_reply(self, reply_id: Union[str, int], content: str, parent_id: int = 0):
        data = _post(f'/web/forums/replies/{str(reply_id)}/comments',
                     data={"content": content, "parent_id": parent_id},
                     cookies=self.__cookies).json()
        try:
            del data['error_code']
            raise UserError(data['error_message'])
        except KeyError:
            self.__log('回复成功')
            return data['id']
    
    def apply_workshop(self,workshop_id:int,qq = None):
        data = _post('/web/work_shops/users/apply/join',cookies = self.__cookies,
                data = {'id':workshop_id,
                        'qq':qq})
        self.__log('申请成功')
        print(data)
    #暂时不可用
    def contribute_workshop(self,workshop_id:int,work_id:int):
        data = _post('/web/work_shops/works/contribute',cookies = self.__cookies,
                data = {'id':workshop_id,
                        'work_id':work_id})
        self.__log('功能暂时不知可不可用')
        print(data)
    #暂时不可用
    def rmwork_workshop(self,workshop_id:int,work_id:int):
        data = _post('/web/work_shops/works/remove',cookies = self.__cookies,
                data = {'id':workshop_id,
                        'work_id':work_id})
        
        self.__log('功能暂时不知可不可用')
        print(data)
    #暂时不可用
    def approveuser_workshop(self,workshop_id,user_id,status):
        data = _post('/web/work_shops/users/audit',cookies = self.__cookies,
                data = {'id':workshop_id,
                    'status':status,
                    'user_id':user_id})
        self.__log('功能暂时不知可不可用')
        print(data)

    #本功能制作中
    #def get_message(self,_type):
        #data = _get('/web/message-record?query_type={}&limit=20&offset=0'.format(_type),
                    #cookies = self.__cookies).json()
    
    def reload(self):
        self.__init__(self.identity, self.password)


class another:
    def __init__(self, user_id: Union[str, int]):
        self.user_id = user_id
        self.__data = {}
        data = _get('/api/user/info/detail/' + str(user_id)).json()
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
        data = _get('/creation-tools/v1/user/center/honor?user_id=' + str(user_id)).json()
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
        data = _get(f'/creation-tools/v1/user/center/work-list?user_id={str(user_id)}&offset=1&limit=200').json()
        self.works.data = data
        for __item in range(len(data['items'])):
            self.works.items += [self.works().getItem(__item)]
        data = _get(f'/creation-tools/v1/user/center/collect/list?user_id={str(user_id)}&offset=1&limit=200').json()
        self.collections.data = data
        for __item in range(len(data['items'])):
            self.collections.items += [self.collections().getItem(__item)]
        data = _get(f'/creation-tools/v1/user/followers?user_id={str(user_id)}&offset=1&limit=200').json()
        self.followers.data = data
        for __item in range(len(data['items'])):
            self.followers.items += [self.followers().getItem(__item)]
        data = _get(f'/creation-tools/v1/user/fans?user_id={str(user_id)}&offset=1&limit=200').json()
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


class post:
    def __init__(self, post_id: Union[str, int]):
        class __user:
            def __init__(self, data_: dict):
                if data_['id'] == 0:
                    raise UserError('该用户不存在')
                self.data = data_
                self.id: str = data_['id']
                self.nickname: str = data_['nickname']
                self.avatar_url: str = data_['avatar_url']
                self.subject_id: int = data_['subject_id']
                self.work_shop_name: str = data_['work_shop_name']
                self.work_shop_level: str = data_['work_shop_level']
                self.wuhan_medal: bool = data_['wuhan_medal']
                self.has_signed: bool = data_['has_signed']

        data = _get(f'/web/forums/posts/{str(post_id)}/details').json()
        try:
            del data['error_code']
            raise UserError(data['error_message'])
        except KeyError:
            ...
        self.data: dict = data
        self.ask_help_flag: int = data['ask_help_flag']
        self.board_id: str = data['board_id']
        self.board_name: str = data['board_name']
        self.content: str = data['content']
        self.created_at: int = data['created_at']
        self.id: str = data['id']
        self.is_authorized: bool = data['is_authorized']
        self.is_featured: bool = data['is_featured']
        self.is_hotted: bool = data['is_hotted']
        self.is_pinned: bool = data['is_pinned']
        self.n_replies: int = data['n_replies']
        self.n_comments: int = data['n_comments']
        self.n_views: int = data['n_views']
        self.title: str = data['title']
        self.tutorial_flag: int = data['tutorial_flag']
        self.updated_at: int = data['updated_at']
        self.user: __user = __user(data['user'])


class workshop:
    def __init__(self, workshop_id: Union[str, int]):
        data = _get('/web/shops/' + str(workshop_id)).json()
        self.data: dict = data
        self.id: int = data['id']
        self.shop_id: int = data['shop_id']
        self.name: str = data['name']
        self.total_score: int = data['total_score']
        self.preview_url: str = data['preview_url']
        self.recommend_preview_url: str = data['recommend_preview_url']
        self.description: str = data['description']
        self.n_works: int = data['n_works']
        self.n_views: int = data['n_views']
        self.n_likes: int = data['n_likes']
        self.n_likes: int = data['n_likes']
        self.level: int = data['level']
        self.status: str = data['status']
        self.latest_joined_at: int = data['latest_joined_at']
        self.created_at: int = data['created_at']
        self.updated_at: int = data['updated_at']
        
        users = _get('/web/shops/{}/users?offset=1&limit=100'.format(workshop_id)).json()
        #print(users)
        self.user_num = users['total']
        u_info = []
        for i in users['items']:
            d = {}
            d['user_id'] = i['user_id']
            d['user_name'] = i['name']
            d['qq'] = i['qq']
            d['position'] = i['position']
            u_info.append(d)
        self.user_info = u_info
        



def random_nickname():
    return _get('/api/user/random/nickname').json()['data']['nickname']

class work:
    def __init__(self,id):
        data = _get('/tiger/work/tree/{}'.format(id)).json()
        detail = _get('/creation-tools/v1/works/{}'.format(id)).json()
        self.type = detail['type']
        self.operation = detail['operation']
        self.description = detail['description']
        self.parent_id = detail['parent_id']
        self.parent_user_name = detail['parent_user_name']
        self.remake_times = detail['n_tree_nodes']
        self.view_times = detail['view_times']
        self.collect_times = detail['collect_times']
        self.share_times = detail['share_times']
        self.praise_times = detail['praise_times']
        self.fork_enable = detail['fork_enable']
        self.comment_times = detail['comment_times']
        try:
            del data['error_code']
            raise UserError(data['error_message'])
        except KeyError:
            pass
        self.data = data
        self.author_id = data['author']['user_id']
        self.author_name = data['author']['nickname']
        c = []
        for i in data['children']:
            author_ = i['author']['nickname']
            author_id = i['author']['user_id']
            work_id = i['id']
            d = {}
            d['author'] = author_
            d['author_id'] = author_id
            d['work_id'] = work_id
            c.append(d)
        self.children = c
        self.children_num = len(c)
        self.collection_times = data['collection_times']
        self.id = data['id']
        self.is_deleted = data['is_deleted']
        self.is_published = data['is_published']
        self.parent_id = data['parent_id']
        self.praise_times = data['praise_times']
        self.preview = data['preview']
        self.publish_time = data['publish_time']
        self.view_times = data['view_times']
