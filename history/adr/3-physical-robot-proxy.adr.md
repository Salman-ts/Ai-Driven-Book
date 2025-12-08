# ADR-3: Physical Robot Proxy

> **Scope**: Document decision clusters, not individual technology choices. Group related decisions that work together (e.g., "Frontend Stack" not separate ADRs for framework, styling, deployment).

- **Status:** Accepted
- **Date:** 2025-12-06
- **Feature:** 001-physical-ai-robotics-book
- **Context:** The book's curriculum culminates in a sim-to-real capstone project and physical robot control. The choice of a physical robot proxy is important for demonstrating core concepts effectively and engaging the reader.

<!-- Significance checklist (ALL must be true to justify this ADR)
     1) Impact: Long-term consequence for architecture/platform/security?
     2) Alternatives: Multiple viable options considered with tradeoffs?
     3) Scope: Cross-cutting concern (not an isolated detail)?
     If any are false, prefer capturing as a PHR note instead of an ADR. -->

## Decision

The physical robot proxy for the capstone and VLA chapters will be a **Unitree Go2 or G1 (quadrupedal robot)**.

<!-- For technology stacks, list all components:
     - Framework: Next.js 14 (App Router)
     - Styling: Tailwind CSS v3
     - Deployment: Vercel
     - State Management: React Context (start simple)
-->

## Consequences

### Positive

- **Compelling and Advanced**: A quadrupedal robot aligns well with the "humanoid" and advanced robotics theme, offering a more engaging and impressive platform than simpler mobile robots.
- **ROS 2 Support**: Unitree robots have good ROS 2 interfaces, allowing seamless integration with the software stack developed in earlier modules.
- **Onboard Sensors**: Equipped with sensors crucial for navigation and perception, directly supporting the modules' learning objectives.

<!-- Example: Integrated tooling, excellent DX, fast deploys, strong TypeScript support -->

### Negative

- **High Cost and Complexity**: Significantly more expensive and complex to operate than simpler wheeled robots (e.g., TurtleBot). This is managed by focusing on navigation and high-level control rather than complex quadrupedal locomotion algorithms.
- **Accessibility**: The high cost may make direct acquisition challenging for all readers, necessitating a focus on the simulation components first, with the physical robot as a final deployment target.

<!-- Example: Vendor lock-in to Vercel, framework coupling, learning curve -->

## Alternatives Considered

- **Alternative 1: Simple Wheeled Robot (e.g., TurtleBot)**: While more affordable and easier to operate, a simple wheeled robot does not align as strongly with the "humanoid" and advanced physical AI theme of the book. It offers less compelling demonstrations for topics like locomotion and complex interaction.

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
