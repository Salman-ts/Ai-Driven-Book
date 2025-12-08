import os
from .base import AgentSkill

def write_file(filepath: str, content: str):
    # Ensure directory exists
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return f"File written to {filepath}"

file_writer_skill = AgentSkill(
    name="write_file",
    description="Write content to a file at the specified path.",
    function=write_file,
    parameters={
        "type": "object",
        "properties": {
            "filepath": {"type": "string", "description": "Absolute path to the file"},
            "content": {"type": "string", "description": "Content to write"}
        },
        "required": ["filepath", "content"]
    }
)
