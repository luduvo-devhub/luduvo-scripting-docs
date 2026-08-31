---
icon: lucide/box
---

# Queries

Queries are the main way you search for an arbitrary amount of unknown Instances in a Luduvo World. If you know the specific type or specific locations of Instance you're looking for, you can use a [Script handle](scripts.md#script-handles) or [Instance hierarchy methods](instances.md#using-the-editor).

## `World.Query`

The main method for querying Instances in a Luduvo World is through the `World.Query` method:

```luau
type World = {
    Query: (...componentNames: string) -> Query,
}
```
!!! warning
    `World.Query`, `Query.With`, and `Query.Without` should not be used inside loops, as there can only be so many queries until Luduvo foceibly stops you.

When making a query, you can "initialize" it with a starting query that searches for entities with the specified component names attached to it. 

After initialization, `World.Query` will return a `Query` object that you will use for the rest of your the query operations:

```luau
type Query = {
    count: number,
    Entity: {Instance},
    [string]: {Component},
    Refresh: () -> number,
    With: (componentName: string) -> Query,
    Without: (componentName: string) -> Query,
}
```

`With` and `Without` are used to add filters to the query results outside of the initial query initiated in `World.Query`. These methods return a new `Query` object with the filter applied and does not mutate in-place.

`With` and `Without` are also chainable:

```luau
local query = world.Query("Position", "Velocity")
    :With("Health")
    :Without("Material")
```

### Using Queries

After initializing a query with `World.Query` and honing the results with `With` and `Without`, you can then directly access the found entities by directly iterating over the `Query` object. However, `Query` does not store the found entities in a list; it is organized by their (matched?) components. Conceptually, a query result may look like this:

```luau
local movableParts: Query = game.World.Query("Position", "Shape")
movableParts = {
    Position: { Vector3(1, 2, 3), Vector3(4, 5, 6) },
    Shapes: { "Cube", "Sphere" },
    count: 2,
    Entities: { Instance at <0x083ad>, Instance at <0x083ae> },
}
```
Queries organize the found entities by their (matched?) components, with each index corresponding a specific entity instead of returning the entire Entity in giant entity tables.

Another thing to know about Queries is that they do not automatically update when the world changes. So, before using a query result, you should call `Refresh` to re-query the world:

```luau
local looseParts: Query = game.World.Query("Position", "Scale") --operates the same as ":With" I believe
    :With("Shape")
    :Without("Anchored") -- Looks for components without this

function Update(dt) do
    looseParts:Refresh()
    print(`Current captured Entities: {looseParts.count}`)
    for loosePart in looseParts do end -- INCORRECT!!! LooseParts does not store its found results in a list of entites. It is organized by their (matched?) components
    for i = 1, looseParts.count do -- correct :). It may also be `for i=1, looseParts:Refresh() do end` because Refresh gives back the number of entities it found`
        local loosePartPosition = looseParts.Position[i] -- this gets entity i's Position value
        looseParts.Position[i] += loosePartPosition -- I think it can also be mutated through the same operation
    end
end
```

Of course, you can still attempt to loop through the entities:
```luau
for loosePart in looseParts.Entites do end
```
But you cannot edit or read components from Instances. If you want to read or edit a component from an Instance, you must do it through the method shown above.

The final important thing to know about Queries is that Queries operate differently depending on where they are called and made. If made in server scripts, changes to components get replicated to all clients. However,if Queries are made in client scripts, changes to components only affect that specific client. If you try to change components made by the server in a client script, Luduvo will throw an error. And if you try to change components made by a client in a server script, Luduvo will not be able to find them (since such changes aren't replicated to the server) and therefore throw an error.

If you need to replicate changes to components from a client to the server, you can use [Events](events.md) to request the server to update said component.

## `World.Each`

!!! warning
    This section of the document is still a work in progress. Details may be incomplete or inaccurate. Contributions are welcome!
    
The `World.Each` method is very similiar to `World.Query`, but it only accepts a single component type and does not return a Query result. Instead, it returns a list of all Instances that have the specified component. If you need a quock way to iterate over a group of Instances, this is how you do it:

```luau
type World = {
    Each: (component: string) -> { Instance }
}

for instance in World.Each("SpawnPoint") do
    print(instance.Name)
end
