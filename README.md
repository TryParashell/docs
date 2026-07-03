# Parashell docs

This Mintlify site is the agent-facing Parashell reference. The content is optimized for MCP retrieval by CAD agents, not for end-user onboarding.

## Local preview

Install the Mintlify CLI if needed:

```bash
npm i -g mint
```

Run from this `docs` directory:

```bash
mint dev
```

## Structure

- `index.mdx`: retrieval map and mandatory invariants.
- `quickstart.mdx`: first-call sequence for agents.
- `agent/`: operating model, schemas, coverage contract, all-file source scan coverage, code-derived best practices, Python quirks, compatible module map, runtime introspection, TypeIds/properties, Python API, syntax, workflows, generated Python references.
- `agent/tools/`: generated MCP tool reference from `Parashell-Modules/Source/Bridge/tools`.
- `docs.json`: Mintlify navigation and site configuration.

## Terminology

Use `Parashell` for the product. Use `FreeCAD-compatible` only when describing API compatibility or required Python module import names.
