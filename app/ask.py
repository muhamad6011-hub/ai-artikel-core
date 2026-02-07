from fastapi import APIRouter, Request
from get_answer import get_answer

router = APIRouter()

@router.post("/ask")
async def ask(request: Request):
    data = await request.json()
    question = data.get("question", "")
    answer = get_answer(question)
    return {"question": question, "answer": answer}
