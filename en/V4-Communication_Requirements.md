# V4: Communication Requirements

## Control Objective

Devices use network communication to exchange data and receive commands within their ecosystem. So that the different parties can trust the contents of communications, they need to be protected, ensuring the authenticity of parties, integrity against malicious changes, and confidentiality against information leakage. In practice, this translates to deploying up-to-date communication protocols and configuring their security features, including cryptography. Since industry guidelines on secure TLS, Bluetooth, and Wi-Fi change frequently, configurations should be periodically reviewed to ensure that communications security is always effective.

- Always use TLS or equivalent strong encryption and authentication, regardless of the sensitivity of the data being transmitted. 
- Other security practices include certificate-based authentication with pinning and mutual authentication.
- Use up to date configurations to enable and set the preferred order of algorithms and ciphers used for communication.
- Disable deprecated or known insecure algorithms and ciphers.
- Use the strongest security settings available for Bluetooth and Wi-Fi communication

## Security Verification Requirements

### General

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.1.1** | Verify that communication with other components in the IoT ecosystem (including sensors, gateway and supporting cloud) occurs over a secure channel in which the confidentiality and integrity of data is guaranteed and in which protection against replay attacks is built in the communication protocol. | ✓ | ✓ | ✓ |
| **4.1.2** | Verify that in case TLS is used that its securely configured. | ✓ | ✓ | ✓ |
| **4.1.3** | Verify that in case TLS is used, the device cryptographically verifies the X.509 certificate. | ✓ | ✓ | ✓ |
| **4.1.4** | Verify that for availability critical applications, either protection or detection of jamming is provided.  | | ✓ | ✓ |
| **4.1.6** | Verify that device's TLS implementation uses its own certificate store, pins to the endpoint certificate or public key, and disallows connections from endpoints with different certificates or key, even if signed by a trusted CA. | | ✓ | ✓ |

### Machine-to-Machine

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.2.1** | Verify that unencrypted communication is limited to data and instructions that are not of a sensitive nature.  | ✓ | ✓ | ✓ |
| **4.2.2** | Verify that if shared secrets are used to cryptographically secure communication, that the same key is not hardcoded in each device or sensor.  | ✓ | ✓ | ✓ |
| **4.2.3** | Verify MQTT brokers only allow authorized IoT devices to subscribe and publish message topics. | ✓ | ✓ | ✓ |
| **4.2.7** | Verify certificates are favored over native username and passwords to authenticate MQTT transactions. | ✓ | ✓ | ✓ |

### Bluetooth

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.3.1** | Verify that pairing and discovery is blocked in Bluetooth devices except when necessary. | ✓ | ✓ | ✓ |
| **4.3.2** | Verify that PIN or PassKey codes are not easily guessable. For example, verify PIN codes are not ‘0000’or ‘1234’. | ✓ | ✓ | ✓ |
| **4.3.3** | Verify devices that support for old versions of Bluetooth with simple modes of authentication require a PIN to pair devices. | ✓ | ✓ | ✓ |
| **4.3.4** | Verify that for modern versions of Bluetooth, at least 6 digits are required for Secure Simple Pairing (SSP) authentication under all versions except “Just Works”. | ✓ | ✓ | ✓ |
| **4.3.5** | Verify that encryption keys are the maximum allowable size. Bluetooth has configurable key size parameters for establishing a session, with configurations that allow keys of smaller size than the 16-32 byte size used by AES. | ✓ | ✓ | ✓ |
| **4.3.6** | Verify the most secure Bluetooth pairing method available is used. Verify Out Of Band (OOB), Numeric Comparison, or Passkey Entry pairing methods are used depending on the communicating device's capabilities. | ✓ | ✓ | ✓ |
| **4.3.7** | Verify the strongest Bluetooth Security Mode and Level supported by the device is used. For example, for Bluetooth 4.1 devices, Security Mode 4, Level 4 should be used to provide authenticated pairing and encryption. | ✓ | ✓ | ✓ |

### Wi-Fi

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.4.1** | Verify Wi-Fi connectivity is disabled unless required as part of device functionality. Devices with no need for network connectivity or which support other types of network connectivity, such as Ethernet, should have the Wi-Fi interface disabled. | ✓ | ✓ | ✓ |
| **4.4.2** | Verify that WPA2 or higher is used to protect Wi-Fi communications. | ✓ | ✓ | ✓ |
| **4.4.3** | Verify that in case WPA is used, it is used with AES encryption (CCMP mode). | ✓ | ✓ | ✓ |
| **4.4.4** | Verify that Wi-Fi Protected Setup (WPS) is not used to establish Wi-Fi connections between devices. | ✓ | ✓ | ✓ |


## References
For more information, see also: 
- OWASP Transport Layer Protection Cheat Sheet : <https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html>
- NIST SP800-52r2 - Guidelines for the Selection, Configuration, and Use of TLS Implementations: <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r2.pdf>
- IETF RFC 7525 - Recommendations for Secure Use of TLS and DTLS: <https://tools.ietf.org/html/rfc7525>
- NIST SP800-121r2 - Guide to Bluetooth Security: <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-121r2.pdf>
- NIST SP800-97 - Establishing Wireless Robust Security Networks: <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-97.pdf>