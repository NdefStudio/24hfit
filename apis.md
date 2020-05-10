# 后端api地址 

> 全都没有写数据库相关代码，留出空位了

根目录在
**/api**

## /crt

CurrentRouTime:get,获取当前routinelist  
接收用户id，发送data包含：

- routinelist：字典数组  
  e.g.[{name:'睡眠',icon:'icon1'},{name:'睡眠',icon:'icon2'}]
- selected:字符串，相应某个routine的name值

## /crtp

CurrentRouTinePost:
**post**

接收data包含：

- id
- selected:字符串，同上
- time:字符串，yyyy-mm-dd hh:mf:ss

## /psts

PoSTs:
**get**

接收用户id，发送内容包含

- allposts:字典数组  
  e.g.[{~~title: '第一条'~~,
        content: 'zsbdzsbd',
        time: 'yyyy-mm-dd hh:mf:ss'},{...}]

~~有无帖子id等到写数据库再定~~

## /npst *暂时没有写前端请求*

New PoST:
**post**

接收内容包含：

- id:字符串
- post:字典，格式见allpost中的一项

## /usr

USeR:
**get**

接收id，发送内容包含：

- username 用户名
- quote 个性签名
- usetime 使用总时间（暂定） 单位为h
- gender 性别（male/female）
- height 身高 单位cm
- weight 体重 单位kg
- age 年龄
- healthstatus 健康状态 暂定优良差

均为字符串，不带单位
