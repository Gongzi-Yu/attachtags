# AttachTags

attachtags是一个用来管理和归类你Windows里文件的工具。用来帮你把一些无法移动或移动很麻烦的文件进行整理、归类。

- [TOC]

## 介绍

我们可能经常遇到这样的情况：我们电脑中的一些软件在保存我们的文件时经常将其保存在层层路径之下。每当我们想查找它们时总是要费九牛二虎之力才能找到它们。在安装软件和系统更新时，电脑里也经常会生成一些不知所谓的文件夹。最开始我们可能还知道这些文件夹来自哪里、用处是什么，但时间一长，我们难免就忘记了这些文件夹到底出自何处了。于是我们陷入了想删但又不敢删的境地。attachtags则是为了解决这个问题而做出的命令行脚本工具。通过给文件或文件夹添加标签，来达到归类文件的目的。

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

`attach`用来给一个文件或文件夹附上一个tag，使用`--all-in-dirs`可以给一个文件夹里的所有文件和文件夹附上一个tag;

`remove`用来从一个文件或文件夹移除一个tag，使用`--all-in-dirs`可以给一个文件夹里的所有文件和文件夹全部移除一个tag;

### `show`、`search`

`show`可以展示一个文件或文件夹所附的tag，使用`-s`可以展示多个；

`search`可以查找一个文件夹里的文件或文件夹有没有属于你所输入的tag的，并输出满足的文件；

## 如何更新

```
pip install --upgrade attachtags
```

## 你有话说

如果你有对这个脚本的疑问、发现了这个脚本的不足、或者希望这个脚本加上一些功能，你可以使用[GitHub bug tracker](https://github.com/Gongzi-Yu/attachtags/issues)提出你的想法。

## 作者

[Gongzi-Yu (Gongzi-Yu) (github.com)](https://github.com/Gongzi-Yu)