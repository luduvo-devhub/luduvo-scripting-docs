---
icon: lucide/box
---

# Instances

Instances in Luduvo are essentially any objects that can physically show up in the World hiearchy tree. Menus, parts, characters, sounds, lights, Spawners, and more are all classified as an "Instance" under the hood.

However, despite their name, Luduvo Instances are not a "base" class like you might expect to see in object-oriented game engines like Roblox. Quite literally, everything in a Luduvo World tree is an Instance.

But on the other hand, Luduvo Instances are also not the traditional "entities" that you might expect to see in other ECS-based game engines. Normally, Entities are tiny husks that have almost no data or behavior of their own, and are instead almost entirely defined by the Components they hold inside of them. This is mostly true in Luduvo since it is also an ECS engine, but Instances almost resemble OOP base classes in the sense that they have a comparitively ginormous amount of built-in functionality designed to be extended by the user.

This unprecidented class size is mostly due to Instances containing everything that a helper function might have handled in its stead. There are a few weird exceptions that will likely be removed in later updates, but largely anything that pertains to an Instance can be handled directly by the Instance itself.

## Creating Instances

There are three ways to create an Instance: 

### Using the Editor

To avoid writing code, you can use the editor to directly create Instances that all automatically get initialized as soon as the project starts. Once they're created, you can then [parent scripts](scripts.md) to them to serve as a "starting point" for you to branch from. To access the other instances in your project, you can use hierarchy-related methods to traverse the World tree. These include:

| Field | Description |
| --- | --- |
| `Instance:FindFirstChild(name: string) -> Instance?` | Returns the first nested Instance with that name, or `nil`. There is no recursive argument. |
| `Instance:GetChildren() -> {Instance}` | Returns an array of immediate children. |
| `Instance:IsDescendantOf(ancestor: Instance) -> boolean` | Tests if the current Instance is nested inside the given `ancestor` Instance. |
| `Instance.Parent: Instance?` | Returns the Instance currently nesting the current instance in, or `nil` if it has no parent. |

All of these methods are available on all Instances regardless of where they are called.

### Using Prefabs

If you need to factory spawn instances, you can use the [Prefab](/luduvo-scripting-docs/api/prefabs) system to create instances from a pre-defined template through the `World.Prefab:Spawn("PrefabName)` method. Details are available in the aformentioned documentation.

### Using Clones

Instances also manage their own lifecycle, with the ability to clone and destroy themselves through the aptly named `Instance:Clone()` and `Instance:Destroy()` methods.

Interestingly, only `Instance:Clone()` is available for use on the client, while `Instance:Destroy()` is a server-only method. When called on the client, `Instance:Clone()` will return a copy of the instance that **is not replicated to the server**. This is likely a bug (`Instance.Destroy()` being server only, not cloning being available on the client), so be careful using this method on the client. On top of that, `Instant:Clone` intentionally clones the instance without parenting them to the World hierarchy in case you want to wait before sending clones to the server. As such, you need to remember to add the clone to the World hierarchy yourself by setting its `Parent` property to the desired parent instance.

If you need to make a clone that is replicated to the server from the client, use [Events](events.md).

## Component Management

!!! note
    You currently cannot create custom components, as all components are currently hardcoded into the engine. See the list of usable [Components](components/index.md) for the ones that are available for management.

Like with other ECS Entities, Instances are still laregely defined by the [Components](components/index.md) that are attached to them. Components are managed through `Instance:AddComponent(name: string)`, `Instance:RemoveComponent(name: string)` and `Instance:HasComponent(name: string)` methods. As their names suggest, these methods are used to add, remove and check for the presence of a component on an instance respectively. 

These three components can be used on both the client and server, but the components are only manageable from the place that they were created from. For example, if you call `Instance:AddComponent(name: string)` from the server, only other server scripts will be able to access the component. If you try to manage the component from the client, you will be greeted with an error along the lines of `'<name>' is replicated; only server scripts may write it`. Server components remain readable to all clients, however. 

If you call `Instance:AddComponent(name: string)` from the client, only that specific client will be able to manage the component because it isn't replicated to the server at all. Attempting to access a client component from the server or other clients than the one that created it will result in a component-not-found-esq error.

