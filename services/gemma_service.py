from langchain_ollama import ChatOllama

llmGemma2 = ChatOllama(
    model="gemma2:2b",
    base_url="http://localhost:11434",
    api_key="ollama",
    options={'temperature': 0.7}
)

async def generate_changelog_gemma2(commits: list[str]):
    if not commits:
        return {"changelog": "No se detectaron cambios nuevos desde la última versión."}

    commits_text = "\n".join(f"- {c}" for c in commits)

    prompt = f"""
    A partir de estos commits:
    {commits_text}

    Genera un texto breve y natural en bullets (máximo 5 líneas) describiendo
    las mejoras y correcciones en lenguaje humano. A cada bullets agregale un emoji.
    No uses lenguaje técnico ni menciones “commit”.
    Además en lenguaje español latinoamericano.
    """

    messages = [
        ("system", "Eres una asistente de desarrollo que crea descripciones amigables para usuarios finales basadas en mensajes de commits de una app Flutter."),
        ("user", f"{prompt}")
    ]

    result = llmGemma2.invoke(messages)
    return {"changelog": result.content}