---
icon: lucide/globe
---

# Game

`game` is Luduvo's largest and potentially most important global variable. In addition to information that affects the entire game, it holds utility and diagnostic services that do not have another obvious home.


## `game.Prefabs`

| Method | Scope | Behavior |
| --- | --- | --- |
| `Spawn(name: string) -> Instance?` | Server | Generates an [Instance](instances.md){ data-preview } from the given prefab name, or `nil` if lookup or creation fails. The generated Instance is not automatically positioned or parented to the World Hierarchy. |
| `Exists(name: string) -> boolean` | Server and Client | Checks if the given prefab name exists in `core://prefab` or `project://prefab` without creating anything. |

See [Prefabs](prefabs/index.md) for more information on how to use prefabs.

## `game.World`

| Method | Scope | Behavior |
| --- | --- | --- |
| `Each(component: string) -> () -> Instance?` | Server and Client | Returns an iterator over Instances in the current snapshot that have the given component. Unknown names raise an error. |
| `DumpAttributes() -> ()` | Server and Client | Prints the attribute-name usage for every Instance in the entire World. |
| `DumpAttributes(entity: Instance) -> ()` | Server and Client | Prints world-wide usage, then the selected Instance's attributes.|
| `Query(...componentNames: string) -> Query` | Server and Client | Creates a reusable ECS Query. At least one component name is required. Each game can hold at most 256 live queries. |
| `System(name: string, query: Query, callback: (Query) -> (), phase: "Default" \| "Physics"?) -> ()` | Server and Client | Registers a system that refreshes the Query and runs the callback every scheduled phase, including when the Query has no matches. |

See [Queries](query.md) and [Systems](systems.md) for more information.

## `game.Physics`

```luau
type RaycastResult = {
    Position: vector,
    Normal: vector,
    Entity: Instance?,
    Distance: number,
}
```

| Method | Scope | Behavior |
| --- | --- | --- |
| `RegisterCollisionGroup(name: string) -> ()` | Server | Adds a collision group. Names are limited to 23 letters/bytes, and the build-specific table can hold up to 32 names including `Default`. |
| `RenameCollisionGroup(from: string, to: string) -> ()` | Server | Renames a registered group. The destination must be nonempty, at most 23 letters/bytes, and unused. |
| `SetCollisionRule(a: string, b: string, collidable: boolean) -> ()` | Server | Changes whether two registered groups can collide. |
| `Raycast(origin: vector, direction: vector, maxDistance: number, ignore: Instance?) -> RaycastResult?` | Server and Client | Casts in the caller's local physics world. A miss, near-zero direction, or non-positive distance returns `nil`. `RaycastResult.Entity` may be `nil` if the hit Instance is destroyed by the time you read the value. |
| `OverlapSphere(center: vector, radius: number, out: {Instance}?) -> (number, {Instance})` | Server and Client | Returns the first 64 unique Instances that are within the specified sphere. If `out` is supplied, Luduvo reuses it and overwrites indices `1..count`; older entries above `count` remain. |

```luau
local hit = game.Physics.Raycast(
    self.Position,
    Vector3.new(0, -1, 0),
    100,
    self
)

if hit ~= nil then
    print(hit.Entity, hit.Position, hit.Normal, hit.Distance)
end
```

`game.Physics` comes with some properties as well:

| Property | Scope | Behavior |
| --- | --- | --- |
| `Gravity: number` | Read Server and Client; Write Server | Reads or writes the [`WorldConfig.Gravity`](components/WorldConfig.md){ data-preview } Component field. |
| `FallenPartsDestroyHeight: number` | Read Server and Client; Write Server | Reads or writes the [`WorldConfig.FallenPartsDestroyHeight`](components/WorldConfig.md){ data-preview } Component field. |

## `game.Session`

| Method | Scope | Behavior |
| --- | --- | --- |
| `BindCharacter(userId: number, character: Instance) -> ()` | Server | Assigns the character to the user, resets movement intent, and ensures native humanoid and floor state. It rejects a destroyed Instance or a second different live character for the same user. |
| `CharacterOf(userId: number) -> Instance?` | Server and Client | Returns the live character bound to the user in the caller's session view, or `nil`. |

