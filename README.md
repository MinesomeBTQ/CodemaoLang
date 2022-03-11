# Codemao Lang

### 当前版本列表：

[v1.0.0]()

### 更新日志：

```
v1.0.0:
  (1).正式发布
```

## 下载 Codemao Lang

### 1.直接下载文件

[下载 codemaoLang.py](http://tobtq.top/file/codemaoLang.py)

### 2.使用pip下载

`python -m pip install codemaoLang`

## 使用文档 (v1.0.0)

### 目录

- [user 类](#user)
- - 1\. [参数](#user_1)
- - 2\. [变量](#user_2)
- - 3\. [集合](#user_3)
- - - [auth (认证)](#user_auth)
- - - [info (信息)](#user_info)
- - 4\. [方法](#user_4)
- - - [修改用户信息](#user_4_1)
- - - [修改用户密码](#user_4_2)
- - - [退出登录](#user_4_3)
- [another 类](#another)
- - 1\. [参数](#another_1)
- - 2\. [变量](#another_2)
- - 3\. [集合](#another_3)
- - - [info(信息)](#another_info)
- - - [work(代表作)](#another_work)
- - - [honor(荣誉信息)](#another_honor)
- - 4\. [类](#another_4)
- - - [works(作品列表)](#another_works)
- - - [collections(收藏列表)](#another_collections)
- - - [followers(关注列表)](#another_followers)
- - - [fans(粉丝列表)](#another_fans)
- [random_nickname 函数](#random_nickname)

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

| 方法名                | 用法            |
|--------------------|---------------|
| usr.setNickname    | 设置昵称          |
| usr.setFullname    | 设置全名          |
| usr.setDescription | 设置自我描述        |
| usr.setSex         | 设置性别(1为男，0为女) |
| usr.setBirthday    | 设置生日时间戳       |
| usr.setAvatar_url  | 设置用户头像URL     |

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

### 2. another 类

用于通过id获取用户信息（包括公开信息、代表作信息、荣誉信息、作品列表、收藏作品列表、关注列表、粉丝列表）

#### (1) 参数

`id: int` - 账户 id

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
| usr.info.data    | dict | 所有信息组成的字典 |
| usr.info.id      | int  | 作品ID      |
| usr.info.name    | str  | 作品名       |
| usr.info.preview | str  | 作品图片链接    |

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

### 3. random_nickname 函数

用于生成一个随机昵称

示例:

```python
from codemaoLang import *
print(random_nickname()) # 如：浪漫的飞电鼠ZRA5 务实的潘达熊9xKs
```

##### - BT.Q 2022.3.11
