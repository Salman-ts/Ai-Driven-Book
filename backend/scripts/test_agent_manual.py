import asyncio
import os
import sys

# Add parent dir
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.definitions.doc_gen import doc_gen_agent

async def main():
    print("🤖 Starting Manual Agent Test...")
    print("   Target: DocGenAgent")
    print("   Goal: Create a test file 'test_output.md'")
    
    # Ensure key is present
    if "OPENAI_API_KEY" not in os.environ:
        print("❌ Error: OPENAI_API_KEY not found in environment variables.")
        print("   Please set it in your .env or shell.")
        return

    try:
        # 1. Initialize
        print("\n1. Initializing Agent (Communicating with OpenAI)...")
        await doc_gen_agent.initialize()
        print(f"   ✅ Agent Initialized. ID: {doc_gen_agent.assistant_id}")
        
        # 2. Run Task
        prompt = "Create a file named 'test_output.md' with the content: '# Success\nThis file was created by the DocGen Agent.'"
        print(f"\n2. Sending Prompt: \"{prompt}\"")
        
        # Using run() which handles the full loop
        # For streaming demo, you'd use run_stream
        response = await doc_gen_agent.run(prompt)
        
        # 3. Verify Output
        print(f"\n3. Agent Response: {response.content[0].text.value}")
        
        if os.path.exists("test_output.md"):
            print("   ✅ SUCCESS: File 'test_output.md' was created!")
            with open("test_output.md", "r") as f:
                print(f"   [Content]: {f.read().strip()}")
            # Cleanup
            os.remove("test_output.md")
        else:
            print("   ❌ FAILURE: File was NOT created.")
            
    except Exception as e:
        print(f"\n❌ Exception occurred: {e}")

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv() # Load .env if present
    asyncio.run(main())
