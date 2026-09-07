---
icon: lucide/box
---

# Part

!!! note
    This page is still a work in progress.

`Part` is Luduvo's basic visible physics-object prefab.

```luau
local part = game.Prefabs.Spawn("Part")

if part ~= nil then
    part.Position = Vector3.new(0, 5, 0)
    part.Parent = self
end
```

`Spawn` is server-only. The returned root is detached, so set `Parent` explicitly when it should enter an existing hierarchy.

Studio groups several fields under labels such as Transform, Data, Physics, Color, and Material. The corresponding scripting component names include `Position`, `Rotation`, `Scale`, `Name`, `RigidBody`, `BrickColor`, and `SurfaceMaterial`; the group labels themselves are not component names.
