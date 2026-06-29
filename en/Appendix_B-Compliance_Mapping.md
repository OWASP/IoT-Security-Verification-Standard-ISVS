---
layout: default
title: Appendix B - Compliance Mapping
nav_order: 7
---

# Appendix B: Compliance Mapping

## Overview

This appendix provides a cross-reference between ISVS security requirements and three major IoT-related regulatory and technical frameworks: the EU Cyber Resilience Act (CRA), the EU Radio Equipment Directive Delegated Regulation 2022/30 (RED), the NIST SP 800-213A IoT Device Cybersecurity Requirements Catalog, and ETSI EN 303 645 v2.1.1.

The mapping is provided in two directions. Table 1 (ISVS to Frameworks) allows practitioners to determine which regulatory or framework obligations a given ISVS requirement supports. Table 2 (Frameworks to ISVS) allows compliance teams working from a specific regulation to identify which ISVS requirements collectively address a given clause.

**This appendix is informative only.** Satisfying ISVS requirements does not constitute legal compliance with any regulation listed here, and compliance with a framework cannot be claimed solely based on this mapping. Readers should consult the full text of each framework and, where applicable, seek legal or conformity assessment advice.

**Scope note:** This mapping covers ISVS requirements present in the v1.0 release (master branch). Requirements introduced in subsequent releases — including V1.5 Incident Response, additional V2, V3, V4, and V5 requirements targeting Bluetooth 5.3+, post-quantum cryptography, and related topics — will be incorporated in a future update of this appendix.

A mapping cell marked **Partial** indicates that the ISVS requirement addresses part of the referenced clause but does not satisfy it entirely on its own. A cell containing a clause reference without qualification indicates substantive, direct alignment. A dash (—) indicates no meaningful alignment exists.

---

## Frameworks Covered

### EU Cyber Resilience Act (CRA)

The Cyber Resilience Act (Regulation (EU) 2024/2847) entered into force on December 11, 2024, with product security obligations applying from December 11, 2027 and vulnerability handling obligations from September 11, 2026. It applies to all products with digital elements placed on the EU market, including IoT devices. Annex I, Part I specifies essential cybersecurity requirements covering secure default configuration, authentication, encryption, attack surface minimization, exploitation mitigation, security monitoring, and secure data handling. Annex I, Part II covers vulnerability handling obligations including software bill of materials (SBOM), coordinated vulnerability disclosure, and active vulnerability remediation. Article 13 imposes manufacturer obligations on technical documentation, designated contact points, and supply chain due diligence.

### EU Radio Equipment Directive — Delegated Regulation 2022/30 (RED)

Commission Delegated Regulation (EU) 2022/30 supplements the Radio Equipment Directive (2014/53/EU) by activating Article 3.3(d), (e), and (f) for internet-connected radio equipment. It became mandatory on August 1, 2025. Harmonized standards EN 18031-1, EN 18031-2, and EN 18031-3 provide the technical specifications for, respectively, network protection, personal data and privacy protection, and fraud prevention. The RED applies to a broad range of connected consumer and industrial radio devices including Wi-Fi, Bluetooth, Zigbee, LoRaWAN, and cellular devices, making it highly relevant to IoT deployments.

### NIST SP 800-213A

NIST Special Publication 800-213A, "IoT Device Cybersecurity Requirements Catalog," is a companion to SP 800-213 ("IoT Device Cybersecurity Guidance for the Federal Government"). It provides a catalog of IoT device-level technical capabilities and non-technical supporting capabilities that federal agencies and other organizations can use to identify, assess, and specify cybersecurity requirements for IoT devices. SP 800-213A organizes device cybersecurity capabilities into seven technical areas — Device Identification (DI), Device Configuration (DC), Data Protection (DP), Logical Access to Interfaces (LA), Software Update (SU), Cybersecurity State Awareness (CS), and Device Security (DS) — plus non-technical supporting capability areas covering Documentation, Vulnerability/cybersecurity information reception, and Cybersecurity event notification. Each area is further subdivided into specific sub-capabilities (e.g., DI (IMS), DP (CRY), LA (IFC)) that map directly to device-level security behaviors. This mapping references SP 800-213A sub-capability identifiers in that format.

### ETSI EN 303 645 v2.1.1

ETSI EN 303 645 is the leading international baseline security standard for consumer IoT, published by the European Telecommunications Standards Institute. Version 2.1.1 comprises 13 provisions covering the most critical security outcomes for consumer IoT products. It forms the technical basis for several national IoT security schemes (including the UK Product Security and Telecommunications Infrastructure Act) and is referenced by the EU CRA harmonized standard development process. Its provisions address default password elimination, vulnerability disclosure, software updates, credential storage, secure communication, attack surface minimization, software integrity, personal data protection, resilience, telemetry, data deletion, secure installation, and input validation.

---

## Important Notes

1. **Informative status.** This appendix is informative and does not constitute legal or conformity advice. Manufacturers and operators seeking to demonstrate compliance with any listed regulation must engage with the full normative text of that regulation and, where required, an appropriate conformity assessment body.

2. **Partial coverage.** Many regulatory clauses address organizational, process, and documentation obligations that extend beyond the technical controls in the ISVS. A mapping marked "Partial" reflects genuine technical alignment while acknowledging that the full clause requires additional organizational measures.

3. **Framework versions.** Mappings reflect the versions stated in the section headings. Future revisions to any framework may alter the alignment described here.

4. **Level independence.** ISVS requirements appear in this mapping regardless of which verification level (L1, L2, L3) they apply to. The level column in each chapter's requirement table indicates applicability; compliance teams should apply that context when using this mapping.

5. **Future updates.** This mapping will be revised when additional ISVS requirements (V1.5, Bluetooth 5.3+, post-quantum cryptography, and others) are formally adopted into the standard.

6. **Notation.** In Table 1, a cell containing a clause reference without qualification indicates substantive, direct alignment; the word `Partial` indicates the requirement addresses part of the clause only. In Table 2, requirement IDs followed by **(P)** indicate partial coverage of that clause. A dash (—) in either table indicates no meaningful alignment exists.

7. **Ecosystem-level obligations.** Some framework clauses impose obligations at the network or ecosystem level rather than on the device itself. These are correctly mapped to `—` not because ISVS has a content gap, but because the obligation falls outside the scope of a device-level standard. CRA Annex I 2(i) ("minimize negative impact on connected devices or networks") is the primary example: it is satisfied through network architecture, operational practices, and ecosystem design rather than through device-level controls.

8. **CRA harmonized standards.** As of the date of this appendix, no harmonized standards for the Cyber Resilience Act (EN 40000 series) have been published in the EU Official Journal. CRA Annex I requirements in this mapping are drawn directly from the regulation text. Until harmonized standards are cited in the Official Journal (projected Q4 2026 at the earliest), manufacturers must self-assess against Annex I directly. For current status, monitor the European Commission's harmonized standards register and [stan4cra.eu](https://www.stan4cra.eu).

