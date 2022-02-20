# V4: Communication Requirements

## Control Objective

Devices use network communication to exchange data and receive commands within their ecosystem. So that the different parties can trust the contents of communications, they need to be protected, ensuring the authenticity of parties, integrity against malicious changes, and confidentiality against information leakage. In practice, this translates to deploying up-to-date communication protocols and configuring their security features, including cryptography. Since industry guidelines on secure TLS, Bluetooth, and Wi-Fi change frequently, configurations should be periodically reviewed to ensure that communications security is always effective.

- Always use TLS or equivalent strong encryption and authentication, regardless of the sensitivity of the data being transmitted.
- Other security practices include certificate-based authentication with pinning and mutual authentication.
- Use up to date configurations to enable and set the preferred order of algorithms and ciphers used for communication.
- Disable deprecated or known insecure algorithms and ciphers.
- Use the strongest security settings available for wired and wireless communication protocols.

## Security Verification Requirements

### General

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.1.1** | Verify that communication with other components in the IoT ecosystem (including sensors, gateway and supporting cloud) occurs over a secure channel in which the confidentiality and integrity of data is guaranteed and in which protection against replay attacks is built into the communication protocol. | ✓ | ✓ | ✓ |
| **4.1.2** | Verify that in case TLS is used, its configured to only use FIPS-compliant cipher suites (or equivalent). | ✓ | ✓ | ✓ |
| **4.1.3** | Verify that in case TLS is used, the device cryptographically verifies the X.509 certificate. | ✓ | ✓ | ✓ |
| **4.1.4** | Verify that either protection or detection of jamming is provided for availability-critical applications.  | | ✓ | ✓ |
| **4.1.6** | Verify that the device's TLS implementation uses its own certificate store, pins to the endpoint's certificate or public key, and disallows connections to endpoints with different certificates or keys, even if signed by a trusted CA. | | ✓ | ✓ |
| **4.1.7** | Verify that inter-chip communication is encrypted (e.g. main board to daughter board communication). | | | ✓ |

### Machine-to-Machine

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.2.1** | Verify that unencrypted communication is limited to data and instructions that are not of a sensitive nature.  | ✓ | ✓ | ✓ |
| **4.2.2** | Verify MQTT brokers only allow authorized IoT devices to subscribe and publish message topics. | ✓ | ✓ | ✓ |
| **4.2.3** | Verify certificates are favored over native username and passwords to authenticate MQTT transactions. | ✓ | ✓ | ✓ |

