from llama_index.core.tools.tool_spec.base import BaseToolSpec
from dotenv import load_dotenv
from app.engine.search import search

load_dotenv()

class FallbackToHumanSpec(BaseToolSpec):
    """Fallback to human Spec"""
    
    spec_functions=["fallback_to_human"]
    
    def fallback_to_human(self, query: str):
        "A tool for getting human contact. Always call this tool when user wants to speak to a human."
        

        result = {
            "email": "emailsupport@seaspace.com",
            "message": "Contact us on this email."
        }
        
                        
        return result