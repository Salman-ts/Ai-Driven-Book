# ADR-4: VLA Model Architecture

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-06
- **Feature:** 001-physical-ai-robotics-book
- **Context:** The Vision-Language-Action (VLA) module requires integrating Speech-to-Text (STT) and Large Language Models (LLMs) to enable voice-driven robot control. The architecture for deploying these AI models needs careful consideration.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The VLA model architecture will use a **Local STT model (e.g., Whisper) on the Jetson Orin NX, combined with a Cloud LLM API (e.g., GPT-4, Claude)** for task planning.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

- **Low-Latency Speech Transcription**: Running STT locally on the Jetson provides fast conversion of voice commands to text, improving the responsiveness of the robot.
- **State-of-the-Art Task Planning**: Leveraging a powerful cloud LLM allows for advanced natural language understanding, complex task decomposition, and sophisticated reasoning capabilities that are currently superior to local, edge-optimized models.
- **Resource Optimization**: Distributes the computational load, using the Jetson's local processing for time-critical STT and offloading heavy LLM inference to the cloud.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

- **Internet Dependency**: The capstone project will require an active internet connection to communicate with the cloud LLM. This is an acceptable tradeoff for the enhanced planning capability.
- **API Cost**: Cloud LLM usage incurs API costs, which readers need to be aware of.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

- **Alternative 1: All models run locally on the Jetson**: Current local LLMs suitable for edge deployment often lack the advanced reasoning and task planning capabilities of larger cloud models. This would significantly limit the complexity of the VLA tasks the robot could perform.
- **Alternative 2: Cloud APIs for both STT and LLM**: While simpler to set up, routing real-time audio data to a cloud STT service introduces network latency, which can degrade the user experience for interactive voice commands. Local STT provides a more immediate response.

<!-- Group alternatives by cluster:
     Alternative Stack A: Remix + styled-components + Cloudflare
     Alternative Stack B: Vite + vanilla CSS + AWS Amplify
     Why rejected: Less integrated, more setup complexity
-->

## References

- Feature Spec: specs/001-physical-ai-robotics-book/spec.md
- Implementation Plan: specs/001-physical-ai-robotics-book/plan.md
- Related ADRs:
- Evaluator Evidence: history/prompts/001-physical-ai-robotics-book/2-create-technical-plan.plan.prompt.md
