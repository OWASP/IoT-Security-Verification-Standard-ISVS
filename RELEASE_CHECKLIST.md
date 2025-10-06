# OWASP ISVS 1.0 Official Release Checklist

**Release Version**: 1.0
**Target Date**: October 2025
**Last Updated**: October 5, 2025

---

## ✅ Completed Tasks

### Documentation & Content
- [x] **165 Security Requirements** documented across 5 categories (V1-V5)
- [x] **CHANGELOG.md** - Comprehensive changelog created
- [x] **RELEASE_NOTES.md** - Detailed release notes prepared
- [x] **Using_ISVS.md** - "Handling Non-Conformities" section added (Issue #63)
- [x] **Contributors recognition** - CONTRIBUTORS.md created
- [x] **README.md** - Updated with release badges and links

### Requirements Enhancements (Based on Community Feedback)
- [x] **Issue #55** - Fixed numbering gaps (3.3.3, 4.1.5)
- [x] **Issue #63** - Added guidance on handling non-conformities
- [x] **Issue #82** - Enhanced Bluetooth/WiFi L3 requirements
  - BT 5.3+ for L3 with 128-bit encryption enforcement
  - WPA3 requirement for L3 WiFi
  - Comprehensive research documented in BLUETOOTH_RESEARCH_SUMMARY.md
- [x] **Issue #86** - Added Incident Response section (V1.5)
  - 3 new requirements (1.5.1-1.5.3)
- [x] **Issue #88** - Added anti-bruteforce & reauthentication
  - Requirements 2.1.12 and 2.1.13
- [x] **Post-Quantum Cryptography (PQC)** - 7 new L3 requirements
  - Requirements 2.4.7-2.4.8, 3.1.9, 3.4.13, 4.1.7-4.1.8, 5.1.13
  - Aligns with NIST timeline and regulatory requirements

### Infrastructure & Build System
- [x] **GitHub Pages** - Migration from GitBook complete
  - Jekyll configuration (_config.yaml)
  - GitHub Actions workflow (.github/workflows/pages.yml)
  - Professional landing page (index.md)
  - All markdown files have YAML front matter
- [x] **Build Pipeline** - Automated document generation
  - PDF, EPUB, DOCX generation (pandoc)
  - CSV, JSON, XML export (Python tools)
  - GitHub Actions workflows operational
- [x] **Dependencies** - Gemfile.lock generated for reproducible builds
- [x] **Export Tools** - Verified working (CSV, JSON, XML)

### Quality Assurance
- [x] **External Links** - Verified all documentation URLs work
- [x] **Requirement Count** - Verified 165 requirements parse correctly
- [x] **Sequential Numbering** - All requirements numbered correctly

---

## ⏳ Pending Tasks (BLOCKERS for 1.0 Tag)

### Critical Path to Release

#### 1. **ISVS Overview Figure** (High Priority)
**Status**: ⚠️ BLOCKER
**Issue**: #65
**Action Required**:
- [ ] Generate new professional ISVS overview diagram
- [ ] Replace en/images/ISVS-Overview-small.png
- [ ] Update Using_ISVS.md to reference new figure
- [ ] Commit separately before tagging 1.0

**Rationale**: Current figure is outdated. windBlaze provided updated design in Issue #65 comments (Dec 2022), but team decided to create a new one instead for 1.0.

#### 2. **GitHub Pages Verification**
**Status**: 🔍 Needs Verification
**Action Required**:
- [ ] Verify GitHub Pages is enabled in repository settings
- [ ] Confirm Pages source set to "GitHub Actions"
- [ ] Test site deployment at https://owasp.org/IoT-Security-Verification-Standard-ISVS/
- [ ] Verify search functionality works
- [ ] Check mobile responsiveness

**Technical Details**:
- Workflow file exists: `.github/workflows/pages.yml`
- Configuration exists: `_config.yaml`, `Gemfile`
- Content ready: All .md files have YAML front matter

#### 3. **Release Build Test**
**Status**: ⚠️ Needs Testing
**Action Required**:
- [ ] Test Docker image: `owaspisvs/isvs-docgenerator:latest`
- [ ] Run local build test for all 6 formats
- [ ] Verify pandoc generates PDF/EPUB/DOCX correctly
- [ ] Confirm export.py generates valid CSV/JSON/XML

**Commands to Test**:
```bash
# Pull Docker image
docker pull owaspisvs/isvs-docgenerator:latest

# Test document generation
docker run --rm -u `id -u`:`id -g` -v ${PWD}:/pandoc owaspisvs/isvs-docgenerator:latest '/pandoc_makedocs.sh en 1.0'

# Test exports
docker run -v ${PWD}:/documents owaspisvs/isvs-docgenerator:latest 'cd /documents/tools && python3 export.py --format csv --lang en > OWASP_ISVS-1.0.csv'
```

#### 4. **Create 1.0 Git Tag**
**Status**: 🚫 BLOCKED (waiting on items 1-3)
**Action Required**:
- [ ] Ensure all previous checklist items complete
- [ ] Create annotated tag: `git tag -a 1.0 -m "Official OWASP ISVS 1.0 Release"`
- [ ] Push tag: `git push origin 1.0`
- [ ] Monitor GitHub Actions for automated release build
- [ ] Verify all 6 artifacts appear on Releases page

**What Happens on Tag**:
- `.github/workflows/release.yaml` triggers automatically
- Generates: PDF, EPUB, DOCX, CSV, JSON, XML
- Creates GitHub Release with all artifacts
- Release is only created if pusher is cbassem or scriptingxss

---

## 📋 Post-Release Tasks (After 1.0 Tag)

### Immediate Post-Release (Day 1)

#### 1. **Verify Release Artifacts**
- [ ] Download each artifact and verify:
  - [ ] PDF - Opens correctly, all pages render
  - [ ] EPUB - Opens in e-reader, TOC works
  - [ ] DOCX - Opens in Word, formatting intact
  - [ ] CSV - Imports to Excel, 165 rows
  - [ ] JSON - Valid JSON, all requirements present
  - [ ] XML - Valid XML, parses correctly

#### 2. **GitHub Issues Management**
- [ ] Close Issue #55 (Numbering) - ✅ Fixed
- [ ] Close Issue #63 (Non-conformities) - ✅ Guidance added
- [ ] Close Issue #82 (Bluetooth/WiFi) - ✅ Enhanced
- [ ] Close Issue #86 (Incident Response) - ✅ Added
- [ ] Close Issue #88 (Anti-bruteforce) - ✅ Added
- [ ] Update Issue #65 (Figure) - Status based on new figure
- [ ] Label Issue #89 (RAM scrambling) - Milestone: 1.1
- [ ] Label Issue #80 (Freeze/Mix-Match) - Milestone: 1.1
- [ ] Mark PR #26 (V3 updates) - Milestone: 1.1

#### 3. **Communications & Announcements**

**OWASP Channels**:
- [ ] Update OWASP project page (https://owasp.org/www-project-iot-security-verification-standard/)
- [ ] Post to #project-isvs Slack channel
- [ ] Email OWASP mailing lists

**Social Media** (if project leads approve):
- [ ] LinkedIn announcement (tag OWASP, IoT security, embedded security)
- [ ] Twitter/X post with release highlights
- [ ] Reddit r/IoT, r/netsec (community-appropriate posts)

**Key Highlights for Announcements**:
- 165 security requirements across 3 verification levels
- NEW: Post-Quantum Cryptography (PQC) readiness for 2030+
- ENHANCED: Bluetooth 5.3+ and WPA3 for L3 devices
- NEW: Incident Response requirements
- Available in 6 formats (PDF, EPUB, DOCX, CSV, JSON, XML)
- Online documentation with full search

**Announcement Template**:
```
🎉 OWASP ISVS 1.0 Official Release! 🎉

The OWASP Internet of Things Security Verification Standard (ISVS) v1.0 is now officially released!

✨ What's New:
• 165 comprehensive security requirements
• Post-Quantum Cryptography (PQC) readiness for devices operating beyond 2030
• Enhanced L3 wireless security (Bluetooth 5.3+, WPA3)
• Incident response planning requirements
• Multiple download formats: PDF, EPUB, DOCX, CSV, JSON, XML

📖 Read online: https://owasp.org/IoT-Security-Verification-Standard-ISVS/
📥 Download: https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/releases

#IoTSecurity #OWASP #CyberSecurity #EmbeddedSecurity #PQC
```

### Week 1 Post-Release

#### 4. **Documentation & Resources**
- [ ] Create "Getting Started with ISVS" tutorial
- [ ] Publish FAQ based on common questions
- [ ] Create mapping to other standards (ASVS, MASVS, NIST)
- [ ] Develop sample assessment template/checklist

#### 5. **Community Engagement**
- [ ] Schedule community call/webinar to present 1.0
- [ ] Reach out to IoT device manufacturers
- [ ] Contact security tool vendors for integration
- [ ] Invite security researchers for feedback

### Month 1 Post-Release

#### 6. **Adoption & Feedback**
- [ ] Monitor GitHub issues for bug reports
- [ ] Track download statistics
- [ ] Collect feedback from early adopters
- [ ] Begin 1.1 milestone planning

---

## 🗓️ Version 1.1 Roadmap (Future)

**Target**: April 2026 (6-month cycle)

### Deferred from 1.0
- **Issue #89** - RAM scrambling clarification (needs expert input)
- **Issue #80** - Freeze and Mix-Match attack scenarios
- **PR #26** - V3 Software Platform Requirements updates (needs discussion)
- **Issue #65** - Final ISVS overview figure refinement

### Planned Enhancements
- **Expanded Wireless Coverage** - Additional protocol requirements
  - Thread/Matter
  - NFC security
  - Cellular IoT (NB-IoT, LTE-M)
- **Supply Chain Security** - Enhanced SBOM and provenance
- **AI/ML in IoT** - Security requirements for edge AI
- **Translations** - Begin translation to priority languages

### Process Improvements
- **Assessment Tools** - Reference implementation
- **Certification Framework** - ISVS compliance certification
- **Training Materials** - Official ISVS training course

---

## 📊 Release Metrics Tracking

### Pre-Release
- Total Requirements: **165**
- New PQC Requirements: **7** (all L3)
- Issues Resolved: **6** (#55, #63, #82, #86, #88, #90)
- Pull Requests Merged: **5** (since 1.0RC)
- Contributors: **10+**

### Post-Release (To Track)
- Downloads (first week): _____
- Downloads (first month): _____
- GitHub Stars: _____
- Slack Community Members: _____
- Documentation Page Views: _____
- Issues Opened: _____
- Pull Requests: _____

---

## 🔍 Quality Gates

Before creating 1.0 tag, verify ALL of the following:

- [ ] **Content Complete**: All 165 requirements documented and reviewed
- [ ] **Numbering Correct**: Sequential numbering verified (no gaps)
- [ ] **Links Valid**: All external URLs tested and working
- [ ] **Build Success**: Local build test passes for all 6 formats
- [ ] **GitHub Pages**: Site deployed and functional
- [ ] **Dependencies**: Gemfile.lock committed
- [ ] **Documentation**: README, CHANGELOG, RELEASE_NOTES updated
- [ ] **Figure**: New ISVS overview diagram integrated
- [ ] **Branch Clean**: All intended commits on master
- [ ] **CI/CD**: GitHub Actions workflows passing

---

## 👥 Responsibilities

### Project Leads
- **Cédric Bassem** (@cbassem)
  - Final approval for 1.0 tag
  - OWASP project page updates
  - Community announcements

- **Aaron Guzman** (@scriptingxss)
  - Release artifact verification
  - Technical review sign-off
  - Industry outreach

### Community
- **Contributors**: Testing, feedback, bug reports
- **Users**: Adoption, case studies, testimonials

---

## 📞 Contact & Support

**Questions or Issues?**
- GitHub Issues: https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/issues
- Slack: https://owasp.slack.com/messages/project-isvs
- Email: aaron.guzman@owasp.org, cedric.bassem@owasp.org

---

**Last Reviewed**: October 5, 2025
**Next Review**: After 1.0 tag creation
**Status**: ⚠️ PENDING - Awaiting new ISVS overview figure before tag
