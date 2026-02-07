from read_bigdata import read_bigdata

def get_answer(question: str) -> str:
    question_lower = question.lower()
    bigdata = read_bigdata()
    for folder, content in bigdata.items():
        if question_lower in content.lower():
            start_index = content.lower().find(question_lower)
            snippet = content[start_index:start_index+300]
            return snippet + "..."
    return "Maaf, saya belum menemukan jawaban yang sesuai di dataset."
