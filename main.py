from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.ai.projects.models import PromptAgentDefinition

import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

PROMPT = os.getenv("PROMPT", "Guide me for python backend developer")


user_endpoint = os.getenv("USER_ENDPOINT")

project_client = AIProjectClient(
    endpoint=user_endpoint,
    credential=DefaultAzureCredential()
)

agent_name = "career-guidance-agent"
model_deployment_name = "gpt-4.1"

# Create an agent, bumps the agent version if parameter have changed
agent = project_client.agents.create_version(
    agent_name=agent_name,
    definition=PromptAgentDefinition(
        model=model_deployment_name,
        instructions="You are a career guidance agent. You guide best career path and skill required based on user prompt and context"
    )
)

openai_client = project_client.get_openai_client()

# reference the agent to get the response
response = openai_client.responses.create(
    input=[
        {
            "role": "user", 
            "content": PROMPT
        }
    ],
    extra_body={"agent": {"name": agent.name, "type": "agent_reference"}},
)

print(f"Response output: {response.output_text}")
