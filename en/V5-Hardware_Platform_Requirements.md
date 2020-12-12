# V5: Hardware Platform Requirements

## Control Objective

## Security Verification Requirements

### Design

| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **5.1.1** | Verify that the platform supports disabling or protecting access to debugging interfaces (e.g. JTAG, SWD). | | ✓ | ✓ |
| **5.1.2** | Verify that the platform supports validating the authenticity of the first stage bootloader. | | ✓ | ✓ |
| **5.1.3** | Verify that cryptographic functions are provided by the platform. e.g. by leveraging dedicated functionality provided by the main chip or by external security chips. | | ✓ | ✓ |
| **5.1.4** | Verify that sensitive data such as private keys and certificates can be stored securely by leveraging dedicated hardware security features. | | ✓ | ✓ |
| **5.1.5** | Verify that the platform provides memory and I/O protection capabilities so that only privileged processes can access certain resources. | | ✓ | ✓ |
| **5.1.6** | Verify that the platform security configuration of the platform can be locked. e.g. through burning OTP fuses.  | | ✓ | ✓ |
| **5.1.7** | Verify that debugging headers are removed from PCBs. | | ✓  | ✓ |
| **5.1.8** | Verify the chosen hardware has no unofficially documented debug features, such as special pin configurations that can enable or disable certain functionality. | | ✓ | ✓ |
| **5.1.9** | Verify that the platform provides protection against physical decapsulation, side channel and glitching attacks. | | | ✓ |
| **5.1.10** | Verify descriptive silkscreens are removed from PCBs | | | ✓ |

## References
For more information, see also: 
- IoT Security - Physical and Hardware Security: <https://www.embedded.com/iot-security-physical-and-hardware-security/>
- IETF RFC 8576 - IoT Security: State of the Art and Challenges (5.10 Reverse Engineering Considerations):  <https://tools.ietf.org/html/rfc8576>
- ENISA - Baseline Security Recommendations for IoT: <https://www.enisa.europa.eu/publications/baseline-security-recommendations-for-iot/at_download/fullReport>
- GSMA - IoT Security Guidelines for Endpoint Systems <https://www.gsma.com/iot/wp-content/uploads/2017/10/CLP.13-v2.0.pdf>
