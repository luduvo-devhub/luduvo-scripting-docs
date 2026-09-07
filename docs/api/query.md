---
icon: lucide/list-filter
---

# Queries

Queries are the main way you search for any number of [Instances](instances.md){ data-preview } in a Luduvo World. If you know the specific type or location of the Instance you're looking for, you can use a [Script handle](scripts.md#script-handles) or [Instance hierarchy methods](instances.md#world-hierarchy).

## Query for Components

The main method for querying Instances in a Luduvo World is through the `World.Query` method:

```luau
game.World.Query(...componentNames: string) -> Query
```

The only parameter to `World.Query` is a list of component names to pre-initialize a Query object with. As such, at least one component filter in `World.Query` is required, and every filter must be a valid component name.

!!! warning
    Luduvo at most can keep track of a maximum of 256 live Query objects. Do not create queries inside `Update`/`PhysicsUpdate`, callbacks, or loops else Luduvo will error.

After calling `World.Query`, it returns a `Query` object that is the main vehicle every future query-related operations will be done through:

```luau
type QueryColumn<T> = {
    [string]: T,
}

type Query = {
    count: number,
    Entity: QueryColumn<Instance>,
    
    [string]: QueryColumn<any>,

    Refresh: (self: Query) -> number,
    With: (self: Query, componentName: string) -> Query,
    Without: (self: Query, componentName: string) -> Query,
}
```

### Filtering

`With` and `Without` mutate the Query and return that same object for chaining:

```luau
local movers = game.World.Query("Position", "Velocity")
    :With("Shape")
    :Without("Anchored")
```

!!! warning
    Luduvo at most can keep track of a maximum of 8 queries terms per Query, and every `:With`/`:Without` adds a new term to the query. Do not modify queries inside `Update`/`PhysicsUpdate`, callbacks, or loops else Luduvo will error.

### Activating Queries

After initializing a query with `World.Query` and honing the results with `With` and `Without`, you must then manually tell Luduvo to search for Instances that match the query using `Refresh()`:

```luau
local movers = game.World.Query("Position", "Velocity")
    :Without("Anchored")

function Update(dt: number)
    movers:Refresh()
end
```
!!! note
    `Refresh()` is not chainable

!!! warning
    If other script modifies a component that is being listened to by a Query, the modification is invisible to all other scripts until the beginning of the next frame when `Query:Refresh()` is called. Be careful of race conditions!

Alongside `Query.count`, `Refresh()` also returns the number of matching Instances it found from its search.

!!! note
    For performance reasons, only [System Queries](systems.md) are capable of updating themselves without manually calling `Refresh()`.

### Using Queries

When a Query is refreshed, Luduvo records the Query's results in three types of fields:
1. `query.count` - the number of matching Instances found from its search
2. `query.Entity` - a list of `Instance` objects that matches the searched Query
3. `query.ComponentName` - the component values of the `Instance` in the order they appear in `Query.Entity`

Both 2. and 3. are stored internally as a `QueryColumn`, which has specific rules for how you are allowed to access their values. Specifically, you can only access their values using a numeric index loop like so:

```luau
for i = 1, movers.count do
    local entity: Instance = movers.Entity[i]
    local position: vector = movers.Position[i]
    local velocity: vector = movers.Velocity[i]
end
```


??? warning "key-value loops"
    Accessing values through a key-value loop will error:

    ```luau
    for key, value in movers.Position do --(1)!
        error("QueryColumns cannot be used in a k, v pair loop")
    end
    ```
    1. `for key, value in pairs(movers.Position) do` and `for i, value in ipairs(movers.Position) do` will also error.

From there, any reads or modifications to the QueryColumn's values will be synced in the respective Instance's Components/properties:

```luau
for i = 1, movers.count do
    local entity: Instance = movers.Entity[i]

    entity.Name = "Test"
    print(entity.Kind)
end

```

When it comes to modifying Components through a Query (case 3), there are three shapes that they might be returned in.

!!! warning
    Query writes are invisible to all other scripts until the beginning of the next frame when other queries run `Query:Refresh()`. Be careful of race conditions!

!!! note
    Server and client writes to components follow strict replication rules. Client writes modify only the client's local World and cannot be seen by other clients. Clients also cannot write to replicated or components otherwise owned by a server script. If you need to edit a Server-script owned value, use a [`ToServer` EventTable](events.md).

The first way is to access its value directly, similarly to an Instance property:

```luau
for i = 1, movers.count do
    local position: vector = movers.Position[i]
    local velocity: vector = movers.Velocity[i]

    movers.Position[i] = position + velocity * dt
end
```
!!! note
    This whole-value access is a fixed binding for the four components listed below. It is not determined by how many serialized fields a component has.

As of writing, only four built-in components can be exposed as raw values in this build, and not all of them are writable:

| Column | Luau type | Writable |
| --- | --- | :---: |
| `query.Position[i]` | `vector` | yes |
| `query.Scale[i]` | `vector` | yes |
| `query.BrickColor[i]` | `vector` | yes |
| `query.Velocity[i]` | `vector` | no |

The second possible shape is a nested field proxy:

```luau
local spawners = game.World.Query("PlayerSpawner")
spawners:Refresh()

local prefabName: string = spawners.PlayerSpawner.character[1]
spawners.PlayerSpawner.respawnDelay[1] = 3
```

For now, only Components that the engine refers to as "custom" (like [`PlayerSpawner`](components/PlayerSpawner.md){ data-preview } and [`Tool`](components/Tool.md){ data-preview }) expose these nested field proxies.

The third possible shape is no value column at all, which is what most Components currently return. The six Components mentioned above (`Position`, `Scale`, `BrickColor`, `Velocity`, `PlayerSpawner`, and `Tool`) are the only Components currently accessible as values through a Query. To change the rest, use an available property or method on [game](game.md) or an [Instance](instances.md#reference).

## Query for Instances

The `World.Each` method is similar to `World.Query`, but it only accepts a single component query term and does not return a Query result. Instead, it returns an iterator over Instances that have the specified component. If you need a quick way to iterate over a group of Instances, this is how you do it:

```luau
game.World.Each(component: string) -> () -> Instance?

for spawnPoint in game.World.Each("SpawnPoint") do
    print(spawnPoint.Name)
end
```

It skips Instances managed internally by Luduvo, Instances that are marked to be destroyed, and Instances that only obtained the queried component the same frame it was queried on. 

Like `Query`, `Each` does not automatically refresh itself, and you must call it again to get an updated snapshot of eligible Instances from that frame.

`Each` is useful if you need to find Instances but don't want to create a `Query`. Use `World.Query` when you need several component filters, component values, or a reusable result.
