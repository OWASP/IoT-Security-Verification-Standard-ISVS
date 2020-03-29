##V8: Embedded OS & Applications Requirements

## Control Objective
TODO: Control Objective description

## Security Verification Requirements

### Embedded OS & Applications Requirements

| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **8.1.1** | Verify that the Embedded OS is securely configured (e.g. consult vendor security best practices or CIS benchmarks where applicable).| ✓ | ✓ |   |
| **8.1.1** | Verify that applications are secure (e.g. consult OWASP ASVS for web applications). | ✓ | ✓ |   |
| **8.1.1** | Verify if all network services exposed by the device on every network adapter are necessary services. | ✓ | ✓ |   |
| **8.1.1** | Verify that all software components used are up to date and are vulnerable to any known vulnerabilities. | ✓ | ✓ |   |
| **8.1.1** | Verify that internal IP ranges (e.g. localhost or those reserved for backend services) are not reachable from the device LAN. | ✓ | ✓ |   |
| **8.1.1** | Verify banned insecure C/C++  functions do not exist within source code. | ✓ | ✓ |   |
| **8.1.1** | Verify that applications running on the device use the security features of the underlying operating system or kernel. | ✓ | ✓ |   |
| **8.1.1** | Verify that memory protection controls such as ASLR and DEP are enabled by the embedded operating system, if applicable. | ✓ | ✓ |   |
| **8.1.1** | Verify that the operating system provides mechanisms to avoid exploitation of buffer overflows (e.g. secure compiler flags such as -fPIE, -fstack-protector-all, -Wl,-z,noexecstack, -Wl,-z,noexecheap). | ✓ | ✓ |   |
| **8.1.1** | Device firmware should be designed to isolate privileged code, processes and data from portions of the firmware that do not need access to them, and device hardware should provide isolation concepts to prevent unprivileged from accessing security sensitive code. in order to minimize the potential for compromised code to access those code and/or data. | ✓ | ✓ |   |
| **8.1.1** | Verify hardware level memory protection is used and privilege levels are enforced. | ✓ | ✓ |   |
| **8.1.1** | Verify the embedded OS provides protection against unauthorized access to RAM (e.g. RAM scrambling). | ✓ | ✓ |   |
| **8.1.1** | Verify that operations that process core secrets or cryptographic keys utilize RAM that is internal to the MCU. | ✓ | ✓ |   |
| **8.1.1** | Verify unprivileged software is restricted from accessing privileged resources such as drivers, configuration files and other objects. | ✓ | ✓ |  |

### Superloop application Requirements

| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **8.2.1** | Lorem Ipsum | ✓ | ✓ |   |

## Requirements Mapping

| # | ENISA | ... |
| -- | ---------------------- | ---------------------- |
|**8.1.1**| Lorem Ipsum | ... |

## References
