---
icon: lucide/box
---

!!! note
    Studio's property groups and the scripting component API are different. A
    label shown in the Properties panel is not automatically a component name or
    a Luau field.

# Position

`Position` is a (case-sensitive) built-in component name that stores where an Instance is located in the world.
You can use it with [`game.World.Query`](../query.md){ data-preview },
`Query:With`, `Query:Without`, [`game.World.Each`](../query.md){ data-preview },
and the Instance component methods.

## Script access

As a [Value-Based Component](index.md#value-based-components){ data-preview }, Queries expose `query.Position[i]` as `vector` (read/write). It can also be accessed via `Instance.Position: vector`.

Inspector fields are serialization/editor metadata and are not automatically
available as Luau fields. See [Components](index.md){ data-preview } for that
distinction and [Instances](../instances.md){ data-preview } for fixed property
types and write scope.

## Stored fields

| Field | Stored type | Notes |
| --- | --- | --- |
| `x` | `number` |  |
| `y` | `number` |  |
| `z` | `number` |  |

