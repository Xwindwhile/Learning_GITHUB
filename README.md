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
      - 如果在输入命令是没有加上`-m"xxx"`往往会出现提示信息，此时有以下几种做法
        - 按`i`出现insert，然后输入你要的信息
        - 再按左上角的`Esc`退出插入模式
        - 输入`:wq`再回车即可成功commit（当然如果你commit错了也可以直接输入这个然后退出，信息不会被提交）

  - 拉取远程仓库

    - `git clone`+目标库的网址（如https://github.com/Xwindwhile/Learning_GITHUB.git，其结构是github的域名后面接用户名再是目标仓库的名称），也可以是（git@github.com:Xwindwhile/Learning_GITHUB.git，而后者速度更快）
    - `git remote add origin`+目标库网址
    - 完了之后就会有一个对应仓库名的文件夹在你的User文件下（默认是这个），之后就可以对这个仓库进行一些操作啦（操作步骤同上面的步骤一致`git add` ->`git commit -m "xxx"`）

- 状态查看

  - `git status` **随时掌握工作区的状态**命令可以让我们时刻掌握仓库当前的状态，命令输出会告诉我们哪些文件被修改了，但是未被提交commit
  - `git diff` **查看文件修改前后差异**查看更改前后两个文件的差别，做了哪些修改（如果内容多，用鼠标向下滑动查看或方向键↓，当然可直接按 `q`、`Q`、`ZZ` 直接退出该查看模式）
  - `git log` **查看文件更改的所有历史记录**（最近到最远）
    - 如果嫌输出信息太多，看得眼花缭乱的，可以试试加上`--pretty=oneline`参数。这可以看到自己的版本号command id
  - `git reset --hard HEAD^` **版本回退**
    - `HEAD ^`指的是回退到前一个版本，`HEAD~10`指的是回退到前十个版本
    - ==**注意的是，文件必须要git add才能被git管理，如果你的某个文件没有被add的话，此时你执行回退git reset --hard的话，文件内容就会被删掉**==
    - 在回退之前可以`git log pretty=oneline`，这样就可以看到自己的每个文件版本对应的版本号，此时执行`git reset --hard`+版本号（可以只是前面部分数字）
    - 如果找不到版本号，用`git reflog`来查看自己的每一次命令，根据每次commit等关键次来找到版本号
  - 工作区与版本去概念理解
    - `git add`命令负责将要提交的文件存入暂存区
    - `git commit`命令则是将所有在暂存区的文件提交到分支（仓库的一个分支）
    - 需要明白的是，git跟踪的不是文件，而是修改。这个修改得经过暂存区（也就是修改需要被`git add`命令所执行），最终`git commit`得到的才会有所有的内容。过程可以描述如下
      - 第一次修改 -> `git add` -> 第二次修改 -> `git commit`，**仅第一次修改被提交**
      - 第一次修改 -> `git add` -> 第二次修改 -> `git add` -> `git commit`，**所有的修改均被提交**
  - 撤销修改
    - 未执行`git add`时
      - `git checkout -- `+文件名（注意**--**不能漏掉），丢弃工作区的修改（注意此时的丢弃修改的内容无法找回）。其起到的作用是一键还原
    - 未执行`git commit`时
      - `git reset HEAD` + 文件名，即`git reset`即可以回退版本，又可以把暂存区的修改回退到工作区。用`HEAD`来表示最新的版本（没有加`^`）
    - 已执行`git commit`，但未提交到远端时
      - 直接用版本回退`git reset --hard HEAD^`
      - 只不过此时小错误（一段话）会让你之前大部分内容丢失（但可以复制粘贴过去补充到回退的内容上）
  - 删除
    - 直接在命令行中执行`rm`+文件名（或者手动删除），这样文件就在**工作区**被删除了。如果是真的要删，看1，如果删错了，看2
      - 1 执行`git rm`并且`git commit`，这样文件在版本库中也会被删除
      - 2 删除了的话，直接`git checkout --`+文件名
  
- 远程仓库

  - 先要有一个ssh key才能把你的内容推送到位于GITHUB的仓库中

    - ```
      $ ssh-keygen -t rsa -C "youremail@example.com"
      ```

    - 登陆GitHub，打开“Account settings”，“SSH Keys”页面，把`.ssh`文件夹中public的密匙cv进去

  - 传递内容

    - `git push origin main` 这个`main`是默认的branch，如果你想传到其他branch上，那就换成对应的branch名成即可
    
  - 信息查看

    - `git remote`或是`git remote -v`查看当前远程仓库的信息（后者显示了可以抓取和推送的`origin`的地址）
    - 

- 分支管理

  - `git checkout -b` +名称，表示创建一个新分支并切换到该分支上
    - `git checkout` + 名称，是指转到该分支
    - `git branch` 可以用来查看所有的分支以及当前所在的分支
    - 当转到新的分支之后，所有的操作都会存到当前这个新分支中，之前工作所在的分支则保持不变（从时序的角度来看，相当于原分支位置一直处于原地，而新分支随着修改的进程不断变化，如下图所示）。
      - ![不同分支的进程不一致](C:\Users\Xwindwaaaani\Desktop\py量化\Typora文件集\不同分支的进程不一致.png)
      - **同时**，值得注意的是，对于所有分支而言， 工作区和暂存区是公共的。也就是说如果你在新分支上做操作，在主分支main上仍是可以看到状态改变的`git status`。但如果你在新分支上add然后commit之后，再切换到主分支上查看内容，看不到你所在新分支所做的内容更改。
    - `git merge` + 分支名称，将新分支的内容整合到当前所在分支中。可以利用`git checkout`转到main中，然后再用`git merge + dev`，就把上图中的dev分支合并到main（即master）中。
    - `git branch -d`+分支名，删除掉该分支（当然如果你还位于该分支上，是会报错的）
  - `git switch`新的命令用于切换分支（防止与`git checkout --`+文件名，这类撤销操作混淆）
    - `git switch -c dev`，创建一个名为dev的分支并转到
    - `git swithc main`，转到main分支
  - 当你在新分支commit完后，回到main上，又对文件进行了相应操作。如果你此时执行`git merge new_branch`  将new_branch和main合并，就会出现合并冲突。这部分会同时些如文件中，但是会有`<<<<<<<`，`=======`，`>>>>>>>`标记出不同分支的内容。
    - 此时需要解决冲突，手动将其重复的内容合并
    - 随后add再commit
    - 可以利用`git log --graph`看到分支的合并情况
  - 默认情况下，git使用的是fast forward方式合并。如果要强制禁用`Fast forward`模式，Git就会在merge时生成一个新的commit，这样，从分支历史上就可以看出分支信息
    - `git merge --no-ff -m"xxx"`+分支名称
    - 这样就可以得到一个新的内容提交
  - 同时，如果你更改了某一个分支的文件但没有commit，系统就不会允许你执行`git switch`操作（就是换分支），此时解决方法如下：
    - `git stash`把当前工作现场“储藏”起来
    - `git stash list` 查看存储的工作区
    - 当从其他分支转回到该分支时，需要执行`git stash apply`或`git stash pop`来恢复（前者恢复后并不删除stash中的内容，需要手动`git stash drop`来删除，而后者会删除
    - 在main分支上修复的bug，想要合并到当前dev分支，可以用`git cherry-pick <commit>`命令（其中`commit`指的是版本号），把bug提交的修改“复制”到当前分支，避免重复劳动。
  - `git branch -D`+名称，来删除一个没有被合并过的分支（信息会直接被删除掉）
  - 

