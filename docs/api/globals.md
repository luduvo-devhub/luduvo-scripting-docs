---
icon: lucide/globe
---

# Globals

## Keywords

| Name                 | Description                                                                                            |
| -------------------- | ------------------------------------------------------------------------------------------------------ |
| `self`               | Returns the Instance that the script is attached to                                                    |
| `handles`            | Returns the [Script Handles](scripts.md#script-handles) of the Instance that the script is attached to |

## Functions

| Name                 | Description                               |
| -------------------- | ----------------------------------------- |
| `tick()`             | Return the current timestamp, in seconds  |
| `typeof(x: unknown)` | Returns the Luduvo type name of the value |

## Lifetime Functions

| Name                        | Description                                               |
| --------------------------- | --------------------------------------------------------- |
| `Update(dt: number)`        | Fires every frame on the client or server                 |
| `PhysicsUpdate(dt: number)` | Fires every physics step, presumably at a fixed frequency |