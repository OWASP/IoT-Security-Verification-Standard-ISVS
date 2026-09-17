# Skills

## Overview

This directory holds "skills" used to maintain and use parts of the ISVS —
self-contained bundles of instructions, reference material, and plain Python
scripts for a specific task.

Each skill is written so it can be used **with or without an AI assistant**.
The scripts do the mechanical work (parsing, filtering, validation) and
require nothing but `python3` from the standard library. The `SKILL.md` file
in each skill is a step-by-step playbook that a human contributor can follow
directly, or that an AI coding assistant can follow on a contributor's
behalf.

## Available skills

- [`isvs-custom-mapping-builder/`](isvs-custom-mapping-builder/README.md) —
  builds a product-context-specific mapping from ISVS requirements to other
  standards by filtering the generalized Appendix B mapping. It preserves
  ISVS and framework versions, sources, and uncertain mappings, and never
  invents new framework equivalence.
