# Career Guidance Agent (Azure AI Projects + Streamlit)

This project is a small demo showing how to use **Azure AI Projects** with a custom **Agent** and expose it through a simple **Streamlit** UI.

Users type a career-related prompt (e.g., *“Guide me for Python backend developer”*) and the Azure Agent returns a structured, helpful response in Markdown.

---

## How I installed from scratch

```bash
pip install --pre "azure-ai-projects>=2.0.0b1"
pip install azure-identity
pip install openai
pip install python-dotenv
pip install streamlit=1.45
```

Since I am using agent built from Azure AI Foundary by so you will need to create agent there by going to [Microsoft Foundry](https://ai.azure.com/)

and then from your local you need to configure Azure login using

```bash
az login
```

If you don't have azure cli installed you can do it using brew. Now being a developer don't ask me how to do that, not everything can be vibe coded, just search it on google and do that.

---

## 🔧 How It Works

The project is split into two parts:

1. **`main.py`**

   * Connects to Azure AI Projects
   * Creates or references a career-guidance agent
   * Sends the user prompt
   * Prints the agent's response in Markdown
   * Used internally by Streamlit (run as a subprocess)

2. **`app.py`**

   * Streamlit interface
   * Textbox for user prompt
   * A Submit button
   * Calls `main.py` and displays its output nicely

---

## 🚀 Getting Started

### 1. Clone the Repo

```bash
git clone <your-repo-url>
cd <repo-folder>
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

(Include Streamlit + Azure SDK packages in your `requirements.txt`.)

### 4. Set Up Environment Variables

Create a `.env` file:

```
AZURE_EXISTING_AGENT_ID="career-guidance-agent:1"
AZURE_ENV_NAME="..."
AZURE_LOCATION="..."
AZURE_SUBSCRIPTION_ID="..."
AZURE_EXISTING_AIPROJECT_ENDPOINT="..."
AZURE_EXISTING_AIPROJECT_RESOURCE_ID="..."
AZURE_EXISTING_RESOURCE_ID="..."
```

> Make sure you have authenticated using `az login` or have set service principal credentials.

---

## ▶️ Running the App

Start Streamlit:

```bash
streamlit run app.py
```

Enter a prompt, click **Submit**, and the response from your Azure Agent will be displayed.

---

## 🧩 Project Structure

```
.
├── main.py        # Handles Azure agent communication and prints response
├── app.py         # Streamlit UI
├── .env           # Environment variables (not committed)
└── requirements.txt
```

---

## ✨ Features

* Simple, clean UI for user prompts
* Markdown response rendering
* Uses Azure AI Projects agent
* Modular design (UI + agent code separated)

---

## 📌 Notes

* Streamlit calls `main.py` as a subprocess, so the output from `main.py` must be clean Markdown.
* Agent creation happens inside `main.py`. If you already have an existing agent, set `AZURE_EXISTING_AGENT_ID` to avoid creating new versions.
* Make sure you run Streamlit from the same environment that has the Azure SDK installed.


