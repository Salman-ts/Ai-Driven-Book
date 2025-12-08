from ..base import ChatKitAgent, AgentSkill
from ..skills.file_ops import file_writer_skill

class DocGenAgent(ChatKitAgent):
    def __init__(self):
        super().__init__(
            name="DocGen",
            role="Document Generator specialized in creating markdown documentation."
        )
        # Re-wrap skill with proper schema if needed, or update file_ops to have schema
        # For now, we assume file_writer_skill needs update or we add it directly
        self.add_skill(file_writer_skill)

doc_gen_agent = DocGenAgent()
