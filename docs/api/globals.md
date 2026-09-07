---
icon: lucide/globe
---

# Globals

Luduvo injects the following variables to every script it loads to run:

## Tables and Userdata

| Name | Description |
| --- | --- |
| `self: Instance` | The [Instance](instances.md) to which the current script is attached. |
| `handles` | A table containing all named [script handles](scripts.md#script-handles). Does not get injected if there are no defined handles. |
| `game` | The root table for Luduvo's nine [global properties](game.md). |

## Functions

| Name | Description |
| --- | --- |
| `print(...any) -> ()` | Writes values to the output log. |
| `warn(...any) -> ()` | Writes a warning to the output log. |
| `tick() -> number` | Returns a runtime time value in seconds. Use differences between calls to measure elapsed time. |
| `typeof(value: any) -> string` | Returns Luduvo's runtime type name for a value. |
| `EventTable(...) -> EventTable` | Declares or opens a typed [client/server event table](events.md). |
| `EventTableDump() -> ()` | Prints diagnostic information about active event tables. |

## Lifecycle functions

These are specially Luduvo-owned functions that a script may define:

| Name | Description |
| --- | --- |
| `Update(dt: number)` | A function that Luduvo runs every frame. |
| `PhysicsUpdate(dt: number)` | A function that Luduvo consistently calls to run every `dt` (`0.01666666753590107`) seconds. |

## Datatypes

Luduvo has the following global datatypes:

```luau
Vector3.new(x: number, y: number, z: number) -> vector
Vector3.zero: vector
Vector3.one: vector
Vector3.xAxis: vector
Vector3.yAxis: vector
Vector3.zAxis: vector

Vector2.new(x: number, y: number) -> vector -- z is 0
Color3.new(r: number, g: number, b: number) -> vector

UDim2.new(
    xScale: number?,
    xOffset: number?,
    yScale: number?,
    yOffset: number?
) -> UDim2
```

`Vector3`, `Vector2`, and `Color3` all produce Luau's native `vector` type and can therefore be used interchangeably.
`UDim2` is very similar to Roblox's `UDim2` type, but Luduvo does not expose Roblox's full `UDim2` API. See [Datatypes](datatypes.md) for full details.
