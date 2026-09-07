---
icon: lucide/file-text
---

# Datatypes

!!! warning
    This section is incomplete. It includes the types confirmed in the current build, but not every Luau standard-library type.

## Vectors

Luduvo uses Luau's native `vector` value for 3D vectors, 2D points, and colors. The constructor table describes the value's intended meaning; it does not change its runtime type.

```luau
local position: vector = Vector3.new(1, 2, 3)
local point: vector = Vector2.new(10, 20) -- (10, 20, 0)
local red: vector = Color3.new(1, 0, 0)
```

`Vector3` also exposes `zero`, `one`, `xAxis`, `yAxis`, and `zAxis`. Vector arithmetic and members come from Luau's native vector implementation rather than a Luduvo-specific `Vector3` class.

## `UDim2`

```luau
UDim2.new(
    xScale: number?,
    xOffset: number?,
    yScale: number?,
    yOffset: number?
) -> UDim2
```

The arguments default to zero. The stored values mean X scale, X pixel offset, Y scale, and Y pixel offset, matching Roblox's four-part layout.

Luduvo's API is smaller than Roblox's: this build exposes construction, the `UDim2` runtime type, and string conversion. It does not expose `X`, `Y`, nested `UDim` values, `fromScale`, `fromOffset`, or arithmetic operators.

## Events

When creating Events in Luduvo, you must specify the kind of data you are looking to transport within the event. Luduvo provides the following global data types:

- F32
- I32
- U8
- Bool
- Vec3
- Color
- Entity
- ToServer
- ToClients

All of these types are closer to enum values than a data type, as their only use is to act as var. 

See [Events](events.md) for more details.

## `Instance`

An `Instance` is the scripting equivalent of an ECS Entity. While there is currently no `Instance.new()` constructor, you can still programmatically obtain an Instance from [`game.Prefabs.Spawn`](prefabs/index.md#spawning-prefabs), [`Instance:Clone`](instances.md#cloning), [queries](query.md), [World hierarchy traversal](instances.md#from-existing-instances), [script handles](scripts.md#script-handles), and any other APIs that return entities.

See [Instances](instances.md#reference) for more details.

## `Signal`

```luau
instance:GetSignal(name: string) -> Signal
signal:Connect(callback: (...any) -> ()) -> ()
signal:Emit(...any) -> ()
```

`GetSignal` finds or creates a signal associated with an Instance and name. Signals are local to the current client or server that makes them, and they do not replicate.

`Connect` is a method that runs its given function when the signal is emitted. Currently, there are no `Disconnect`, `Wait`, or `Once` operations, so a callback must make its own versions.

See [Instance signals](instances.md#signals) for more details.