### Bluetooth

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.3.1** | Verify that pairing and discovery is blocked in Bluetooth devices except when necessary. | ✓ | ✓ | ✓ |
| **4.3.2** | Verify that PIN or PassKey codes are not easily guessable (e.g. don't use 0000 or 1234). | ✓ | ✓ | ✓ |
| **4.3.3** | Verify that devices using old versions of Bluetooth with simple modes of authentication enabled require a PIN for pairing. | ✓ | ✓ | ✓ |
| **4.3.4** | Verify that for modern versions of Bluetooth, at least 6 digits are required for Secure Simple Pairing (SSP) authentication under all versions except “Just Works”. | ✓ | ✓ | ✓ |
| **4.3.5** | Verify that encryption keys are the maximum size the device supports and that this size is sufficient to adequately protect the information transmitted over the Bluetooth connection. | ✓ | ✓ | ✓ |
| **4.3.6** | Verify the most secure Bluetooth pairing method available is used. Verify Out Of Band (OOB), Numeric Comparison, or Passkey Entry pairing methods are used depending on the communicating device's capabilities. | ✓ | ✓ | ✓ |
| **4.3.7** | Verify the strongest Bluetooth Security Mode and Level supported by the device is used. For example, for Bluetooth 4.1 devices, Security Mode 4, Level 4 should be used to provide authenticated pairing and encryption. | ✓ | ✓ | ✓ |

### Wi-Fi

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.4.1** | Verify Wi-Fi connectivity is disabled unless required as part of device functionality. Devices with no need for network connectivity or which support other types of network connectivity, such as Ethernet, should have the Wi-Fi interface disabled. | ✓ | ✓ | ✓ |
| **4.4.2** | Verify that WPA2 or higher is used to protect Wi-Fi communications. | ✓ | ✓ | ✓ |
| **4.4.3** | Verify that in case WPA is used, it is used with AES encryption (CCMP mode). | ✓ | ✓ | ✓ |
| **4.4.4** | Verify that Wi-Fi Protected Setup (WPS) is not used to establish Wi-Fi connections between devices. | ✓ | ✓ | ✓ |

### Zigbee 

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.5.1** | Verify that Zigbee version 3.0 is used for new applications. | ✓ | ✓ | ✓ |
| **4.5.2** | Verify that a suitable Zigbee security architecture (Centralized or Distributed) is selected, depending on the application's security level requirements and threat model. The Centralized architecture generally offers higher security at the cost of flexibility. | ✓ | ✓ | ✓ |
| **4.5.3** | Verify that the most secure way of joining the Zigbee network is used, depending on the selected security architecture. For example, for the Centralized architecture, use out-of-band install codes. For the Distributed one, use pre-configured link keys. | ✓ | ✓ | ✓ |
| **4.5.4** | Verify that the default pre-configured global link key (ZigbeeAlliance09) is not used to join the network, except if explicitly required for compatibility reasons and if associated risks have been taken into account. | ✓ | ✓ | ✓ |
| **4.5.5** | Verify that user interaction is required to activate pairing mode for both the joining nodes and the Zigbee Trust Center / router. Devices should automatically exit pairing mode after a pre-defined short amount of time, even if pairing is unsuccessful. | ✓ | ✓ | ✓ |
| **4.5.6** | Verify that the network key is randomly generated (for example during the initial network setup). | ✓ | ✓ | ✓ |
| **4.5.7** | Verify that the network key is periodically rotated. |   |   | ✓ |
| **4.5.8** | Verify that users can obtain an overview of paired devices to validate that they are legitimate (for example, by comparing the MAC addresses of connected devices to the expected ones). |   |   | ✓ |

### LoRaWAN

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.6.1** | Verify that LoRaWAN version 1.1 is used by new applications. | ✓ | ✓ | ✓ |
| **4.6.2** | Verify that the network, join and application servers of the LoRaWAN ecosystem are appropriately hardened according to industry best practices and benchmarks. | ✓ | ✓ | ✓ |
| **4.6.3** | Verify that all communication between the LoRaWAN gateway and the network, join and application servers occurs over a secure channel (for example TLS or IPsec), guaranteeing at least the integrity and authenticity of the messages.  | ✓ | ✓ | ✓ |
| **4.6.4** | Verify that root keys are unique per end device. | ✓ | ✓ | ✓ |
| **4.6.5** | Verify that replay attacks are not possible using off-sequence frame counters. For example, in case end device counters are reset after a reboot, verify that old messages cannot be replayed to the gateway.  |   | ✓ | ✓ |

## References
For more information, see also:

- OWASP Transport Layer Protection Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html>
- NIST SP800-52r2 - Guidelines for the Selection, Configuration, and Use of TLS Implementations: <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-52r2.pdf>
- IETF RFC 7525 - Recommendations for Secure Use of TLS and DTLS: <https://tools.ietf.org/html/rfc7525>
- NIST SP800-121r2 - Guide to Bluetooth Security: <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-121r2.pdf>
- NIST SP800-97 - Establishing Wireless Robust Security Networks: <https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-97.pdf>
- HKCERT - ZigBee Security Study: <https://www.hkcert.org/f/blog/264453/3a1c8eed-012c-4b59-9d9e-971001d66c77-DLFE-14602.pdf>
- A systematic review of security in LoRaWAN: <https://arxiv.org/pdf/2105.00384.pdf> 
