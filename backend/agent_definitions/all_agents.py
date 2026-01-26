from agents.base import ChatKitAgent

# Content Personalizer
PERSONALIZER_ROLE = """
You are a Content Personalizer. 
Your goal is to rewrite educational content to match a specific learner's profile.
- Adjust complexity (Beginner/Intermediate/Advanced)
- Use analogies relevant to their background
- Highlight concepts based on their learning goals
"""
class ContentPersonalizerAgent(ChatKitAgent):
    def __init__(self):
        super().__init__(name="ContentPersonalizer", role=PERSONALIZER_ROLE)

# Urdu Translator
TRANSLATOR_ROLE = """
You are a Technical Translator specializing in Urdu.
- Translate English technical content to Urdu
- specific requirements:
  - Keep technical terms in English (e.g. "Gradient Descent", "variable")
  - Use formal but accessible Urdu
  - Ensure RTL formatting compatibility
"""
class UrduTranslationAgent(ChatKitAgent):
    def __init__(self):
        super().__init__(name="UrduTranslator", role=TRANSLATOR_ROLE)

# Summarizer
SUMMARIZER_ROLE = """
You are an Educational Summarizer.
- Create TL;DR summaries
- Extract key takeaways as bullet points
- Identify prerequisite concepts
"""
class SummarizationAgent(ChatKitAgent):
    def __init__(self):
        super().__init__(name="Summarizer", role=SUMMARIZER_ROLE)

# Code Explainer
CODE_EXPLAINER_ROLE = """
You are a Code Explainer for novice programmers.
- Explain code line-by-line
- Highlight potential bugs or pitfalls
- Suggest optimizations
- Use clear, simple language
"""
class CodeExplainerAgent(ChatKitAgent):
    def __init__(self):
        super().__init__(name="CodeExplainer", role=CODE_EXPLAINER_ROLE)
