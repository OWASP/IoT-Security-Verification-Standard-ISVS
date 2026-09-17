# Product context schema and worked archetypes

This file defines the `context.json` input for `build_custom_mapping.py` and
provides three representative archetypes used to validate the skill. Copy an
archetype and edit the values — do not invent new top-level keys without
updating the build script's validator.

## Schema

| Key | Type | Required | Meaning |
|-----|------|----------|---------|
| `product_name` | string | yes | Human label recorded in the output header. |
| `device_type` | string | yes | Short archetype tag, e.g. `consumer_camera`, `industrial_gateway`, `ble_wearable`. Free text is allowed but prefer the archetype tags below so rules stay comparable. |
| `connectivity` | string list | yes | Radio or network bearers in the product, e.g. `wifi`, `ble`, `zigbee`, `lorawan`, `cellular`, `ethernet`. Empty list means no radio; RED applicability then becomes `review`. |
| `handles_personal_data` | boolean or null | yes | `true` if the product processes personal data (video, audio, location, accounts). `null` means unknown and forces privacy-sensitive items to `review`. |
| `payment_capable` | boolean or null | yes | `true` if the product can initiate monetary transfer. Controls RED 3.3(f) relevance. `null` forces payment-adjacent items to `review`. |
| `target_markets` | string list | yes | e.g. `EU`, `US-Federal`, `UK`, `Global`. Unknown markets do not remove framework columns; they add a review note about which columns matter most. |
| `safety_critical` | boolean or null | yes | `true` for products whose failure can cause physical harm. Raises logging, update, and integrity items to in scope when they would otherwise be review. |
| `update_mechanism` | string or null | yes | `ota`, `usb`, `none`, or `null` (unknown). `none` or `null` marks update-related requirements for review rather than silently scoping them out. |
| `notes` | string | no | Free text about deployment, cloud, onboarding, or business constraints. Recorded verbatim in the output header. |

Unknown values must be `null`, never guessed. The build script treats `null`
as "cannot decide" and emits `review` with a reviewer prompt.

## Archetype A — Consumer Wi-Fi camera with cloud and mobile app

```json
{
  "product_name": "Example consumer Wi-Fi camera",
  "device_type": "consumer_camera",
  "connectivity": ["wifi"],
  "handles_personal_data": true,
  "payment_capable": false,
  "target_markets": ["EU"],
  "safety_critical": false,
  "update_mechanism": "ota",
  "notes": "Video and audio, cloud storage, mobile app onboarding"
}
```

Scoping notes: personal-data requirements in scope; RED 3.3(f) column marked
not applicable by context (payment incapable) but its Appendix B cells are
still preserved verbatim with a context note; CRA and ETSI columns matter
most for EU consumer placement.

## Archetype B — Industrial LoRaWAN sensor gateway

```json
{
  "product_name": "Example industrial LoRaWAN gateway",
  "device_type": "industrial_gateway",
  "connectivity": ["lorawan", "ethernet", "cellular"],
  "handles_personal_data": false,
  "payment_capable": false,
  "target_markets": ["EU", "Global"],
  "safety_critical": true,
  "update_mechanism": "ota",
  "notes": "No personal data, safety-relevant telemetry, managed fleet updates"
}
```

Scoping notes: privacy-led requirements become out of scope with an explicit
reason (no personal data), while logging, update, and integrity requirements
stay in scope due to safety relevance; RED 3.3(f) again not applicable by
context.

## Archetype C — BLE wearable with mobile app

```json
{
  "product_name": "Example BLE wearable",
  "device_type": "ble_wearable",
  "connectivity": ["ble"],
  "handles_personal_data": true,
  "payment_capable": null,
  "target_markets": ["Global"],
  "safety_critical": false,
  "update_mechanism": null,
  "notes": "Health-adjacent data over BLE, update path not yet confirmed"
}
```

Scoping notes: `payment_capable: null` and `update_mechanism: null` force the
related items to `review` with prompts ("confirm whether the wearable can
initiate payment", "confirm update path") rather than assuming them away.
This archetype exercises the uncertain-mapping path end to end.
