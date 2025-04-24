class LLM:
    model = None

    @classmethod
    def query(cls) -> str:
        """Return some wisdom
        
        This function calls the llm to provide some wisdom
        """
        return "True knowledge exists in knowing that you know nothing"