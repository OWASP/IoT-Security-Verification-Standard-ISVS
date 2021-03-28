# V1: IoT Ecosystem Requirements

## Control Objective

System security design performed before development, and a security process that continuously supports system development integrated into all phases of its lifecycle, are necessary fundamentals for creating secure product architecture implementations. Iterative system threat modeling provides a means to prepare for malintent and develop mitigation plans as part of product design lifecycles.

A secure development process ensures the identification and documentation of all sensitive information and functionality required for the system, enforces all the security controls at the determined level, and ensures that end-users and customers get notified about vulnerabilities and that security solutions deliver on time. Ensure to incorporate sister OWASP verification standards as part of development processes provided in the references section below.

The supply chain has vital importance for the security of every product. A secure development process verifies that all security requirements for suppliers and third-party code implement controls with the appropriate security level and development-time features are not left on devices, exposing them to vulnerabilities.

To ensure the security of all software produced, the build process for the system software must be done in a secure build environment that verifies the integrity and authenticity of all components. The code must be written using best security practices and compiled using the best security options available.

System configuration changes must employ appropriate logging and monitoring capabilities to provide audit trails for security events. Attributes detailing events aid with investigations while overly verbose logs containing sensitive information introduce security risks.

## Security Verification Requirements

### Application and Ecosystem Design

| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **1.1.1** | Verify that all applications in the IoT ecosystem are developed with a level of security that is in line with the security criticality of the application. | ✓ | ✓ | ✓ |
| **1.1.2** | Verify that all components and communication channels in the IoT application's ecosystem have been identified and are known to be needed. Remove or disable any that aren't necessary. | ✓ | ✓ | ✓ |
| **1.1.3** | Verify the use of threat modeling as part of each product introduction design (i.e. new and mature) and security-relevant feature changes to identify likely threats and facilitate appropriate risk responses to guide security testing. | ✓ | ✓ | ✓ |
| **1.1.4** | Verify that security controls are enforced server-side and that data and instructions are not blindly trusted by server-side components. | ✓ | ✓ | ✓ |
| **1.1.5** | Verify that a responsible disclosure policy has been established and that it is easily found on the company website. Ensure that the policy provides a clear overview on how vulnerabilities can be communicated securely and how they'll be followed up on. | ✓ | ✓ | ✓ |
| **1.1.6** | Verify that users and relevant stakeholders are informed when vulnerabilities affect products through established communication channels (website, e-mail, security advisory pages, changelogs, etc.). | ✓ | ✓ | ✓ |


### Supply Chain
| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **1.2.1** | Verify that each application (including firmware) in the ecosystem maintains a software bill of materials (SBOM) cataloging third-party components, versioning, and published vulnerabilities. | ✓ | ✓ | ✓ |
| **1.2.2** | Verify that potential areas of risk that come with the use of third-party and open-source software have been identified and that actions to mitigate such risks have been taken. | ✓ | ✓ | ✓ |
| **1.2.3** | Verify the device is released with firmware configured with secure defaults appropriate for a release build (as opposed to debug versions). | ✓ | ✓ | ✓ |
| **1.2.4** | Verify that access to debugging interfaces (e.g. JTAG, SWD) is disabled or protected before shipping the device. Processors may refer to this as code protection, read back protection, CodeGuard, or access port protection. | | ✓ | ✓ |
| **1.2.5** | Verify that debug capabilities in FPGAs are disabled on production PCBs. | | ✓ | ✓ |
| **1.2.6** | Verify that devices are provisioned with a cryptographic root of trust that is hardware-based and immutable. | | ✓ | ✓ |
| **1.2.7** | Verify that code integrity protection mechanisms are enabled and locked in hardware before shipping the device to customers. For example, ensure secure boot is enabled and the boot configuration locked. | | ✓ | ✓ |
| **1.2.8** | Verify third-party code and components are analyzed using static analysis tools to ensure backdoors are not introduced. | | ✓ | ✓ |
| **1.2.9** | Verify that all components including semiconductor drivers, SDKs, and modules (5G, LTE, Bluetooth, Wi-Fi, ZigBee) can be updated to provide security patches in alignment with the product's support or end-of-life policy. | | ✓ | ✓ |

### Secure Development

| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **1.3.1** | Verify that each application in the ecosystem is built using a secure and repeatable build environment. | ✓ | ✓ | ✓ |
| **1.3.2** | Verify GPL based firmware has its source code published and that no sensitive or proprietary information is accidentally included in the process. | ✓ | ✓ | ✓ |
| **1.3.3** | Verify that use of banned C/C++ functions (memcpy, strcpy, gets, etc.) are replaced with safe equivalents functions (e.g. Safe C, Safe Strings library). | | ✓ | ✓ |
| **1.3.4** | Verify packages are downloaded and built from trusted sources. | ✓ | ✓ | ✓ |
| **1.3.5** | Verify build pipelines only perform builds of source code maintained in version control systems. | ✓ | ✓ | ✓ |
| **1.3.6** | Verify that compilers, version control clients, development utilities, and software development kits are analyzed and monitored for tampering, trojans, or malicious code | ✓ | ✓ | ✓ |
| **1.3.7** | Verify packages are compiled with Object Size Checking (OSC) (e.g. -D_FORTIFY_SOURCE=2). | | ✓ | ✓ |
| **1.3.8** | Verify packages are compiled with No eXecute (NX) or Data Execution Protection (DEP) (e.g. -z,noexecstack). | | ✓ | ✓ |
| **1.3.9** | Verify packages are compiled with Position Independent Executable (PIE) (e.g. -fPIE). | | ✓ | ✓ |
| **1.3.10** | Verify packages are compiled with Stack Smashing Protector (SSP) (e.g. -fstack-protector-all). | | ✓ | ✓ |
| **1.3.11** | Verify packages are compiled with read-only relocation (RELRO) (e.g. -Wl,-z,relro). | | ✓ | ✓ |
| **1.3.12** | Verify release builds do not contain debug code or privileged diagnostic functionality. | ✓ | ✓ | ✓ |
| **1.3.13** | Verify that debug and release firmware images are signed using different keys. | | ✓ | ✓ |
| **1.3.14** | Verify that debug information does not contain sensitive information, such as PII, credentials or cryptographic material. | ✓ | ✓ | ✓ |
| **1.3.15** | Verify that embedded applications are not susceptible to OS command injection by performing input validation and escaping of parameters within firmware code, shell command wrappers, and scripts. | ✓ | ✓ | ✓ |

### Logging

| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **1.4.1** | Verify that devices can collect logs about events with security implications, such as successful and failed authentication attempts, access to debugging functionality etc. | | ✓ | ✓ |
| **1.4.2** | Verify that collected logs have the adequate granularity to enable actionable insights and alerts. Logs should include, at a minimum, the type of event, timestamp, source, outcome, and identification of involved actors. | | ✓ | ✓ |
| **1.4.3** | Verify that devices contain or are synchronized with a reliable time source, to ensure the validity of log timestamps. | | ✓ | ✓ |
| **1.4.4** | Verify that collected logs do not include sensitive information, such as PII, credentials and cryptographic keys. | | ✓ | ✓ |
| **1.4.5** | Verify that collected logs can be securely retrieved from the devices over an online collection, either periodically or on-demand. | | ✓ | ✓ |
| **1.4.6** | Verify that collected logs are preserved for the amount of time required by organizational policies and that they are safely deleted when the retention period is over. | | ✓ | ✓ |
| **1.4.7** | Verify that the confidentiality, integrity and authenticity of collected logs is appropriately protected, both on the devices that created them and on other systems that store or process them. | | ✓ | ✓ |

## References
For more information, see also:

- OWASP ASVS: <https://owasp.org/www-project-application-security-verification-standard/>
- OWASP MASVS: <https://owasp.org/www-project-mobile-security-testing-guide/>
- OWASP Threat Modeling: <https://owasp.org/www-community/Application_Threat_Modeling>
- OWASP SCVS: <https://owasp.org/www-project-software-component-verification-standard/>
- OWASP Software Assurance Maturity Model: <https://owaspsamm.org/>
- OWASP Secure SDLC Cheat Sheet: <https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets_excluded/Secure_SDLC_Cheat_Sheet.md>
- Microsoft SDL: <https://www.microsoft.com/en-us/sdl/>
- OWASP C-based Toolchain Hardening Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/C-Based_Toolchain_Hardening_Cheat_Sheet.html>
- OWASP Embedded Application Security: <https://owasp.org/www-project-embedded-application-security/>
- Banned C Functions (Safe Strings library): <https://github.com/intel/safestringlib/wiki/SDL-List-of-Banned-Functions>
- NIST Draft NISTIR 8259D: <https://nvlpubs.nist.gov/nistpubs/ir/2020/NIST.IR.8259D-draft.pdf>
