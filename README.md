# Odoo12系统集成钉钉     12.0-v2

## 注意： 模块中***部分功能***已使用sdk，请使用pip3对`requirements.txt`中的依赖项进行安装

```ssh
pip3 install -r requirements.txt
```

### 这是一个新的分支，用于授权企业的线上使用环境，和master分支是分开的，请勿与master分支混合

### 你可以理解为这是集成钉钉应用的第二个版本，这个分支更加注重稳定、完善权限机制以及企业用户实际使用体验，当然，最主要目的是为了更好的配合非开源模块的融合使用，比如工资核算、人事管理、各类报表等。

### 本分支除现master上所有功能外，会新增odoo接口模块和rpc接口用于小程序（微信、钉钉）的调用

> 注意： 本分支未经同意或授权就部署在公司企业正式环境中导致出现的任何问题后果，作者和贡献者概不负责并且不提供任何支持。

### 如何安装钉钉审批
#### 1. 可通过钉钉设置项中直接选择需要的审批模块，比如出勤休假，勾选后点击保存即可
#### 2. 或直接在应用中搜索`dingding`, 按分类进行查找即可看到钉钉的所有模块，按需安装
#### 安装完成后需要设置相应的用户权限才能在主界面显示

