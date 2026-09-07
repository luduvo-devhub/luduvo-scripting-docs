---
icon: lucide/users-round
---

# PlayerSpawner

!!! note
    This page is still a work in progress.

`PlayerSpawner` is the built-in server prefab that creates and binds player characters. Its core script is available read-only at `core://scripts/PlayerSpawner.lua`.

```luau
local spawner = game.Prefabs.Spawn("PlayerSpawner")
```

The logical name has no space. `Spawn` is server-only and returns a detached root.

This prefab carries a platform custom component with two exact fields:

```luau
type PlayerSpawnerComponent = {
    character: string,
    respawnDelay: number,
}

self.PlayerSpawner.character = "Character"
self.PlayerSpawner.respawnDelay = 3
```

The core script listens for session joins, leaves, and character deaths, chooses an entity with the `SpawnPoint` component, spawns the configured character prefab, and calls `game.Session.BindCharacter`.
