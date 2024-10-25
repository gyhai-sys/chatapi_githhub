from openai import OpenAI
from sparkai.llm.llm import ChatSparkLLM, ChunkPrintHandler
from sparkai.core.messages import ChatMessage


spark = ChatSparkLLM(streaming=False)

# gptapi.py

def load_prompt_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            prompt = file.read()
        return prompt
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return None

# 使用示例
if __name__ == "__main__":
    prompt_path = "prompt.txt"  # 如果文件在同目录下，直接写文件名即可
    prompt = load_prompt_from_file(prompt_path)
    
    
    messages = [ChatMessage(
        role="user",
        content=prompt,
        )]
    handler = ChunkPrintHandler()
    a = spark.generate([messages], callbacks=[handler])
    print(a)

