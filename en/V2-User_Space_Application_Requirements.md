# V2: User Space Application Requirements

## Control Objective

## Security Verification Requirements

### Identification & Authentication

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **2.1.1** | Verify that all forms of users in the IoT ecosystem can be uniquely identified.  | ✓ | ✓ | ✓ |
| **2.1.2** | Verify that all connected devices within the IoT ecosystem can be uniquely identified. This includes both devices that are directly connected to the cloud (hubs) as devices that are connected to other devices (sensors). | ✓ | ✓ | ✓ |
| **2.1.3** | Verify strong user and device authentication is enforced across the IoT ecosystem. | ✓ | ✓ | ✓ |
| **2.1.4** | Verify that user, services, and device authentication schemes share a common frameworks centrally managed in the IoT ecosystem. | ✓ | ✓ | ✓ |
| **2.1.5** | Verify certificate based authentication is preferred over password based authentication within the IoT ecosystem. | ✓ | ✓ | ✓ |
| **2.1.6** | Verify good password policies are established. Do not hardcode passwords into the device and do not provision duplicate identities or passwords across multiple devices. Require password changes on a regular basis. | ✓ | ✓ | ✓ |


### Authorization

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **2.2.1** | Verify that all privileged operations within the IoT system are identified and that elevated roles are mapped to those privileged operations. Roles may include trusted device, privileged local user, system administrator, trusted application, and trusted gateway. | ✓ | ✓ | ✓ |
| **2.2.2** | Verify that IoT system accounts across users, services and devices share a common authorization framework. | ✓ | ✓ | ✓ |
| **2.2.3** | Verify that devices enforce the concept of least privilege by limiting applications and services that run as root or administrator. | ✓ | ✓ | ✓ |
| **2.2.4** | Verify device debug capabilities can only be accessed by allowed staff (e.g. support and engineering teams) and verify that access is monitored/logged. | ✓ | ✓ | ✓ |

### Registration

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **2.3.1** | TODO | ✓ | ✓ | ✓ |


### Data Protection

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **2.4.1** | Verify that sensitive information such as personal identifiable information (PII) used by the device is stored securely on the device. Protection can include encryption against data leakage, and hashing or integrity checking against unauthorized modification. | ✓ | ✓ | ✓ |
| **2.4.2** | Verify that sensitive information maintained in memory is overwritten with zeros as soon as it is no longer required. | ✓ | ✓ | ✓ |
| **2.4.3** | Verify that user credentials and API keys are stored within hardware backed secure storage locations. | ✓ | ✓ | ✓ |
| **2.4.5** | Verify that in case a device is decommissioned, all sensitive information such as PII data and credentials can be removed from the device. | ✓ | ✓ | ✓ |
| **2.4.6** | Verify that in case a device is decommissioned, it is marked as such in a centrally managed database in the ecosystem. | ✓ | ✓ | ✓ |


### Cryptography

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **2.5.1** | Verify the cryptographic libraries used are FIPS 140-2 certified or similar. | ✓ | ✓ | ✓ |
| **2.5.2** | Verify cryptographic secrets are unique per device. | ✓ | ✓ | ✓ |
| **2.5.3** | Verify proper use of cryptography. Only standard and strong algorithms should be used, with adequate key size and secure implementations. | ✓ | ✓ | ✓ |
| **2.5.4** | Verify secure sources of randomness are provided by the operating system and/or hardware for all security needs. | ✓ | ✓ | ✓ |
| **2.5.5** | Verify that cryptographic secrets used by the device are stored securely through leveraging dedicated hardware functionality. | ✓ | ✓ | ✓ |

## Requirements Mapping

| # | ENISA | ... |
| -- | ---------------------- | ---------------------- |
|**2.1** | Lorem Ipsum | ... |

## References
