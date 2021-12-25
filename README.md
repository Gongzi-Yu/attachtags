# AttachTags

attachtags是一个用来记录和归类你Windows里文件的工具。用来帮你把一些难以记住文件名的文件进行整理、归类。

## 介绍

我们是否都曾有过这样的想法：搞清楚自己的电脑里到底都有些什么文件。但各种各样的文件格式、乱七八糟的文件名总是让我们头疼。在通过种种方式搞清楚了这些文件是干什么的之后，过了个几天，就又忘了。

或者这样一种情况：我们在删除一个软件时，总会剩下那么一些不知所谓的文件留在电脑里。想要对电脑做一次清洗，删除掉无用的文件，又不知道哪些是重要的文件，哪些可以删除。

attachtags就是为了解决这个问题而做出的命令行脚本工具。通过给文件或文件夹添加一个好记的标签，来达到记录、归类文件的目的。

## attachtags命令

```
usage: attachtags [-h] [-v] [-l]
                  {create,delete,rename,show,search,attach,remove} ...

positional arguments:
  {create,delete,rename,show,search,attach,remove}
    create              create one new tag
    delete              delete one tag
    rename              rename some tags with a new name
    show                show tags from some path
    search              search paths with this tags in this path
    attach              attach a tag to some paths
    remove              remove a tag from some paths

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -l, --list            list all tags
```

## 安装

首先、你的电脑里必须要有python（版本>=3.7）！

### 使用`pip`

```
pip install attachtags
```

## 用法

### `-h`、`-v`、`-l`

`-h`用来显示帮助文档，你可以对所有`{create,delete,rename,show,search,attach,remove}`使用`-h`，来显示对应的帮助文档；

`-v`用来显示脚本当前的脚本，`-l`用来显示目前已经存在的tag

### `create`、`delete`、`rename`

`create`用来创建一个或多个新的tag；

`delete`用来删除一个或多个tag；

`rename`用来将一个或者多个tag重新命名

### `attach`、`remove`

`attach`用来给一个文件或文件夹附上一个tag，使用`--all-in-dirs`可以给一个文件夹里的所有文件和文件夹附上一个tag。

`remove`用来从一个文件或文件夹移除一个tag，使用`--all-in-dirs`可以给一个文件夹里的所有文件和文件夹全部移除一个tag。

### `show`、`search`

`show`可以展示一个文件或文件夹所附的tag，使用`-s`可以展示多个。

`search`可以查找一个文件夹里的文件或文件夹有没有属于你所输入的tag的，并输出满足的文件。

## 如何更新

```
pip install --upgrade attachtags
```

## 你有话说

如果你有对这个脚本的疑问、发现了这个脚本的不足、或者希望这个脚本加上一些功能，你可以使用[GitHub bug tracker](https://github.com/Gongzi-Yu/attachtags/issues)提出你的想法。

## 作者

[Gongzi-Yu (Gongzi-Yu) (github.com)](https://github.com/Gongzi-Yu)
