# V2: User Space Application Requirements

## Control Objective

The purpose of the controls listed in this chapter is to ensure secure access to an IoT system by users and machines and to protect sensitive data by using security best practices.

Authentication and authorization are necessary to secure access. Relevant controls include strong unique secure identity, user role segregation, and the concept of least privilege. Authentication is the act of establishing, or confirming, the identity of someone (or something) as authentic, as a basis to believe that claims made by a person or about a device are correct and resistant to impersonation. Additional necessary controls include preventing recovery or interception of authentication credentials such as passwords. Authorization is the act of establishing, or confirming  someone (or something) has access rights to resources or actions satisfying the secure access policy.

Protection of sensitive data including credentials, and fair treatment of private information, are necessary to ensure secure use of system resources, such as files containing data or code, and the contents of memory.

Many controls in this chapter are implemented through cryptography. Therefore additional controls are necessary to select the right cryptographic primitives and configure them with secure credential storage.

## Security Verification Requirements

### Identification & Authentication

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **2.1.1** | Verify that all forms of users and accounts in the IoT ecosystem can be uniquely identified. | ✓ | ✓ | ✓ |
| **2.1.2** | Verify that all connected devices within the IoT ecosystem can be uniquely identified including connected to the cloud, hubs, as well as to other devices (sensors). | ✓ | ✓ | ✓ |
| **2.1.3** | Verify strong user and device authentication is enforced across the IoT ecosystem. | ✓ | ✓ | ✓ |
| **2.1.4** | Verify that user, services, and device authentication schemes share a common framework centrally managed in the IoT ecosystem. | ✓ | ✓ | ✓ |
| **2.1.5** | Verify certificate based authentication is preferred over password based authentication within the IoT ecosystem. | ✓ | ✓ | ✓ |
| **2.1.6** | Verify good password policies are enforced throughout the IoT ecosystem by disallowing hardcoded passwords and provisioning duplicate identities or passwords across devices. | ✓ | ✓ | ✓ |
| **2.1.7** | Verify that no undocumented or unmanageable accounts or interfaces exist on the system. | ✓ | ✓ | ✓ |


### Authorization

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **2.2.1** | Verify that sensitive information such as personal identifiable information (PII) and API keys are stored securely using encryption to protect from data leakage, and integrity checking to protect against unauthorized modification. | ✓ | ✓ | ✓ |
| **2.2.2** | Verify that IoT system accounts across users, services and devices share a common authorization framework. | ✓ | ✓ | ✓ |
| **2.2.3** | Verify that devices enforce the concept of least privilege by limiting applications and services that run as root or administrator. | ✓ | ✓ | ✓ |
| **2.2.4** | Verify that ownership is validated upon registration and as part of decommissioning when devices move across accounts. e.g. Device reselling, leasing, and renting.  | ✓ | ✓ | ✓ |
| **2.2.5** | Verify device debug capabilities can only be accessed by approved staff (e.g. support and engineering teams) and verify that access is monitored/logged. | | ✓ | ✓ |


### Data Protection

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **2.3.1** | Verify that sensitive information such as personal identifiable information (PII) used by the device is stored securely on the device. Protection can include encryption against data leakage, and hashing or integrity checking against unauthorized modification. | ✓ | ✓ | ✓ |
| **2.3.2** | Verify that in case a device is decommissioned, or in case the owner changes, all sensitive information such as PII data and credentials can be removed from the device. | ✓ | ✓ | ✓ |
| **2.3.3** | Verify that in case a device is decommissioned, or the owner changes, it is marked as such for auditable purposes in a centrally managed database in the ecosystem. | ✓ | ✓ | ✓ |
| **2.3.4** | Verify that sensitive information maintained in memory is overwritten with zeros as soon as it is no longer required. | | ✓ | ✓ |


### Cryptography

| # | Description | L1 | L2 | L3 |
| --  | ---------------------- | - | - | - |
| **2.4.1** | Verify cryptographic secrets are unique per device. | ✓ | ✓ | ✓ |
| **2.4.2** | Verify proper use of cryptography. Only standard and strong algorithms should be used, with adequate key size and secure implementations. | ✓ | ✓ | ✓ |
| **2.4.3** | Verify secure sources of randomness are provided by the operating system and/or hardware for all security needs. | | ✓ | ✓ |
| **2.4.4** | Verify that cryptographic secrets used by the device are stored securely by leveraging functionality provided by dedicated security chips. | | ✓ | ✓ |
| **2.4.5** | Verify that cryptographic primitives used by the device are provided by dedicated security chips. | | ✓ | ✓ |
| **2.4.6** | Verify the cryptographic libraries used are certified to be compliant with a recognized cryptographic security standard. | | ✓ | ✓ |

## References
For more information, see also:

- OWASP Authentication Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html>
- OWASP Access Control Cheat Sheet: <https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html>
- OWASP Top 10 Privacy Countermeasures: <https://owasp.org/www-pdf-archive/OWASP_Top_10_Privacy_Countermeasures_v1.0.pdf>
- NIST SP800-63B - Digital Identity Guidelines: <https://pages.nist.gov/800-63-3/sp800-63b.html>
- FIPS 140-2 - Security Requrements for Cryptographic Modules: <https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.140-2.pdf>
- ECRYPT CSA - D5.4 - Algorithms, Key Size and Protocols Report (2018): <https://www.ecrypt.eu.org/csa/documents/D5.4-FinalAlgKeySizeProt.pdf>
