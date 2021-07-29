# GIT Learning from liaoxuefeng

## 1. Some operation about Git BASH

- 基本命令操作

  - 返回上一级：`cd ..`(`cd`与 `..` 之间有一空格)
  - 进入某一目录：`cd git` (进入 git 目录)
  - 显示当前路径：`pwd`
  - 创建文件：`mkdir `+ 文件名

- Git的运行逻辑

  - 创建仓库（`git init`）这样就在将当前文件夹变为一个git管理的仓库（最好是空文件夹，创建完后可发现一个.git的文件）

    - 如果你没有看到`.git`目录，那是因为这个目录默认是隐藏的，用`ls -ah`命令就可以看见

    - 这是本地创建一个库，也可以选择从服务器pull库到本地进行一些操作

  - 提交本地代码

    - 