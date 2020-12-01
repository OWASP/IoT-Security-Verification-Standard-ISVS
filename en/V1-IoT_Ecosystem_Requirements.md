# V1: IoT Ecosystem Requirements

## Control Objective

## Security Verification Requirements

### Application and Ecosystem Design

| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **1.1.1** | Verify that all applications in the IoT ecosystem are developed with a level of security that is in line with the security criticality of the application. | ✓ | ✓ | ✓ |
| **1.1.2** | Verify that all components and communication channels in the IoT application's ecosystem have been identified and are known to be needed. Remove or disable any that aren't necessary. | ✓ | ✓ | ✓ |
| **1.1.3** | Verify that sensitive information and security critical actions have been identified and documented. | ✓ | ✓ | ✓ |
| **1.1.4** | Verify that the location where sensitive data is stored in the ecosystem is clearly identified and separated from unprivileged storage locations. | ✓ | ✓ | ✓ |
| **1.1.5** | Verify that security controls are enforced server-side and that data and instructions are not blindly trusted by server-side components. | ✓ | ✓ | ✓ |
| **1.1.6** | Verify that a responsible disclosure policy has been established and that it is easily found on the company website. Ensure that the policy provides a clear overview on how vulnerabilities can be communicated securely and how they'll be followed up on. | ✓ | | |
| **1.1.7** | Verify that users and relevant stakeholders are notified when vulnerabilities are identified through established communication channels (website, e-mail ...). | ✓ | ✓ | ✓ |


### Supply Chain
| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **1.2.1** | Verify that each application in the ecosystem maintains a software bill of materials (SBOM) cataloging third-party components, versioning, and published vulnerabilities. | ✓ | ✓ | ✓ |
| **1.2.2** | Verify that potential areas of risk that come with the use of third-party and open-source software have been identified and that actions to mitigate such risks have been taken. | ✓ | ✓ | ✓ |
| **1.2.3** | Verify that access to debugging interfaces (e.g. JTAG, SWD) is disabled or protected before shipping the device to customers.   | | ✓ | ✓ |
| **1.2.4** | Verify debug capabilities in FPGAs are disabled. | | ✓ | ✓ |
| **1.2.5** | Verify that devices are provisioned with a cryptographic root of trust that is hardware-based and immutable. | | ✓ | ✓ |
| **1.2.6** | Verify that code integrity protection mechanisms are enabled before shipping the device to customers. For example, ensure secure boot is enabled. | | ✓ | ✓ |
| **1.2.7** | Verify third-party code and components are analyzed using static analysis tools to ensure backdoors are not introduced. | | ✓ | ✓ |
| **1.2.8** | Verify debug paths and traces are depopulated from production PCBs. | | | ✓ |

### Secure Development

| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **1.3.1** | Verify that each application in the ecosystem is built using a secure and repeatable build environment. | ✓ | ✓ | ✓ |
| **1.3.2** | Verify GPL based firmware has its source code published and that no sensitive or proprietary information is accidentally included in the process. | ✓ | ✓ | ✓ |
| **1.3.3** | Verify that C/C++ code are using safe C libraries. | | ✓ | ✓ |
| **1.3.4** | Verify packages are downloaded and built from trusted sources. | ✓ | ✓ | ✓ |
| **1.3.5** | Verify build pipelines only perform builds of source code maintained in version control systems. | ✓ | ✓ | ✓ |
| **1.3.6** | Verify that compilers, version control clients, development utilities, and software development kits are analyzed and monitored for tampering, trojans, or malicious code | ✓ | ✓ | ✓ |
| **1.3.7** | Verify packages are compiled with Object Size Checking (OSC). e.g. -D_FORTIFY_SOURCE=2 | | ✓ | ✓ |
| **1.3.8** | Verify packages are compiled with No eXecute (NX) or Data Execution Protection (DEP). e.g. -z,noexecstack | | ✓ | ✓ |
| **1.3.9** | Verify packages are compiled with Position Independent Executable (PIE). e.g. -fPIE | | ✓ | ✓ |
| **1.3.10** | Verify packages are compiled with Stack Smashing Protector (SSP). e.g. -fstack-protector-all | | ✓ | ✓ |
| **1.3.11** | Verify packages are compiled with read-only relocation (RELRO). e.g. -Wl,-z,relro | | ✓ | ✓ |
| **1.3.12** | Verify release builds do not contain debug code or privileged diagnostic functionality. | ✓ | ✓ | ✓ |

## References
For more information, see also: 
- OWASP ASVS: <https://owasp.org/www-project-application-security-verification-standard/> 
- OWASP MASVS: <https://github.com/OWASP/owasp-masvs> 
- OWASP Threat modelling: <https://owasp.org/www-community/Application_Threat_Modeling>
- OWASP Secure SDLC Cheat Sheet: <https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets_excluded/Secure_SDLC_Cheat_Sheet.md>
- Microsoft SDL: <https://www.microsoft.com/en-us/sdl/>
- OWASP C-based Toolchain Hardening Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/C-Based_Toolchain_Hardening_Cheat_Sheet.html>
