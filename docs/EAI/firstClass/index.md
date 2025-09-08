# 第一次内训：环境配置与 python 基础

!!! tip "tips"
	该文档主要讲解 git 版本控制，使用 Conda 进行环境管理以及 python 基础。
	
	学习过程中有任何问题请及时联系我们！！！

## GIT 

GIT 是什么？

- Git 是一个免费的开源分布式版本控制系统，旨在快速高效地处理从小型到大型的所有项目，作者 [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds)。

如何理解分布式版本控制系统（DVCS，Distributed Version Control System）？

- 分布式：去中心化，不需要联网，在本地就可以使用的代码仓库
- 版本控制：记录、管理、回溯文件的修改历史
- 基于内容寻址的存储系统（vs基于文件）

### 安装 GIT

参考[Install GIT](https://www.atlassian.com/zh/git/tutorials/install-git)

###基础命令

#### 创建本地版本库

```bash
git init 		# 使当前文件夹成为 git 仓库，并创建 .git 隐藏文件夹
git inti <folder>		# 创建文件夹并使其成为 git 仓库
```

!!! warning "warning"
	请不要随意更改  `.git`文件夹中的内容！！！

#### 暂存区修改和提交

```bash
git add <filename>			# 提交修改的文件
git add .				    # 提交所有修改

git commit -m "message"		# 编辑提交信息，记录更改内容，便于回溯
```

#### 使用分支(branch)

- 创建与删除分支

  ```bash
  git branch <branchname>			# 基于当前 HEAD 创建
  git branch <branchname> id		# 基于 id 创建
  git branch -d <branchname>		# 删除某一分支
  ```

- 查看分支

  ```bash
  git branch			# -a 查看远程分支  -v 显示当前分支信息
  ```

- 内容比较

  ```bash
  git diff <branch1> <branch2>			# 比较两个不同分支
  git diff <branch>						# 比较工作区与分支
  git diff 								# 比较工作区与暂存区
  ```

- 合并

  ```bash
  git merge <branch1> <branch2> ...			# 将多个分区合并到当前分区
  ```

#### 忽略特殊文件

`.gitinnore`规定了 git 会忽略一些文件，语法如下

- \# 开头的行为注释
- \* 通配多个字符，`**` 通配中间目录（有或无  --eg： *.c 匹配所有 C 文件，a/**/b 匹配 a/b、a/x/b、a/x/y/b 等
- / 开头只匹配根目录，否则匹配所有目录
- ! 取消忽略

### 远程版本库

#### GIT SSH

可以使用如下命令获取 SSH 密钥

```bash
ssh-keygen -t ed25519 -C "your_email@example.com" #推荐，更现代，密钥长度短

ssh-keygen -t rsa -C "your_email@example.com" #兼容性更强
```

生成后会在系统的用户文件夹下新建`.ssh` 文件夹，里面保存了生成的公钥(.pub)与私钥(无后缀)。

!!! warning "warning"
	请不要让任何人知道你的私钥！！！

#### 在托管平台上绑定SSH

在用户设置中的SSH密钥中添加自己的公钥即可。

#### 常用

- 测试连接

  ```bash
  ssh -T git@github.com
  ```

- 添加或者删除远程仓库

  ```bash
  git remote add origin <repo>			# 添加
  git remote remove origin				# 删除
  git remote -v							# 查看
  ```

!!! tip "tips"
  	远程仓库名`origin`可以更换为你喜欢的名字。

- pull 和 push

  ```bash
  git pull <remote>    		#拉取远程版本
  git push <remote> <branch>    #上传远程存储库
  ```

## Conda 环境管理

Conda是一个开源的包管理系统和环境管理系统，核心功能是包管理与环境管理。通过Conda,用户
可以轻松安装和管理多个版本的Python以及相关的软件包。

Miniconda 则是 Conda 的轻量化版本——它只包含最基本的 python 解释器与 Conda 包管理器，以及一些必须的依赖项，后续内容均基于 Miniconda 展开。

### 安装 Miniconda

=== "Windows Command Prompt"
    ```bash
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
    start /wait "" .\miniconda.exe /S
    del .\miniconda.exe
    ```
=== "Windows PowerShell"
    ```bash
    wget "https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe" -outfile ".\miniconda.exe"
    Start-Process -FilePath ".\miniconda.exe" -ArgumentList "/S" -Wait
    del .\miniconda.exe
    ```
=== "MacOS" 
    - arm64
    ```bash
    mkdir -p ~/miniconda3
    curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
    bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
    rm ~/miniconda3/miniconda.sh
    ```
    - x86
      ```bash
      mkdir -p ~/miniconda3
      curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
      bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
      rm ~/miniconda3/miniconda.sh
      ```
    然后刷新并初始化conda
    ```bash
    source ~/miniconda3/bin/activate
    conda init --all
    ```

### 












  ​



















































