---
icon: lucide/send
---

# Events

Events are the main way to send data back and forth between the client and server without worrying about scope and replication issues. They are not Instances nor for script-to-script local communication. Instead, use local [signals](instances.md#signals) when there is no need to communicate through the internet.

## Creating Events

In Luduvo, Events are not objects in the World Hierarchy. To create an Event, use the global `EventTable()` function:

```luau
type EventDirection = typeof(ToServer) | typeof(ToClients)
type EventFieldType =
    typeof(F32) | typeof(I32) | typeof(U8) | typeof(Bool)
    | typeof(Vec3) | typeof(Color) | typeof(Entity) 

EventTable(
    name: string,
    direction: EventDirection,
    fields: {{string | EventFieldType}}
) -> EventTable
```

!!! note
    The directions and field types are **not** strings, but a [global datatype](datatypes.md#events). You should not need to use quotation marks. 

An EventTable takes the `name` of the event, which `direction` data is expected to transfer (it can either travel to the Server or to the Clients), and a table outlining the shape future data tables (A.K.A `fields`) will take when you send or receive data through this Event.

The server declaration is authoritative. A client cannot introduce a table that the server did not declare, and its declaration must match the server's direction and schema.

### Fields

More on the `fields` parameter, each table entry should be a two-element array containing the field name and the data type they take:
 
```luau
local damage = EventTable("Damage", ToServer, {
    {"target", Entity},
    {"amount", F32},
    {"critical", Bool},
}) --(1)!
```

1. If this EventTable were to be used to send data to a server, the payload dictated by the `fields` mean that it would always take the form of:
  ```luau
  {
      target = SomeInstance,
      amount = someNumber,
      critical = someBool,
  }
  ```

When making fields for an EventTable, these are the supported field types you can use:

- `F32`, which represents a 32-bit floating-point number from `-3.402823466e+38` to `3.402823466e+38`
- `I32`, which represents a 32-bit signed integer from `-2147483648` to `2147483647`
- `U8`, which represents an unsigned 8-bit integer from `0` to `255`
- `Bool`, which represents a boolean
- `Vec3`, which represents a Vector2 or Vector3 value
- `Color`, which represents a Color3 value
- `Entity`, which represents an Instance

**Strings, nested tables, and arrays are not allowed as field types.** 

!!! note
    A `Prefab` field type appears have also been a planned for use with EventTables, but Luduvo currently rejects it. It seems to have some connection to the fact that you cannot transfer strings over an EventTable.

??? tip "Getting around EventTable field restrictions"

    If you need to send a string, convert it into bytes with `string.charCodeAt()` or `string.byte()`, and use a `U8` field type.

    If you need to encode an array, send each element as a separate event or consolidate the array into a single value that you can then decode and reseparate once you receive it.

    If you need to encode a nested table, flatten structured data across fields or replace tables with a pointer value that points to data sent in a separate event.

## Using EventTables

Similarly to [Queries](query.md#query-for-components), after creating an EventTable through `EventTable()`, you get an `EventTable` object that you then use to send and receive events through the internet:

```luau

type EventColumn<T> = {
    [string]: T,
}

type EventTable = {
    count: number,
    sender: {number}?,
    
    [string]: EventColumn<boolean | number | vector | Instance?>,

    Push: (self: EventTable, ...any) -> (),
    PushTo: (self: EventTable, userId: number, ...any) -> (),
}
```

### Sending Events

Because EventTables are purposely designed to only go one direction, the way you are able to send events differs depending on the direction you chose during initialization.

Regardless of the direction, you will have access to `Push`. `Push` is an EventTable method that pushes its given parameters through the internet and to its intended destination. The data you push must match both the declaration order as well as the expected contents for every field that was declared in the EventTable. 

However, `Push` operates differently depending on the direction. If the direction is `ToServer`, it sends the data straight to the server. However, if the direction is `ToClients`, it sends the data to every player/client currently connected to that server.

If you need to send data only to a particular client, `ToClients` EventTables has access to `PushTo`, which sends the data to the user ID specified in the parameter **before** you specify which data to send.

### Receiving Events

When events are pushed to your device, the `EventTable` object automatically stores and converts the received data into luau-friendly values:

| Field type | Luau value when the data is received |
| --- | --- |
| `F32`, `I32`, `U8` | `number` |
| `Bool` | `boolean` |
| `Vec3`, `Color` | `vector` |
| `Entity` | `Instance?` |

!!! note
    Because there is a chance that the Instance sent through an `Entity` field will get destroyed before the data is able to arrive to its intended destination, the field accepts an `Instance` or `nil` if the reference cannot be resolved.

!!! warning
    EventTables store every event that they receive during a frame. When the frame ends, **the EventTable is cleared regardless of whether you are done with that data.** Store data separately if you need to process it over multiple frames or you will lose it. For more information, see the [Lifetime and Batch rules section](#batch-lifetime-rules-and-limits).

Every time an event is received, the `EventTable` object stores the received payloads directly inside itself through a dedicated `EventColumn` array for each expected field. 

Outside of the event payload data, EventTables also populates a `count` that stores the number of events the EventTable received in that frame. If the EventTable in question is a `ToServer` table, it will also create a dedicated `sender` eventColumn that stores the userId of the client that sent the event.

Similarly to [QueryColumns](query.md#using-queries), data received from events pushed to your device are sorted by field and must be accessed through index-based `for` loops:

```luau
for i = 1, damage.count do
    local senderId = damage.sender[i] -- server-side ToServer tables only
    local target = damage.target[i]
    local amount = damage.amount[i]
    local critical = damage.critical[i]
end
```
!!! warning
    Putting any EventColumn data in key-value pair loops (e.g. `for k, v in x do`, `for k, v in pairs() do`, and `for k, v in ipairs() do`) will cause an error

## Batch Lifetime Rules and Limits

Incoming events are the batch of events received on that specific frame. Unlike Queries, there is no `Refresh`, `Pop`, or general lifecycle management exposed to the public API. 

Multiple scripts may read the same rows during that frame, but reading said events does not consume them. Luduvo clears the incoming batch when the event system advances to the next frame, so you will need to copy any data to a new variable if you need said data to survive longer.

Each EventTable accepts at most 64 incoming and 64 outgoing events per frame. There does not seem to be a similar limit on the number of event columns.

If you ever need to debug event tables, the global `EventTableDump()` prints diagnostic information about every active event table to the console, but returns nothing.

Currently there doesn't seem to be a way to destroy created event tables.