---

## Table 1: ISVS to Framework Mapping

The table below maps each ISVS requirement to the most relevant clauses in each covered framework. Requirements are grouped by chapter (V1–V5).

| ISVS Req | CRA Annex I Part I | CRA Annex I Part II | RED 3.3(d) EN 18031-1 | RED 3.3(e) EN 18031-2 | RED 3.3(f) EN 18031-3 | NIST SP 800-213A | ETSI EN 303 645 |
|----------|-------------------|--------------------|-----------------------|-----------------------|-----------------------|------------------|-----------------|
| **V1 — IoT Ecosystem Requirements** | | | | | | | |
| **1.1.1** Verify IoT system security level matches capabilities and deployment risk | — | — | — | — | — | — | — |
| **1.1.2** Verify all components and channels are identified; unnecessary ones removed | 2(j) | — | Partial | — | — | DI (IMS), DS (DIN) | 5.6-1, 5.6-5 |
| **1.1.3** Verify threat modeling is used for product design and feature changes | — | — | — | — | — | — | — |
| **1.1.4** Verify security controls enforced server-side; data not blindly trusted | 2(d), 2(f) | — | — | — | — | LA (AUZ), DP (STX) | 5.13-1 |
| **1.1.5** Verify responsible disclosure policy is established and published | — | Part II (CVD) | — | — | — | Non-tech (BUG) | 5.2-1, 5.2-2 |
| **1.1.6** Verify users are notified when vulnerabilities affect products | — | Part II (CVD) | — | — | — | Non-tech (VNT) | 5.2-3 |
| **1.2.1** Verify SBOM is maintained for each application in the ecosystem | — | Part II (SBOM) | — | — | — | Non-tech (DOC) | — |
| **1.2.2** Verify risks from third-party and open-source software are identified and mitigated | — | Part II | — | — | — | Non-tech (DOC), DS (DIN) | — |
| **1.2.3** Verify devices released with secure default firmware configurations | 2(b) | — | Partial | — | — | DC (CTL), DC (AUT) | 5.1-1, 5.1-2 |
| **1.2.4** Verify debugging interfaces disabled or protected before shipping | 2(j), 2(k) | — | — | — | — | LA (IFC), DS (OPS) | 5.6-2 |
| **1.2.5** Verify FPGA debug capabilities disabled on production PCBs | 2(j) | — | — | — | — | LA (IFC) | 5.6-2 |
| **1.2.6** Verify hardware-based, immutable cryptographic root of trust | 2(f), 2(k) | — | Partial | — | — | DS (DIN), DS (EXE) | 5.7-1 |
| **1.2.7** Verify code integrity protection enabled and locked in hardware | 2(f), 2(k) | — | Partial | — | — | DS (DIN) | 5.7-1 |
| **1.2.8** Verify third-party code analyzed via static analysis for backdoors | — | Part II | — | — | — | Non-tech (DOC) | — |
| **1.2.9** Verify all components including drivers and modules can be updated for security patches | 2(c) | — | — | — | — | SU (UPD) | 5.3-2 |
| **1.3.1** Verify builds use a secure and repeatable build environment | — | Part II | — | — | — | Non-tech (DOC) | — |
| **1.3.2** Verify GPL firmware source is published without sensitive information | — | — | — | — | — | Non-tech (DOC) | — |
| **1.3.3** Verify banned C/C++ functions replaced with safe equivalents | 2(k) | — | — | — | — | DS (EXE) | — |
| **1.3.4** Verify packages downloaded from trusted sources | — | Part II | — | — | — | SU (UPD) | — |
| **1.3.5** Verify build pipelines only build source code from version control | — | Part II | — | — | — | Non-tech (DOC) | — |
| **1.3.6** Verify compilers and development tools are monitored for tampering | — | Part II | — | — | — | DS (DIN) | — |
| **1.3.7** Verify packages compiled with Object Size Checking (FORTIFY_SOURCE) | 2(k) | — | — | — | — | DS (EXE) | — |
| **1.3.8** Verify packages compiled with NX / DEP | 2(k) | — | — | — | — | DS (EXE) | — |
| **1.3.9** Verify packages compiled with PIE | 2(k) | — | — | — | — | DS (EXE) | — |
| **1.3.10** Verify packages compiled with Stack Smashing Protector (SSP) | 2(k) | — | — | — | — | DS (EXE) | — |
| **1.3.11** Verify packages compiled with RELRO | 2(k) | — | — | — | — | DS (EXE) | — |
| **1.3.12** Verify release builds contain no debug code or privileged diagnostics | 2(b), 2(j) | — | — | — | — | DC (CTL), LA (IFC) | 5.6-2 |
| **1.3.13** Verify debug and release firmware signed with different keys | 2(f), 2(k) | — | — | — | — | SU (UPD), DP (CRY) | 5.7-1 |
| **1.3.14** Verify debug info does not contain sensitive information (PII, credentials, keys) | 2(e), 2(g) | — | — | Partial | — | DP (STO) | 5.8-1 |
| **1.3.15** Verify embedded applications are not susceptible to OS command injection | 2(k) | — | — | — | — | DS (EXE) | 5.13-1 |
| **1.4.1** Verify devices can collect security event logs | 2(l) | — | Partial | — | — | CS (LCT), CS (EIM) | 5.10-1 |
| **1.4.2** Verify logs have adequate granularity (event type, timestamp, source, outcome, actors) | 2(l) | — | Partial | — | — | CS (RDL) | 5.10-1 |
| **1.4.3** Verify devices use a reliable time source for log timestamp validity | 2(l) | — | — | — | — | CS (SRT) | — |
| **1.4.4** Verify logs do not include sensitive information (PII, credentials, keys) | 2(g), 2(l) | — | — | Partial | — | CS (RDL), DP (STO) | 5.8-1 |
| **1.4.5** Verify logs can be securely retrieved from devices | 2(l) | — | Partial | — | — | CS (AUP) | 5.10-1 |
| **1.4.6** Verify logs retained per policy and safely deleted when retention expires | 2(g), 2(m) | — | — | Partial | — | CS (LSR) | 5.8-1, 5.11-1 |
| **1.4.7** Verify confidentiality, integrity and authenticity of logs is protected | 2(e), 2(f), 2(l) | — | — | — | — | CS (AUP), DP (CRY) | — |
| **V2 — User Space Application Requirements** | | | | | | | |
| **2.1.1** Verify all users and accounts can be uniquely identified | 2(d) | — | Partial | Partial | — | DI (IMS) | — |
| **2.1.2** Verify all connected devices can be uniquely identified | 2(d) | — | Partial | — | — | DI (IMS), DI (AID) | — |
| **2.1.3** Verify strong user and device authentication is enforced across the ecosystem | 2(d) | — | Partial | Partial | Partial | LA (AUN), DI (DAS) | 5.1-1 |
| **2.1.4** Verify user, service, and device authentication shares a common centrally managed framework | 2(d) | — | Partial | — | — | LA (AUN), DC (AUT) | — |
| **2.1.5** Verify user passwords are at least 12 characters | 2(d) | — | — | — | — | LA (ACF) | 5.1-1 |
| **2.1.6** Verify users can change their password and must provide current password | 2(b), 2(d) | — | — | — | — | LA (ACF), DC (AUT) | 5.1-1 |
| **2.1.7** Verify device authentication passwords are sufficiently long and complex | 2(d) | — | Partial | — | — | LA (ACF) | 5.1-1 |
| **2.1.8** Verify default user or device credentials can be changed by authorized parties | 2(b), 2(d) | — | Partial | — | — | DC (AUT), LA (ACF) | 5.1-1, 5.1-2 |
| **2.1.9** Verify authentication credentials are not hardcoded in firmware or applications | 2(a), 2(d) | — | Partial | — | — | DP (KEY), DC (AUT) | 5.1-2, 5.4-1 |
| **2.1.10** Verify provisioned device authentication credentials are unique per device | 2(d) | — | Partial | — | — | DI (DAS), DP (KEY) | 5.1-2 |
| **2.1.11** Verify authentication schemes can revoke credentials of compromised or decommissioned devices | 2(d) | — | Partial | — | — | LA (ACF), DI (DAS) | — |
| **2.2.1** Verify IoT system accounts share a common authorization framework | 2(d) | — | — | — | — | LA (AUZ), LA (ROL) | — |
| **2.2.2** Verify least privilege is enforced; applications not run as root/admin unnecessarily | 2(d), 2(j) | — | Partial | — | — | LA (ROL), DS (OPS) | 5.6-3 |
| **2.2.3** Verify ownership is validated upon registration and decommissioning | 2(d), 2(m) | — | — | — | — | LA (AUZ), DI (AID) | 5.11-1 |
| **2.2.4** Verify device debug access is limited to approved staff and access is monitored or logged | 2(d), 2(l) | — | — | — | — | LA (ROL), CS (EIM) | 5.6-2 |
| **2.3.1** Verify sensitive information (PII, credentials) stored using strong encryption with integrity checking | 2(e), 2(f) | — | — | Partial | — | DP (STO), DP (CRY) | 5.4-1, 5.8-1 |
| **2.3.2** Verify sensitive data and credentials can be removed from device on decommission or ownership change | 2(m) | — | — | Partial | — | DP (STO), DS (OPS) | 5.11-1 |
| **2.3.3** Verify decommissioned devices are marked in a centrally managed database for audit | 2(m) | — | — | — | — | CS (LCT), DI (AID) | 5.11-1 |
| **2.3.4** Verify sensitive information in memory is overwritten with zeros when no longer required | 2(e), 2(g) | — | — | Partial | — | DP (STO), DS (RSC) | 5.8-1 |
| **2.4.1** Verify cryptographic secrets and keys are unique per device | 2(e), 2(f) | — | — | Partial | — | DP (KEY) | 5.4-1 |
| **2.4.2** Verify proper use of cryptography: standard algorithms, adequate key size, secure implementations | 2(e), 2(f) | — | Partial | Partial | Partial | DP (CRY) | 5.5-1, 5.8-1 |
| **2.4.3** Verify secure sources of randomness provided by OS or hardware | 2(e), 2(k) | — | — | — | — | DP (CRY), DP (KEY) | — |
| **2.4.4** Verify cryptographic secrets stored securely using dedicated security chip functionality | 2(e), 2(f) | — | — | Partial | — | DP (KEY), DP (STO) | 5.4-1 |
| **2.4.5** Verify cryptographic primitives are provided by dedicated security chips | 2(e), 2(k) | — | — | — | — | DP (CRY) | — |
| **2.4.6** Verify cryptographic libraries are certified to a recognized standard | 2(e) | — | — | — | — | DP (CRY) | — |
| **V3 — Software Platform Requirements** | | | | | | | |
| **3.1.1** Verify bootloader does not allow code loaded from arbitrary local or network locations | 2(f), 2(j), 2(k) | — | Partial | — | — | DS (EXE), DS (DIN) | 5.7-1 |
| **3.1.2** Verify bootloader configurations are immutable in production | 2(b), 2(f) | — | Partial | — | — | DS (DIN), DC (CTL) | 5.7-1 |
| **3.1.3** Verify communication interfaces (USB, UART) disabled or protected during boot | 2(j) | — | Partial | — | — | LA (IFC), DS (OPS) | 5.6-2 |
| **3.1.4** Verify first-stage bootloader authenticity verified by hardware root of trust | 2(f), 2(k) | — | Partial | — | — | DS (DIN), SU (UPD) | 5.7-1 |
| **3.1.5** Verify bootloader stages and application code cryptographically verified before execution | 2(f), 2(k) | — | Partial | — | — | DS (DIN), DP (CRY) | 5.7-1 |
| **3.1.6** Verify bootloader stages do not expose sensitive information during start-up | 2(e), 2(g) | — | — | Partial | — | DP (STO) | 5.4-1 |
| **3.1.7** Verify firmware stored in encrypted volume at rest | 2(e) | — | — | Partial | — | DP (STO) | 5.8-1 |
| **3.1.8** Verify Direct Memory Access (DMA) is not possible during boot | 2(f), 2(k) | — | — | — | — | DS (RSC), DS (EXE) | — |
| **3.2.1** Verify embedded OS configured per industry best practices and uses secure defaults | 2(b) | — | Partial | — | — | DC (CTL) | — |
| **3.2.2** Verify only necessary network services are exposed on each interface | 2(j) | — | Partial | — | — | LA (IFC), DS (COM) | 5.6-1 |
| **3.2.3** Verify device does not use legacy or insecure protocols (Telnet, FTP) | 2(a), 2(j) | — | Partial | — | — | DS (COM), LA (IFC) | 5.5-1, 5.6-4 |
| **3.2.4** Verify OS kernel and software components are up to date and free of known vulnerabilities | 2(a), 2(c) | Part II | — | — | — | SU (UPD) | 5.3-1 |
| **3.2.5** Verify persistent filesystem storage volumes are encrypted | 2(e) | — | — | Partial | — | DP (STO) | 5.8-1 |
| **3.2.6** Verify applications use OS/kernel security features (crypto, key storage, RNG, auth, logging, comms) | 2(e), 2(f), 2(k) | — | — | — | — | DS (EXE), DP (CRY) | — |
| **3.2.7** Verify ASLR and DEP enabled by the embedded OS | 2(k) | — | — | — | — | DS (EXE), DS (RSC) | — |
| **3.2.8** Verify hardware-level memory protection is used and privilege levels enforced | 2(f), 2(k) | — | — | — | — | DS (RSC), DS (EXE) | — |
| **3.2.9** Verify embedded OS provides protection against unauthorized RAM access (e.g. RAM scrambling) | 2(f), 2(k) | — | — | — | — | DS (RSC) | — |
| **3.2.10** Verify Integrity Measurement Architecture (IMA) or similar integrity subsystem is used | 2(f), 2(k) | — | Partial | — | — | DS (DIN) | 5.7-1 |
| **3.2.11** Verify third-party applications run in a hardened containerized runtime environment | 2(j), 2(k) | — | — | — | — | DS (EXE), LA (IFC) | 5.6-3 |
| **3.3.1** Verify processes are isolated using Linux kernel namespaces | 2(j), 2(k) | — | — | — | — | DS (EXE), DS (RSC) | — |
| **3.3.2** Verify critical processes limit resources using cgroups | 2(h) | — | Partial | — | — | DS (RSC), DS (OPS) | 5.9-1 |
| **3.3.4** Verify Linux kernel capabilities configured with minimal set for elevated access | 2(j), 2(k) | — | — | — | — | DS (EXE), LA (ROL) | 5.6-3 |
| **3.3.5** Verify seccomp BPF with filters is used and configured to allow only necessary syscalls | 2(j), 2(k) | — | — | — | — | DS (EXE) | 5.6-3 |
| **3.3.6** Verify use of kernel security modules (SELinux, AppArmor, GRSEC, or equivalent) | 2(j), 2(k) | — | — | — | — | DS (EXE), LA (AUZ) | 5.6-3 |
| **3.4.1** Verify packages and user space apps support OTA updates decoupled from firmware | 2(c) | — | — | — | — | SU (UPD), SU (APP) | 5.3-2 |
| **3.4.2** Verify devices can be updated automatically on a pre-defined schedule | 2(c) | — | — | — | — | SU (APP) | 5.3-3 |
| **3.4.3** Verify updates are cryptographically signed by a trusted source and verified before execution | 2(c), 2(f) | — | Partial | — | — | SU (UPD), DP (CRY) | 5.3-4, 5.7-1 |
| **3.4.4** Verify update process is not vulnerable to TOCTOU attacks | 2(c), 2(f) | — | — | — | — | SU (UPD) | 5.3-4 |
| **3.4.5** Verify updates do not silently modify user-configured preferences or security/privacy settings | 2(b), 2(c) | — | — | Partial | — | DC (CTL), SU (APP) | 5.12-1 |
| **3.4.6** Verify devices cannot be downgraded to known vulnerable versions (anti-rollback) | 2(a), 2(c) | — | — | — | — | SU (UPD), DS (DIN) | 5.3-1 |
| **3.4.7** Verify that on update failure the device reverts to a backup image or notifies the ecosystem | 2(c), 2(h) | — | — | — | — | DS (OPS), SU (APP) | 5.3-5, 5.9-1 |
| **3.4.8** Verify unsigned debug pre-production firmware cannot be flashed onto devices | 2(b), 2(f) | — | Partial | — | — | SU (UPD), DS (DIN) | 5.7-1 |
| **3.4.9** Verify encrypted firmware images are securely decrypted on the device | 2(e), 2(f) | — | — | — | — | DP (CRY), SU (UPD) | — |
| **3.4.10** Verify device authenticates to the update server before downloading the update | 2(d), 2(f) | — | Partial | — | — | LA (AUN), SU (UPD) | 5.3-4 |
| **3.4.11** Verify firmware updates are stored encrypted server-side | 2(e) | — | — | — | — | DP (STO) | — |
| **3.4.12** Verify software and firmware updates transmitted over an encrypted communication channel | 2(c), 2(e) | — | Partial | — | — | DP (STX), SU (UPD) | 5.3-4, 5.5-1 |
| **3.5.1** Verify encryption is used on the bus between security chip and other hardware components | 2(e), 2(f) | — | — | — | — | DP (STX), DP (CRY) | — |
| **3.5.2** Verify keys used to enable security chip bus encryption are properly secured on the host | 2(e) | — | — | — | — | DP (KEY) | 5.4-1 |
| **3.5.3** Verify any default vendor keys used in bus encryption are replaced in production | 2(b), 2(e) | — | — | — | — | DP (KEY), DC (AUT) | 5.4-1 |
| **3.5.4** Verify deprecated ciphers and hash functions not used even when provided by security chip | 2(e) | — | Partial | Partial | — | DP (CRY) | 5.5-1 |
| **3.6.1** Verify loaded kernel modules are cryptographically signed and verified | 2(f), 2(k) | — | Partial | — | — | DS (DIN), DP (CRY) | 5.7-1 |
| **3.6.2** Verify only required kernel modules are enabled during runtime | 2(j) | — | — | — | — | DS (EXE), LA (IFC) | 5.6-1 |
| **V4 — Communication Requirements** | | | | | | | |
| **4.1.1** Verify communication with all ecosystem components occurs over a secure channel (confidentiality, integrity, replay protection) | 2(e), 2(f) | — | Partial | Partial | — | DP (STX), DS (COM) | 5.5-1 |
| **4.1.2** Verify only strong cipher suites are enabled, with strongest set as preferred | 2(e) | — | Partial | Partial | Partial | DP (CRY), DS (COM) | 5.5-1 |
| **4.1.3** Verify TLS implementation cryptographically verifies X.509 certificates | 2(d), 2(e), 2(f) | — | Partial | Partial | — | DP (STX), LA (AUN) | 5.5-1 |
| **4.1.4** Verify jamming protection or detection is provided for availability-critical applications | 2(h) | — | Partial | — | — | DS (OPS), CS (EIM) | 5.9-1 |
| **4.1.6** Verify TLS implementation uses its own certificate store and pins to endpoint certificate or key | 2(d), 2(e), 2(f) | — | Partial | — | — | DP (STX), LA (AUN) | 5.5-1 |
| **4.1.7** Verify inter-chip communication is encrypted | 2(e), 2(f) | — | — | — | — | DP (STX) | — |
| **4.2.1** Verify unencrypted communication is limited to non-sensitive data and instructions | 2(e) | — | Partial | Partial | — | DP (STX) | 5.5-1 |
| **4.2.2** Verify MQTT brokers only allow authorized devices to subscribe and publish | 2(d) | — | Partial | — | — | LA (AUN), LA (AUZ) | — |
| **4.2.3** Verify certificates are favored over username/password for MQTT authentication | 2(d), 2(e) | — | Partial | — | — | LA (AUN), DP (STX) | 5.5-1 |
| **4.3.1** Verify Bluetooth pairing and discovery is blocked except when necessary | 2(j) | — | Partial | — | — | LA (IFC) | 5.6-1 |
| **4.3.2** Verify Bluetooth PIN or PassKey codes are not easily guessable | 2(d) | — | Partial | — | — | LA (ACF), DI (DAS) | 5.1-1 |
| **4.3.3** Verify older Bluetooth devices with simple authentication require a PIN for pairing | 2(d) | — | Partial | — | — | LA (ACF) | 5.1-1 |
| **4.3.4** Verify modern Bluetooth SSP authentication requires at least 6 digits (except "Just Works") | 2(d) | — | Partial | — | — | LA (ACF) | 5.1-1 |
| **4.3.5** Verify Bluetooth encryption keys are maximum size the device supports | 2(e) | — | Partial | — | — | DP (CRY) | 5.5-1 |
| **4.3.6** Verify the most secure Bluetooth pairing method available is used (OOB, Numeric Comparison, or Passkey) | 2(d), 2(e) | — | Partial | — | — | DI (DAS), LA (AUN) | 5.5-1 |
| **4.3.7** Verify strongest Bluetooth Security Mode and Level supported by the device is used | 2(d), 2(e) | — | Partial | — | — | LA (IFC), DP (CRY) | 5.5-1 |
| **4.4.1** Verify Wi-Fi is disabled unless required as part of device functionality | 2(j) | — | Partial | — | — | LA (IFC) | 5.6-1 |
| **4.4.2** Verify WPA2 or higher is used to protect Wi-Fi communications | 2(e) | — | Partial | — | — | DP (CRY), DS (COM) | 5.5-1 |
| **4.4.3** Verify WPA uses AES encryption (CCMP mode) when applicable | 2(e) | — | Partial | — | — | DP (CRY) | 5.5-1 |
| **4.4.4** Verify Wi-Fi Protected Setup (WPS) is not used | 2(d), 2(j) | — | Partial | — | — | LA (IFC) | 5.6-4 |
| **4.5.1** Verify Zigbee version 3.0 is used for new applications | 2(a), 2(e) | — | Partial | — | — | DS (COM), DP (CRY) | 5.5-1 |
| **4.5.2** Verify a suitable Zigbee security architecture is selected per the application's security requirements | 2(d), 2(e) | — | Partial | — | — | DS (COM) | — |
| **4.5.3** Verify the most secure Zigbee network join method is used per security architecture | 2(d), 2(e) | — | Partial | — | — | DI (DAS), DS (ONB) | 5.5-1 |
| **4.5.4** Verify the default global link key (ZigbeeAlliance09) is not used unless explicitly required | 2(b), 2(d) | — | Partial | — | — | DP (KEY), DC (AUT) | 5.1-2, 5.4-1 |
| **4.5.5** Verify user interaction is required to activate Zigbee pairing mode, with automatic timeout | 2(d), 2(j) | — | Partial | — | — | LA (IFC), DS (ONB) | 5.6-1 |
| **4.5.6** Verify Zigbee network key is randomly generated | 2(e) | — | Partial | — | — | DP (KEY) | 5.4-1 |
| **4.5.7** Verify Zigbee network key is periodically rotated | 2(e) | — | Partial | — | — | DP (KEY) | 5.4-3 |
| **4.5.8** Verify users can view paired Zigbee devices to validate legitimacy | 2(d) | — | — | — | — | CS (EIM), DI (AID) | — |
| **4.6.1** Verify LoRaWAN version 1.1 is used by new applications | 2(a), 2(e) | — | Partial | — | — | DS (COM), DP (CRY) | 5.5-1 |
| **4.6.2** Verify LoRaWAN network, join, and application servers are hardened per industry best practices | 2(b), 2(j) | — | Partial | — | — | DC (CTL), DS (COM) | — |
| **4.6.3** Verify all LoRaWAN gateway communications use a secure channel for integrity and authenticity | 2(e), 2(f) | — | Partial | — | — | DP (STX), DS (COM) | 5.5-1 |
| **4.6.4** Verify LoRaWAN root keys are unique per end device | 2(d), 2(e) | — | Partial | — | — | DP (KEY), DI (DAS) | 5.4-1 |
| **4.6.5** Verify LoRaWAN replay attacks are not possible using off-sequence frame counters | 2(f) | — | Partial | — | — | DP (STX), DS (COM) | — |
| **V5 — Hardware Platform Requirements** | | | | | | | |
| **5.1.1** Verify platform supports disabling or protecting debugging interfaces (JTAG, SWD, UART) | 2(j) | — | — | — | — | LA (IFC), DS (OPS) | 5.6-2 |
| **5.1.2** Verify platform supports validating authenticity of the first-stage bootloader | 2(f), 2(k) | — | Partial | — | — | DS (DIN) | 5.7-1 |
| **5.1.3** Verify platform provides cryptographic accelerator functions | 2(e), 2(k) | — | — | — | — | DP (CRY) | — |
| **5.1.4** Verify sensitive data (private keys, certificates) can be stored using dedicated hardware security features | 2(e) | — | — | Partial | — | DP (KEY), DP (STO) | 5.4-1 |
| **5.1.5** Verify platform security configuration can be locked (e.g. OTP fuses) | 2(b), 2(f) | — | Partial | — | — | DS (DIN), DC (CTL) | — |
| **5.1.6** Verify debugging headers are removed from PCBs | 2(j) | — | — | — | — | LA (IFC) | 5.6-2 |
| **5.1.7** Verify hardware has no undocumented debug features or special pin configurations | 2(a), 2(j) | — | — | — | — | DS (DIN), DS (OPS) | 5.6-2 |
| **5.1.8** Verify platform supports memory and I/O protection using MMU | 2(f), 2(k) | — | — | — | — | DS (RSC) | — |
| **5.1.9** Verify platform provides protection against physical decapsulation, side channel, and glitching attacks | 2(k) | — | — | — | — | DS (DIN), DS (OPS) | — |
| **5.1.10** Verify descriptive silkscreens are removed from PCBs | 2(j) | — | — | — | — | DS (OPS) | — |
| **5.1.11** Verify debug paths and traces are depopulated from production PCBs | 2(j) | — | — | — | — | LA (IFC) | 5.6-2 |
| **5.1.12** Verify FPGA bitstreams are encrypted using strong, secure algorithms | 2(e), 2(f) | — | — | — | — | DP (CRY), DP (STO) | — |

