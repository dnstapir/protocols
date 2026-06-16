# DNS TAPIR Protocols Documentation

This repository contains protocol documentation.

- OpenAPI (as YAML), view with https://editor-next.swagger.io/
- Messages JSON schemata (as YAML)


## MQTT Topics

### Edge to Core

- `events/up/SENDER/#` (signed)
  - [new_qname](events/new_qname.yaml)

- `status/edm/up/SENDER/#` (signed)
  - [edm_status](status/status_edm.yaml)

- `status/pop/up/SENDER/#` (signed)
  - [pop_status](status/status_pop.yaml)

### Core to Edge

- `observations/down/#`  (signed)
  - [Observation](edge-observations.yaml)
  - [An example](observation.sample.json)

- `config/down/#` (signed)
  - TBD

### Core to Core

- `aggregates` (unsigned)
  - [new_aggregate](events/new_aggregate.yaml)
