# ADR-2: Edge AI Platform

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-06
- **Feature:** 001-physical-ai-robotics-book
- **Context:** The book's curriculum includes deploying AI perception and VLA pipelines to edge hardware for real-world application. The choice of edge computing platform is critical for performance and reader experience.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The primary edge AI platform will be the **NVIDIA Jetson Orin NX**.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

- **High Performance**: Provides sufficient computational power (GPU and CPU) to run advanced perception models and the VLA pipeline concurrently without significant performance degradation, ensuring a smoother reader experience.
- **Future-Proofing**: Offers more headroom for future expansions and more complex AI models.
- **Isaac ROS Compatibility**: Fully compatible with NVIDIA Isaac ROS, enabling hardware-accelerated ROS 2 nodes.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

- **Higher Cost**: More expensive than lower-end Jetson models (e.g., Orin Nano), potentially impacting budget-conscious readers. This is mitigated by ensuring all code is also compatible with the Nano, but with documented performance limitations.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

- **Alternative 1: NVIDIA Jetson Orin Nano**: While more affordable, the Orin Nano has lower processing power compared to the NX. This could lead to performance bottlenecks when running complex AI models or multiple components of the VLA pipeline simultaneously, potentially hindering the reader's experience with advanced labs.

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
