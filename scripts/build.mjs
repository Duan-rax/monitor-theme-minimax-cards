import { mkdir, readFile, writeFile } from "node:fs/promises"

const source = await readFile(new URL("../src/index.html", import.meta.url), "utf8")
const inlineScript = source.match(/<script>([\s\S]*?)<\/script>/)
if (!inlineScript) throw new Error("src/index.html 缺少内联脚本")
new Function(inlineScript[1])
for (const marker of ["在线节点", "剩余价值", "流量统计", "实时网速", "cardLatencyBlock"]) {
  if (!source.includes(marker)) throw new Error(`缺少必要功能：${marker}`)
}
await mkdir(new URL("../dist/", import.meta.url), { recursive: true })
await writeFile(new URL("../dist/index.html", import.meta.url), source)
console.log(`built dist/index.html (${Buffer.byteLength(source)} bytes)`)
