# 企业官网项目文档

## 项目概述

本项目是一个基于 **Django + Vue** 技术栈构建的企业官网系统，包含前端展示网站和后端管理后台。

---

## 技术栈

| 分类 | 技术 | 版本 |
|------|------|------|
| 后端框架 | Django | 6.0.6 |
| 前端框架 | Vue | 3.4.21 |
| 前端构建 | Vite | 5.1.6 |
| 路由管理 | Vue Router | 4.3.0 |
| 数据库 | SQLite | - |
| 管理后台 | Django SimpleUI | - |

---

## 项目结构

```
QYGW/
├── .venv/                    # Python虚拟环境
├── frontend/                 # Vue前端项目
│   ├── src/
│   │   ├── views/           # 页面组件
│   │   │   ├── Home.vue     # 首页
│   │   │   ├── About.vue    # 关于我们
│   │   │   ├── Services.vue # 服务项目
│   │   │   └── Contact.vue  # 联系我们
│   │   ├── router/
│   │   │   └── index.js     # 路由配置
│   │   ├── App.vue          # 根组件
│   │   └── main.js          # 入口文件
│   ├── index.html           # HTML模板
│   ├── vite.config.js       # Vite配置
│   ├── package.json         # 依赖配置
│   └── start_vue.js         # Vue启动脚本
├── qygw_website/            # Django后端项目
│   ├── homepage/            # 首页应用
│   ├── qygw_website/        # 项目配置
│   │   ├── settings.py      # 配置文件
│   │   └── urls.py          # URL路由
│   └── manage.py            # Django管理入口
├── start_server.bat         # Django启动脚本
├── start_vue.bat            # Vue启动脚本
└── agent.md                 # 项目文档
```

---

## 快速开始

### 1. 启动Django后端

```bash
# 方法一：双击启动脚本
start_server.bat

# 方法二：手动启动
cd QYGW
.venv\Scripts\activate.bat
python qygw_website\manage.py runserver 127.0.0.1:8000
```

### 2. 启动Vue前端

```bash
# 方法一：双击启动脚本
start_vue.bat

# 方法二：手动启动
cd QYGW\frontend
node start_vue.js
```

---

## 访问地址

| 服务 | 地址 | 说明 |
|------|------|------|
| Vue前端网站 | http://localhost:5174/ | 面向用户的企业官网 |
| Django管理后台 | http://127.0.0.1:8000/admin/ | 管理员后台 |

---

## 管理员账号

| 字段 | 值 |
|------|-----|
| 用户名 | tangyu |
| 密码 | 221210 |
| 邮箱 | ty316319@163.com |
| 昵称 | 是唐哥哥啊 |

---

## 功能模块

### 前端网站
- **首页** - 企业介绍、核心优势展示
- **关于我们** - 企业简介、发展历程、核心团队
- **服务项目** - 企业咨询、技术服务、数据分析、品牌设计等
- **联系我们** - 联系方式、留言表单

### 管理后台
- 用户管理
- 内容管理（待扩展）
- 系统设置

---

## 开发说明

### 开发模式
- **Vue开发**：修改 `frontend/src/` 目录下的文件，Vite会自动热重载
- **Django开发**：修改 `qygw_website/` 目录下的文件

### 构建生产版本

```bash
cd frontend
node "C:\Program Files\nodejs\node_modules\npm\bin\npm-cli.js" run build
```

构建产物会输出到 `qygw_website/static/dist/` 目录。

---

## 配置说明

### Django配置
- **settings.py** - 数据库配置、应用注册、SimpleUI配置
- **urls.py** - URL路由配置

### Vue配置
- **vite.config.js** - 开发服务器、代理配置、构建配置
- **router/index.js** - 前端路由配置

---

## 注意事项

1. 开发环境需要同时启动Django和Vue两个服务
2. Vue开发服务器默认使用5174端口（5173被占用时自动切换）
3. 管理后台使用SimpleUI框架，已配置中文界面
4. 数据库使用SQLite，数据文件位于 `qygw_website/db.sqlite3`
