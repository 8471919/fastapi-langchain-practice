from fastapi import APIRouter
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
from pydantic import BaseModel

# from IPython.display import display, Markdown

load_dotenv()

OPENAI_API_KEY=os.environ.get("OPENAI_API_KEY")

v1_router = router = APIRouter()
openai = ChatOpenAI(api_key=OPENAI_API_KEY, model="gpt-4", temperature=0.7)
# prompt = ChatPromptTemplate.from_template(q)

# chain = create_stuff_documents_chain(openai, prompt)

necessary = """
그리고 
나는 학생이고, 너는 xml을 이해하는 수학 선생님이야. 너는 xml을 이해하는 수학 선생님으로서 학생에게 문제에 대한 해설을 '간단한 해설'과 '자세한 해설'로 나누어서 설명해줄 의무가 있어.
'간단한 해설'은 '자세한 해설'을 요약해서 작성한 해설본이고, '자세한 해설'은 유치원생도 문제를 이해할 수 있도록 작성한 해설본이야.
만약 너가 문제를 맞히지 못하면 벌을 줄테니 각오해.

다음은 내가 가져온 수학 문제인데 xml형식이야. 너는 xml을 이해하는 수학 선생님으로서 이 문제를 풀고 해설을 텍스트로 변환해. 
그리고 출력 형식은

[간단한 해설]
너가 작성한 '간단한 해설'

[자세한 해설]
너가 작성한 '자세한 해설'

[정답]
너가 생각한 '정답'

으로 하도록 해.
\n
"""

class Input(BaseModel):
    question: str
    prompt: str

@router.post("/")
async def getAnswerFromOpenAi(input: Input):
    answer = openai.invoke(f"{input.prompt}\n{necessary}\n{input.question}").content
    return answer