# ISVS Interactive Web Tool - Technical Specification

**Version**: 1.1
**Date**: October 2025 (reviewed June 2026)
**Status**: Proposal — under review, implementation deferred until after the ISVS 1.1 release
**Branch**: `isvs-tool`

> **Note:** See [Spec Review Status & Remaining Work](#spec-review-status--remaining-work) below for the authoritative MVP scope, what has been fixed, and the open decisions to resolve before implementation begins.

---

## Spec Review Status & Remaining Work

This section records the outcome of the June 2026 spec review (issue #94). It is the authoritative source where it conflicts with older prose further down the document.

### Done
- **Data layer unblocked.** `tools/isvs.py` now emits a `category` field (e.g. `"V1"`, derived from the requirement ID) and a `subsection` field (the `###` heading, e.g. `"Supply Chain"`) in JSON output. Verified: all requirements carry both fields; CSV and XML output are unchanged (additive change, backward compatible with the existing `OWASP_ISVS-SNAPSHOT.json` artifact).

### Open decisions (resolve at implementation time, post-release)
1. **JSON key casing.** `export.py` emits capitalized keys (`ID`, `Description`, `L1`, `L2`, `L3`); the app interfaces in this spec assume lowercase (`id`, `description`, `l1`, `l2`, `l3`). Decision deferred because changing `to_json()` casing would also change the published `OWASP_ISVS-SNAPSHOT.json` artifact. Resolve by either (a) mapping keys in the app, or (b) emitting lowercase from a tool-specific export path.
2. **Deployment.** Replace the third-party `peaceiris/actions-gh-pages@v3` (§5.2) with the official `actions/upload-pages-artifact` + `actions/deploy-pages`. Confirm coexistence with the existing Jekyll GitHub Pages setup (the repo currently serves via `_config.yaml` / `.github/workflows/pages.yml`, not a `docs/` folder). A `webapp/package-lock.json` must exist before `cache: npm` will work.
3. **Deployment URL.** The `https://owasp.org/IoT-...` URL in §5 is likely incorrect; the GitHub Pages URL is probably `https://owasp.github.io/IoT-Security-Verification-Standard-ISVS/isvs-tool/` (or a configured custom domain). Confirm before publishing.

### Corrections to older prose in this document
- **MVP scope is authoritative per issue #94:** F1 (checklist + localStorage), F2 (filtering), F3 (progress dashboard), **F4 — CSV export only**, and CI/CD. Everything else is Phase 2, including: F4 JSON export and print/compliance-certificate view, **F5 deep-linking/sharing** (and therefore the React Router dependency in §2.1), F6 notes, F7 team sync, F8 templates. Where §3.1 lists F5 or F4 JSON/print as "Core (MVP)", treat this section as authoritative instead.
- **Logo "blocker" is invalid.** Issue #94 states `en/images/owasp_logo.png` does not exist; it does exist. No fix needed.
- **Bundle-size target** is inconsistently stated (issue: "<200 KB uncompressed"; §2.1: "<500 KB gzipped"; diagram: "~155 KB"). Standardize on one figure during implementation.
- **Requirement counts are auto-derived** from the markdown; hardcoded counts ("165") in prose/use-cases are illustrative and will drift (the figure becomes 169 once the V1.6 requirements merge). Do not hardcode.
- **Use-case Example 3** ("teams share URLs; CISO views progress in real-time") is not achievable with the localStorage-only, no-backend architecture. Reword to reflect exported-report sharing, not live multi-team viewing.

---

## Executive Summary

This specification defines an interactive web application to make the OWASP IoT Security Verification Standard (ISVS) more accessible and practical for security professionals, IoT developers, and compliance teams. The tool eliminates adoption barriers by replacing static documents with an interactive, browser-based checklist system.

**Core Value**: Transform ISVS from a static PDF/spreadsheet workflow into an engaging, trackable, and reportable verification tool with zero infrastructure costs.

---

## 1. Problem Statement & Value Proposition

### 1.1 Current Adoption Barriers

| Barrier | Impact | User Complaint |
|---------|--------|----------------|
| **Multiple Format Fragmentation** | Users must download PDF, EPUB, DOCX, CSV, JSON, or XML files | "I have 6 different ISVS files, which one should I use?" |
| **No Interactive Tooling** | Unlike OWASP ASVS (Django app) and MASVS (web checklists), ISVS has no interactive tool | "Why can't I just click through requirements like ASVS?" |
| **Manual Tracking Burden** | Security teams use spreadsheets or printed PDFs to track progress | "I'm copying requirements into Excel manually" |
| **No State Persistence** | Cannot save progress or resume audits | "Lost all my work when browser crashed" |
| **Limited Accessibility** | Requires desktop software (PDF readers) or technical skills (parsing JSON/XML) | "Can't use this on my phone during device testing" |
| **No Collaboration Features** | Cannot share progress or specific requirements easily | "How do I show my team requirement V2.1.3?" |

### 1.2 Value Delivered by Interactive Tool

**For Security Auditors:**
- ✅ Interactive checklist to track verification progress across 165 requirements
- 📊 Real-time progress dashboards per category (V1-V5) and security level (L1-L3)
- 💾 Auto-save to browser localStorage - never lose progress
- 📄 Generate compliance reports (PDF/CSV) with completed requirements
- 🔗 Deep-link specific requirements to share with team members

**For IoT Product Developers:**
- 🎯 Filter requirements by security level (L1/L2/L3) matching product risk profile
- 🔍 Search functionality to find specific requirements (e.g., "cryptography", "Bluetooth")
- 📱 Mobile-responsive design for testing on-site
- 🌙 Dark mode for extended use

**For Compliance Teams:**
- 📈 Visual compliance status across all categories
- 📋 Export audit trail showing completed vs pending requirements
- 🏷️ Tag requirements with custom notes (e.g., "N/A - no Bluetooth", "Completed - see ticket #123")
- 📅 Timestamped completion tracking

### 1.3 Real-World Use Case Examples

#### Example 1: Security Audit of Smart Camera Firmware
**Persona**: Sarah, IoT Security Auditor at Smart Home Corp

**Scenario**: Sarah needs to audit a new smart camera's firmware before release.

**Current Workflow** (with PDF):
1. Downloads 40-page ISVS PDF
2. Prints or highlights in PDF reader
3. Creates Excel spreadsheet to track 165 requirements
4. Manually filters for L2 requirements (camera stores sensitive data)
5. Copy-pastes requirement text into audit report
6. Loses progress when PDF reader crashes
7. **Time**: 8 hours of manual work

**New Workflow** (with Interactive Tool):
1. Opens ISVS tool in browser
2. Filters to L2 requirements only (auto-displays 98 relevant items)
3. Checks off completed requirements as tested
4. Adds notes: "V2.1.3 - Verified with test case TC-AUTH-001"
5. Progress auto-saved to browser
6. Exports CSV compliance report
7. **Time**: 3 hours (62% time saving)

#### Example 2: Agile Sprint Planning for IoT Startup
**Persona**: Marcus, Lead Developer at WearableTech Inc

**Scenario**: Planning security tasks for new fitness tracker (L1 device).

**Current Workflow**:
1. Downloads ISVS CSV
2. Imports to Jira manually
3. Deletes L2/L3 requirements not applicable
4. Creates 50+ tickets by hand
5. **Time**: 4 hours

**New Workflow**:
1. Opens tool, filters to L1 requirements only
2. Exports filtered list as CSV
3. Bulk imports to Jira
4. **Time**: 30 minutes (87% time saving)

#### Example 3: Executive Compliance Report
**Persona**: Emily, CISO at Medical IoT Company

**Scenario**: Quarterly board report on IoT security posture.

**Current Workflow**:
1. Collects spreadsheets from 5 product teams
2. Manually consolidates data
3. Creates PowerPoint slides
4. **Time**: 6 hours

**New Workflow**:
1. Product teams share their ISVS tool URLs
2. Emily views each team's progress in real-time
3. Exports combined compliance report
4. **Time**: 1 hour (83% time saving)

---

## 2. Technical Architecture

### 2.1 Minimal Dependencies Philosophy

**Principle**: Every dependency must justify its existence. Total bundle size target: **< 500 KB** (gzipped).

| Dependency | Size | Justification | Alternative Rejected |
|------------|------|---------------|---------------------|
| **React 18** | 45 KB | Component reusability, ecosystem maturity, hooks for state | Vue (similar size but less OWASP familiarity) |
| **Vite** | 0 KB (dev only) | Fast builds (<1s), ESM-native, tree-shaking | Create React App (10x slower, deprecated) |
| **TypeScript** | 0 KB (compile-time) | Type safety for 165 requirements data, better DX | PropTypes (runtime overhead, less safety) |
| **Tailwind CSS** | ~30 KB | Utility-first, purges unused styles, no custom CSS | Bootstrap (150+ KB, opinionated) |
| **Zustand** | 3 KB | Minimal state management, localStorage sync | Redux (40 KB, boilerplate heavy) |
| **React Router** | 12 KB | Deep linking, shareable URLs | Wouter (8 KB but limited features) |

**Total Runtime Bundle**: ~90 KB (before ISVS data ~30 KB JSON) = **~120 KB total**

**ZERO Backend Dependencies**:
- No Node.js server required
- No database needed (localStorage for state)
- No API calls (static JSON data)
- 100% client-side rendering

### 2.2 Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    GitHub Pages (Free Hosting)               │
│                                                               │
│  https://owasp.org/IoT-Security-Verification-Standard-ISVS/  │
│                         /isvs-tool/                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     Static Web App Bundle                    │
│                                                               │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────┐   │
│  │   index.html│  │  isvs-app.js │  │  isvs-data.json  │   │
│  │   (5 KB)    │  │  (120 KB)    │  │  (30 KB)         │   │
│  └─────────────┘  └──────────────┘  └──────────────────┘   │
│                                                               │
│  Total: ~155 KB (gzipped: ~50 KB) - Loads in <1s on 3G      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       Browser Runtime                        │
│                                                               │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  React Components (UI Layer)                           │ │
│  │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐  │ │
│  │  │ Header   │ │ Filters  │ │ Checklist│ │ Export   │  │ │
│  │  └──────────┘ └──────────┘ └──────────┘ └──────────┘  │ │
│  └────────────────────────────────────────────────────────┘ │
│                              │                               │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Zustand Store (State Management)                      │ │
│  │  - requirements: Requirement[]                         │ │
│  │  - filters: { level: string[], category: string[] }   │ │
│  │  - checkedItems: Set<string>                           │ │
│  │  - notes: Map<string, string>                          │ │
│  └────────────────────────────────────────────────────────┘ │
│                              │                               │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Browser localStorage (Persistence)                    │ │
│  │  Key: "isvs-tool-state"                                │ │
│  │  Value: JSON-serialized state (auto-save on change)   │ │
│  └────────────────────────────────────────────────────────┘ │
└─────────────────────────────────────────────────────────────┘
```

### 2.3 Data Flow

```
1. Initial Load:
   GitHub Pages → isvs-data.json → Parse → Zustand Store → React Render

2. User Interaction (Check Requirement):
   User Click → Update Store → Sync to localStorage → Re-render UI

3. Filter Application:
   Filter Change → Compute Filtered Requirements → Update Display

4. Export Report:
   Export Button → Gather State → Generate CSV/JSON → Download File

5. Deep Link (Share Requirement):
   URL: /isvs-tool?req=V2.1.3 → Parse URL → Highlight Requirement → Scroll Into View
```

### 2.4 Component Hierarchy

```
App (Router)
├── Header
│   ├── Logo (OWASP branding)
│   ├── Title ("ISVS Interactive Tool")
│   └── ThemeToggle (Dark/Light mode)
│
├── FilterBar
│   ├── LevelFilter (L1/L2/L3 checkboxes)
│   ├── CategoryFilter (V1-V5 buttons)
│   ├── SearchInput (text search)
│   └── ClearFilters (reset button)
│
├── ProgressDashboard
│   ├── OverallProgress (circular chart: X/165 complete)
│   ├── CategoryProgress (V1: 12/26, V2: 8/22, etc.)
│   └── LevelBreakdown (L1: 80%, L2: 40%, L3: 10%)
│
├── RequirementsList
│   ├── CategorySection (V1, V2, V3, V4, V5)
│   │   ├── CategoryHeader (collapsible)
│   │   └── RequirementItem[]
│   │       ├── Checkbox (checked state)
│   │       ├── RequirementID (e.g., "V2.1.3")
│   │       ├── LevelBadges (L1 L2 L3)
│   │       ├── Description (full text)
│   │       ├── NotesField (user annotations)
│   │       └── ShareButton (copy deep link)
│
└── ExportPanel
    ├── ExportCSV (download CSV)
    ├── ExportJSON (download JSON)
    ├── PrintReport (printable compliance cert)
    └── ResetProgress (clear all data)
```

---

## 3. Feature Specifications

### 3.1 Core Features (MVP - Phase 1)

#### F1: Interactive Checklist
**Description**: Click to mark requirements as verified/completed.

**User Story**: "As a security auditor, I want to check off requirements as I verify them, so I can track my progress."

**Acceptance Criteria**:
- [ ] Each requirement has a checkbox
- [ ] Clicking checkbox toggles checked state (visual feedback within 100ms)
- [ ] Checked state persists in localStorage
- [ ] Checked items have visual indicator (checkmark icon, strikethrough text)
- [ ] Undo capability (unchecking reverts state)

**Technical Implementation**:
```typescript
interface Requirement {
  id: string;           // e.g., "V2.1.3"
  description: string;  // Full requirement text
  l1: boolean;          // Applies to Level 1
  l2: boolean;          // Applies to Level 2
  l3: boolean;          // Applies to Level 3
  category: string;     // "V1", "V2", etc.
}

interface ChecklistState {
  checkedItems: Set<string>;  // Set of checked requirement IDs
  toggleCheck: (id: string) => void;
}
```

#### F2: Smart Filtering
**Description**: Filter requirements by level, category, or search text.

**User Story**: "As an IoT developer, I want to see only L1 requirements for my basic device, so I don't waste time on irrelevant L3 items."

**Acceptance Criteria**:
- [ ] Level filter: L1, L2, L3 (multi-select checkboxes)
- [ ] Category filter: V1-V5 (button group, multi-select)
- [ ] Text search: Real-time filtering (debounced 300ms)
- [ ] Combined filters: AND logic (e.g., "L2 AND V4 AND 'Bluetooth'")
- [ ] Filter persistence: Saved to URL query params
- [ ] Clear all filters button
- [ ] Display count: "Showing 42 of 165 requirements"

**Technical Implementation**:
```typescript
interface FilterState {
  levels: Set<'L1' | 'L2' | 'L3'>;
  categories: Set<'V1' | 'V2' | 'V3' | 'V4' | 'V5'>;
  searchText: string;
}

const filterRequirements = (reqs: Requirement[], filters: FilterState) => {
  return reqs.filter(req => {
    const matchesLevel = filters.levels.size === 0 ||
      [...filters.levels].some(l => req[l.toLowerCase()]);
    const matchesCategory = filters.categories.size === 0 ||
      filters.categories.has(req.category);
    const matchesSearch = filters.searchText === '' ||
      req.description.toLowerCase().includes(filters.searchText.toLowerCase());
    return matchesLevel && matchesCategory && matchesSearch;
  });
};
```

#### F3: Progress Tracking
**Description**: Visual dashboards showing completion percentage.

**User Story**: "As a compliance manager, I want to see overall progress at a glance, so I can report status to executives."

**Acceptance Criteria**:
- [ ] Overall progress: Circular chart (e.g., "85/165 (51%)")
- [ ] Category breakdown: V1 (12/26), V2 (22/22), etc.
- [ ] Level breakdown: L1 (80%), L2 (40%), L3 (10%)
- [ ] Color coding: Red (<30%), Yellow (30-70%), Green (>70%)
- [ ] Progress persists across sessions

**Visual Design**:
```
┌─────────────────────────────────────┐
│      Overall Progress: 51%          │
│        ●●●●●●●●○○ 85/165            │
├─────────────────────────────────────┤
│  V1: IoT Ecosystem        ▓▓▓░░ 46% │
│  V2: User Space Apps      ▓▓▓▓░ 68% │
│  V3: Software Platform    ▓▓░░░ 32% │
│  V4: Communication        ▓▓▓▓▓ 91% │
│  V5: Hardware Platform    ▓░░░░ 15% │
└─────────────────────────────────────┘
```

#### F4: Export & Reporting
**Description**: Generate compliance reports in multiple formats.

**User Story**: "As a security auditor, I want to export my completed checklist as a CSV, so I can attach it to my audit report."

**Acceptance Criteria**:
- [ ] Export CSV: ID, Description, Level, Status (✓/✗), Notes
- [ ] Export JSON: Full state including timestamps
- [ ] Print view: Formatted compliance certificate (CSS @media print)
- [ ] Include metadata: Export date, total/completed counts
- [ ] Filename format: `ISVS_Audit_YYYY-MM-DD.csv`

**CSV Output Format**:
```csv
ID,Description,L1,L2,L3,Status,Notes,Completed Date
V1.1.1,"Verify that the IoT system is developed...",✓,✓,✓,Completed,"Verified in design review",2025-10-05
V1.1.2,"Verify that all components and communication...",✓,✓,✓,Pending,,
```

#### F5: Deep Linking & Sharing
**Description**: Shareable URLs for specific requirements or filter states.

**User Story**: "As a team lead, I want to share a link to requirement V2.1.3 with my developer, so they know exactly which item to address."

**Acceptance Criteria**:
- [ ] URL format: `/isvs-tool?req=V2.1.3`
- [ ] Auto-scroll to highlighted requirement on load
- [ ] Filter state in URL: `/isvs-tool?level=L2&category=V4`
- [ ] Copy link button next to each requirement
- [ ] Toast notification: "Link copied to clipboard"

### 3.2 Enhanced Features (Phase 2 - Future)

#### F6: User Notes & Annotations
- Inline notes field for each requirement
- Markdown support for rich formatting
- Notes saved to localStorage
- Export notes in CSV/JSON

#### F7: Team Collaboration (LocalStorage Sync)
- Export state as JSON blob
- Import teammate's state
- Merge states (union of checked items)

#### F8: Compliance Templates
- Pre-configured filters for common device types:
  - Smart Home L1 (bulbs, switches)
  - Medical IoT L3 (implants, monitors)
  - Industrial L2 (sensors, controllers)

---

## 4. Accessibility & Usability

### 4.1 WCAG 2.1 Level AA Compliance

| Guideline | Implementation | Testing Method |
|-----------|----------------|----------------|
| **1.4.3 Contrast** | Text contrast ratio ≥ 4.5:1 (normal), ≥ 3:1 (large) | Automated: axe DevTools |
| **2.1.1 Keyboard** | All interactive elements accessible via Tab/Enter/Space | Manual: Navigate without mouse |
| **2.4.7 Focus Visible** | Blue outline (2px solid) on focused elements | Manual: Tab through interface |
| **3.1.1 Language** | `<html lang="en">` attribute set | Automated: Lighthouse |
| **4.1.2 Name, Role, Value** | Semantic HTML, ARIA labels where needed | Automated: axe DevTools |

**Screen Reader Support**:
- Requirement count announcements: "85 of 165 requirements completed"
- Filter changes: "Filtered to 42 requirements matching Level 2"
- Checkbox state: "Requirement V2.1.3, verified, checkbox checked"

**Keyboard Shortcuts**:
- `Ctrl/Cmd + K`: Focus search bar
- `Ctrl/Cmd + E`: Open export menu
- `Ctrl/Cmd + F`: Toggle filter panel
- `Escape`: Close modals/panels

### 4.2 Mobile Responsiveness

**Breakpoints**:
- Desktop: ≥ 1024px (3-column layout: filters | checklist | progress)
- Tablet: 768-1023px (2-column: checklist | sidebar)
- Mobile: < 768px (1-column: stacked, bottom nav)

**Mobile Optimizations**:
- Bottom navigation bar (filters, export, progress)
- Swipe gestures (swipe right = check, swipe left = uncheck)
- Touch-friendly checkboxes (44x44px minimum)
- Collapsible category sections (accordion)

### 4.3 Performance Targets

| Metric | Target | Measurement Tool |
|--------|--------|------------------|
| **First Contentful Paint** | < 1.5s | Lighthouse |
| **Time to Interactive** | < 3.0s | Lighthouse |
| **Largest Contentful Paint** | < 2.5s | Lighthouse |
| **Cumulative Layout Shift** | < 0.1 | Lighthouse |
| **Total Bundle Size** | < 200 KB (uncompressed) | Webpack Bundle Analyzer |
| **Filtering Latency** | < 100ms (for 165 items) | React DevTools Profiler |

**Optimization Techniques**:
- Code splitting: Lazy load export functionality
- Virtual scrolling: Render only visible requirements (react-window)
- Debounced search: 300ms delay
- Memoization: useMemo for filtered results
- Service worker: Cache static assets

---

## 5. Free Hosting Strategy (GitHub Pages)

### 5.1 GitHub Pages Configuration

**Repository Structure**:
```
IoT-Security-Verification-Standard-ISVS/
├── docs/                  # GitHub Pages root (existing)
│   └── isvs-tool/        # Tool deployment target
│       ├── index.html
│       ├── assets/
│       │   ├── index-[hash].js
│       │   ├── index-[hash].css
│       │   └── isvs-data.json
│       └── 404.html      # SPA fallback
├── webapp/               # Source code
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── vite.config.ts
└── .github/
    └── workflows/
        └── deploy-tool.yml
```

**Vite Build Configuration** (`webapp/vite.config.ts`):
```typescript
export default defineConfig({
  base: '/IoT-Security-Verification-Standard-ISVS/isvs-tool/',
  build: {
    outDir: '../docs/isvs-tool',
    emptyOutDir: true,
  },
});
```

### 5.2 CI/CD Workflow (GitHub Actions)

**Workflow**: `.github/workflows/deploy-tool.yml`

```yaml
name: Deploy ISVS Tool

on:
  push:
    branches: [main, isvs-tool]
    paths:
      - 'webapp/**'
      - 'tools/export.py'
      - '.github/workflows/deploy-tool.yml'

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Generate ISVS Data JSON
        run: |
          cd tools
          python3 export.py -f json -l en -o ../webapp/public/isvs-data

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
          cache: 'npm'
          cache-dependency-path: webapp/package-lock.json

      - name: Install Dependencies
        run: cd webapp && npm ci

      - name: Build
        run: cd webapp && npm run build

      - name: Deploy to GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./docs/isvs-tool
          destination_dir: isvs-tool
          keep_files: true  # Preserve existing docs
```

**Deployment URL**:
`https://owasp.org/IoT-Security-Verification-Standard-ISVS/isvs-tool/`

**Cost**: **$0.00** (GitHub Pages is free for public repos)

### 5.3 Automatic Data Updates

**Trigger**: Any change to `en/V*.md` files automatically regenerates `isvs-data.json`

```yaml
on:
  push:
    paths:
      - 'en/V*.md'  # Requirement files changed
```

**Data Generation Step**:
```bash
cd tools
python3 export.py -f json -l en -o ../webapp/public/isvs-data
```

This ensures the tool always reflects the latest ISVS requirements.

---

## 6. Visual Design & Branding

### 6.1 OWASP Brand Consistency

**Colors** (from existing ISVS docs):
```css
:root {
  /* Primary */
  --owasp-blue: #2C3E50;
  --owasp-light-blue: #3498DB;

  /* Levels */
  --level-1: #27AE60;  /* Green - L1 Basic */
  --level-2: #F39C12;  /* Orange - L2 Medium */
  --level-3: #E74C3C;  /* Red - L3 High */

  /* Status */
  --completed: #2ECC71;
  --pending: #95A5A6;

  /* Dark Mode */
  --dark-bg: #1E1E1E;
  --dark-text: #E0E0E0;
}
```

**Typography**:
- Headings: Inter (sans-serif, weights: 600, 700)
- Body: Inter (weights: 400, 500)
- Code: JetBrains Mono (monospace, for requirement IDs)

**Logo Usage**:
- OWASP logo in header (existing SVG from `en/images/owasp_logo.png`)
- "IoT Security Verification Standard" wordmark
- Footer: "Powered by OWASP | CC BY-SA 4.0"

### 6.2 UI Mockup (Desktop)

```
┌─────────────────────────────────────────────────────────────────────┐
│  [OWASP Logo]  ISVS Interactive Tool                     [🌙 Dark]  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │ 🔍 Search requirements...                                    │   │
│  └─────────────────────────────────────────────────────────────┘   │
│                                                                       │
│  Security Level:  [ ] L1  [ ] L2  [ ] L3      Clear Filters          │
│  Category:        [V1] [V2] [V3] [V4] [V5]                           │
│                                                                       │
│  ┌───────────────────────────────────┐  ┌──────────────────────┐   │
│  │ ▼ V1: IoT Ecosystem (12/26) 46%  │  │  Overall Progress    │   │
│  │                                   │  │                      │   │
│  │ □ V1.1.1 Verify that the IoT     │  │      ●●●●●○○○○○      │   │
│  │   system is developed with...     │  │     85/165 (51%)     │   │
│  │   [L1][L2][L3] 🔗 Share          │  │                      │   │
│  │                                   │  │  V1: ▓▓▓░░ 46%      │   │
│  │ ☑ V1.1.2 Verify that all         │  │  V2: ▓▓▓▓░ 68%      │   │
│  │   components and communication... │  │  V3: ▓▓░░░ 32%      │   │
│  │   [L1][L2][L3] 🔗 Share          │  │  V4: ▓▓▓▓▓ 91%      │   │
│  │   Notes: Verified in Sprint 3    │  │  V5: ▓░░░░ 15%      │   │
│  │                                   │  │                      │   │
│  │ ▼ V2: User Space Apps (22/22)    │  │ [Export CSV]         │   │
│  │   ...                             │  │ [Export JSON]        │   │
│  └───────────────────────────────────┘  │ [Print Report]       │   │
│                                          └──────────────────────┘   │
│                                                                       │
│  Showing 85 of 165 requirements                                      │
└─────────────────────────────────────────────────────────────────────┘
```

### 6.3 Dark Mode Design

**Auto-detection**: Respect `prefers-color-scheme` media query
**Toggle**: Persistent localStorage preference

**Dark Mode Palette**:
```css
[data-theme="dark"] {
  --bg-primary: #1E1E1E;
  --bg-secondary: #2D2D2D;
  --text-primary: #E0E0E0;
  --text-secondary: #A0A0A0;
  --border: #404040;
}
```

---

## 7. Reporting Capabilities

### 7.1 Export Formats

#### CSV Export
**Filename**: `ISVS_Compliance_Report_2025-10-05.csv`

**Columns**:
```csv
Requirement ID,Category,Description,Level 1,Level 2,Level 3,Status,Notes,Completed Date,Completed By
V1.1.1,V1: IoT Ecosystem,Verify that the IoT system is developed with...,✓,✓,✓,Completed,"Verified via design review",2025-10-05,sarah@example.com
V1.1.2,V1: IoT Ecosystem,Verify that all components and communication...,✓,✓,✓,Pending,,,
```

**Use Case**: Import to Excel, Jira, or compliance management tools.

#### JSON Export
**Filename**: `ISVS_State_2025-10-05.json`

```json
{
  "version": "1.0",
  "exportDate": "2025-10-05T14:30:00Z",
  "totalRequirements": 165,
  "completedCount": 85,
  "completionPercentage": 51.5,
  "checkedItems": ["V1.1.1", "V1.1.2", ...],
  "notes": {
    "V1.1.1": "Verified via design review",
    "V2.1.3": "See ticket JIRA-123"
  },
  "completionTimestamps": {
    "V1.1.1": "2025-10-05T10:15:00Z"
  }
}
```

**Use Case**: Backup state, share with team, import to another browser.

### 7.2 Compliance Certificate (Print View)

**Trigger**: Click "Print Report" or Ctrl+P

**CSS** (`@media print`):
```css
@media print {
  .no-print { display: none; } /* Hide filters, export buttons */
  .requirement { page-break-inside: avoid; }
  .category-section { page-break-after: always; }
}
```

**Output** (Page 1):
```
┌────────────────────────────────────────────────────────────┐
│               OWASP IoT Security Verification Standard      │
│                      Compliance Certificate                 │
│                                                             │
│  Product: Smart Camera X200                                │
│  Security Level: L2                                        │
│  Audit Date: October 5, 2025                               │
│  Auditor: Sarah Johnson (sarah@example.com)                │
│                                                             │
│  ──────────────────────────────────────────────────────   │
│                                                             │
│  Overall Compliance: 85/165 (51%)                          │
│                                                             │
│  Category Breakdown:                                        │
│    ✓ V1: IoT Ecosystem Requirements       12/26 (46%)     │
│    ✓ V2: User Space Applications          22/22 (100%)    │
│    ✓ V3: Software Platform                18/32 (56%)     │
│    ✓ V4: Communication                    28/31 (90%)     │
│    ✓ V5: Hardware Platform                5/16 (31%)      │
│                                                             │
│  ──────────────────────────────────────────────────────   │
│                                                             │
│  Verified Requirements:                                     │
│  V1.1.1 ✓ Verify that the IoT system is developed...      │
│          Notes: Verified in design review                  │
│                                                             │
│  V1.1.2 ✓ Verify that all components and...               │
│          Notes: Architecture diagram reviewed              │
│  ...                                                        │
└────────────────────────────────────────────────────────────┘
```

### 7.3 Report Customization

**Filters Applied to Report**:
- If filters active (e.g., L2 only), report shows: "Report Scope: Level 2 Requirements Only (98 total)"
- Include filter state in filename: `ISVS_L2_Report_2025-10-05.csv`

**Metadata Included**:
- Export timestamp
- ISVS version (1.0)
- Tool version (e.g., "v1.2.0")
- Browser info (for debugging state issues)

---

## 8. Build Workflow & Developer Documentation

### 8.1 Project Structure

```
webapp/
├── public/
│   ├── isvs-data.json          # Generated by tools/export.py
│   └── favicon.ico
│
├── src/
│   ├── main.tsx                # Entry point
│   ├── App.tsx                 # Root component
│   │
│   ├── components/
│   │   ├── Header.tsx
│   │   ├── FilterBar.tsx
│   │   ├── ProgressDashboard.tsx
│   │   ├── RequirementsList.tsx
│   │   ├── RequirementItem.tsx
│   │   └── ExportPanel.tsx
│   │
│   ├── stores/
│   │   └── useISVSStore.ts     # Zustand store
│   │
│   ├── utils/
│   │   ├── filterRequirements.ts
│   │   ├── exportCSV.ts
│   │   ├── exportJSON.ts
│   │   └── deepLink.ts
│   │
│   ├── types/
│   │   └── requirement.ts      # TypeScript interfaces
│   │
│   └── styles/
│       └── globals.css         # Tailwind imports
│
├── package.json
├── tsconfig.json
├── vite.config.ts
├── tailwind.config.js
└── README.md
```

### 8.2 Development Workflow

**Prerequisites**:
- Node.js 20+ (LTS)
- npm 10+
- Python 3.9+ (for data generation)

**Setup**:
```bash
# 1. Generate ISVS data
cd tools
python3 export.py -f json -l en -o ../webapp/public/isvs-data

# 2. Install dependencies
cd ../webapp
npm install

# 3. Start dev server
npm run dev
# → http://localhost:5173/isvs-tool/
```

**Build**:
```bash
npm run build
# Output: ../docs/isvs-tool/
```

**Preview Production Build**:
```bash
npm run preview
# → http://localhost:4173/isvs-tool/
```

### 8.3 npm Scripts

**package.json**:
```json
{
  "scripts": {
    "dev": "vite --open",
    "build": "tsc && vite build",
    "preview": "vite preview",
    "lint": "eslint src --ext ts,tsx",
    "format": "prettier --write 'src/**/*.{ts,tsx,css}'",
    "test": "vitest",
    "generate-data": "cd ../tools && python3 export.py -f json -l en -o ../webapp/public/isvs-data"
  }
}
```

### 8.4 Code Quality Standards

**ESLint** (`.eslintrc.json`):
```json
{
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:react-hooks/recommended"
  ],
  "rules": {
    "no-console": "warn",
    "@typescript-eslint/no-unused-vars": "error"
  }
}
```

**Prettier** (`.prettierrc`):
```json
{
  "semi": true,
  "singleQuote": true,
  "tabWidth": 2,
  "printWidth": 100
}
```

**Git Hooks** (via Husky):
```bash
# Pre-commit
npm run lint
npm run format

# Pre-push
npm run build  # Ensure production build succeeds
```

---

## 9. Testing Strategy

### 9.1 Unit Tests (Vitest)

**Coverage Target**: ≥ 80%

**Test Files**:
```
src/
├── utils/
│   ├── filterRequirements.test.ts
│   ├── exportCSV.test.ts
│   └── deepLink.test.ts
├── stores/
│   └── useISVSStore.test.ts
```

**Example Test**:
```typescript
// filterRequirements.test.ts
import { filterRequirements } from './filterRequirements';

describe('filterRequirements', () => {
  it('filters by L2 level', () => {
    const reqs = [
      { id: 'V1.1.1', l1: true, l2: true, l3: false, ... },
      { id: 'V1.1.2', l1: true, l2: false, l3: false, ... },
    ];
    const filters = { levels: new Set(['L2']), categories: new Set(), searchText: '' };
    const result = filterRequirements(reqs, filters);
    expect(result).toHaveLength(1);
    expect(result[0].id).toBe('V1.1.1');
  });
});
```

### 9.2 Integration Tests (React Testing Library)

**Test Scenarios**:
- [ ] Check requirement → State updates → localStorage synced
- [ ] Apply filter → Display count updates
- [ ] Export CSV → File downloads with correct data
- [ ] Deep link → Requirement highlighted and scrolled into view

**Example Test**:
```typescript
import { render, screen, fireEvent } from '@testing-library/react';
import { App } from './App';

test('checking a requirement persists to localStorage', () => {
  render(<App />);
  const checkbox = screen.getByLabelText(/V1.1.1/);
  fireEvent.click(checkbox);

  expect(checkbox).toBeChecked();
  const state = JSON.parse(localStorage.getItem('isvs-tool-state')!);
  expect(state.checkedItems).toContain('V1.1.1');
});
```

### 9.3 E2E Tests (Playwright)

**Critical User Flows**:
1. **Audit Workflow**: Load → Filter L2 → Check 5 requirements → Export CSV
2. **Share Workflow**: Open deep link → Verify requirement highlighted
3. **Persistence**: Check items → Reload page → Verify state restored

**Example Test**:
```typescript
test('audit workflow', async ({ page }) => {
  await page.goto('/isvs-tool/');
  await page.click('text=L2');  // Filter to L2
  await expect(page.locator('.requirement')).toHaveCount(98);

  await page.click('input[aria-label*="V2.1.1"]');
  await page.click('button:has-text("Export CSV")');

  const download = await page.waitForEvent('download');
  expect(download.suggestedFilename()).toMatch(/ISVS_.*\.csv/);
});
```

### 9.4 Accessibility Tests

**Automated** (axe-core via vitest-axe):
```typescript
import { render } from '@testing-library/react';
import { axe } from 'vitest-axe';

test('no accessibility violations', async () => {
  const { container } = render(<App />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});
```

**Manual Checklist**:
- [ ] Keyboard navigation (Tab, Enter, Space, Arrow keys)
- [ ] Screen reader announcements (NVDA, VoiceOver)
- [ ] Color contrast (WebAIM Contrast Checker)
- [ ] Focus indicators visible

---

## 10. README Documentation

### 10.1 User-Facing README (`webapp/README.md`)

```markdown
# ISVS Interactive Tool

🚀 **Live Demo**: https://owasp.org/IoT-Security-Verification-Standard-ISVS/isvs-tool/

An interactive web application for the OWASP IoT Security Verification Standard (ISVS). Track your IoT security verification progress with an easy-to-use checklist interface.

## ✨ Features

- ✅ **Interactive Checklist** - Mark requirements as completed
- 🔍 **Smart Filtering** - Filter by security level (L1/L2/L3) and category (V1-V5)
- 📊 **Progress Tracking** - Visual dashboards showing completion status
- 💾 **Auto-Save** - Progress saved to browser localStorage
- 📄 **Export Reports** - Generate CSV/JSON compliance reports
- 🔗 **Deep Linking** - Share specific requirements via URL
- 📱 **Mobile-Friendly** - Responsive design for on-site testing
- 🌙 **Dark Mode** - Easy on the eyes

## 🎯 Quick Start

1. **Open the tool**: [Launch ISVS Tool](https://owasp.org/IoT-Security-Verification-Standard-ISVS/isvs-tool/)
2. **Filter requirements**: Select your device's security level (L1, L2, or L3)
3. **Start verification**: Check off requirements as you verify them
4. **Export report**: Download your compliance report as CSV or JSON

## 📖 How to Use

### For Security Auditors
1. Filter to the appropriate security level for the device under audit
2. Check requirements as you verify them during testing
3. Add notes to document evidence (e.g., "Verified in test case TC-001")
4. Export CSV report to attach to your audit documentation

### For IoT Developers
1. Filter to requirements applicable to your device (e.g., L1 for basic devices)
2. Use as a checklist during development sprints
3. Export filtered requirements as CSV to import into Jira/GitHub Issues

### For Compliance Managers
1. View overall progress across all categories
2. Generate compliance certificates for stakeholder reporting
3. Share deep links to specific requirements with team members

## 🔧 Technical Details

- **Framework**: React 18 + TypeScript
- **Build Tool**: Vite
- **Styling**: Tailwind CSS
- **State Management**: Zustand
- **Data Source**: Auto-generated from ISVS markdown files
- **Hosting**: GitHub Pages (free)
- **Bundle Size**: ~120 KB (gzipped: ~40 KB)

## 📋 Data Privacy

All data is stored **locally in your browser** (localStorage). Nothing is sent to any server. Your progress is private and persists across sessions on the same device.

## 🤝 Contributing

Found a bug or have a feature request?
- [Open an Issue](https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/issues)
- [Submit a Pull Request](https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/pulls)

## 📄 License

This tool is part of the OWASP ISVS project and is licensed under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/).
```

### 10.2 Developer README (`webapp/DEVELOPMENT.md`)

```markdown
# ISVS Tool - Development Guide

## Prerequisites

- Node.js 20+ (LTS)
- npm 10+
- Python 3.9+ (for data generation)

## Setup

### 1. Generate ISVS Data

The tool requires `isvs-data.json` generated from the markdown files:

```bash
cd tools
python3 export.py -f json -l en -o ../webapp/public/isvs-data
```

### 2. Install Dependencies

```bash
cd webapp
npm install
```

### 3. Start Development Server

```bash
npm run dev
```

Opens at http://localhost:5173/isvs-tool/

## Scripts

| Script | Description |
|--------|-------------|
| `npm run dev` | Start dev server with HMR |
| `npm run build` | Build for production → `../docs/isvs-tool/` |
| `npm run preview` | Preview production build locally |
| `npm run lint` | Run ESLint |
| `npm run format` | Format code with Prettier |
| `npm test` | Run unit tests (Vitest) |
| `npm run generate-data` | Re-generate ISVS data from markdown |

## Project Structure

```
src/
├── components/     # React components
├── stores/         # Zustand state stores
├── utils/          # Helper functions
├── types/          # TypeScript interfaces
└── styles/         # Global CSS
```

## State Management

Uses Zustand with localStorage persistence:

```typescript
import { create } from 'zustand';
import { persist } from 'zustand/middleware';

const useISVSStore = create(
  persist(
    (set) => ({
      checkedItems: new Set<string>(),
      toggleCheck: (id: string) => set((state) => {
        const newChecked = new Set(state.checkedItems);
        newChecked.has(id) ? newChecked.delete(id) : newChecked.add(id);
        return { checkedItems: newChecked };
      }),
    }),
    { name: 'isvs-tool-state' }
  )
);
```

## Building for Production

```bash
npm run build
```

Output: `../docs/isvs-tool/` (deployed to GitHub Pages)

## Deployment

Automatic via GitHub Actions on push to `main` or `isvs-tool` branches:

1. Generates `isvs-data.json` from markdown
2. Builds React app
3. Deploys to GitHub Pages

See `.github/workflows/deploy-tool.yml`

## Testing

```bash
# Unit tests
npm test

# Coverage report
npm test -- --coverage

# E2E tests (requires Playwright installed)
npm run test:e2e
```

## Code Style

- **ESLint**: `npm run lint`
- **Prettier**: `npm run format`
- **Pre-commit hook**: Auto-formats on commit (Husky)

## Troubleshooting

### Data not loading
- Ensure `public/isvs-data.json` exists
- Run `npm run generate-data`

### localStorage issues
- Check browser dev tools → Application → Local Storage
- Clear state: `localStorage.removeItem('isvs-tool-state')`

### Build errors
- Clear cache: `rm -rf node_modules .vite && npm install`
```

---

## 11. Success Metrics & KPIs

### 11.1 Adoption Metrics (6 months post-launch)

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Monthly Active Users** | 500+ | Google Analytics |
| **Average Session Duration** | 15+ minutes | GA (indicates active use vs bounce) |
| **Export/Download Actions** | 200+/month | Event tracking |
| **Deep Link Shares** | 100+/month | Link click tracking |
| **Mobile Traffic** | 30%+ | Device breakdown |

### 11.2 User Satisfaction

| Metric | Target | Measurement |
|--------|--------|-------------|
| **GitHub Stars** | 100+ | Repository metrics |
| **Positive Feedback** | 80%+ | Issues/discussions sentiment analysis |
| **Feature Requests** | 10+/quarter | GitHub issues tagged "enhancement" |
| **Bug Reports** | <5/month | GitHub issues tagged "bug" |

### 11.3 Technical Performance

| Metric | Target | Measurement |
|--------|--------|-------------|
| **Lighthouse Score** | 95+ | Automated CI checks |
| **Uptime** | 99.9%+ | GitHub Pages status |
| **Build Success Rate** | 100% | GitHub Actions history |
| **Zero-Cost Hosting** | $0/month | AWS bill (should be $0) |

---

## 12. Future Roadmap (Post-MVP)

### Phase 2 (Q1 2026)
- **Multi-language support**: Spanish, French, German translations
- **Offline mode**: Service worker for full offline functionality
- **Custom requirement sets**: User-defined requirement groups
- **JIRA/GitHub integration**: One-click export to issue trackers

### Phase 3 (Q2 2026)
- **Team collaboration**: Real-time sync via WebRTC or Firebase
- **AI assistant**: GPT-powered requirement interpretation
- **Compliance mapping**: Map ISVS to NIST, ISO 27001, etc.
- **Automated testing**: Generate test cases from requirements

### Phase 4 (Q3 2026)
- **Mobile app**: React Native iOS/Android app
- **Browser extension**: Quick ISVS lookup from any page
- **API**: RESTful API for programmatic access
- **Certification program**: Official ISVS certification workflow

---

## 13. Approval Checklist

### Pre-Implementation Review

- [ ] **Value Proposition Validated**: Stakeholders agree this solves adoption barriers
- [ ] **Technical Stack Approved**: React + Vite + TypeScript + Tailwind accepted
- [ ] **Zero-Cost Hosting Confirmed**: GitHub Pages strategy approved
- [ ] **Accessibility Requirements Clear**: WCAG 2.1 AA compliance mandated
- [ ] **Data Privacy Addressed**: localStorage-only approach acceptable
- [ ] **Success Metrics Defined**: KPIs for 6-month post-launch agreed upon

### Implementation Readiness

- [ ] **Specifications Document Reviewed**: This document approved by project leads
- [ ] **README Documentation Drafted**: User and developer guides ready
- [ ] **Build Workflow Designed**: CI/CD pipeline architecture finalized
- [ ] **Timeline Estimated**: 6-8 hour implementation schedule realistic

---

## 14. Contact & Support

**Project Leads**:
- Cédric Bassem: cedric.bassem@owasp.org
- Aaron Guzman: aaron.guzman@owasp.org

**Developer**:
- [Your Name/Team]

**Support Channels**:
- GitHub Issues: https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/issues
- OWASP Slack: #project-isvs

---

## Appendix A: Competitive Analysis

| Tool | Platform | Interactivity | Cost | Limitations |
|------|----------|---------------|------|-------------|
| **OWASP ASVS Web App** | Django | High (project mgmt) | Free | Requires backend, harder to deploy |
| **OWASP MASVS Checklist** | Web (static?) | Medium (checkboxes) | Free | No state persistence mentioned |
| **Excel/CSV Approach** | Desktop | Low (manual) | Free | No filtering, poor UX |
| **PDF Workflow** | Desktop | None | Free | No tracking, print/highlight only |
| **ISVS Tool (Proposed)** | Web (SPA) | High (filters, export, deep links) | Free | **Requires browser** |

**Conclusion**: ISVS Tool offers best-in-class interactivity with zero infrastructure costs, bridging the gap between static PDFs and complex Django apps.

---

## Appendix B: Risk Analysis

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| **localStorage limit (5-10 MB)** | Low | Medium | ISVS data ~30 KB, user state ~10 KB = well under limit |
| **Browser compatibility issues** | Low | Medium | Target modern browsers (Chrome 90+, Firefox 88+, Safari 14+) |
| **GitHub Pages downtime** | Very Low | Low | 99.9% uptime SLA, static fallback available |
| **Data loss (localStorage cleared)** | Medium | Low | Export/import functionality, warn users before clear |
| **Accessibility non-compliance** | Low | High | Automated testing (axe), manual WCAG audit pre-launch |
| **Low adoption** | Medium | High | Marketing via OWASP channels, integrate into main docs |

---

**Document End**

**Next Steps**:
1. Review and approve this specification
2. Create `webapp/README.md` (development guide)
3. Begin implementation (Phase 1: Project Setup)

**Estimated Reading Time**: 30 minutes
**Estimated Implementation Time**: 6-8 hours (for experienced React developer)
