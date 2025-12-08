# ADR-1: Primary Simulation Platform

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-06
- **Feature:** 001-physical-ai-robotics-book
- **Context:** The book aims to teach full-stack Physical AI and humanoid robotics, leveraging various simulation platforms. A key decision involves selecting the primary high-fidelity simulation environment.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The primary high-fidelity simulation platform will be **NVIDIA Isaac Sim**. While Gazebo is used for foundational ROS 2 concepts and Unity for exploring high-fidelity rendering, Isaac Sim will be the central platform for advanced topics like synthetic data generation, GPU-accelerated perception, and sim-to-real workflows.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

- **Photorealistic Rendering**: Enables the generation of high-quality synthetic data for training AI models, crucial for perception and VLA.
- **GPU-Accelerated Physics**: Provides efficient and realistic simulation, reducing iteration times.
- **Integrated AI Tools**: Seamless integration with Isaac ROS and synthetic data generation tools simplifies advanced AI robotics development.
- **Direct Pipeline to Jetson**: Facilitates sim-to-real transfer and deployment to edge devices.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

- **High Hardware Requirements**: Necessitates a powerful NVIDIA RTX GPU, potentially limiting accessibility for some readers. This is mitigated by offering cloud-based options (AWS g5/g6e).
- **Steeper Learning Curve**: Isaac Sim, being a more comprehensive platform, may have a steeper initial learning curve compared to simpler simulators.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

- **Alternative 1: Gazebo/RViz2**: While a ROS 2 standard, it lacks integrated high-fidelity rendering and advanced AI tools for synthetic data generation compared to Isaac Sim. Separate tools (e.g., Unity for rendering) are needed to achieve comparable visual quality, increasing complexity.
- **Alternative 2: Unity with ROS Connectors**: Offers high-fidelity rendering but requires more manual integration for physics simulation (though it has its own physics engine) and a less direct pipeline to NVIDIA's AI-specific tools (Isaac ROS, synthetic data) compared to Isaac Sim.

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
