# OWASP ISVS 1.0 Release Notes

## Official Release - October 2025

We are pleased to announce the official 1.0 release of the OWASP Internet of Things Security Verification Standard (ISVS)!

### What is ISVS?

The OWASP ISVS is a comprehensive security verification standard for Internet of Things (IoT) ecosystems. It provides security requirements for IoT systems and their components including IoT hardware, software, embedded applications, and communication protocols.

### Release Highlights

This official 1.0 release includes **165 security requirements** organized across three security verification levels (L1, L2, L3) and five verification categories:

- **V1: IoT Ecosystem Requirements** (40 requirements)
- **V2: User Space Application Requirements** (34 requirements) - includes 2 new PQC requirements
- **V3: Software Platform Requirements** (49 requirements) - includes 2 new PQC requirements
- **V4: Communication Requirements** (46 requirements) - includes 2 new PQC requirements
- **V5: Hardware Platform Requirements** (13 requirements) - includes 1 new PQC requirement

### What's New in 1.0

#### Enhanced Requirements Based on Community Feedback

**Incident Response (V1.5)** - NEW SECTION
- Requirements for incident response planning
- Procedures for handling compromised credentials
- Device legitimacy validation mechanisms

**Authentication Improvements (V2.1)**
- Anti-bruteforce protection requirements (2.1.12)
- Periodic reauthentication requirements (2.1.13)

**Enhanced L3 Wireless Security (V4)** - Research-Driven Enhancements
- **Bluetooth Security Overhaul** (4.3.7-4.3.10):
  - L1/L2 baseline strengthened to Bluetooth 4.2+ with LE Secure Connections
  - L3 upgraded to **Bluetooth 5.3+** with mandatory security features:
    - 128-bit encryption key size enforcement (prevents KNOB/downgrade attacks)
    - Encrypted Advertising Data support (prevents pre-connection eavesdropping)
    - Channel security and adaptive frequency hopping (defends against interference)
  - Protects against CVE-2023-24023 (BLUFFS), CVE-2020-26558, and MITM attacks
  - Based on market research: 62% BLE 5.x adoption, negligible cost impact
- WPA3 requirement for L3 WiFi communications (4.4.5)

**Post-Quantum Cryptography (PQC) Readiness** - NEW FOR 1.0
- **7 New L3 Requirements** for quantum-resistant security:
  - **V2.4.7-2.4.8**: Cryptographic migration to post-quantum algorithms (ML-KEM, ML-DSA, SLH-DSA) or hybrid approaches for devices operating beyond 2030
  - **V3.1.9**: Secure boot with post-quantum digital signatures
  - **V3.4.13**: Firmware updates with post-quantum or hybrid cryptographic schemes
  - **V4.1.7-4.1.8**: TLS with post-quantum key exchange and certificates
  - **V5.1.13**: Hardware platform support for PQC algorithms
- **Regulatory Alignment**: US Executive Order 14144 (Jan 2025), EU Cyber Resilience Act
- **Timeline-Based**: Targets devices designed in 2025 for 2027+ deployment with 10-15 year lifetimes
- **Standards Compliance**: NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA)
- **Hybrid Cryptography**: Combines classical (RSA/ECC) and post-quantum algorithms for resilience

#### Improved Documentation

**Non-Conformity Guidance**
- New section in "Using the ISVS" explaining how to handle failed controls
- Risk-based decision-making framework
- Guidance on partial compliance and continuous improvement

#### Critical Fixes

**Requirement Numbering**
- Fixed missing requirement 3.3.3 in V3
- Fixed missing requirement 4.1.5 in V4
- Verified all 156 requirements have sequential numbering

**Updated References**
- Fixed broken ENISA URL
- Updated RFC references to current locations
- Updated OWASP project URLs

### GitHub Issues Addressed

This release resolves the following community-reported issues:

- **#55**: Fix numbering before release ✅
- **#63**: Add info on how to deal with non-conformities ✅
- **#65**: Update 'Using ISVS' Figure (documentation added, figure update deferred to 1.1)
- **#82**: L3 requirements for Bluetooth and WiFi aren't high enough ✅
- **#86**: Detect & Response set of requirements missing ✅
- **#88**: V2: Missing anti-bruteforce & reauthentication requirements ✅

### Deferred to Version 1.1

The following items have been deferred to allow for a timely 1.0 release:

- **PR #26**: V3 Software Platform Requirements updates (requires broader discussion)
- **Issue #65**: ISVS Overview figure redesign (documentation guidance added in 1.0)
- **Issue #89**: RAM scrambling clarification
- **Issue #80**: Freeze and Mix-Match attack scenarios

### Online Documentation

**[https://owasp.org/IoT-Security-Verification-Standard-ISVS/](https://owasp.org/IoT-Security-Verification-Standard-ISVS/)**

Read the complete standard online with:
- Full-text search across all requirements
- Mobile-responsive design
- Easy navigation between sections
- Permanent OWASP.org hosting

> **Migration Note**: Documentation is now hosted on GitHub Pages for easier maintenance and community contributions. The previous GitBook hosting has been deprecated.

### Download Formats

ISVS 1.0 is available in multiple formats:

- PDF (for reading and printing)
- EPUB (for e-readers)
- DOCX (for editing and customization)
- CSV (for spreadsheet analysis)
- JSON (for programmatic use)
- XML (for integration with tools)

All formats are available on the [GitHub Releases page](https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/releases).

### How to Use ISVS

The ISVS can be used in multiple ways:

1. **Security Assessment**: Verify IoT devices and ecosystems meet security requirements
2. **Development Guidance**: Use as security requirements during SDLC
3. **Procurement**: Specify security levels required from vendors
4. **Training**: Guide security training curriculum development
5. **Compliance**: Demonstrate security posture to stakeholders

See the [Using the ISVS](en/Using_ISVS.md) section for detailed guidance.

### Contributors

Special thanks to all contributors who helped make this release possible:

- Cédric Bassem (Project Lead)
- Aaron Guzman (Project Lead)
- Théo Rigas
- Leo Dorrendorf
- Anna Schnaiderman
- windBlaze (Community Contributor)
- All community reviewers and issue reporters

### Get Involved

ISVS is an open-source community effort. We welcome contributions!

- **Slack**: Join [#project-isvs](https://owasp.slack.com/messages/project-isvs)
- **Issues**: Report bugs or suggest enhancements on [GitHub](https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/issues)
- **Pull Requests**: Submit improvements via [Pull Requests](https://github.com/OWASP/IoT-Security-Verification-Standard-ISVS/pulls)

See our [Contributing Guide](Contributing.md) for more information.

### Next Steps - Version 1.1 Roadmap

We're already planning version 1.1! Planned improvements include:

- Redesigned ISVS overview figure
- V3 software platform requirements review and enhancements
- Additional attack scenario coverage
- Community-requested clarifications
- Expanded wireless protocol coverage

### License

ISVS is released under the [Creative Commons Attribution ShareAlike 4.0 license](https://creativecommons.org/licenses/by-sa/4.0/).

---

**Thank you for using the OWASP IoT Security Verification Standard!**

For questions or feedback, please contact the project leads or open an issue on GitHub.
