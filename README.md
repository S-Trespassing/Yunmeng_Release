# notice-json-editor

一个面向 `notice.json` 的可视化编辑器，适合维护云梦这类
应用的公告数据。

它是纯前端静态工具，不需要构建，不依赖后端。打开
`index.html` 就能导入、编辑、预览并导出通知 JSON。

## 功能特点

- 可视化编辑通知列表，避免手改 JSON 时漏逗号、写错字段
- 支持新增、删除、复制、上移、下移单条通知
- 支持按时间倒序排序，置顶通知优先
- 支持自动补全缺失 ID
- 支持直接复制 JSON 或下载 `notice.json`
- 支持读取同目录 `notice.json`，并保存回同目录文件
- 支持内容预览，能识别图片链接、Markdown 图片、`<img src>`
- 自动缓存当前编辑内容，刷新页面后不容易丢数据

## 适用场景

- 维护应用内公告、通知、活动信息
- 需要频繁调整 `notice.json`，但不想手写 JSON
- 希望让非技术同学也能安全修改通知内容

## 支持的数据格式

支持以下两种输入结构：

```json
{
  "version": 1,
  "notices": [
    {
      "id": "2026-02-26-001",
      "title": "示例标题",
      "content": "示例内容",
      "url": "https://example.com",
      "source": "云梦通知",
      "pinned": true,
      "published_at": "2026-02-26T13:43:00.344Z"
    }
  ]
}
```

或直接传入通知数组：

```json
[
  {
    "id": "2026-02-26-001",
    "title": "示例标题",
    "content": "示例内容"
  }
]
```

## 字段兼容规则

- 链接字段兼容 `url` 和 `link`，导出时统一写成 `url`
- 时间字段兼容 `published_at`、`date`、`time`
- 置顶字段兼容 `pinned`、`is_pinned`、`isPinned`、`top`、
  `sticky`、`pin`
- `source` 不在编辑卡片中单独展示，导出时会保留原值；缺失时
  默认写入 `云梦通知`

## 快速开始

1. 克隆或下载本仓库
2. 使用现代浏览器打开 `index.html`
3. 导入现有 `notice.json`，或点击“读取同目录 notice.json”
4. 编辑通知内容
5. 通过“复制 JSON”“下载 notice.json”或“保存到 notice.json”
   导出结果

## 使用建议

- 推荐使用最新版 Chrome 或 Edge，目录读写体验更完整
- 第一次点击“保存到 notice.json”时，浏览器会请求目录授权
- 如果直接从本地文件打开后遇到权限限制，建议用本地静态服务器
  访问，例如：

```bash
python -m http.server 8080
```

然后访问：

```text
http://localhost:8080/
```

## 编辑器能力说明

- `title` 为空时，App 侧通常会跳过该条通知
- `published_at` 推荐使用 ISO 8601，例如
  `2026-02-15T14:30:00Z`
- `pinned` 为布尔值，置顶通知会优先显示
- `content` 支持正文文本、图片链接、Markdown 图片和 HTML
  图片标签
- 页面右侧会实时生成导出 JSON，方便边改边确认结果

## 仓库文件说明

- `index.html`：主编辑器页面
- `notice.json`：示例通知数据
- `auth.py`：独立的配置加密小脚本，会将结果写入 `config.txt`
- `config.txt`：加密结果输出文件

## 技术实现

- 原生 HTML、CSS、JavaScript
- 使用 `localStorage` 保存当前编辑状态
- 使用 `IndexedDB` 记住目录授权句柄
- 使用 File System Access API 读写同目录 `notice.json`

## 后续可继续完善

如果你打算把仓库长期放在 GitHub 展示，后面还可以继续补：

- 1 张编辑器整体截图
- 1 张单条通知编辑卡片截图
- 1 个“导入前 / 导出后”的示例说明

这样首页展示会更完整，也更方便别人一眼看懂这个工具在做什么。
