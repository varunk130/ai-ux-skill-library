# FAQ

## What is this library?

A collection of skills for designing UX for AI-native products - AI agents, copilots, and AI-powered features. Each skill is a reusable contract you can invoke from Claude Code, GitHub Copilot, or any agent harness that supports the Skills format.

## Who is this for?

- **Product designers** working on AI features who want a structured starting point.
- **PMs and engineers** who need to think through AI UX patterns without redoing the work.
- **AI agent builders** who want to wire UX heuristics into their tools.

## How do I use a skill?

Skills are Markdown contracts with a description and structured instructions. To use one:

1. Browse the repo and find a skill that matches your task.
2. Read its description and instructions.
3. Invoke it from your tool of choice (Claude Code, Copilot CLI, etc.) - typically by referencing the skill name or pointing at the skill file.

## Can I combine multiple skills?

Yes. Skills are designed to compose. A typical flow might chain:

1. **Audit** - run a heuristic review of the existing experience.
2. **Generate** - produce design alternatives or wireframes.
3. **Validate** - pressure-test the design against AI UX principles.

## How is this different from a regular UX checklist?

A checklist tells you *what* to look for. A skill tells your AI tool *how* to look - it provides the prompt, the structure for the output, and the heuristics to apply. The result is consistent, reviewable, and re-runnable.

## Does it require a specific AI provider?

No. Each skill is plain Markdown - you can paste the contents into any LLM chat and ask it to follow the instructions. The Skills format is a convenience for tool integrations, not a hard dependency.

## Can I extend a skill?

Yes. Fork or copy the skill file and adjust its description or instructions. Submit it back as a PR if you think others would benefit.

## Can I contribute a new skill?

Open an issue describing the skill you want to add, then submit a PR with the new contract file. See `CONTRIBUTING.md` if present for the workflow.

## What if my favorite tool doesn't support skills?

You can still use the skills manually - paste the Markdown into your chat or copy the instructions into a prompt template. The structured format makes them easy to lift into any agent harness.

## Is there a reference implementation?

Each skill is self-contained - the Markdown file is the implementation. For richer examples, check the `examples/` or `samples/` directories if present.

## License

See `LICENSE` for details.
