# V9: Tamper & Reverse Engineering Protection Requirements


## Control Objective
TODO: Control Objective description

## Security Verification Requirements

### Hardware Requirements

| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **9.1.1** | Verify that hardware tamper detection mechanisms are used (TODO elaborate).  | ✓ | ✓ |   |
| **9.1.2** | Verify that hardware reverse engineering prevention mechanisms are used (TODO elaborate).  | ✓ | ✓ |   |
| **9.1.3** | Verify that debugging interfaces are disabled or adequately protected (fe. JTAG, SWD).  | ✓ | ✓ |   |

### Boot Requirements

| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **9.2.1** | Verify that application level debugging interfaces such USB, UART, and other variants are disabled or adequately protected during every stage of the device's boot process. | ✓ | ✓ |   |
| **9.2.2** | Verify that the first stage bootloader is located securely in internal ROM and within the correct partition or "segment".  | ✓ | ✓ |   |
| **9.2.3** | Verify that the first stage bootloader is locked and cannot be altered. | ✓ | ✓ |   |
| **9.2.4** | Verify that the authenticity of next bootloader stages or application code is securely verified during every step of the boot process. | ✓ | ✓ |  |
| **9.2.5** | Verify that the bootloader does not allow code to be loaded from arbitrary storage locations.  | ✓ | ✓ |   |


### Firmware Requirements
| # | Description | L1 | L2 | L3 |
| -- | ---------------------- | - | - | - |
| **9.3.1** | Lorem | ✓ | ✓ |   |

## Requirements Mapping

| # | ENISA | ... |
| -- | ---------------------- | ---------------------- |
|**10.1** | Lorem Ipsum | ... |

## References
