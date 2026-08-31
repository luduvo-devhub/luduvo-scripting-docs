---
icon: lucide/map-pin-house
---

# SpawnLocation
SpawnLocation is a prefab that represents a location where a player can respawn when they die. It's largely just a `Part` with an additional `SpawnLocation` component.

Works hand-in-hand with the `PlayerSpawner` prefab, where the player spawning logic itself is handled.

## Constructor(s)

- `Prefab.spawn("SpawnLocation")`

!!! note
    SpawnLocations are automatically parented to the 3D world.

## Components

### Removable

- `Transform`
- `Data`
- `PrefabInstance`
- `Shape`
- `Physics`
- `Color`
- `Material`
- `SpawnLocation`

### Permanent

- `Attributes`
