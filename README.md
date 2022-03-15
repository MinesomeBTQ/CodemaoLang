# Codemao Lang

### 当前版本列表：

v1.0.0
v1.1.0

### 更新日志：

```
v1.0.0:
    (1).正式发布
v1.1.0:
    (1).user类新增发帖、回帖、回复等论坛功能
    (2).修改user类messages方法
    (3).新增post、workshop类
```

## 下载 Codemao Lang

### 1.直接下载文件(推荐)

[下载 codemaoLang.py](http://tobtq.top/file/codemaoLang.py)

### 2.使用 [pip](https://pypi.org/project/codemaoLang/) 下载

`python -m pip install codemaoLang`

### 3.使用 [Github](https://github.com/MinesomeBTQ/CodemaoLang) 下载

## 使用文档 (v1.1.0)

### 1. user 类

用于通过账号和密码登录用户并获取和修改信息

#### (1) 参数

`identity: str` - 账户 手机号/用户名/邮箱

`password: str` - 账户 密码

示例：

```python
from codemaoLang import *
usr = user('账号', '密码')
```

#### 注意：以下文档中的 usr 均代表一个已经登录的 user() 实例

#### (2) 变量


| 变量名             | 类型   | 解释          |
|-----------------|------|-------------|
| usr.identity    | str  | 账号          |
| usr.password    | str  | 密码          |
| usr.ifLogon     | bool | 是否登录        |
| usr.id          | int  | ID          |
| usr.nickname    | str  | 昵称          |
| usr.avatar_url  | str  | 头像链接        |
| usr.fullname    | str  | 真实姓名        |
| usr.birthday    | int  | 生日时间戳       |
| usr.sex         | int  | 性别（0为女，1为男） |
| usr.qq          | str  | QQ 号码       |
| usr.description | str  | 自我描述        |

#### (3) 集合

##### auth(认证):


| 变量名                       | 类型   | 解释                 |
|---------------------------|------|--------------------|
| usr.auth.data             | dict | 所有信息组成的字典          |
| usr.auth.token            | str  | token              |
| usr.auth.phone_number     | str  | 手机号(如:123****4567) |
|                           |      |                    |
| usr.auth.has_password     | bool | 是否设置密码             |
| usr.auth.is_weak_password | bool | 是否为弱密码             |

##### info(信息):


| 变量名                  | 类型   | 解释          |
|----------------------|------|-------------|
| usr.info.data        | dict | 所有信息组成的字典   |
| usr.info.id          | int  | ID          |
| usr.info.nickname    | str  | 昵称          |
| usr.info.avatar      | str  | 头像链接        |
| usr.info.email       | bool | 邮箱(空)       |
| usr.info.gold        | str  | 金币数         |
| usr.info.qq          | str  | QQ号码(空)     |
| usr.info.real_name   | str  | 真实姓名        |
| usr.info.sex         | str  | 性别(M为男，F为女) |
| usr.info.description | str  | 自我描述        |
| usr.info.level       | int  | 用户等级        |

#### (4)方法

##### 修改用户信息


| 方法名                            | 用法            |
|--------------------------------|---------------|
| usr.setNickname(value: str)    | 设置昵称          |
| usr.setFullname(value: str)    | 设置全名          |
| usr.setDescription(value: str) | 设置自我描述        |
| usr.setSex(value: int)         | 设置性别(1为男，0为女) |
| usr.setBirthday(value: int)    | 设置生日时间戳       |
| usr.setAvatar_url(value: str)  | 设置用户头像URL     |

##### 修改用户密码

`usr.setPassword(password: str)`

示例：

```python
from codemaoLang import *
usr = user('账号', '当前密码')
usr.setPassword('新密码')
```

##### 退出登录

`usr.logout()`

PS：建议退出后删除此对象

示例：

```python
from codemaoLang import *
usr = user('账号', '密码')
usr.logout()
del usr
```

##### 刷新信息

`usr.reload()` - 用于重新刷新信息，以同步用户在其他地方修改信息

##### 获取消息

`usr.messages()`

返回一个item对象，包含以下值

| 变量名                          | 类型   | 解释        |
|------------------------------|------|-----------|
| usr.messages().data          | dict | 所有信息组成的字典 |
| usr.messages().comment_reply | int  | 评论与回复     |
| usr.messages().like_fork     | int  | 赞与被购买     |
| usr.messages().system        | int  | 系统消息      |

示例：

```python
from codemaoLang import *
usr = user('账号', '密码')
print(usr.messages().data)
# 若无消息，则输出为 {'comment_reply': 0, 'like_fork': 0, 'system': 0}
```

##### 论坛发帖

`usr.post(title: str, content: str, board_name: str, studio_id: str = None)`

###### 参数说明

title: 帖子标题 _（长度必须在5-50字之间）_

content: 帖子内容 _（应为HTML格式，长度必须不小于10字）_

board_name: 要将帖子发布到的板块 _（热门活动，积木编程乐园，工作室&师徒，你问我答，神奇代码岛，图书馆，CoCo，Python乐园，源码精灵，NOC编程猫比赛，灌水池塘，通天塔，训练师小课堂等）_

studio_id(可选): 活动 ID _（当且仅当board_name为热门活动时，此信息有效，帖子会发布在相应活动的讨论区）_

###### 返回值

若发帖成功，则返回帖子id，类型为 str

##### 删除帖子

`usr.del_post(post_id: str | int)`

###### 参数说明

post_id: 要删除的帖子的id _（可以在帖子链接尾部数字获取）_

##### 回帖

`usr.reply_post(post_id: str | int, content: str)`

###### 参数说明

post_id: 要回复的帖子的id _（可以在帖子链接尾部数字获取）_

content: 回帖内容 _（应为HTML格式）_

###### 返回值

若发帖成功，则返回回帖id，类型为 str

##### 回复

`usr.reply_reply(reply_id: str | int, content: str, parent_id: int = 0)`

###### 参数说明

reply_id: 要回复的回帖的id _（可以在帖子链接尾部数字获取）_

content: 回帖内容 _（应为HTML格式）_

parent_id(可选)：回复的其他回复id _（默认为 0，即直接回复回帖，否则应设置为已有回复的id，显示为：“xxx 回复 xxx”）_

示例：

```python
from codemaoLang import *
import time

usr = user('账号', '密码')  # 登录
post_id = usr.post('标题(Title)', '内容(Content)', '灌水池塘')  # 发布帖子
reply_id = usr.reply_post(post_id, '回帖')
usr.reply_reply(reply_id, '回复')
time.sleep(60)  # 等待60秒
usr.del_post(post_id)  # 删除帖子

```

###### 返回值

若发帖成功，则返回回复id，类型为 str

### 2. another 类

用于通过id获取用户信息（包括公开信息、代表作信息、荣誉信息、作品列表、收藏作品列表、关注列表、粉丝列表）

#### (1) 参数

`user_id: str | int` - 账户 id

示例：

```python
from codemaoLang import *
usr = another(6595064) # 作者的编程猫id，可替换为任意有效的编程猫id
```

#### 注意：以下文档中的 usr 均代表一个有效的 another() 实例

#### (2) 变量


| 变量名         | 类型  | 解释   |
|-------------|-----|------|
| usr.user_id | str | 用户ID |

#### (3) 集合

##### info(信息)


| 变量名                      | 类型   | 解释          |
|--------------------------|------|-------------|
| usr.info.data            | dict | 所有信息组成的字典   |
| usr.info.id              | int  | ID          |
| usr.info.nickname        | str  | 昵称          |
| usr.info.avatar          | str  | 头像链接        |
| usr.info.sex             | int  | 性别(1为男，0为女) |
| usr.info.description     | str  | 自我描述        |
| usr.info.doing           | str  | 正在做的事       |
| usr.info.preview_work_id | int  | 代表作id       |
| usr.info.level           | int  | 等级          |

##### work(代表作)


| 变量名              | 类型   | 解释        |
|------------------|------|-----------|
| usr.work.data    | dict | 所有信息组成的字典 |
| usr.work.id      | int  | 作品ID      |
| usr.work.name    | str  | 作品名       |
| usr.work.preview | str  | 作品图片链接    |

##### honor(荣誉信息)


| 变量名                                 | 类型   | 解释               |
|-------------------------------------|------|------------------|
| usr.honor.data                      | dict | 所有信息组成的字典        |
| usr.honor.attention_status          | bool | 是否关注该用户          |
| usr.honor.block_total               | int  | nemo 作品积木总数      |
| usr.honor.re_created_total          | int  | 作品被再创作总数         |
| usr.honor.attention_total           | int  | 该用户关注的人总数        |
| usr.honor.fans_total                | int  | 该用户的粉丝总数         |
| usr.honor.collected_total           | int  | 作品被收藏总数          |
| usr.honor.liked_total               | int  | 作品被点赞总数          |
| usr.honor.view_times                | int  | 作品被浏览总数          |
| usr.honor.author_level              | int  | 该用户等级            |
| usr.honor.is_official_certification | int  | 是否为官方帐户（0为否，1为是） |
| usr.honor.subject_id                | int  | 用户工作室 ID         |
| usr.honor.work_shop_name            | str  | 用户工作室名           |
| usr.honor.work_shop_level           | int  | 用户工作室等级          |
| usr.honor.like_score                | int  | 用户点赞分            |
| usr.honor.collect_score             | int  | 用户收藏分            |
| usr.honor.fork_score                | int  | 用户再创作分           |

#### (4) 类

##### works(作品列表)

-- `data` 所有数据组成的字典

-- `items` 所有作品对象组成的列表, 每一项都为 item 对象

-- `getItem(number: int)` 获取作品列表里的第几项

-- `item`对象:

    -- 包含以下值:


| 变量名           | 类型   | 解释                   |
|---------------|------|----------------------|
| data          | dict | 所有信息组成的字典            |
| id            | int  | 作品ID                 |
| type          | int  | 类型（1为Kitten, 8为Nemo） |
| work_name     | str  | 作品名                  |
| preview       | str  | 封面图片链接               |
| view_times    | int  | 被浏览次数                |
| collect_times | int  | 被收藏次数                |
| liked_times   | int  | 被点赞次数                |
| parent_id     | int  | 原创：0；再创作：原作品 ID      |
| fork_enable   | bool | 是否允许再创作              |
| fork_times    | int  | 被再创作次数               |
| publish_time  | int  | 作品发布时间戳              |
| description   | str  | 作品介绍                 |

##### collections(收藏列表)

-- `data` 所有数据组成的字典

-- `items` 所有收藏作品对象组成的列表, 每一项都为 item 对象

-- `getItem(number: int)` 获取收藏作品列表里的第几项

-- `item`对象:

    -- 包含以下值:


| 变量名               | 类型   | 解释                     |
|-------------------|------|------------------------|
| data              | dict | 所有信息组成的字典              |
| id                | int  | 作品ID                   |
| name              | str  | 作品名                    |
| preview           | str  | 作品封面图片链接               |
| user_id           | int  | 作者ID                   |
| nickname          | str  | 作者昵称                   |
| avatar_url        | str  | 作者头像链接                 |
| views_count       | int  | 作品被浏览次数                |
| collections_count | int  | 作品被收藏次数                |
| likes_count       | int  | 作品被点赞次数                |
| is_deleted        | bool | 是否被删除                  |
| publish_time      | int  | 作品发布时间戳                |
| work_type         | int  | 作品类型（1为Kitten, 8为Nemo) |
| description       | str  | 作品介绍                   |

