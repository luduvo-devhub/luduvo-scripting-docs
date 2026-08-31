---
icon: lucide/globe
---

!!! note 
    This page currently is a work in progress and some information may be missing, incomplete, or incorrect. Contributions are welcome!

# Game

Game is Luduvo's biggest and potentially most important global variable. Outside of holding information that universally affects the entire game, it also somewhat doubles somewhat as a junk drawer that hold debug information that don't have any other obvious place to live.

Most things in `game` are only usable on the server.

Here are all of its subfields:

## `game.Prefabs`

```luau
game.Prefabs.Spawn(name: string) -> Instance?
game.Prefabs.Exists(name: string) -> boolean
```

See [Prefabs](prefabs/index.md) for more information.


## `game.World`

```luau
game.World.Each(component: string) -> () -> Instance?
game.World.DumpAttributes(entity: Instance?) -> ()
game.World.Query(...string) -> Query
game.World.System(name: string, q: Query, fn: (Query) -> (), phase: string?) -> ()
```

World controls the [Query](query.md) and [System](systems.md) aspects of Luduvo. More information can be found in their respective documentation.

## `game.Physics`

```luau
game.Physics.RegisterCollisionGroup(name: string) -> ()
game.Physics.RenameCollisionGroup(from: string, to: string) -> ()
game.Physics.SetCollisionRule(a: string, b: string, collidable: boolean) -> ()
game.Physics.Raycast(
    origin: vector,
    dir: vector,
    maxDist: number,
    ignore: Instance?
) -> RaycastResult?
game.Physics.OverlapSphere(
    center: vector,
    radius: number,
    out: {Instance}?
) -> (number, {Instance})

game.Physics.Gravity: number
game.Physics.FallenPartsDestroyHeight: number
```

`Gravity` presumably affects the `FallenPartsDestroyHeight` is the height where fallen parts despawn and no longer replicated or tracked by the server or clients.

## `game.Session`

```luau
game.Session.BindCharacter(userId: number, character: Instance) -> ()
game.Session.CharacterOf(userId: number) -> Instance?

game.Session.PlayerJoined: Signal
game.Session.PlayerLeft: Signal
game.Session.CharacterDied: Signal
```
Specifically, the Session's signals have the following shapes:

```luau
game.Session.PlayerJoined:Connect(function(userId)
end)

game.Session.PlayerLeft:Connect(function(character, userId)
end)

game.Session.CharacterDied:Connect(function(character, userId)
    -- userId may be nil
end)
```

## `game.Locale`

```luau
game.Locale.Get() -> string
game.Locale.Set(tag: string) -> (boolean, string)
game.Locale.Translate(key: string) -> string
```

## `game.Items`

```luau
type kinds = "place" | "model" | "accessory"
game.Items.Examine(kind: kinds, bytes: string) -> {[string]: any}
```

While `game.Items.Examine` is technically a public function, it is functionally useless outside of internal use. `bytes` requires the entire Luduvo file to be passed in as a luau string, and there is no way to get this without hardcoding the exact bytes yourself.

## `game.Profiler`

```luau
game.Profiler.Frame() -> FrameStats?
game.Profiler.Scripts() -> {ScriptCost}
game.Profiler.Dropped() -> number
```

## `game.Lighting`

Note that game.Lighting are all properties, not methods:

```luau
game.Lighting.Sun = {
    Azimuth: number,
    Elevation: number,
    Tint: vector,
    Intensity: number,
}

game.Lighting.Ambient = {
    Tint: vector,
    Intensity: number,
    Source: number,
}

game.Lighting.Sky = {
    Mode: number,
    Color: vector,
    Contribution: number,
}

game.Lighting.Shadows = {
    Mode: number,
    Fill: number,
}

game.Lighting.Exposure = {
    MinEV: number,
    MaxEV: number,
}

game.Lighting.Stars = {
    Luminance: number,
}

game.Lighting.Flare = {
    Intensity: number,
    Scale: number,
    Tint: vector,
    Ghost: number,
}
```

## `game.Sound`

```luau
game.Sound.SurfaceSoundsVolume: number
```
