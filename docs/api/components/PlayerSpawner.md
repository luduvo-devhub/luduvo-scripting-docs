---
icon: lucide/box
---

!!! note
    Studio's property groups and the scripting component API are different. A
    label shown in the Properties panel is not automatically a component name or
    a Luau field.

# PlayerSpawner

`PlayerSpawner` is a (case-sensitive) built-in component name that stores the world's player spawner settings.
You can use it with [`game.World.Query`](../query.md){ data-preview },
`Query:With`, `Query:Without`, [`game.World.Each`](../query.md){ data-preview },
and the Instance component methods.

## Script access

As a [Field-Based Component](index.md#field-based-components){ data-preview }, Queries expose `query.PlayerSpawner.fieldName` as the type specified in the Stored Fields section. All fields have read/write access. There is no other way to access this component in scripts.

Inspector fields are serialization/editor metadata and are not automatically
available as Luau fields. See [Components](index.md){ data-preview } for that
distinction and [Instances](../instances.md){ data-preview } for fixed property
types and write scope.

## Stored fields

| Field | Stored type | Notes |
| --- | --- | --- |
| `character` | `Enum` |  |
| `respawnDelay` | `number` |  |

