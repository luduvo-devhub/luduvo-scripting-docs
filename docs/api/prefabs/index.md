---
icon: lucide/package
---

# Prefabs

!!! note
    If you are familiar with Unity, Luduvo prefabs are conceptually similar to [Unity prefabs](https://docs.unity3d.com/6000.7/Documentation/Manual/Prefabs.html).

Prefabs are premade, serialized [Instances](../instances.md){ data-preview } that can be reused between Luduvo projects. Luduvo scripts use them to programmatically spawn Instances that are not clones of an existing entity.

Luduvo ships these core prefabs:

- [Part](part.md)
- [SpawnLocation](spawnlocation.md)
- [PlayerSpawner](playerspawner.md)
- [Menu](menu.md)
- [Character](character.md)

## Storage

Prefabs are stored in the `core://prefabs/` and `project://prefabs/` virtual mounts. Prefabs and other files stored in `core://` are versioned and updated by Luduvo.

## Creating and editing prefabs

Opening a core prefab for editing creates a project copy at `project://prefabs/<Name>.ldv` and opens it in a prefab-edit world. Edit the project copy, not the installed core content.

To create a prefab from scene content, stop playtesting, select exactly one root entity, and use **File > Export Model...**. The exported `.ldv` can then be stored under the project's prefab directory. Prefab lookup reads the registered core/project store; inserting a prefab into the current scene is not required to make `Exists` or `Spawn` find it.

There is no Luau API for defining or saving prefab files at runtime.

## Spawning prefabs

Service functions use dot syntax:

```luau
if game.Prefabs.Exists("MyPrefab") then
    local root = game.Prefabs.Spawn("MyPrefab")

    if root ~= nil then
        root.Parent = self
    end
end
```

| Method | Scope | Behavior |
| --- | --- | --- |
| `game.Prefabs.Exists(name: string) -> boolean` | Client and server | Checks a logical, case-sensitive name without creating anything. |
| `game.Prefabs.Spawn(name: string) -> Instance?` | Server only | Instantiates the complete tree and returns its detached root, or `nil` on failure. |

Pass `"MyPrefab"`, not a `.ldv` path or URI. The returned root is not automatically parented or positioned.