---

## Table 2: Framework to ISVS Mapping

This table provides a reverse lookup. For each framework clause, it identifies the ISVS requirements that substantively address that clause. Requirements marked **(P)** provide partial coverage only.

### EU Cyber Resilience Act — Annex I, Part I

| CRA Annex I Part I Clause | Clause Description | ISVS Requirements |
|---------------------------|--------------------|-------------------|
| 2(a) | No known exploitable vulnerabilities at market placement | 1.2.3, 1.2.8**(P)**, 1.3.3**(P)**, 2.1.9, 3.2.3**(P)**, 3.2.4, 3.4.6, 4.5.1**(P)**, 4.6.1**(P)**, 5.1.7 |
| 2(b) | Secure default configuration; factory reset capability | 1.2.3, 1.3.12, 2.1.6, 2.1.8, 3.1.2, 3.2.1, 3.4.5, 3.4.8, 3.5.3, 4.5.4**(P)**, 4.6.2**(P)**, 5.1.5 |
| 2(c) | Security updates; automatic installation with opt-out; 10-year minimum | 1.2.9, 3.4.1, 3.4.2, 3.4.3**(P)**, 3.4.4, 3.4.5, 3.4.6, 3.4.7, 3.4.10**(P)**, 3.4.12 |
| 2(d) | Authentication and access control; prevent unauthorized access | 2.1.1, 2.1.2, 2.1.3, 2.1.4, 2.1.5, 2.1.6, 2.1.7, 2.1.8, 2.1.9, 2.1.10, 2.1.11, 2.2.1, 2.2.2**(P)**, 2.2.3, 2.2.4, 3.4.10, 4.1.3, 4.1.6, 4.2.2, 4.2.3**(P)**, 4.3.2, 4.3.3, 4.3.4, 4.3.6, 4.4.4**(P)**, 4.5.2**(P)**, 4.5.3**(P)**, 4.5.4**(P)**, 4.5.5, 4.5.8, 4.6.4 |
| 2(e) | Data confidentiality; encryption in transit and at rest | 1.3.14**(P)**, 2.3.1, 2.3.4, 2.4.1, 2.4.2, 2.4.3**(P)**, 2.4.4, 2.4.5**(P)**, 2.4.6**(P)**, 3.1.6**(P)**, 3.1.7, 3.2.5, 3.4.9, 3.4.11, 3.4.12, 3.5.1, 3.5.2, 3.5.3**(P)**, 3.5.4, 4.1.1, 4.1.2, 4.1.3, 4.1.6, 4.2.1, 4.2.3, 4.3.5, 4.3.6, 4.3.7, 4.4.2, 4.4.3, 4.5.2, 4.5.3, 4.5.6, 4.6.1**(P)**, 4.6.3, 4.6.4, 5.1.3**(P)**, 5.1.4, 5.1.12 |
| 2(f) | Data integrity; protection against unauthorized modification | 1.2.6, 1.2.7, 1.3.13, 1.4.7, 2.4.1, 2.4.2**(P)**, 3.1.1, 3.1.2, 3.1.4, 3.1.5, 3.1.8, 3.2.8, 3.2.9, 3.2.10, 3.4.3, 3.4.8, 3.4.9, 3.5.1, 4.1.1, 4.1.3, 4.1.6, 4.6.3, 4.6.5, 5.1.2, 5.1.5, 5.1.8, 5.1.12 |
| 2(g) | Data minimization; collect only necessary data | 1.3.14, 1.4.4, 1.4.6**(P)**, 2.3.4 |
| 2(h) | Availability and DoS resilience | 3.3.2, 3.4.7**(P)**, 4.1.4 |
| 2(i) | Network protection; minimize negative impact on connected devices | — |
| 2(j) | Attack surface reduction; minimize external interfaces | 1.1.2, 1.2.4, 1.2.5, 1.3.12**(P)**, 2.2.2, 3.1.1, 3.1.3, 3.2.2, 3.2.3**(P)**, 3.2.11, 3.3.1, 3.3.4, 3.3.5, 3.3.6, 3.6.2, 4.3.1, 4.4.1, 4.4.4**(P)**, 4.5.5, 5.1.1, 5.1.6, 5.1.7, 5.1.10, 5.1.11 |
| 2(k) | Exploitation mitigation (ASLR, DEP, code signing, stack canaries) | 1.2.6**(P)**, 1.2.7, 1.3.3, 1.3.7, 1.3.8, 1.3.9, 1.3.10, 1.3.11, 1.3.15**(P)**, 2.4.3**(P)**, 2.4.5**(P)**, 3.1.1**(P)**, 3.1.4, 3.1.5, 3.1.8, 3.2.6**(P)**, 3.2.7, 3.2.8, 3.2.9, 3.2.10, 3.3.4**(P)**, 3.3.5, 3.3.6, 3.6.1, 5.1.2, 5.1.8, 5.1.9 |
| 2(l) | Security monitoring and logging; user opt-out capability | 1.4.1, 1.4.2, 1.4.3, 1.4.4**(P)**, 1.4.5, 1.4.6**(P)**, 1.4.7**(P)**, 2.2.4 |
| 2(m) | Secure data removal and transfer | 1.4.6**(P)**, 2.2.3**(P)**, 2.3.2, 2.3.3**(P)** |

