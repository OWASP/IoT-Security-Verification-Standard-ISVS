# Releasing the OWASP ISVS

This document describes how ISVS releases are versioned, branched, reviewed, and cut. It is for
project leads and maintainers. For how to *contribute* content, see [Contributing.md](Contributing.md).

## Versioning

The ISVS follows [Semantic Versioning](https://semver.org/spec/v2.0.0.html): `MAJOR.MINOR.PATCH`.

- **MAJOR** — structural or breaking changes (e.g. requirement renumbering, chapter restructuring).
- **MINOR** — new requirements or sections that do not break existing numbering.
- **PATCH** — corrections, clarifications, link and typo fixes.
- **Release candidate** — append `-RCn`, e.g. `1.0.0-RC2`. RCs are published for community review
  before a General Availability (GA) release.

Requirement numbering is part of the public contract. Once a version is tagged GA, requirement IDs
are stable; changes that renumber requirements should be batched into a MAJOR release. This is why
refinement that changes numbering (see issue #116) is done *before* the first GA tag.

## Branch model

`master` is the **bleeding edge** (the ASVS/MASVS model). All work merges into `master` via pull
request; there is no long-lived integration branch.

- Feature/fix branches → PR → `master`.
- `master` is protected: a PR and a green **Document Build** check are required to merge. Repo admins
  (project leads) may bypass; force-pushes and branch deletion are disabled.
- Releases are **git tags** on `master`, not branches.

## Release types

- **Release Candidate (RC):** cut from `master`, published as a GitHub *pre-release*, and opened for a
  ~3-week community review window (MASVS-style). The live site carries a "Release Candidate — under
  review" banner. Outreach is low-key: a GitHub Discussions thread plus a call-for-review on Slack
  (`#project-isvs`) and the mailing list. **No** social-media or project-page promotion yet.
- **General Availability (GA):** the final release. The version number (e.g. `1.0.0` vs `1.1.0`),
  removal of the RC banner, and public/marketing announcement are **project-lead decisions**.

## What a tag triggers

Pushing a tag runs [`.github/workflows/release.yaml`](.github/workflows/release.yaml), which:

1. Only proceeds when the tag is pushed by a project lead (`github.actor` is `cbassem` or
   `scriptingxss`).
2. Pulls the `owaspisvs/isvs-docgenerator` Docker image and builds **six artifacts** named for the
   tag: `.pdf`, `.epub`, `_WIP_.docx`, `.csv`, `.json`, `.xml`.
3. Creates a GitHub Release for the tag with those six files attached.

> The workflow matches **any** tag pattern. For an RC, mark the GitHub Release as a **pre-release**.

## Pre-release checklist

Before tagging, land these on `master` (each as its own reviewed PR). Tracked under issue #109.

- [ ] **Requirement counts** reconciled everywhere they appear (`index.md`, `README.md`,
      `RELEASE_NOTES.md`, frontispiece) and derived from the tools, not hand-counted:
      `cd tools && python3 export.py --format json --lang en` and count the entries.
- [ ] **Version & date strings** updated (`en/0x01-Frontispiece.md`, `index.md`, `README.md`).
- [ ] **CHANGELOG.md** entry added in [Keep a Changelog](https://keepachangelog.com/) format under a
      new `## [VERSION] - YYYY-MM-DD` heading.
- [ ] **Sequential numbering** verified (no gaps/duplicates) after any consolidation or renumbering.
- [ ] **Build is green** on `master` (Document Build) and the rendered site looks correct
      (nav, glossary, Appendix tables, links).
- [ ] For an RC: **site banner** present; GA-only items (final version, banner removal, marketing)
      explicitly deferred.

## Cutting a release

```bash
# 1. Make sure master is up to date and the build is green
git checkout master
git pull origin master

# 2. Tag (RC example) and push — this triggers release.yaml
git tag 1.0.0-RC2
git push origin 1.0.0-RC2
```

Then:

1. Watch the **Upload Release Asset** workflow run and confirm all six artifacts attach to the
   GitHub Release.
2. For an RC, edit the Release to mark it **pre-release**, open the review Discussion, and post the
   call-for-review.
3. Notify the other project lead.

## After a GA release

Project leads decide and own: the final version number, removing the RC site banner, the public
announcement/marketing, and any optional retroactive tag. Then continue normal `feature → master`
work toward the next version.
