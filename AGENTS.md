# Documentation project instructions

## About this project

- This is a documentation site built on [Mintlify](https://mintlify.com)
- Pages are MDX files with YAML frontmatter
- Configuration lives in `docs.json`
- The content is agent-facing Parashell API documentation intended for MCP retrieval

## Terminology

- Product name: `Parashell`.
- Compatibility phrase: `FreeCAD-compatible`.
- Do not equate Parashell with the upstream product. Only mention compatibility where it affects API usage.
- It is acceptable to document required Python module names such as `FreeCAD`, `FreeCADGui`, `Part`, and `Sketcher`.

## Style preferences

- Optimize for exact retrieval by an agent.
- Prefer dense signatures, schemas, invariants, and failure modes over tutorial prose.
- Keep JSON-like examples inside fenced code blocks so MDX does not parse braces as expressions.
- Code-format file names, commands, paths, function names, and TypeIds.

## Content boundaries

- Document MCP tools, schemas, execution rules, Python API patterns, validation, and workflows.
- Do not add end-user marketing copy.
- Do not document speculative APIs.
