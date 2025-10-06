# Changelog

All notable changes to the OWASP IoT Security Verification Standard (ISVS) will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0] - 2025-10-04

### Official Release
This is the official 1.0 release of the OWASP IoT Security Verification Standard (ISVS). The standard provides comprehensive security requirements for IoT ecosystems and their components.

### Added
- Complete security requirements across 5 verification categories:
  - V1: IoT Ecosystem Requirements (40 requirements including new incident response section)
  - V2: User Space Application Requirements (32 requirements including anti-bruteforce protection)
  - V3: Software Platform Requirements (47 requirements)
  - V4: Communication Requirements (42 requirements with enhanced L3 wireless security)
  - V5: Hardware Platform Requirements (12 requirements)
- Three-level security verification framework (L1, L2, L3)
- Comprehensive usage guide and documentation
- Glossary of IoT security terms
- Build and export tools for multiple formats (PDF, EPUB, DOCX, CSV, JSON, XML)
- GitHub Actions workflows for automated document generation
- Contribution guidelines and peer review process
- **New requirements added based on community feedback:**
  - **V1.5**: Incident Response section (3 requirements) addressing security compromise detection and response [Issue #86]
  - **V2.1.12**: Anti-bruteforce protection for authentication mechanisms (L1, L2, L3) [Issue #88]
  - **V2.1.13**: Periodic reauthentication requirements (L2, L3) [Issue #88]
  - **V4.4.5**: WPA3 requirement for L3 WiFi communications [Issue #82]
- **Enhanced Bluetooth security requirements (research-driven enhancement)** [Issue #82]:
  - **V4.3.7** (Modified): Strengthened L1/L2 baseline to require Bluetooth 4.2+ with LE Secure Connections, eliminating vulnerable BT 4.1
  - **V4.3.8** (Enhanced): Upgraded L3 to require Bluetooth 5.3+ with mandatory 128-bit encryption key size enforcement (prevents KNOB attacks)
  - **V4.3.9** (NEW): Encrypted Advertising Data requirement for L3 (prevents pre-connection eavesdropping)
  - **V4.3.10** (NEW): Channel security and adaptive frequency hopping for L3 (defends against interference attacks)
  - Based on comprehensive research: 62% BLE 5.x market adoption, negligible cost impact, defends against CVE-2023-24023 (BLUFFS) and CVE-2020-26558
- **New guidance section**: "Handling Non-Conformities" in Using_ISVS.md providing risk-based decision framework [Issue #63]
- **Post-Quantum Cryptography (PQC) requirements (7 new L3 requirements)** [Regulatory alignment]:
  - **V2.4.7** (NEW): PQC migration requirement for devices operating beyond 2030 - hybrid cryptography combining classical and post-quantum algorithms
  - **V2.4.8** (NEW): NIST-approved PQC algorithm validation (FIPS 203, 204, 205)
  - **V3.1.9** (NEW): Secure boot with post-quantum digital signatures (ML-DSA, SLH-DSA) or hybrid schemes
  - **V3.4.13** (NEW): Firmware update signing with post-quantum or hybrid cryptography
  - **V4.1.7** (NEW): TLS post-quantum key exchange (ML-KEM) or hybrid key exchange
  - **V4.1.8** (NEW): X.509 certificates with post-quantum signatures (ML-DSA, SLH-DSA) or hybrid chains
  - **V5.1.13** (NEW): Hardware support for PQC algorithms or sufficient software performance
  - Aligns with NIST quantum-safe migration timeline (deprecation 2030, full transition 2035)
  - Addresses US Executive Order 14144 (Jan 2025) and EU Cyber Resilience Act requirements
  - Protects devices designed in 2025 for 2027+ deployment with 10-15 year operational lifetimes

### Changed
- Updated copyright year from 2021 to 2025
- Updated version date to October 2025
- Transitioned from peer review status to official release
- Updated README.md to reflect official release status

### Fixed
- **Critical numbering issues** [Issue #55]:
  - Fixed missing requirement 3.3.3 in V3 (Linux section)
  - Fixed missing requirement 4.1.5 in V4 (General communication section)
  - Verified sequential numbering across all 165 requirements
- **Content corrections**:
  - Typo in Using_ISVS.md: "communicaiton" → "communication"
  - Various vocabulary and style improvements from community feedback
- **Broken external reference URLs**:
  - Updated ENISA IoT Baseline Security Recommendations URL
  - Updated RFC 7525 to new IETF datatracker location
  - Updated OWASP MASVS URL to new canonical location (owasp.org/mas)

### Contributors
Special thanks to all contributors and reviewers who helped make this release possible:
- Cédric Bassem (Project Lead)
- Aaron Guzman (Project Lead)
- Théo Rigas
- Leo Dorrendorf
- Anna Schnaiderman
- Community reviewers and contributors

## [1.0RC] - 2021-01-22

### Release Candidate
- Initial release candidate for peer review
- All core content and requirements finalized
- Ready for community feedback and validation

---

For the complete list of changes and detailed commit history, see the [GitHub repository](https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS).
