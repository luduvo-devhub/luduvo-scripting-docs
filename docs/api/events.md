---
icon: lucide/box
---

# Events

!!! note
    If you are looking for client to client or server to server communication, use [Signals](instances.md#signals) instead.

Events are the only way for client and server scripts to communicate with each other in Luduvo.

## Creating Events
Unlike other game engines, Events are not instances that are part of the world hiearchy. To create an Event, you instead use the global `EventTable()` function:

```luau
type EventTable = (
    name: string,
    target: ToServer | ToClients,
    fields: {{[string]: EventType | string}},
) -> Event

type EventType = Bool | I32 | F32 | U8 | Vec3 | Color | Entity

-- Example code:
local clientEvent: Event = EventTable(
    "EventName", 
    ToServer, 
    {{"MyAwesomeColor" = Color}, {"ACoolNumber" = I32}}
)
local serverEvent: Event = EventTable(
    "EventName", 
    ToClients, 
    {{"MyDumbNumber" = I32}, {"MyCoolBoolean" = Bool}}
)
```
!!! note
    `target`'s possible values, and all values of `EventType` are all global variables, so do not surround them with quotes. `Prefab` seems to be another EventType that will be supported in the future.
!!! warning
    String values are deliberately not supported as a possible `EventType`. Don't use them.. There is also a hard cap of 64 fields per event, so take care not to exceed it.
!!! tip
    EventTables ironically cannot take raw tables as an `EventType`. You'll have to manually flatten the table into multiple `EventType` fields if it's a dictionary, or send values over the course of multiple events if its a list/array

## Handling Events

Once you call `EventTable()`, you get back an `Event` object that you can use to "push" events through the event fields you defined. An event looks like this:

```luau
type Event = {
    count: number, -- The number of events collected in this frame
    sender: UserId, -- Exclusive to events initialized with `ToServer`
    [string]: EventColumn, -- Each string is a field name defined in the Event's corresponding EventTable
}

type EventData = boolean | number | Vector3 | Color3 | Instance

type EventColumn = {
    push: (value: EventData) -> (),
    pushTo: (target: UserId, value: EventData) -> (), -- Only relevant to events initialized with `ToClients`
    [number]: EventData,
}

-- Example code:

clientEvent.MyAwesomeColor.push(Color3.new(1, 0, 0)) -- pushes to the server
serverEvent.MyDumbNumber.push(424242) -- pushes to all clients
serverEvent.MyCoolBoolean.pushTo(123456, true) -- pushes to a specific client with the UserId "123456"

-- POV: some server code is receiving events from the client via `clientEvent`
function Update(dt: number)
    for i = 1, clientEvent.count do -- iterate over all events received from the client
        local color = clientEvent.MyAwesomeColor[i]
        local coolNum = clientEvent.ACoolNumber[i]
        
        if clientEvent.sender == 12345 then -- only print colors sent by a client with the UserId "123456"
            print(color)
        end
    end
end
```
!!! tip
    To "sync" events between the client and server, both the client and server need to make the same `EventTable` under the same name containing the same names. The fields and the direction do not need to be the same, but you should use seprate names for seprate fields for your own sanity (different directions is okay though).
!!! note
    `EventData` is a "luau-ified" version of `EventType` that maps all its possible data types to their corresponding luau equivalents. `I32`, `F32`, and `U8` collapse into `number`, `Entity` become `Instance`, and `Vec3`/`Color` become `Vector3` and `Color3` respectively
!!! warning
    Unlike [Queries](query.md), events don't need to be refreshed to get the latest version of them because Luduvo automatically clear every event updates every frame. Not only can multiple scripts listen for and react to the same events without knowing that of each other's existance, but **any event not dealth with the frame it was push are gone forever**. If the client/server skips frames, **it can also potentially skip events**. Watch for race conditions and invisible bugs!

It's easiest to think of `Event`s as a collection of remote events constantly listening for updates. Since a server or a client can push multiple events in a single frame, events need to be processed with a loop over `Event.count` (which is the number of events collected in the current frame).
