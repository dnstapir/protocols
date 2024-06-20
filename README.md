# DNS TAPIR Protocols Documentation

This repository contains protocol documentation.

- OpenAPI (as YAML), view with https://editor-next.swagger.io/
- Messages JSON schemata (as YAML)


## MQTT Topics

### Edge to Core

- `events/up/SENDER/#`
  - [new_aggregate](events-mqtt-message-new_qname.yaml) (signed)

- `status/up/SENDER/#`
  - TBD (signed)

### Core to Edge

- `observations/down/#`
  - TBD (signed)

- `config/down/#`
  - TBD (signed)

### Core to Core

- `aggregates`
  - [new_aggregate](events-mqtt-message-new_aggregate.yaml) (unsigned)
