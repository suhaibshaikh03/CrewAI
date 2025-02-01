from litellm import completion
import os

## set ENV variables
os.environ["GEMINI_API_KEY"] = "AIzaSyCljp_8plKhCqFtH_zaBwNK4-_SQiIMI2M"
def call_gemini():
    response = completion(
    model="gemini/gemini-1.5-flash",
    messages=[{ "content": "Hello, how are you?","role": "user"}]
    )
    print(response['choices'][0]['message']['content'])

def call_gemini2():
    response = completion(
    model="gemini/gemini-2.0-flash-exp",
    messages=[{ "content": "Who is the founder of Pakistan","role": "user"}]
    )
    print(response['choices'][0]['message']['content'])