### EU Cyber Resilience Act — Annex I, Part II (Vulnerability Handling)

| CRA Annex I Part II Obligation | ISVS Requirements |
|-------------------------------|-------------------|
| SBOM — machine-readable, maintained per component | 1.2.1 |
| Continuous vulnerability identification and remediation | 1.2.2, 1.2.8, 1.2.9, 3.2.4 |
| Coordinated Vulnerability Disclosure (CVD) procedure | 1.1.5, 1.1.6 |
| Secure development lifecycle and supply chain integrity | 1.3.1, 1.3.4, 1.3.5, 1.3.6 |

### EU Radio Equipment Directive — Article 3.3(d) / EN 18031-1 (Network Protection)

| RED 3.3(d) / EN 18031-1 Control Area | ISVS Requirements |
|--------------------------------------|-------------------|
| Secure boot and bootloader integrity | 1.2.6**(P)**, 1.2.7, 3.1.1, 3.1.2, 3.1.3, 3.1.4, 3.1.5, 3.4.3**(P)**, 3.4.8, 5.1.2 |
| Access control before network access | 2.1.1**(P)**, 2.1.2**(P)**, 2.1.3**(P)**, 2.1.4**(P)**, 2.1.7**(P)**, 2.1.8**(P)**, 2.1.9**(P)**, 2.1.10**(P)**, 2.2.2**(P)**, 4.2.2**(P)** |
| Network interface hardening and attack surface minimization | 1.1.2**(P)**, 3.2.1**(P)**, 3.2.2, 3.2.3**(P)**, 3.3.2**(P)**, 4.4.1, 4.4.4**(P)** |
| Traffic monitoring and logging | 1.4.1**(P)**, 1.4.2**(P)**, 1.4.5**(P)** |
| DoS prevention and resilience | 3.3.2**(P)**, 4.1.4 |
| Strong cipher suites and secure communication channels | 2.4.2**(P)**, 3.4.10**(P)**, 3.4.12**(P)**, 3.5.4**(P)**, 4.1.1**(P)**, 4.1.2**(P)**, 4.1.3**(P)**, 4.3.5**(P)**, 4.3.7**(P)**, 4.4.2**(P)**, 4.4.3**(P)**, 4.5.1**(P)**, 4.5.2**(P)**, 4.5.3**(P)**, 4.5.5**(P)**, 4.6.2**(P)**, 4.6.3**(P)** |
| Integrity measurement and runtime protection | 3.2.10**(P)**, 3.6.1**(P)**, 5.1.5**(P)** |

