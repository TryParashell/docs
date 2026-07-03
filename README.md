# Parashell docs

This Mintlify site is the agent-facing Parashell reference. The content is optimized for MCP retrieval by CAD agents, not for end-user onboarding.

## Local preview

Install the Mintlify CLI if needed:

```bash
npm i -g mint
```

Run from this `docs` directory:

```bash
mintlify dev
```

## Structure

- `index.mdx`: retrieval map and mandatory invariants.
- `quickstart.mdx`: first-call sequence for agents.
- `agent/`: operating model, schemas, coverage contract, best practices, Python quirks, compatible module map, runtime introspection, TypeIds/properties, Python API, syntax, workflows, generated Python references.
- `agent/tools/`: MCP tool reference pages.
- `docs.json`: Mintlify navigation and site configuration.

## Terminology

Use `Parashell` for the product. Use `FreeCAD-compatible` only when describing API compatibility or required Python module import names.

## Path naming checks

When renaming implementation directories, search the docs repository for stale CI or private source-tree paths before committing. Do not add documentation that depends on private implementation paths. Prefer published MCP tool names, FreeCAD-compatible module import names, and page-relative documentation paths.
