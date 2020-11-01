# V4: Communication Requirements

## Control Objective

## Security Verification Requirements

### General

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.1.1** | Verify that communication with other components in the IoT ecosystem (including sensors, gateway and supporting cloud) occurs over a secure channel in which the confidentiality and integrity of data is guaranteed and in which protection against replay attacks is built in the communication protocol. Stick to proven technologies such as TLS. | ✓ | ✓ | ✓ |
| **4.1.2** | Verify that in case TLS is used that its securely configured. | ✓ | ✓ | ✓ |
| **4.1.3** | Verify that in case TLS is used, the device cryptographically verifies the X.509 certificate. Make sure that no custom verification schemes are used.  | ✓ | ✓ | ✓ |
| **4.1.4** | Verify that for availability critical applications, either protection or detection of jamming is provided.  | ✓ | ✓ | ✓ |
| **4.1.5** | Verify that the authenticity of the data received is cryptographically verified. | ✓ | ✓ | ✓ |
| **4.1.6** | Verify that in case TLS is used, the device either uses its own certificate store, or pins the endpoint certificate or public key, and subsequentially does not establish connections with endpoints that offer a different certificate or key, even if signed by a trusted CA. | ✓ | ✓ | ✓ |

### Machine-to-Machine

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.2.1** | Verify all TCP-based communications (e.g., REST, MQTT, AMQP) are encrypted between system components using X.509 authenticated Transport Layer Security (TLS). | ✓ | ✓ | ✓ |
| **4.2.2** | Verify all UDP-based communications (e.g., Constrained Application Protocol (CoAP)) between system components are using the Datagram Transport Layer Security (DTLS) protocol specified in IETF RFC 7525 or newer. | ✓ | ✓ | ✓ |
| **4.2.3** | Verify that unencrypted communication is limited to data and instructions that are not of a sensitive nature.  | ✓ | ✓ | ✓ |
| **4.2.4** | Verify that if shared secrets are used to cryptographically secure communication, that the same key is not hardcoded in each device or sensor.  | ✓ | ✓ | ✓ |
| **4.2.5** | Verify MQTT brokers only allow authorized IoT devices to subscribe and publish message topics. | ✓ | ✓ | ✓ |
| **4.2.6** | Verify all MQTT messages that include sensitive information are encrypted using TLS. | ✓ | ✓ | ✓ |
| **4.2.7** | Verify certificates are used to authenticate MQTT transactions instead of the native username and password capabilities. | ✓ | ✓ | ✓ |

### Bluetooth

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.3.1** | Verify that pairing and discovery is blocked in Bluetooth devices except when necessary. | ✓ | ✓ | ✓ |
| **4.3.2** | Verify that PIN or PassKey codes are not easily guessable. For example, verify PIN codes are not ‘0000’or ‘1234’. | ✓ | ✓ | ✓ |
| **4.3.3** | Verify that in case old versions of Bluetooth and if simple modes of authentication are supported, a PIN is required to pair devices. | ✓ | ✓ | ✓ |
| **4.3.4** | Verify that for modern versions of Bluetooth, at least 6 digits are required for Secure Simple Pairing (SSP) authentication under all versions except “Just Works”. | ✓ | ✓ | ✓ |
| **4.3.5** | Verify that encryption keys are the maximum allowable size. Bluetooth has configurable key size parameters for establishing a session, with configurations that allow keys of smaller size than the 16-32 byte size used by AES. | ✓ | ✓ | ✓ |
| **4.3.6** | Verify the most secure Bluetooth pairing method available is used. Verify Out Of Band (OOB), Numeric Comparison, or Passkey Entry pairing methods are used depending on the communicating device's capabilities. | ✓ | ✓ | ✓ |
| **4.3.7** | Verify the best Bluetooth Security Mode and Level supported by the device is used. | ✓ | ✓ | ✓ |

### Wi-Fi

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **4.4.1** | Verify Wi-Fi connectivity is disabled unless required as part device functionality. Devices with no need for network connectivity or which support other types of network connectivity, such as Ethernet, should have the Wi-Fi interface disabled. | ✓ | ✓ | ✓ |
| **4.4.2** | Verify that WPA2 or higher is used to protect Wi-Fi communications. | ✓ | ✓ | ✓ |
| **4.4.2** | Verify that in case WPA is used, it is used with AES encryption (CCMP mode). | ✓ | ✓ | ✓ |
| **4.4.2** | Verify that Wi-Fi Protected Setup (WPS) is not supported to establish Wi-Fi connections. | ✓ | ✓ | ✓ |


## References
