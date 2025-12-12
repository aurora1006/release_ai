import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv

load_dotenv()

llmOpenAI = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0.7,
    api_key = os.getenv("OPENAI_API_KEY")
)

changelog_template = PromptTemplate(
    input_variables=["commits_text"],
    template="""
    Eres una asistente de desarrollo que crea descripciones amigables para usuarios finales
    basadas en mensajes de commits de una app movil.

    A partir de estos commits:

    {commits_text}

    Genera un texto breve y natural en bullets (máximo 5 líneas) describiendo
    las mejoras y correcciones en lenguaje humano. A cada bullets agregale un emoji.
    No uses lenguaje técnico ni menciones “commit”.
    Además en lenguaje español latinoamericano.
    """
)

parser = StrOutputParser()

# 🔧 Funciones para logs
def log_prompt(input_dict):
    print("\n===== 🟦 PROMPT RENDERIZADO =====")
    print(input_dict["prompt"])
    return input_dict

def log_raw_output(output):
    print("\n===== 🟩 RESPUESTA RAW DEL MODELO =====")
    print(output)
    return output

def log_final_output(output):
    print("\n===== 🟨 RESPUESTA FINAL PARSEADA =====")
    print(output)
    return output

# 🧱 Chain con pasos intermedios y logs
changelog_chain = (
    {
        # Render prompt
        "prompt": changelog_template,  
        "commits_text": RunnablePassthrough()
    }
    # Log del prompt
    | RunnablePassthrough(func=log_prompt)
    # Solo enviamos el prompt como input al modelo
    | (lambda d: d["prompt"])
    # LLM
    | llmOpenAI
    # Log respuesta bruta
    | RunnablePassthrough(func=log_raw_output)
    # Parseo final
    | parser
    # Log respuesta final
    | RunnablePassthrough(func=log_final_output)
)

async def generate_changelog_openai(commits: list[str]):
    print("\n===== OPEN AI =====")
    if not commits:
        return {"changelog": "No se detectaron cambios nuevos desde la última versión."}

    commits_text = "\n".join(f"- {c}" for c in commits)

    content = await changelog_chain.ainvoke({
        "commits_text": commits_text
    })
    return {"changelog": content}