If you need to manage a component from a different place than where it was created, you will need to create them from the server and use [Events](events.md) to let clients request mutations to the component.

Once created, the only way to mutate the component fields themselves is through [Queries](query.md).

## Signals

!!! note
    If you are looking for client to server communication, use [Events](events.md) instead.
!!! warning
    Custom signals cannot be deleted, and will remain in memory until the instance is destroyed. You need to make your own "deleted" check in custom signals if you plan on using them without causing memory leaks in your game.

Signals are Luduvo's equivalent of BindableEvents/RBXScriptSignals, or some other game engine's "hook" event equivalent. Luduvo uses them internally to hook scripts into engine events, but they can also be created by you using `Instance:GetSignal(name: string, ...args: any) -> Signal`.

Interstingly, `:GetSignal()` is the only way to create a signal, so they are likely intended to only be usable in the context of instances.

### Emitting Signals

Once a signal is attached to an instance, it can be fired using `Signal:Emit(...args: any)`, and you can connect listeners to run callback functions on successful emission using `Signal:Connect(callback: (...args: any) -> ())`. 

Signal connections and emmissions are completely local to where they are created, so they will **not** be replicated to other clients nor the server. If the server emits a signal on an instance that is replicated to and seen by other clients, only the server's signals will be emitted. If a client emits a signal on an instance that multiple clients and the server are listening to, only that client's signals will be emitted. The `args` defied in `GetSignal` are the exact args that you must emit in `Signal:Emit()` as well as the arguments given to the signal's `:Connect()` listeners.

If you need a signal to emit across multiple clients and the server, you will need to do so by using [Events](events.md) or by putting emmission logic in a `game.World.Server` that polls for changes to the instance's components (which is likely how Luduvo's own signals are handled).


Funnily enough, the `Emit` method will work on ANY signal, even if the Signal is supposed to be managed by Luduvo itself. This includes all 4 of the signals naturally created upon Instance creation:

- `Instance.Changed:Connect()`, which does nothing
- `Instance.ChildAdded:Connect(child: Instance)`, which fires when an instance is repareted to this instance via `Instance.Parent`. The `child` argument is the new instance that is being repareted to it.
- `Instance.ChildRemoved:Connect(child: Instance)`, which fires when an instance under it is repareted to another instance or `nil` via `Instance.Parent`. The `child` argument is the old instance that is leaving your hierarchy.
- `Instance.Activated:Connect(activator: Instance)`, which fires when the instance is clicked on. This signal is only relevant to UI Instances that have the [UIClickable](components/UIClickable.md) component attached to them. UIs with the [UIDisabled](components/UIClickable.md) component attached will be ignored and not trigger `Activated`.

!!! warning
    There are a few oddities about these signals that are worth noting:
    - `ChildAdded`/`ChildRemoved` does not check if the instance being repareted to is itself and will fire even if the instance is being repareted to itself.
    - `Changed` does nothing, has no arguments, and will not fire unless you manually `:Emit()` it.
    - `Activated` will not fire if the character/player that activated is actively being destroyed or doesn't have a [Health](components/Health.md) component attached to it. It doesn't actually care if the character is dead or not, or is even a player at all (though you kind of have to be a player to click on it).

Alongside `signal:Emit()`, Instances also have `Instance:Emit(name: string, ...args: any)` that can be used to fire any signal by name you gave it when running `Instance:GetSignal()`.

## Hardcoded Component Logic

Currently, the line between what is owned by an Instance and what is owned by Components is shakey since many component and component fields are directly coupled to Instance methods and properties. This was probably done because of time constraints or the fact the Luduvo currently doesn't currently have the internal plumbing to express them in any other way. Here is a list of all of them, but expect these to be slowly phased out as the engine matures:

### Input

While this is technically user input, it's specialized specifically for character movement. Sorry if I excited you.

#### Relevant Types

```luau
type MoveIntent = {
    x: number,
    z: number,
    jump: boolean,
    shiftLock: boolean,
    targetYaw: number,
}
```

#### Methods

