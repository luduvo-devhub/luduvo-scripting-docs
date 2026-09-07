---
icon: lucide/map-pin-house
---

# SpawnLocation

`SpawnLocation` is a part-like prefab marked as a possible character spawn point. The exact scripting component name is `SpawnPoint`, not `SpawnLocation`.

```luau
local location = game.Prefabs.Spawn("SpawnLocation")

if location ~= nil then
    location.Parent = self
    print(location.SpawnPoint) -- true when the tag is present
end
```

`Spawn` is server-only and returns a detached root. The built-in [PlayerSpawner](playerspawner.md) searches with `game.World.Each("SpawnPoint")` when choosing a spawn location.
