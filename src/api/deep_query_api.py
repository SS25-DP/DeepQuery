from fastapi import FastAPI
import ollama


from src.models.llm_request_model import LLMRequestModel
from src.models.llm_response_model import LLMResponseModel

# Befehl zum starten der API: uvicorn src.api.deep_query_api:app --host 0.0.0.0 --port 8888
app = FastAPI(root_path="/api", debug=True)
ollama_client = ollama.Client(host='http://localhost:11434', timeout=10.0)

@app.post("/llm-response")
def generate_llm_response(data: LLMRequestModel):
    prompt = data.prompt
    response_with_reasoning = ollama.chat(
        model="deepseek-r1:14b",
        messages=prompt,
    )
    response_without_reasoning= response_with_reasoning["message"]["content"].split("</think>")[1]
    llm_response = LLMResponseModel(response=response_without_reasoning)
    return llm_response
