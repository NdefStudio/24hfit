# 后端api地址

根目录在/api

## /crt

CurrentRouTine:get,获取当前routinelist
接收用户id
发送data是包含：

- routinelist：字典数组
  e.g.[{name:'睡眠',icon:'icon1'},{name:'睡眠',icon:'icon2'}]
- selected:字符串，相应某个routine的name值

## /crtp

CurrentRouTinePost:post,接收data包含：

- selected:字符串，同上
- time:字符串，yyyy-mm-dd hh:mf:ss