##### followers(关注列表)

-- `data` 所有数据组成的字典

-- `items` 所有关注对象组成的列表, 每一项都为 item 对象

-- `getItem(number: int)` 获取关注列表里的第几项

-- `item`对象:

    -- 包含以下值:


| 变量名         | 类型   | 解释        |
|-------------|------|-----------|
| data        | dict | 所有信息组成的字典 |
| id          | int  | 用户ID      |
| nickname    | str  | 用户昵称      |
| avatar_url  | str  | 用户头像链接    |
| n_works     | int  | 用户作品总数    |
| total_likes | int  | 用户被点赞总数   |
| is_followed | bool | 是否关注该用户   |
| description | str  | 用户自我描述    |

##### fans(粉丝列表)

-- 与 followers 用法完全一样

#### (5) 方法

##### 刷新信息

`usr.reload()` - 用于重新刷新信息，以同步用户在其他地方修改信息

### 3.board类

用于获取论坛所有面板的信息

#### (1) boards

类型：list

包含所有论坛板块的item对象

item对象包含以下值


| 变量名      | 类型   | 解释        |
|----------|------|-----------|
| data     | dict | 所有信息组成的字典 |
| id       | str  | 板块id      |
| is_hot   | bool | 是否为热门板块   |
| icon_url | str  | 板块图标 URL  |
| name     | str  | 板块名称      |

