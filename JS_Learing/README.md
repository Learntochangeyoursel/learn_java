## 前端学习——day001
> ### git的安装与GitHub ssh配置
>
1.配置自己的用户名
````git
git config --global user.name "user name"
````
2.配置自己的邮箱
```` git 
git config --global user.email "pengsijiaiao@163.com"
````
3.查看自己是否配置成功
```` git
git config --global --list
````
4.生成ssh
````git 
ssh-keygen -t rsa
````
**生成ssh后，系统提示输入密码等三个选项直接跳过，不然以后每次远程控制都会输入账号密码**
5.