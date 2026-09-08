# Seedance 2 / Seedance 2.5 API

仅在真正调用、组织 payload 或排查任务时读这一份。只写故事或 Prompt 时不需要。

## 模型选择

两代模型走同一个 `POST /v1/videos`：

| 用途 | 模型 | 时长 | 最高分辨率 | 分镜数 |
|---|---|---:|---:|---:|
| 默认 15 秒片段 | `doubao-seedance-2-0-260128` | `4-15s` | `1080p` | 5 |
| 原生 30 秒片段 | `doubao-seedance-2-5-260628` | `4-30s` | `720p` | 10 |

提交前优先用同一鉴权读 `/v1/models` 确认模型仍然可用，不要凭记忆发明模型 ID。

## 请求体

默认 15 秒片段，无 BGM、只有可见来源声音：

```json
{
  "model": "doubao-seedance-2-0-260128",
  "prompt": "<完整的 15 秒五镜片段 Prompt>",
  "metadata": {
    "content": [
      {
        "type": "image_url",
        "image_url": {"url": "<character-or-scene-reference-url>"},
        "role": "reference_image"
      }
    ],
    "resolution": "1080p",
    "ratio": "16:9",
    "generate_audio": false,
    "duration": 15
  }
}
```

原生声音项目（BGM + 出镜对白），额外传当前片段的精确台词切片：

```json
{
  "model": "doubao-seedance-2-0-260128",
  "prompt": "<含 AUDIO LOCK 的 15 秒片段 Prompt>",
  "metadata": {
    "content": [
      {
        "type": "image_url",
        "image_url": {"url": "<character-board-url>"},
        "role": "reference_image"
      },
      {
        "type": "audio_url",
        "audio_url": {"url": "<current-segment-dialogue-slice-url>"},
        "role": "reference_audio"
      }
    ],
    "resolution": "1080p",
    "ratio": "16:9",
    "generate_audio": true,
    "duration": 15
  }
}
```

Seedance 2.5 原生 30 秒：

```json
{
  "model": "doubao-seedance-2-5-260628",
  "prompt": "<完整的 30 秒十镜 Prompt>",
  "metadata": {
    "content": [
      {
        "type": "image_url",
        "image_url": {"url": "<character-or-scene-reference-url>"},
        "role": "reference_image"
      }
    ],
    "resolution": "720p",
    "ratio": "16:9",
    "generate_audio": false,
    "duration": 30
  }
}
```

## 参数规则

- `metadata.duration` 必须是整数。Seedance2 为 `4-15`，Seedance 2.5 为 `4-30`；本 skill 的标准值是 `15` 和 `30`。**禁止把 `duration` 放在请求根级别**：网关可能忽略它并生成默认时长的片段，同时仍返回成功。
- `metadata.content` 是参考媒体真正生效的地方。留空数组等于没传参考图，Prompt 里的 `@Image1` 就成了空指针，角色一致性全部失效。每一项都要写 `role`。
- `@Image1..@ImageN`、`@Audio1..@AudioN` 与 `content` 数组顺序严格一一对应，且不跨片段重排。
- `metadata.resolution`：Seedance2 可用 `480p` / `720p` / `1080p`；Seedance 2.5 用 `480p` 或 `720p`，不要请求 `1080p`。
- `metadata.ratio` 用 `16:9`、`9:16` 或用户指定的受支持比例。
- `metadata.generate_audio` 默认 `false`（对应默认的无 BGM 策略）；原生声音项目改 `true`，并配合 [audio-production.md](audio-production.md)。
- 参考媒体必须是生成侧可访问的公网 URL，本地文件先上传。
- 不把 API Key、Authorization header 或临时凭据写进 skill、脚本、日志或生产包。

实测上限（2026-08 在 Grain `generateImageToVideo` 上验证，换网关时要重新核对）：最多 9 张参考图、最多 3 条 MP3/WAV 参考音频、音频累计不超过 15 秒；使用音频参考时必须同时提供至少一张图。

## 提交示例

```python
import requests

reference_content = [
    {
        "type": "image_url",
        "image_url": {"url": character_image_url},
        "role": "reference_image",
    },
]
if dialogue_slice_url:  # 原生对白项目才加
    reference_content.append({
        "type": "audio_url",
        "audio_url": {"url": dialogue_slice_url},
        "role": "reference_audio",
    })

model = "doubao-seedance-2-5-260628" if duration == 30 else "doubao-seedance-2-0-260128"
resolution = "720p" if duration == 30 else "1080p"

payload = {
    "model": model,
    "prompt": video_prompt,
    "metadata": {
        "content": reference_content,
        "resolution": resolution,
        "ratio": "16:9",
        "generate_audio": bool(dialogue_slice_url) or native_audio,
        "duration": duration,
    },
}

resp = requests.post(
    f"{base_url}/v1/videos",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    json=payload,
    timeout=60,
)
resp.raise_for_status()
task_id = resp.json().get("id") or resp.json().get("task_id")
persist_task(segment_id, task_id, reference_content)  # 立即落盘，不要等整批结束
```

## 付费与排查纪律

- 每次提交后立即持久化真实任务 ID、片段编号和参考资产映射；不要等 `Promise.all` 或整个脚本结束才记录，否则单个提交异常会让其余已付费任务难以追踪。
- 上游长时间 `running` 是允许状态。没有明确的“提交前被拒绝”证据时不要补交；状态不明时先查调用记录或等原进程终态。
- 多片段生成用有界并发。失败片段保留任务 ID 再排查，不静默重提。
- 任务完成后立即下载返回的 `metadata.url` 或供应商等价视频 URL，用 `ffprobe` 测量实际时长和分辨率；不要相信响应里的预计时长字段，也不要因为接口返回成功就跳过片段边界检查。
- 如果用户要求使用 CDN 或外部参考资产，先确认 URL 对生成侧可访问；CDN 不是本 skill 的固定前置步骤。