### EU Radio Equipment Directive — Article 3.3(e) / EN 18031-2 (Personal Data and Privacy)

| RED 3.3(e) / EN 18031-2 Control Area | ISVS Requirements |
|--------------------------------------|-------------------|
| Encryption of personal, traffic, and location data | 2.3.1**(P)**, 2.4.4**(P)**, 3.1.7**(P)**, 3.2.5**(P)**, 5.1.4**(P)** |
| Data minimization | 1.3.14**(P)**, 1.4.4**(P)**, 2.3.4**(P)** |
| Third-party and unauthorized access control | 2.1.3**(P)**, 2.1.4**(P)** |
| Secure deletion and data removal | 1.4.6**(P)**, 2.3.2**(P)** |
| Privacy-preserving logging | 1.4.4**(P)**, 3.1.6**(P)** |
| Strong cryptographic algorithms | 2.4.2**(P)**, 3.5.4**(P)**, 4.1.2**(P)** |
| Update process respects privacy settings | 3.4.5**(P)** |

### EU Radio Equipment Directive — Article 3.3(f) / EN 18031-3 (Fraud Prevention)

| RED 3.3(f) / EN 18031-3 Control Area | ISVS Requirements |
|--------------------------------------|-------------------|
| Strong authentication for transactions | 2.1.3**(P)**, 4.1.3**(P)** |
| Encrypted transaction channels | 2.4.2**(P)**, 4.1.2**(P)** |
| Transaction signing and integrity | 4.1.3**(P)** |

