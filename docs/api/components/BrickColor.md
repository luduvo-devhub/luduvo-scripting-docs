---
icon: lucide/box
---

!!! note
    Studio's property groups and the scripting component API are different. A
    label shown in the Properties panel is not automatically a component name or
    a Luau field.

# BrickColor

`BrickColor` is a (case-sensitive) built-in component name that stores an Instance's color.
You can use it with [`game.World.Query`](../query.md){ data-preview },
`Query:With`, `Query:Without`, [`game.World.Each`](../query.md){ data-preview },
and the Instance component methods.

## Script access

As a [Value-Based Component](index.md#value-based-components){ data-preview }, Queries expose `query.BrickColor[i]` as `vector` (read/write). It can also be accessed via `Instance.Color: vector`.

Inspector fields are serialization/editor metadata and are not automatically
available as Luau fields. See [Components](index.md){ data-preview } for that
distinction and [Instances](../instances.md){ data-preview } for fixed property
types and write scope.

## Stored fields

| Field | Stored type | Notes |
| --- | --- | --- |
| `r` | `number` |  |
| `g` | `number` |  |
| `b` | `number` |  |

