
from fastapi import FastAPI
from services.openai_service import generate_changelog_openai
from services.llama3_service import generate_changelog_llama3
from services.deepseek_service import generate_changelog_deepseek
from services.mistral_service import generate_changelog_mistral
from services.gemma_service import generate_changelog_gemma2

app = FastAPI(title="Release AI", version="1.0.0")

@app.post("/generate-changelog/openai")
async def generate_openai(commits: list[str]):
    result = await generate_changelog_openai(commits)
    return {"changelog": result}

@app.post("/generate-changelog/llama3")
async def generate_llama3(commits: list[str]):
    result = await generate_changelog_llama3(commits)
    return {"changelog": result}

@app.post("/generate-changelog/deepseek")
async def generate_deepseek(commits: list[str]):
    result = await generate_changelog_deepseek(commits)
    return {"changelog": result}

@app.post("/generate-changelog/mistral")
async def generate_mistral(commits: list[str]):
    result = await generate_changelog_mistral(commits)
    return {"changelog": result}

@app.post("/generate-changelog/gemma")
async def generate_mistral(commits: list[str]):
    result = await generate_changelog_gemma2(commits)
    return {"changelog": result}