# DNS TAPIR Protocols Documentation

This repository contains protocol documentation.

- OpenAPI (as YAML), view with https://editor-next.swagger.io/
- Messages JSON schemata (as YAML)


## MQTT Topics

### Edge to Core

- `events/up/SENDER/#` (signed)
  - [new_qname](events-mqtt-message-new_qname.yaml)

- `status/up/SENDER/#` (signed)
  - TBD

### Core to Edge

- `observations/down/#`  (signed)
  - TBD

- `config/down/#` (signed)
  - TBD

### Core to Core

- `aggregates` (unsigned)
  - [new_aggregate](events-mqtt-message-new_aggregate.yaml)
