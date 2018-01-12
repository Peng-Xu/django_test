# Django 后台登陆

## 1.  版本需求
```
python    3.5
django    1.11+ 
```


## 2.配置数据库为mysql
```
文件路径 finally/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'ovs1',//数据库名
        'USER':'django',//mysql用户名
        'PASSWORD':'******',//mysql密码
        'HOST':'127.0.0.1',
        'PORT':'3306'
    }
}
