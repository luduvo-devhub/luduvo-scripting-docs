---
icon: lucide/box
---

# Systems

Systems in Luduvo are the main way to add logic and behavior to specfic components or component interaction. This is different from `Update` and `PhysicsUpdate`, which should be used for per-entity logic or for logic that transcends any given entity or component.

You can register a system using `game.World.System`:
```luau

type PhaseType = "Default" | "Physics"

game.World.System(
    name: string,
    query: Query,
    callback: (Query) -> (),
    phase: PhaseType?
) -> ()
```
Systems won't run until the component Query given in its `query` argument is satisfied. When it is satisfied, the `callback` is called with the query result as its only argument. For details on the query result, see [Query](query.md). However, unlike regular queries, Luduvo systems streamline query management by automatically:

1. Refreshing the query.
2. Calling the callback with that query as its only argument.
3. Flushing staged query writes.

In exchange, Luduvo Systems do **not** receive `dt`. If the calculation needs elapsed time, you'll have to track `tick()` yourself:
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

When you register a system, the system registration belongs to the current script under the name `name`. If you register a new system with the same name again later in the same script, it silently overwrites the old registration with the new query and callback. 

`phase` dictates the order in which the system is executed relative to other systems. In Luduvo and other ECS game engines, every System is organized into a handful of "phases" that run by the discretion of the engine. If `phase` is omitted, the system will automatically choose "Default" as the phase. Inside each phase, systems are likely organized by youngest to oldest registration.
