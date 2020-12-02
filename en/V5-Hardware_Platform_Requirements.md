# V5: Hardware Platform Requirements

## Control Objective

## Security Verification Requirements

### Design

| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **5.1.1** | Verify that the platform supports disabling or protected access to debugging interfaces (e.g. JTAG, SWD). | ✓ | ✓ |   |
| **5.1.2** | Verify that the platform provides code integrity protection mechanisms such as write-protecting flash. | ✓ | ✓ |   |
| **5.1.3** | Verify that the platform provides memory and I/O protection capabilities to limit access so that only privileged processes can access certain memory areas. | ✓ | ✓ |   |
| **5.1.4** | Verify that cryptographic functions are provided by the platform. Either directly by the MCU, a cryptographic coprocessor, or by an external TPM or SE module. | ✓ | ✓ |   |
| **5.1.5** | Verify that sensitive data such as private keys and certificates can be stored securely by leveraging dedicated hardware security features. Consider making use of a Secure Element, TPM or TEE (Trusted Execution Environment). | ✓ | ✓ |   |
| **5.1.6** | Verify that the platform provides support for trusted execution environments. | ✓ | ✓ |   |
| **5.1.7** | Verify that the platform provides protection against physical decapsulation, side channel and glitching attacks. | ✓ | ✓ |   |
| **5.1.8** | Verify descriptive silkscreens are removed from PCBs. | ✓ | ✓ |   |
| **5.1.9** | Verify the use of a memory protection unit (MPU) to protect access of sensitive regions of memory. | ✓ | ✓ |   |

## References
