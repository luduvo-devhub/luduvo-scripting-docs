---
icon: lucide/globe
---

# Globals

## Keywords

| Name                 | Description                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------ |
| `self`               | Returns the [Instance](instances.md) that the script is attached to                                                    |
| `handles`            | Returns the [Script Handles](scripts.md#script-handles) of the Instance that the script is attached to |
| `game`               | Returns the [Game](game.md) object that holds all the game-specific state and Services |

## Functions

| Name                 | Description                               |
| -------------------- | ----------------------------------------- |
| `tick()`             | Return the current timestamp, in seconds  |
| `typeof(x: unknown)` | Returns the Luduvo type name of the value |
| `EventHandle()`      | Returns an Event Handle usable for client/server communication |
| `EventTableDump()`   | Returns debug information about all active event handles |

## Lifetime Functions

| Name                        | Description                                               |
| --------------------------- | --------------------------------------------------------- |
| `Update(dt: number)`        | Fires every frame on the client or server                 |
| `PhysicsUpdate(dt: number)` | Fires every physics step, presumably at a fixed frequency |

## Data Types
!!! note
    For more information on specific data types, see [Data Types](datatypes.md)

| Name       | Description                                                                 |
| ---------- | --------------------------------------------------------------------------- |
| `Vector3`  | A functionally identical wrapper around luau's [builtin vector](https://luau.org/library/#vector-library) data type that likely exists for semantic clarity reasons |
| `Vector2`  | A wrapper around luau's [builtin vector](https://luau.org/library/#vector-library) data type, but it sets the vector's `z` component to 0. Functionally identical to a normal `Vector3`, and likely exists for semantic clarity reasons |
| `Color3`   | A wrapper around luau's [builtin color](https://luau.org/library/#color-library) data type. Functionally identical to a normal `Vector3`, and likely exists for semantic clarity reasons |
| `UDim2`    | Roblox's [UDim2](https://developer.roblox.com/en-us/api-reference/datatype/UDim2) data type partially reimplemented into Luduvo. |