Method | Scope | Behavior |
| --- | --- | --- |
| `GetMoveIntent() -> MoveIntent` | Server only | Returns the current character movement request. |


### Appearance

!!! note
    Anything marked runnable by a client is not replicated to the server or any other clients than the one the code was ran on.
!!! note
    Anywhere `vector` is used, `Vector3.new`, `Vector2.new`, and `Color3.new` will also work indiscriminately as inputs as well. See [Data Types](globals.md#data-types) for more information.

#### Properties

Property | Scope | Behavior |
| --- | --- | --- |
`Kind: string` | Read-only, client and server | Computes a creator-facing entity kind from the entity's component set. `Shape.Type` and UI marker components contribute to the result; there is no single `Kind` component or field. |
| `Name: string` | Read/write, client and server | Reads or writes the string value stored by the `Name` component.|
| `Position: vector` | Read/write, client and server | Reads or writes the complete [`Position`](/luduvo-scripting-docs/api/components/position) component value. |
| `Orientation: vector` | Read/write, client and server | Reads or writes the [`Rotation`](/luduvo-scripting-docs/api/components/rotation) component. Note that the Instance name (orientation) differs from the actual component name (rotation), but they are the same thing. |
| `Size: vector` | Read/write, client and server | Reads or writes the complete [`Scale`](/luduvo-scripting-docs/api/components/scale) component value. |
| `Color: vector` | Read/write, client and server | Reads or writes the RGB value in the [`BrickColor`](/luduvo-scripting-docs/api/components/brickcolor) component. |
| `Transparency: number` | Read/write, client and server | Reads or writes the scalar [`Transparency`](/luduvo-scripting-docs/api/components/transparency) component value. |
| `MeshId: number` | Read on client and server; write on server only | Reads or writes the asset-ID value stored by the [`Mesh`](/luduvo-scripting-docs/api/components/mesh) component. The stored field name was not recovered. |
| `TextureId: number` | Read on client and server; write on server only | Reads or writes [`SurfaceAppearance.Albedo`](/luduvo-scripting-docs/api/components/surfaceappearance), exposed to Luau as a numeric asset ID. |
| `EmissiveTextureId: number` | Read on client and server; write on server only | Reads or writes [`SurfaceAppearance.Emissive`](/luduvo-scripting-docs/api/components/surfaceappearance), exposed to Luau as a numeric asset ID. |
| `UnderlayTextureId: number` | Read on client and server; write on server only | Reads or writes [`SurfaceAppearance.Underlay`](/luduvo-scripting-docs/api/components/surfaceappearance), exposed to Luau as a numeric asset ID.|
| `SpawnPoint: boolean` | Read-only, client and server | Reports whether the fieldless [`SpawnPoint`](/luduvo-scripting-docs/api/components/spawnpoint) tag component is present.

### Identity

#### Relevant Types

```luau
type IdentityResult = {
    userId: number,
    displayName: string,
    isAdmin: boolean,
}
```
#### Methods

Method | Scope | Behavior |
| --- | --- | --- |
| `GetIdentity() -> IdentityResult` | Client and server | Returns the entity's identity data.

### Physics
!!! note
    Anything marked runnable by a client is not replicated to the server or any other clients than the one the code was ran on.
!!! note
    Anywhere `vector` is used, `Vector3.new`, `Vector2.new`, and `Color3.new` will also work indiscriminately as inputs as well. See [Data Types](globals.md#data-types) for more information.


```luau
type SwingTwistJoint = {
    Anchor: vector,
    TwistAxis: vector,
    PlaneAxis: vector,
    RestAxis: vector,
    PlaneCone: number,
    NormalCone: number,
    TwistMin: number,
    TwistMax: number,
    Friction: number,
}

type BodyMotionMode = "dynamic" | "kinematic"

```

#### Properties

Property | Scope | Behavior |
| --- | --- | --- |
| `Anchored: boolean` | Read/write, client and server | Reports the presence of the fieldless [`Anchored`](/luduvo-scripting-docs/api/components/anchored) tag component. Writing `true` adds the tag and writing `false` removes it. |
| `CollisionGroup: string` | Read/write, client and server | Reads or writes [`CollisionGroup.Group`](/luduvo-scripting-docs/api/components/collisiongroup) as a collision-group name rather than exposing the stored numeric group entry. |
| `Density: number` | Read/write, client and server | Reads or writes [`RigidBody.Density`](/luduvo-scripting-docs/api/components/rigidbody). |
| `Friction: number` | Read/write, client and server | Reads or writes [`RigidBody.Friction`](/luduvo-scripting-docs/api/components/rigidbody). |
| `Restitution: number` | Read/write, client and server | Reads or writes [`RigidBody.Restitution`](/luduvo-scripting-docs/api/components/rigidbody). |
| `LinearDamping: number` | Read/write, client and server | Reads or writes [`RigidBody.LinearDamping`](/luduvo-scripting-docs/api/components/rigidbody). |
| `AngularDamping: number` | Read/write, client and server | Reads or writes [`RigidBody.AngularDamping`](/luduvo-scripting-docs/api/components/rigidbody). |
| `Velocity: vector` | Read-only, client and server | Reads the complete [`Velocity`](/luduvo-scripting-docs/api/components/velocity) component value. Use the `SetLinearVelocity` method to write. |

#### Methods

Method | Scope | Behavior |
| --- | --- | --- |
| `GetIdentity() -> IdentityResult` | Client and server | Returns the entity's identity data. |
| `GetMoveIntent() -> MoveIntent` | Server only | Returns the current character movement request. |
| `GetSwingTwistJoint() -> SwingTwistJoint?` | Client and server | Reads the joint definition, or returns `nil` when absent. |
| `SetSwingTwistJoint(value: SwingTwistJoint) -> ()` | Server only | Replaces the joint definition. |
| `GetLinearVelocity() ->P vector` | Server only | Reads rigid-body linear velocity. |
| `SetLinearVelocity(value: vector) -> ()` | Server only | Replaces rigid-body linear velocity. |
| `GetAngularVelocity() -> vector` | Server only | Reads rigid-body angular velocity. |
| `SetAngularVelocity(value: vector) -> ()` | Server only | Replaces rigid-body angular velocity. |
| `ApplyForce(force: vector, point: vector?) -> ()` | Server only | Applies a force, optionally at a point. The binding metadata does not label that point's coordinate space. |
| `ApplyImpulse(impulse: vector, point: vector?) -> ()` | Server only | Applies an impulse, optionally at a point. |
| `ApplyTorque(torque: vector) -> ()` | Server only | Applies torque to the rigid body. |
| `SetBodyMotion(mode: BodyMotionMode) -> ()` | Server only | Switches the physics body's motion mode. Interestingly, switching from `Kinematic` to `Dynamic` clears the body's velocity. |
| `Rotate(axis: vector, angle: number) -> ()` | Client and server | Applies an axis-angle rotation, subject to write authority. |


### Animation

!!! note
    Anything marked runnable by a client is not replicated to the server or any other clients than the one the code was ran on.

#### Relevant Types

```luau
type AnimationPreviewState = {
    clip: string,
    time: number,
    speed: number,
    playing: boolean,
    shared: boolean,
}
```

#### Methods

| Method | Scope | Behavior |
| --- | --- | --- |
| `PlayAnimation(clip: string, fadeSeconds: number?, speed: number?) -> ()` | Server only | Starts an animation clip with optional fade and speed arguments. |
| `StopAnimation() -> ()` | Server only | Stops the active animation. |
| `ActiveAnimation() -> string?` | Server only | Returns the active clip name, or `nil`. |
| `AnimationWeight(clip: string) -> number?` | Server only | Returns the clip's current blend weight when available. |
| `PreviewAnimation(clip: string, speed: number?, timeSeconds: number?) -> ()` | Server only | Starts or positions animation-preview playback. |
| `AnimationPreview() -> AnimationPreviewState?` | Server only | Returns the current preview state, or `nil`. |
| `AdvancePreview() -> boolean` | Server only | Advances preview state and reports whether it advanced. |
| `StopPreview() -> boolean` | Server only | Stops preview playback and reports whether a preview was stopped.
