from langchain_groq import ChatGroq

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
    las mejoras y correcciones en lenguaje humano. A cada bullets agregale un emoji.
    No uses lenguaje técnico ni menciones “commit”.
    Además en lenguaje español latinoamericano.
    """

    response = await llm.ainvoke(prompt)

    print("Llama3")
    print(response.content.strip())

    return {
        "changelog": response.content.strip()
    }