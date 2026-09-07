---
icon: lucide/box
---

!!! note
    Studio's property groups and the scripting component API are different. A
    label shown in the Properties panel is not automatically a component name or
    a Luau field.

# UITextStyle

`UITextStyle` is a (case-sensitive) built-in component name that stores text color, alignment, and rendering settings.
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
| `color.r` | `f32` |  |
| `color.g` | `f32` |  |
| `color.b` | `f32` |  |
| `color.a` | `f32` |  |
| `outline_color.r` | `f32` |  |
| `outline_color.g` | `f32` |  |
| `outline_color.b` | `f32` |  |
| `outline_color.a` | `f32` |  |
| `font_size` | `f32` |  |
| `outline_width` | `f32` |  |
| `h_align` | `u8` | Enum |
| `v_align` | `u8` | Enum |
| `no_translate` | `u8` | Boolean |
| `bold` | `u8` | Boolean |

