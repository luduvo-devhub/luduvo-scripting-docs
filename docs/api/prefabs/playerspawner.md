---
icon: lucide/box
---

!!! note
    This is a stub and currently a work in progress. Contribute, or come back later for updates!

# Player Spawner

Player Spawners are an internal Luduvo's prefab for the logic behind spawning player characters in a game. They go hand-in-hand with the [Spawn Location](spawnlocation.md) prefab, where components with the spawn location defines the elegible locations where players can be spawned by the Player Spawner.

Player Spawners use the special `Server Script (Luduvo)` component to define the logic for spawning players, which cannot be removed or edited in any way. Currently, you can see the source code for the Player Spawner prefab in `core://scripts/PlayerSpawner.lua`.

## Constructor(s)

- `Prefab.spawn("Player Spawner")`

## Components

### Removable

- `Player Spawner`
- `Data`
- `PrefabInstance`

### Permanent

- `Attributes`

### Untouchable

- `Server Script (Luduvo)`
