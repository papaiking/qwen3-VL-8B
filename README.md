# Purpose
- This repos for running Qwen3-VL-8B-Instruct model on GPR L4

# Running

## Start model

Export the HG token: export HF_TOKEN=

then start docker:

`
$ ./start.sh
`

For watching logs, run:
`
$ docker logs -f qwen3-vl-server
`

## testing model
Print all models running:
`
curl http://10.148.0.20:8000/v1/models
`

```python
from openai import OpenAI

client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")

response = client.chat.completions.create(
    model="Qwen/Qwen3-VL-8B-Instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "Describe the details in this image."},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"}
                },
            ],
        }
    ],
    max_tokens=512
)

print(response.choices[0].message.content)
```