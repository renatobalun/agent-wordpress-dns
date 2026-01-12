from llama_index.core.tools.tool_spec.base import BaseToolSpec
from dotenv import load_dotenv
from app.engine.search import search

load_dotenv()

class WordpressSpec(BaseToolSpec):
    """Wordpress Spec"""
    
    spec_functions=["wordpress"]
    
    def wordpress(self, query: str):
        "A tool for help with wordpress errors. It has information about most frequent wordpress errors and how to fix them."
        

        result = search(query=query)
        
                        
        return result
        