*Note: RED 3.3(f) applies specifically to payment-capable devices. Most ISVS requirements relevant to fraud prevention address underlying authentication and encryption primitives rather than transaction-specific controls. Teams building payment-capable IoT devices should conduct a dedicated assessment against EN 18031-3.*

### NIST SP 800-213A

| SP 800-213A Sub-Capability | Description | ISVS Requirements |
|---------------------------|-------------|-------------------|
| **Device Identification (DI)** | | |
| DI (IMS) | Identifier Management Support — unique logical device IDs | 1.1.2, 2.1.1, 2.1.2 |
| DI (AID) | Actions Based on Device Identity — access control and monitoring by device identity | 1.1.2, 2.2.3, 2.3.3, 4.5.8 |
| DI (DAS) | Device Authentication Support — authenticate device identity | 2.1.3, 2.1.10, 2.1.11, 4.3.2, 4.3.6, 4.6.4 |
| DI (PID) | Physical Identifiers — unique physical identifiers | — |
| **Device Configuration (DC)** | | |
| DC (PRV) | Logical Access Privilege Configuration | — |
| DC (AUT) | Authentication and Authorization Configuration — auth policies, credential defaults | 1.2.3, 2.1.4, 2.1.6, 2.1.8, 2.1.9, 3.5.3, 4.5.4 |
| DC (INT) | Interface Configuration | — |
| DC (CTL) | Device Configuration Control — settings, baseline restoration, update control | 1.2.3, 1.3.12, 3.1.2, 3.2.1, 3.4.5, 4.6.2, 5.1.5 |
| **Data Protection (DP)** | | |
| DP (CRY) | Cryptography Capabilities and Support — algorithms, signing, hashing, encryption | 1.3.13, 1.4.7, 2.4.2, 2.4.3, 2.4.5, 2.4.6, 3.1.5, 3.2.6, 3.4.3, 3.4.9, 3.5.1, 3.5.4, 3.6.1, 4.1.2, 4.3.5, 4.3.7, 4.4.2, 4.4.3, 4.5.1, 4.6.1, 5.1.3, 5.1.12 |
| DP (KEY) | Cryptographic Key Management — key generation, storage, rotation | 2.1.9, 2.1.10, 2.4.1, 2.4.3, 2.4.4, 3.5.2, 3.5.3, 4.5.4, 4.5.6, 4.5.7, 4.6.4, 5.1.4 |
| DP (STO) | Secure Storage — data at rest encryption, sanitization/purging | 1.3.14, 1.4.4, 2.3.1, 2.3.2, 2.3.4, 2.4.4, 3.1.6, 3.1.7, 3.2.5, 3.4.11, 5.1.4, 5.1.12 |
| DP (STX) | Secure Transmission — cryptographic algorithms for data in transit, integrity | 1.1.4, 3.4.12, 3.5.1, 4.1.1, 4.1.3, 4.1.6, 4.1.7, 4.2.1, 4.2.3, 4.6.3, 4.6.5 |
| **Logical Access to Interfaces (LA)** | | |
| LA (AUN) | Authentication Support — require auth before connecting | 2.1.3, 2.1.4, 3.4.10, 4.1.3, 4.1.6, 4.2.2, 4.2.3, 4.3.6 |
| LA (ACF) | Authentication Configuration — lockout, password policies, account management | 2.1.5, 2.1.6, 2.1.7, 2.1.8, 2.1.11, 4.3.2, 4.3.3, 4.3.4 |
| LA (USE) | System Use Notification Support | — |
| LA (AUZ) | Authorization Support — authorized users and processes | 1.1.4, 2.2.1, 2.2.3, 3.3.6, 4.2.2 |
| LA (AIM) | Authentication and Identity Management | — |
| LA (ROL) | Role Support and Management — least privilege, role hierarchies | 2.2.1, 2.2.2, 2.2.4, 3.3.4 |
| LA (LDU) | Limitations on Device Usage | — |
| LA (XCN) | External Connections — third-party system interaction | 4.1.3**(P)**, 4.1.6**(P)**, 4.2.2**(P)**, 4.2.3**(P)** |
| LA (IFC) | Interface Control — ports, wireless config, remote access, disable unused interfaces | 1.2.4, 1.2.5, 1.3.12, 3.1.3, 3.2.2, 3.2.3, 3.2.11, 3.6.2, 4.3.1, 4.3.7, 4.4.1, 4.4.4, 4.5.5, 5.1.1, 5.1.6, 5.1.11 |
| **Software Update (SU)** | | |
| SU (UPD) | Update Capabilities — authorized updates, signature/checksum verification, source verification | 1.2.9, 1.3.4, 1.3.13, 3.1.4, 3.2.4, 3.4.1, 3.4.3, 3.4.4, 3.4.6, 3.4.8, 3.4.9, 3.4.10, 3.4.12 |
| SU (APP) | Update Application Support — remote/local delivery, automatic verification | 3.4.1, 3.4.2, 3.4.5, 3.4.7 |
| **Cybersecurity State Awareness (CS)** | | |
| CS (AEI) | Access to Event Information — access to device cybersecurity state | 1.4.5**(P)** |
| CS (EIM) | Event Identification and Monitoring — detect events, monitor traffic, config changes | 1.4.1, 2.2.4, 4.1.4, 4.5.8 |
| CS (EVR) | Event Response — alerts, responses to security events | — |
| CS (LCT) | Logging Capture and Trigger Support — audit log generation | 1.4.1, 2.3.3 |
| CS (RDL) | Support of Required Data Logging — user interactions, event type/time/source/outcome | 1.4.2, 1.4.4 |
| CS (LSR) | Audit Log Storage and Retention — persistent storage, retention, deletion policies | 1.4.6 |
| CS (SRT) | Support for Reliable Time — time synchronization, timestamps | 1.4.3 |
| CS (AUP) | Audit Support and Protection — log reporting, protection, integrity | 1.4.5, 1.4.7 |
| **Device Security (DS)** | | |
| DS (EXE) | Secure Execution — execution policies, isolated environments, separation of domains | 1.2.6, 1.3.3, 1.3.7, 1.3.8, 1.3.9, 1.3.10, 1.3.11, 1.3.15, 3.1.1, 3.1.8, 3.2.6, 3.2.7, 3.2.11, 3.3.1, 3.3.4, 3.3.5, 3.3.6, 3.6.2 |
| DS (COM) | Secure Communication — traffic flow, standardized protocols, session management | 3.2.2, 3.2.3, 4.1.1, 4.1.2, 4.5.1, 4.5.2, 4.6.1, 4.6.2, 4.6.3, 4.6.5 |
| DS (RSC) | Secure Resource Usage — memory management, shared resources, disk quotas | 2.3.4, 3.1.8, 3.2.7, 3.2.8, 3.2.9, 3.3.1, 3.3.2, 5.1.8 |
| DS (DIN) | Device Integrity — security compliance checks, unauthorized component detection | 1.1.2, 1.2.2, 1.2.6, 1.2.7, 1.3.6, 3.1.1, 3.1.2, 3.1.4, 3.1.5, 3.2.10, 3.4.6, 3.4.8, 3.6.1, 5.1.2, 5.1.5, 5.1.7, 5.1.9 |
| DS (ONB) | Secure Network Onboarding Support | 4.5.3, 4.5.5 |
| DS (OPS) | Secure Device Operation — operational states, fail-secure, time, restrictive modes | 1.2.4, 2.2.2, 2.3.2, 3.1.3, 3.3.2, 3.4.7, 4.1.4, 5.1.1, 5.1.7, 5.1.9, 5.1.10 |
| **Non-Technical Supporting Capabilities** | | |
| Non-tech (DOC) | Documentation | 1.2.1, 1.2.2, 1.2.8, 1.3.1, 1.3.2, 1.3.5 |
| Non-tech (BUG) | Vulnerability/cybersecurity information reception | 1.1.5 |
| Non-tech (VNT) | Cybersecurity event notification | 1.1.6 |