`game.Session` also exposes three read-only [Signals](instances.md#signals):

```luau
game.Session.PlayerJoined:Connect(function(userId: number)
end)

game.Session.PlayerLeft:Connect(function(character: Instance?, userId: number)
end)

game.Session.CharacterDied:Connect(function(character: Instance?, userId: number?)
end)
```

When run on a server, `game.Session` can store up to 64 `PlayerJoined` notifications until a handler connects and drops the oldest one.

## `game.Locale`

| Method | Scope | Behavior |
| --- | --- | --- |
| `Get() -> string` | Server and Client | Returns the active locale tag, or `""` if no locale store exists. |
| `Set(tag: string) -> (boolean, string)` | Server and Client | Returns `true` with `"changed"` or `"unchanged"`; returns `false` with `"rejected"` or `"unavailable"`. The change is local to that runtime's locale store. |
| `Translate(key: string) -> string` | Server and Client | Returns the translated string or the untranslated `key` when no translation is available. |

## `game.Items`

```luau
game.Items.Examine(
    kind: "place" | "model" | "accessory",
    bytes: string
) -> ItemExamination
```

| Method | Scope | Behavior |
| --- | --- | --- |
| `Examine(kind, bytes: string) -> ItemExamination` | Server | When given an entire `.ldv` file's bytes, it inspects its contents in a test world and returns data useful for debugging and file validation. |

`bytes` expects the file's entire binary contents in a Luau string, not a path or URI. Currently, there is no scripting API endpoint for obtaining an `.ldv` file's raw bytes, so most scripts will not get much mileage out of this method.

Below is all the data inside a `ItemExamination` result:

??? note "Full `ItemExamination` type (very long)"
    ```luau
    type ItemChunk = {
        kind: number,
        name: string,
    }
    
    type ItemHead = {
        byte_len: number,
        format_version: number,
        format_min: number,
        format_max: number,
        declared_expanded: number,
        declared_expanded_text: string,
        expanded_cap: number,
        chunks_readable: boolean,
        chunks: {ItemChunk},
    }
    
    type ItemAttachment = {
        root: boolean,
        slot: number,
    }
    
    type ItemComponent = {
        tid: number,
        name: string,
    }
    
    type ItemEntity = {
        name: string,
        script: boolean,
        attachment: ItemAttachment?,
        components: {ItemComponent},
        unknown: {string},
        pairs: {string},
    }
    
    type ItemSurface = {
        name: string,
        id: string,
    }
    
    type ItemPart = {
        mesh: string,
        position: {number}, -- three values
        scale: {number}, -- three values
        rotation: {number}, -- four values
        surface: {ItemSurface},
    }
    
    type ItemExamination = {
        head: ItemHead, -- present regardless of whether Luduvo could load the file
        loaded: boolean,
        entities: number,
        root_count: number,
        first_root: number,
        holds_core_menu_action: boolean,
        nonfinite: string?, -- only present when an invalid field is found
        ents: {ItemEntity},
        parts: {ItemPart},
        place: {[string]: any}, -- place-specific menu/UI budget data
    }
    ```

## `game.Profiler`

```luau
type FrameStats = {
    sim: number,
    interval: number,
    script: number,
    physics: number,
    network: number,
    render: number,
    gcKB: number,
    gcAllocKBs: number,
}

type ScriptCost = {
    entity: number, -- an internal ECS ID, not an Instance
    path: string,
    avg: number,
    calls: number,
}
```

| Method | Scope | Behavior |
| --- | --- | --- |
| `Frame() -> FrameStats?` | Server and Client | Returns the newest profiler sample from a 120-frame history, or `nil` if none exists. |
| `Scripts() -> {ScriptCost}` | Server and Client | Returns per-script costs, or an empty table if profiling data is unavailable. |
| `Dropped() -> number` | Server and Client | Returns the dropped-script count, or zero when no profile data exists. |

## `game.Lighting`

```luau
game.Lighting.Sun: {
    Azimuth: number, Elevation: number,
    Tint: vector, Intensity: number,
}
game.Lighting.Ambient: {
    Tint: vector, Intensity: number, Source: number,
}
game.Lighting.Sky: {
    Mode: number, Color: vector, Contribution: number,
}
game.Lighting.Shadows: {Mode: number, Fill: number}
game.Lighting.Exposure: {MinEV: number, MaxEV: number}
game.Lighting.Stars: {Luminance: number}
game.Lighting.Flare: {
    Intensity: number, Scale: number, Tint: vector, Ghost: number,
}
```

## `game.Sound`

| Property | Scope | Behavior |
| --- | --- | --- |
| `SurfaceSoundsVolume: number` | Read Server and Client; Write Server | Reads or writes the world surface-sound volume. |
