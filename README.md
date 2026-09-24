# monitor-theme-minimax-cards

基于 `minimax 1.5.3` 主题包继续开发的 Monitor 公开状态页主题。

## 改动

- 首页移除地图/延迟汇总区域，使用四张紧凑卡片显示在线节点、剩余价值、流量统计和实时网速。
- 节点卡片保留近一小时多路延迟，但将首页请求点数从 60 降至 36。
- 延迟请求最多三路并发，并增加请求去重、12 秒超时、失败后快速重试和页面恢复时刷新。
- 延迟数据到达后只更新对应节点的延迟区域，不再重绘整个节点列表。
- 缓存生成的迷你曲线，实时指标每两秒更新时无需重复计算 SVG。

## 开发

源码是无需依赖的单文件页面：

```bash
npm run build
```

构建脚本会检查内联 JavaScript 语法与必要功能标记，然后生成 `dist/index.html`。

## 安装

主题目录结构：

```text
minimax-cards/
├── theme.json
├── preview.png
└── dist/
    └── index.html
```

把目录复制到 Monitor 的主题目录，在后台切换到 `Minimax Cards` 即可。

## 出处

原主题包元数据标注作者为 `bluesmkun`，版本为 `1.5.3`，来源地址为
`https://github.com/bluesmkun/monitor-theme-minimax`。该地址在本项目创建时已无法公开访问。