### ETSI EN 303 645 v2.1.1

| EN 303 645 Provision | Provision Title | ISVS Requirements |
|---------------------|-----------------|-------------------|
| 5.1 (Provision 1) | No universal default passwords | 2.1.5, 2.1.6, 2.1.7, 2.1.8, 2.1.9, 2.1.10, 4.3.2, 4.3.3, 4.3.4, 4.5.4 |
| 5.2 (Provision 2) | Implement means to manage vulnerability reports | 1.1.5, 1.1.6 |
| 5.3 (Provision 3) | Keep software updated | 1.2.9, 3.2.4, 3.4.1, 3.4.2, 3.4.3, 3.4.4, 3.4.5**(P)**, 3.4.6, 3.4.7 |
| 5.4 (Provision 4) | Securely store sensitive security parameters | 2.4.1, 2.4.4, 3.1.6**(P)**, 3.5.2, 3.5.3, 4.5.6, 4.6.4**(P)**, 5.1.4 |
| 5.5 (Provision 5) | Communicate securely | 2.4.2**(P)**, 3.4.12, 3.5.4**(P)**, 4.1.1, 4.1.2, 4.1.3, 4.1.6, 4.2.3, 4.3.5, 4.3.6, 4.3.7, 4.4.2, 4.4.3, 4.5.1**(P)**, 4.5.3**(P)**, 4.6.1**(P)**, 4.6.3 |
| 5.6 (Provision 6) | Minimize exposed attack surfaces | 1.1.2, 1.2.4, 1.2.5, 1.3.12**(P)**, 2.2.2, 2.2.4, 3.1.3, 3.2.2, 3.2.3**(P)**, 3.2.11, 3.3.4, 3.3.5, 3.3.6, 3.6.2, 4.3.1, 4.4.1, 4.4.4, 4.5.5, 5.1.1, 5.1.6, 5.1.7, 5.1.10, 5.1.11 |
| 5.7 (Provision 7) | Ensure software integrity | 1.2.6, 1.2.7, 1.3.13, 3.1.1, 3.1.2, 3.1.4, 3.1.5, 3.2.10**(P)**, 3.4.3, 3.4.8, 3.6.1, 5.1.2 |
| 5.8 (Provision 8) | Ensure personal data is secure | 1.3.14, 1.4.4, 1.4.6**(P)**, 2.3.1, 2.3.4, 3.1.7, 3.2.5 |
| 5.9 (Provision 9) | Make systems resilient to outages | 3.3.2, 3.4.7**(P)**, 4.1.4 |
| 5.10 (Provision 10) | Examine system telemetry data | 1.4.1, 1.4.2, 1.4.5 |
| 5.11 (Provision 11) | Make it easy for users to delete personal data | 1.4.6**(P)**, 2.2.3**(P)**, 2.3.2, 2.3.3**(P)** |
| 5.12 (Provision 12) | Make installation and maintenance of devices easy | 3.4.5**(P)** |
| 5.13 (Provision 13) | Validate input data | 1.1.4**(P)**, 1.3.15 |