#### (2) getBoardId(board_id: str | int)

用于通过id获取指定板块信息

###### 参数：

board_id：板块id

###### 返回值：

一个集合，包含以下值

| 变量名           | 类型   | 解释        |
|---------------|------|-----------|
| id            | str  | 板块 ID     |
| name          | str  | 板块名称      |
| description   | str  | 板块描述      |
| icon_url      | str  | 板块图标 URL  |
| is_hot        | bool | 是否为热门板块   |
| n_posts       | int  | 板块中帖子总数   |
| n_discussions | int  | 板块中帖子回复总数 |

#### (3) getBoardName(board_id: str | int)

用于通过板块名获取指定板块信息

###### 参数：

board_id：板块名 _（热门活动，积木编程乐园，工作室&师徒，你问我答，神奇代码岛，图书馆，CoCo，Python乐园，源码精灵，NOC编程猫比赛，灌水池塘，通天塔，训练师小课堂等）_

###### 返回值：

一个集合，包含以下值

| 变量名           | 类型   | 解释        |
|---------------|------|-----------|
| id            | str  | 板块 ID     |
| name          | str  | 板块名称      |
| description   | str  | 板块描述      |
| icon_url      | str  | 板块图标 URL  |
| is_hot        | bool | 是否为热门板块   |
| n_posts       | int  | 板块中帖子总数   |
| n_discussions | int  | 板块中帖子回复总数 |

