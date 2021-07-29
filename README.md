# GIT Learning from Liaoxuefeng

## 1. Some operation about Git BASH

- 基本命令操作

  - 返回上一级：`cd ..`(`cd`与 `..` 之间有一空格)
  - 进入某一目录：`cd git` (进入 git 目录)
  - 显示当前路径：`pwd`
  - 创建文件：`mkdir `+ 文件名

- Git的运行逻辑（仓库创建和远程拉取）

  - 创建仓库（`git init`）这样就在将当前文件夹变为一个git管理的仓库（最好是空文件夹，创建完后可发现一个.git的文件）

    - 如果你没有看到`.git`目录，那是因为这个目录默认是隐藏的，用`ls -ah`命令就可以看见

    - 这是本地创建一个库，也可以选择从服务器pull库到本地进行一些操作

  - 提交本地代码

    - `git add.` 添加所有当前目录的所有文件
      - `git add `+文件名（含后缀）添加指定的文件
    - `git commit -m "Explantion about this commit"`和服务器的代码合并，后面的内容是注释
      - 执行成功后会告诉你一些基本信息如
        - How many files are changed
        - How many insertions are done
        - How many deletions are done
        - So on……

  - 拉取远程仓库

    - `git clone`+目标库的网址（如https://github.com/Xwindwhile/Learning_GITHUB.git，其结构是github的域名后面接用户名再是目标仓库的名称）
      - 完了之后就会有一个对应仓库名的文件夹在你的User文件下（默认是这个），之后就可以对这个仓库进行一些操作啦（操作步骤同上面的步骤一致`git add` ->`git commit -m "xxx"`）

- 状态查看

  - `git status` **随时掌握工作区的状态**命令可以让我们时刻掌握仓库当前的状态，命令输出会告诉我们哪些文件被修改了，但是未被提交commit
  - `git diff` **查看文件修改前后差异**查看更改前后两个文件的差别，做了哪些修改（如果内容多，用鼠标向下滑动查看或方向键↓，当然可直接按 `q`、`Q`、`ZZ` 直接退出该查看模式）
  - `git log` **查看文件更改的所有历史记录**（最近到最远）
    - 如果嫌输出信息太多，看得眼花缭乱的，可以试试加上`--pretty=oneline`参数。这可以看到自己的版本号command id
  - `git reset --har`

