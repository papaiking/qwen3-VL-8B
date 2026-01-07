from openai import OpenAI

client = OpenAI(base_url="http://10.148.0.20:8000/v1", api_key="none")

response = client.chat.completions.create(
    model="Qwen/Qwen3-VL-8B-Instruct-FP8",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": """
Perform OCR and extract product order information from the file. 

CRITICAL INSTRUCTIONS:
1. Clean the text and keep the original information 
2. Output: Return ONLY a valid JSON object as follow:
        {
            "title": "xxxx"   # Indicate this is document title, such as: Order, Quotation or other...
            "customer": {
                "name": "xxx",
                "phone": "xxxx",
                "addess": "xxxxx",
                "payment_method": "xxx"
            },
            "products": [
                {
                    "name": "xxxxx",
                    "quantity": xxxxx, 
                    "price": xxxxx
                }
            ]
        }
                """},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://lenguyentst.com.vn/wp-content/uploads/2023/09/image-35.png"}
                },
            ],
            # "content": [
            #     {"type": "text", "text": "Describe the details in this image."},
            #     {
            #         "type": "image_url",
            #         "image_url": {"url": "https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggWFoJ-IDwt3J_xgV6hXb5hdluu0jKcTcseSb37yyWYIgllqnUPzUUb_Q2EPDXHOJ-dQPZU9vnbY4jKmOs6UI86jrN0sq1SDBI7qTiQrffXKKh1s5Xll8kBpBgLdaykZdoLKxZww64hQY/s1600/do+luong.png"}
            #     },
            # ],

            # "content": [
            #     {"type": "text", "text": "Tell me on Customer experience."},
            # ],

        }
    ],
    temperature=0.0,      # Randomness
    # top_p=0.8,            # Nucleus sampling
    # top_k=20,             # Top-K sampling
    # presence_penalty=1.5, # Reduce repetition
    # frequency_penalty=0.0,    
    max_tokens=5120
)

print(response.choices[0].message.content)