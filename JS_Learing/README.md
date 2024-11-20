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

5.github上添加ssh
![本地路径](rel/draw/draw1.png "将图片放在自己的资源库文件夹中") <!-- 此路径表示图片和MD文件，处于同一目录 -->
![本地路径](rel/draw/draw2.png "将图片放在自己的资源库文件夹中") <!-- 此路径表示图片和MD文件，处于同一目录 -->

> ### git常用命令

````git 
git init                                //初始化GitHub仓库
git add README.md                       //添加资源文件
git commit -m "first commit"            //对提交的缓存文件进行描述
git branch -M main                      //创建提交的分支
git remote add origin <ssh地址>          //选择仓库提交的地址
git push -u origin main                 //远程仓库与本地仓库同步
git clone <ssh地址>                      //克隆远程仓库
! [rejected] main -> main (fetch first) error: failed to push some refs to 
git fetch                               //来获取远程仓库的最新内容
git pull                                //来合并远程仓库的更改到你的本地分支
````
> Git常用命令包括但不限于以下几种‌：‌12

‌合并提交‌：git merge --squash：将所有合并的提交压缩成一个提交。

‌暂存文件‌：git stash -u：将未跟踪文件和已跟踪文件一起暂存。

‌推送分支‌：git push --all：推送所有分支到远程仓库；git push --tags：推送所有标签到远程仓库。

‌获取远程变更‌：git fetch --prune：获取远程仓库的最新变更并清理无效的远程分支。

‌撤销提交‌：git revert [commit]：撤销指定提交的更改。

‌应用提交‌：git cherry-pick [commit]：将指定提交应用到当前分支。

‌查看提交历史‌：git reflog：查看引用日志，记录HEAD的变更历史。

‌添加子模块‌：git submodule add：添加子模块；git submodule update：更新子模块到最新版本；git submodule sync：更新子模块的URL；git submodule status：显示子模块的状态。
‌Git命令的分类及其功能包括‌：

‌索引（暂存区）‌：索引也称为暂存区，是一个缓冲区，用于准备提交的更改。在执行提交之前，开发者可以将要提交的更改添加到索引中。
‌撤销更改‌：Git提供了多种方式来撤销更改，包括使用git reset命令回滚提交、使用git checkout命令恢复单个文件或文件夹的特定版本，以及使用git revert命令创建一个新的提交来撤销之前的更改。
