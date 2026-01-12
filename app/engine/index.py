import os
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.llms.openai import OpenAI

from dotenv import load_dotenv

from app.engine.tools.wordpress import WordpressSpec
from app.engine.tools.dns import DnsSpec

load_dotenv()

openai_model = os.getenv("MODEL")
openai_llm = OpenAI(model=openai_model)

def get_agent():
    wordpress_tool = WordpressSpec().to_tool_list()
    dns_tool = DnsSpec().to_tool_list()
    
    tools = (wordpress_tool + dns_tool)
    
    agent = FunctionAgent(
        tools=tools,
        llm=openai_llm,
        verbose=True,
        system_prompt="You are an assistant that helps with fixing wordpress and DNS errors. If a domain is mentioned in a query, take that domain and pass it to a DNS tool.",
        max_function_calls=1
    )
    
    return agent