import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama

load_dotenv()

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))
clientGroq = AsyncOpenAI(api_key=os.getenv("GROQ_API_KEY"))

llm = ChatOllama(
    model="deepseek-r1",
    base_url="http://localhost:11434",
    api_key="ollama",
    options={'temperature': 0.7}
)

llmMistral = ChatOllama(
    model="mistral",
    base_url="http://localhost:11434",
    api_key="ollama",
    options={'temperature': 0.7}
)

llmGemma2 = ChatOllama(
    model="gemma2:2b",
    base_url="http://localhost:11434",
    api_key="ollama",
    options={'temperature': 0.7}
)

app = FastAPI()

@app.post("/release_ia/open_ai")
async def generate_changelog_openai(commits: list[str]):
    if not commits:
        return {"changelog": "No se detectaron cambios nuevos desde la última versión."}

    commits_text = "\n".join(f"- {c}" for c in commits)

    prompt = f"""
    Eres una asistente de desarrollo que crea descripciones amigables para usuarios finales
    basadas en mensajes de commits de una app Flutter.

    A partir de estos commits:
    {commits_text}

    Genera un texto breve y natural en bullets (máximo 5 líneas) describiendo
    las mejoras y correcciones en lenguaje humano.
    No uses lenguaje técnico ni menciones “commit”
    Además en lenguajes español latinoamericano.
    """

    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    print("GPT 4")
    print(response.choices[0].message.content.strip())

    return {
        "changelog": response.choices[0].message.content.strip()
    }

@app.post("/release_ia/llama3")
async def generate_changelog_llama3(commits: list[str]):

    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0.7
    )

    if not commits:
        return {"changelog": "No se detectaron cambios nuevos desde la última versión."}

    commits_text = "\n".join(f"- {c}" for c in commits)

    prompt = f"""
    Eres una asistente de desarrollo que crea descripciones amigables para usuarios finales
    basadas en mensajes de commits de una app Flutter.

    A partir de estos commits:
    {commits_text}

    Genera un texto breve y natural en bullets (máximo 5 líneas) describiendo
    las mejoras y correcciones en lenguaje humano.
    No uses lenguaje técnico ni menciones “commit”
    Además en lenguajes español latinoamericano..
    """

    response = await llm.ainvoke(prompt)

    print("Llama3")
    print(response.content.strip())

    return {
        "changelog": response.content.strip()
    }

@app.post("/release_ia/deepseek")
async def generate_changelog_deepseek(commits: list[str]):
    if not commits:
        return {"changelog": "No se detectaron cambios nuevos desde la última versión."}

    commits_text = "\n".join(f"- {c}" for c in commits)

    prompt = f"""
    A partir de estos commits:
    {commits_text}

    Genera un texto breve y natural en bullets (máximo 5 líneas) describiendo
    las mejoras y correcciones en lenguaje humano.
    No uses lenguaje técnico ni menciones “commit”
    Además en lenguajes español latinoamericano..
    """

    messages = [
        ("system", "Eres una asistente de desarrollo que crea descripciones amigables para usuarios finales basadas en mensajes de commits de una app Flutter."),
        ("user", f"{prompt}")
    ]

    result = llm.invoke(messages)
    return {"changelog": result.content}

@app.post("/release_ia/mistral")
async def generate_changelog_mistral(commits: list[str]):
    if not commits:
        return {"changelog": "No se detectaron cambios nuevos desde la última versión."}

    commits_text = "\n".join(f"- {c}" for c in commits)

    prompt = f"""
    A partir de estos commits:
    {commits_text}

    Genera un texto breve y natural en bullets (máximo 5 líneas) describiendo
    las mejoras y correcciones en lenguaje humano.
    No uses lenguaje técnico ni menciones “commit”
    Además en lenguajes español latinoamericano.
    """

    messages = [
        ("system", "Eres una asistente de desarrollo que crea descripciones amigables para usuarios finales basadas en mensajes de commits de una app Flutter."),
        ("user", f"{prompt}")
    ]

    result = llmMistral.invoke(messages)
    return {"changelog": result.content}

@app.post("/release_ia/gemma2")
async def generate_changelog_gemma2(commits: list[str]):
    if not commits:
        return {"changelog": "No se detectaron cambios nuevos desde la última versión."}

    commits_text = "\n".join(f"- {c}" for c in commits)

    prompt = f"""
    A partir de estos commits:
    {commits_text}

    Genera un texto breve y natural en bullets (máximo 5 líneas) describiendo
    las mejoras y correcciones en lenguaje humano.
    No uses lenguaje técnico ni menciones “commit”
    Además en lenguajes español latinoamericano.
    """

    messages = [
        ("system", "Eres una asistente de desarrollo que crea descripciones amigables para usuarios finales basadas en mensajes de commits de una app Flutter."),
        ("user", f"{prompt}")
    ]

    result = llmGemma2.invoke(messages)
    return {"changelog": result.content}
