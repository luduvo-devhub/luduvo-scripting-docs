---
icon: lucide/workflow
---

# Systems

Systems in Luduvo are the main way to add logic and behavior to specific components or component interactions. This is different from `Update` and `PhysicsUpdate`, which should be used for per-entity logic or for logic that transcends any given entity or component.

`game.World.System` hooks a function to a reusable [Query](query.md){ data-preview } prompt:

```luau
game.World.System(
    name: string,
    query: Query,
    callback: (Query) -> (),
    phase: "Default" | "Physics"?
) -> ()
```

!!! warning
    You cannot unregister a System once you make it

`game.World.System` must be called from a script that is attached to an Instance, as the engine internally uses that script Instance to distinguish systems created by different scripts with the same name. Registering the same name again from the same script replaces the old system with the new one.

`phase` decides which group Luduvo runs the system in: `"Physics"` or `"Default"`. The exact ordering relative to internal engine systems is unknown. If no phase is specified, `"Default"` is used.

When a System is registered, Luduvo's system scheduler performs these steps:

1. Refresh the Query.
2. Call the hooked function with that Query as its only argument, even when `query.count` is zero.
3. Flush staged Query writes.

While Luduvo handles Query lifecycles, it does not pass delta time to the callback. Use `tick()` differences when elapsed time is required:

```luau
local movers = game.World.Query("Position"):Without("Anchored")
local lastTime = tick()

game.World.System("Drift", movers, function(rows)
    local now = tick()
    local dt = now - lastTime
    lastTime = now

    for i = 1, rows.count do
        rows.Position[i] = rows.Position[i] + Vector3.new(dt, 0, 0)
    end
end, "Default")
```