---

## References

- **EU Cyber Resilience Act (CRA):** Regulation (EU) 2024/2847 of the European Parliament and of the Council — <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=OJ:L_202402847>
- **EU Radio Equipment Directive (RED):** Directive 2014/53/EU — <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32014L0053>
- **RED Delegated Regulation 2022/30:** Commission Delegated Regulation (EU) 2022/30 — <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32022R0030>
- **EN 18031-1:** ETSI/CEN harmonized standard for network protection — <https://www.etsi.org/deliver/etsi_en/18031_18031099/1803101/>
- **EN 18031-2:** ETSI/CEN harmonized standard for personal data and privacy — <https://www.etsi.org/deliver/etsi_en/18031_18031099/1803102/>
- **EN 18031-3:** ETSI/CEN harmonized standard for fraud prevention — <https://www.etsi.org/deliver/etsi_en/18031_18031099/1803103/>
- **NIST SP 800-213A:** IoT Device Cybersecurity Requirements Catalog — <https://doi.org/10.6028/NIST.SP.800-213A>
- **ETSI EN 303 645 v2.1.1:** Cyber Security for Consumer Internet of Things: Baseline Requirements — <https://www.etsi.org/deliver/etsi_en/303600_303699/303645/02.01.01_60/en_303645v020101p.pdf>
- **OWASP ISVS:** IoT Security Verification Standard — <https://owasp.org/www-project-iot-security-verification-standard/>