### 4. post 类

用于通过id获取指定论坛帖子信息

#### (1) 参数

`post_id: str | int` - 帖子 id（可以在帖子链接尾部的数字获得）

#### 注意：以下文档中的 post 均代表一个有效的 post() 实例

#### (2) 变量

| 变量名                | 类型    | 解释           |
|--------------------|-------|--------------|
| post.data          | dict  | 所有信息组成的字典    |
| post.ask_help_flag | int   | 是否为求助帖       |
| post.board_id      | str   | 帖子所在板块 ID    |
| post.board_name    | str   | 帖子所在板块名称     |
| post.content       | str   | 帖子内容         |
| post.created_at    | int   | 发布时间戳        |
| post.id            | str   | 帖子 ID        |
| post.is_authorized | bool  | 是否为官方贴       |
| post.is_featured   | bool  | 是否为精选贴       |
| post.is_hotted     | bool  | 是否为热门贴       |
| post.is_pinned     | bool  | 是否为置顶帖       |
| post.n_comments    | int   | （每个回帖下的）评论数量 |
| post.n_replies     | int   | 回帖数量         |
| post.n_views       | int   | 浏览次数         |
| post.title         | str   | 帖子标题         |
| post.tutorial_flag | int   | 是否为教程帖       |
| post.updated_at    | int   | 更新时间戳        |
| post.user          | class | _见下文_        |

#### (3) 内置 user 类

内涵帖子发布者消息，包含以下值

| 变量名                  | 类型   | 解释        |
|----------------------|------|-----------|
| post.data            | dict | 所有信息组成的字典 |
| post.id              | str  | 用户 ID     |
| post.nickname        | str  | 用户昵称      |
| post.avatar_url      | str  | 用户头像 URL  |
| post.subject_id      | int  | 用户工作室 ID  |
| post.work_shop_name  | str  | 用户工作室名    |
| post.work_shop_level | str  | 用户工作室等级   |
| post.wuhan_medal     | bool | 是否有武汉勋章   |
| post.has_signed      | bool | 是否签订友好协议  |

### 5. workshop 类

用于通过id获取指定工作室信息

#### (1) 参数

`workshop_id: str | int` - 工作室 id（可以在工作室链接尾部的数字获得）

```python
from codemaoLang import *
ws = workshop(813) # LXYZ工作室的id，可替换为任意有效的工作室id
```

#### 注意：以下文档中的 ws 均代表一个有效的 workshop() 实例

#### (2) 变量

| 变量名                 | 类型   | 解释             |
|---------------------|------|----------------|
| ws.data             | dict | 所有信息组成的字典      |
| ws.id               | int  | 工作室id          |
| ws.shop_id          | int  | 工作室识别码         |
| ws.name             | str  | 工作室名称          |
| ws.total_score      | int  | 工作室总分          |
| ws.preview_url      | str  | 工作室图片 URL      |
| ws.description      | str  | 工作室介绍          |
| ws.n_works          | int  | 工作室作品数量        |
| ws.n_views          | int  | 工作室被浏览次数       |
| ws.level            | int  | 工作室等级          |
| ws.status           | int  | 工作室状态          |
| ws.latest_joined_at | int  | 最后有人加入的时间戳     |
| ws.created_at       | int  | 工作室创建时间戳       |
| ws.updated_at       | int  | 工作室主页最后被访问的时间戳 |

### 6. random_nickname 函数

用于生成一个随机昵称

示例:

```python
from codemaoLang import *
print(random_nickname()) # 如：浪漫的飞电鼠ZRA5 务实的潘达熊9xKs
```

##### - BT.Q 2022.3.15
