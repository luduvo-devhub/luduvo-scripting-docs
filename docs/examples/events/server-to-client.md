# Moving Platform

## Difficulty

This is a **medium** tutorial.

### Concepts Involved

- [Script Handles](../../api/scripts.md#script-handles)
- Luau's [type solver](https://luau.org/types/)
- The [table library](https://luau.org/library/#table-library)
- [EventTables](../../../api/events.md)

## Setup

You need to create a [Script Handles](../../api/scripts.md#script-handles) and attach it to a Part.

You will then need to create as many slots as you need in in the Script Handles: `Pos1`, `Pos2`, ..., `PosN`, with `N` being your final number.

Declare the same table in both scripts. The server validates the request and performs the authoritative mutation.

# Code

```luau title="Notice.server.lua"
local notices = EventTable("Notice", ToClients, {
    {"code", I32},
    {"position", Vec3},
})

notices:Push(1, Vector3.new(0, 5, 0)) -- broadcast
notices:PushTo(123456, 2, Vector3.new(10, 5, 0)) -- one user
```

The client declares the identical `ToClients` table and reads `notices.code[i]` and `notices.position[i]` during `Update`.
