---
icon: lucide/box
---

!!! note
    This is a stub and currently a work in progress. Contribute, or come back later for updates!

!!! note
    In the alpha build of Luduvo, scriptable components and components shown/organized in the editor's properties panel are completely different, with some compoents not even being accessible via the editor's properties panel and vice versa. Tread with caution.

# Position

Position is a Luduvo component that represents the position of an instance in a 3D space.

## Properties

As with the other 4 scriptable components, Luduvo handles this property's Query interactions with a special case. Instead of breaking Position into `X`, `Y`, and `Z` components, it treats it as a single luau `vector` value. As such, use looks like this:

```lua
local positionQuery = game.World.Query("Position")
local position = positionQuery.Position[1]
position = Vector3.new(1, 2, 3)
```
This will also work with luau's [builtin vector](https://luau.org/library/#vector-library) values directly. See [Vector3](luduvo-scripting-docs/api/datatypes) for details.

Outside of Query interactions, You can access Position values in Instances via their `Position` property.
