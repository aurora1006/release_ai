🧠 AI-Powered Release Notes Generator

Automated changelog generation using LLMs (OpenAI, Llama 3, Mistral, Deepseek y Gemma)

Este proyecto es una herramienta que automatiza la generación de notas de liberación a partir de mensajes de commits utilizando modelos de lenguaje avanzados como OpenAI, Llama3 (Groq), Mistral y Deepseek.
Busca optimizar flujos de desarrollo, elevar la calidad de documentación y reducir trabajo manual en procesos de release.

Es un proyecto orientado a demostrar habilidades en:

🔹 Full-Stack Engineering
🔹 AI Integration & LLM
🔹 Backend APIs with FastAPI
🔹 Developer Productivity Automation
🔹 Modern tooling (uv)

✨ Key Features (Recruiter-friendly)

🤖 LLM Integration usando OpenAI, Llama3 (Groq), Mistral y Deepseek.
🧠 AI-Generated Release Notes basadas en commits reales.
🔄 Automated Changelog Pipeline, ideal para CI/CD y DevOps.
⚡ FastAPI backend, asíncrono, limpio.
📦 Architecture designed for extensibility, soporta agregar nuevos modelos fácilmente.
🔍 Prompt engineering para transformar commits técnicos en un lenguaje claro y orientado al usuario.
🏗️ Modern stack: Python 3.11+, uv, AsyncOpenAI, Groq SDK.
🧩 Modular Services Layer (OpenAI, Groq, Mistral-ready).

📝 Project Description

Los commits suelen ser escritos para desarrolladores, no para usuarios finales.
Este proyecto utiliza IA generativa para transformar mensajes técnicos de commits en notas de versión claras, naturales y entendibles, en bullets y sin lenguaje técnico.

Ejemplo:

[
  "fix login bug",
  "update UI colors",
  "improve performance"
]

[
  "Se corrigió un error en el login",
  "Se actualizaron los colores de la interfaz",
  "Mejoró el performance de la aplicación"
]

El sistema produce:

Se solucionó un problema que impedía iniciar sesión.
Se actualizaron los colores de la interfaz para una experiencia más agradable.
La aplicación ahora funciona de manera más eficiente.

Esto permite que los equipos publiquen changelogs profesionales automáticamente, sin invertir tiempo redactando texto manual.

🚀 Tech Stack

Python 3.11+
FastAPI (async API)
uv (entorno y runtime moderno)
OpenAI API
Groq | Llama 3
Async I/O
dotenv

📡 API Endpoints (http://127.0.0.1:8000/docs)
POST /release_ia/openai

🔧 Installation & Setup
1. Clonar repositorio
git clone https://github.com/tu_usuario/tu_repo.git
cd tu_repo

2. Instalar dependencias
uv sync

3. Variables de entorno
OPENAI_API_KEY=your_key
GROQ_API_KEY=your_key

4. Ejecutar servidor
uv run uvicorn main:app --reload --port 8000

🧠 How It Works (LLM Orchestration)

Recibe un arreglo de commits.
Construye un prompt optimizado.
Lo envía al modelo seleccionado (OpenAI, Llama3, Mistral, Deepseek).
El LLM genera texto claro y user-friendly.
La API devuelve bullets listos para publicar.

