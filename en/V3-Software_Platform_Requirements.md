# V3: Software Platform Requirements

## Control Objective

## Security Verification Requirements

### Bootloader

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **3.1.1** | Verify that communication interfaces such as, USB, UART, and other variants are disabled or adequately protected during every stage of the device's boot process. | ✓ | ✓ | ✓ |
| **3.1.2** | Verify that the authenticity of the first stage bootloader is verified by a trusted component of which the configuration cannot be altered. | ✓ | ✓ | ✓ |
| **3.1.3** | Verify that the authenticity of next bootloader stages or application code is cryptographically verified during every step of the boot process. | ✓ | ✓ | ✓ |
| **3.1.4** | Verify that the bootloader does not allow code to be loaded from arbitrary locations. Locations include both storage (SD, USB, etc.) and network locations (over TCP/IP). | ✓ | ✓ | ✓ |
| **3.1.5** | Verify bootloader configurations are immutable. | ✓ | ✓ | ✓ |
| **3.1.6** | Verify that bootloader stages do not contain sensitive information (e.g. private keys or passwords logged to the console) as part of device start-up.  | ✓ | ✓ | ✓ |
| **3.1.7** | Verify that firmware is stored in an encrypted volume at rest. | ✓ | ✓ | ✓ |

### OS Configuration

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **3.2.1** | Verify that the embedded operating is configured according to industry best practices, benchmarks, and uses secure defaults. | ✓ | ✓ | ✓ |
| **3.2.2** | Verify that all network services exposed by the device on every network interface are necessary services and remove any unnecessary ones.| ✓ | ✓ | ✓ |
| **3.2.3** | Verify that the OS kernel and software components used are up to date and are not vulnerable to any known vulnerabilities. | ✓ | ✓ | ✓ |
| **3.2.4** | Verify that applications running on the device use the security features of the underlying operating system or kernel. Including cryptography, key storage, random number generation, authentication and authorization, logging, communications security. | ✓ | ✓ | ✓ |
| **3.2.5** | Verify that memory protection controls such as Address Space Layout Randomization (ASLR) and Data Execution Prevention (DEP) are enabled by the embedded operating system. | ✓ | ✓ | ✓ |
| **3.2.6** | Verify that device firmware isolates privileged code, processes and data from portions of the firmware that do not need access to them, and device hardware should provide isolation concepts to prevent unprivileged code from accessing security sensitive code in order to minimize the potential for compromised code to access those code and/or data. | ✓ | ✓ | ✓ |
| **3.2.7** | Verify that isolation concepts are provided by leveraging dedicated hardware functionality, if applicable.  | ✓ | ✓ | ✓ |
| **3.2.8** | Verify hardware level memory protection is used and privilege levels are enforced. | ✓ | ✓ | ✓ |
| **3.2.9** | Verify the embedded OS provides protection against unauthorized access to RAM (e.g. RAM scrambling). | ✓ | ✓ | ✓ |
| **3.2.10** | Verify that an Integrity Measurement Architecture (IMA) is in use and appropriately configured. | ✓ | ✓ | ✓ |
| **3.2.11** | Verify that that third-party applications and services are configured to execute within a containerized runtime environment (e.g. LXC, Docker, etc.). | ✓ | ✓ | ✓ |
| **3.2.12** | Verify that persistent filesystem storage volumes are encrypted. | ✓ | ✓ | ✓ |

#### Linux

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **3.3.1** | Verify that processes are isolated using Linux kernel namespaces. | ✓ | ✓ | ✓ |
| **3.3.2** | Verify that critical processes are configured to limit resources using control groups (cgroups). | ✓ | ✓ | ✓ |
| **3.3.3** | Verify that processes are not running as root. | ✓ | ✓ | ✓ |
| **3.3.4** | Verify that Linux kernel capabilities are configured with a minimal set for processes that require elevated access. | ✓ | ✓ | ✓ |
| **3.3.5** | Verify the use of kernel security modules such as SELinux, AppArmor, GRSEC, and alike. | ✓ | ✓ | ✓ |
| **3.3.6** | Verify that SECure COMPuting  (seccomp BPF) with filters are used and properly configured to only allow necessary system calls. | ✓ | ✓ | ✓ |

### Software Updates

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **3.4.1** | Verify that packages and user space applications use over the air updates decoupled from firmware updates. | ✓ | ✓ | ✓ |
|**3.4.2**| Verify that devices can be updated automatically upon a pre-defined schedule. | ✓ | ✓ | ✓ |
|**3.4.3**| Verify that the authenticity of updates are cryptographically signed by a trusted source and verified before execution. | ✓ | ✓ | ✓ |
|**3.4.4**| Verify that the update process is not vulnerable to time-of-check time-of-use attacks (TOCTOU). This is generally accomplished by applying the update right after the authenticity of the update is validated.  | ✓ | ✓ | ✓ |
|**3.4.5**| Verify that updates do not modify user-configured preferences, security, and/or privacy settings without notifying the user.  | ✓ | ✓ | ✓ |
|**3.4.6**| Verify that the device cannot be downgraded to known vulnerable versions (anti-rollback). | ✓ | ✓ | ✓ |
|**3.4.7**| Verify that in the event of an update failure, the device reverts to a backup image or notifies the IoT ecosystem. | ✓ | ✓ | ✓ |
|**3.4.8**| Verify that unsigned debug pre-production firmware builds can not be flashed onto devices. | ✓ | ✓ | ✓ |
|**3.4.9**| Verify that encrypted firmware images are securely decrypted on the device. | ✓ | ✓ | ✓ |
|**3.4.10**| Verify that the device authenticates to the  update server component prior to downloading the update.| ✓ | ✓ | ✓ |
|**3.4.11**| Verify that firmware updates are stored encrypted server-side. | ✓ | ✓ | ✓ |

### TPM, SE and other secure hardware integrations

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **3.5.1** | Verify that encryption is used on the bus between the TPM, SE and the MCU. | ✓ | ✓ | ✓ |
| **3.5.2** | Verify that the keys (either secret or private) used to enable encryption on the serial bus are properly secured on the host MCU side. | ✓ | ✓ | ✓ |
| **3.5.3** | Verify any default vendor keys used in bus encryption are replaced in production builds. | ✓ | ✓ | ✓ |
| **3.5.4** | Verify that deprecated or insecure ciphers and hash functions (ex. 3DES, SHA1) in new applications are not used, even if those are provided by the SE. | ✓ | ✓ | ✓ |
| **3.5.5** | Verify that in case a mechanism such as signatures / attestations is used to verify the authenticity of data provided by the SE, ensure the proof is correctly verified for authenticity and freshness. | ✓ | ✓ | ✓ |
| **3.5.6** | Verify that if the SE is used in a multi-tenant setting, appropriate authentication and access control for different tenants is used. Verify that different tenants are required to authenticate to the SE and verify that cryptographic material on the SE is protected by access policies so that only its intended users can access it. | ✓ | ✓ | ✓ |

### Kernel space application requirements

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **3.6.1** | Verify that loaded kernel modules are cryptographically signed and verified. | ✓ | ✓ | ✓ |
| **3.6.2** | Verify that only required kernel modules are enabled during runtime. | ✓ | ✓ | ✓ |

## Requirements Mapping

| # | ENISA | ... |
| --  | ---------------------- | ---------------------- |
|**5.1**| Lorem Ipsum | ... |

## References
