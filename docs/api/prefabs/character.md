---
icon: lucide/user-round
---

# Character

!!! note
    This page is still a work in progress. The spawning API and component names are confirmed; a complete custom-character workflow is not.

`Character` is one of Luduvo's built-in [Prefabs](index.md){ data-preview }. [`PlayerSpawner`](playerspawner.md) creates it by default, positions the returned root, and passes it to `game.Session.BindCharacter`.

```luau
local character = game.Prefabs.Spawn("Character")
```

`Spawn` is server-only and returns a detached root. Character behavior depends on its character, physics, animation, locomotion, health, rig, and body-part components. The editor's grouped labels are not necessarily the exact names accepted by Query or component methods; use the [component registry](../components/index.md) for scripting names.

Creating an NPC from this prefab may still require character-state initialization normally performed by the session and character systems. That workflow has not been fully tested.
