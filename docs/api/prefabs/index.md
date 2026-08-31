---
icon: lucide/box
---

# Prefabs

!!! note
    If you are familiar with Unity, Luduvo prefabs are conceptually [Unity prefabs](https://docs.unity3d.com/6000.7/Documentation/Manual/Prefabs.html).

Prefabs are premade/serialized [Instances](/luduvo-scripting-docs/api/instances) that can be easily reused between Luduvo projects, and are required for Luduvo scripts to programmatically spawn non-cloned instances in your game.

Currently, Luduvo ships with these premade prefabs:

- [Part](part.md)
- [SpawnLocation](spawnlocation.md)
- [PlayerSpawner](playerspawner.md)
- [Menu](menu.md)
- [Character](character.md)

The prefabs stored in `core://` (which translates to Luduvo's `%AppData%` folder) cannot be directly edited. If selected in the editor, they will instead be cloned into your project and open a dummy scene for prefab editing.

You can also make your own prefabs in the editor by creating a new scene, selecting the desired Instance, and going to `File > Export Model...` while your project is not in playtesting. However, you cannot make your own prefabs programmatically.

To import a prefab into your project and expose custom prefabs to scripts, you need to copy it into your project's directory, select it in Luduvo's asset editor, and choose `Insert into Scene` from the right click menu.

Once inserted into the scene, you can access it from scripts using the `Prefab` API:

```lua
if game.Prefab.Exists("PrefabName") then
    local createdInstance = game.Prefab.Spawn("PrefabName")
end
```
!!! warning
    Spawning a prefab in client scripts will throw an error.
