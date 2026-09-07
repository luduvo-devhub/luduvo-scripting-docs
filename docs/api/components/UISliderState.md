---
icon: lucide/box
---

!!! note
    Studio's property groups and the scripting component API are different. A
    label shown in the Properties panel is not automatically a component name or
    a Luau field.

# UISliderState

`UISliderState` is a (case-sensitive) built-in component name that stores a slider's steps and current index.
You can use it with [`game.World.Query`](../query.md){ data-preview },
`Query:With`, `Query:Without`, [`game.World.Each`](../query.md){ data-preview },
and the Instance component methods.

## Script access

While this component can be used as a filter in Queries, it currently does not expose any of its fields to Queries. There is no other way to access this component in scripts.

Inspector fields are serialization/editor metadata and are not automatically
available as Luau fields. See [Components](index.md){ data-preview } for that
distinction and [Instances](../instances.md){ data-preview } for fixed property
types and write scope.

## Stored fields

!!! note
    Currently, these fields are not directly available as editable Luau. As such, they are reported as the types they are stored as in the engine itself instead of Luau types.

| Field | Stored type | Notes |
| --- | --- | --- |
| `steps` | `u8` |  |
| `index` | `u8` | Editor label: Value |

