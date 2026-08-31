---
icon: lucide/file-text
---

# Datatypes

## Types

!!! warning
    This section is incomplete. Feel free to contribute!

### Vector3

#### Constructor(s)

- `Vector3.new(x: number, y: number, z: number)`

#### Properties

- `Vector3.zero`
- `Vector3.one`
- `Vector3.xAxis`
- `Vector3.yAxis`
- `Vector3.zAxis`

#### Methods

- `v:Magnitude()`
- `v:Unit()`
- `v:Dot(v2: Vector3)`
- `v:Cross(v2: Vector3)`
- `v:Lerp(v2: Vector3, t: number)`

---

### UDim2

#### Constructor(s)

- `UDim2.new(xScale: number, xOffset: number, yScale: number, yOffset: number)`

---

### Instance

This is intentionally vague. Some Properties/methods have special read/write/execution rules depending on what type of script it was called with. See [the standalone Instance page](instances.md) for more details.

#### Constructor(s)

- `Prefab.spawn(prefabName: string)`
- `Instance.clone()`

!!! warning
    You cannot spawn prefabs on the Client, and cloning instances from the client doesn't seem replicated to the server. Something there (the fact that cloning is client only or the fact that instance deletion is server only) is a bug.
!!! note
    Instances are automatically parented to the 3D world.

!!! warning
    Unlike Roblox, you cannot get children from dot notation, such as `partA.Child`. You must use `FindFirstChild`, such as `partA:FindFirstChild("Child")`.

#### Properties

- `Instance.Activated`
- `Instance.Anchored`
- `Instance.AngularDamping`

- `Instance.Parent`

- `Instance.Changed`
- `Instance.ChildAdded`
- `Instance.ChildRemoved`

- `Instance.CollisionGroup`

- `Instance.Name`
- `Instance.Color`
- `Instance.Kind`
- `Instance.Transparency`

- `Instance.Orientation`
- `Instance.Position`
- `Instance.Size`
- `Instance.Velocity`

- `Instance.Density`
- `Instance.Friction`

- `Instance.MeshId`
- `Instance.EmissiveTextureId`
- `Instance.TextureId`
- `Instance.UnderlayTextureId`

- `Instance.LinearDamping`
- `Instance.Restitution`
- `Instance.SpawnPoint`

#### Methods

- `Instance:AddComponent(name: string)`
- `Instance:RemoveComponent(name: string)`
- `Instance:HasComponent(name: string)`

- `Instance:Destroy()`

- `Instance:FindFirstChild(name: string)`
- `Instance:GetChildren()`
- `Instance:IsDescendantOf(ancestor: Instance)`

- `Instance:GetSignal(name: string)`
- `Instance:Emit(name: string, ...any)`

- `Instance:GetIdentity()`

- `Instance:GetMoveIntent()`
- `Instance:GetSwingTwistJoint()`
- `Instance:SetSwingTwistJoint(value: SwingTwistJoint)`

- `Instance:GetLinearVelocity()`
- `Instance:SetLinearVelocity(value: vector)`
- `Instance:GetAngularVelocity()`
- `Instance:SetAngularVelocity(value: vector)`

- `Instance:ApplyForce(force: vector, point: vector?)`
- `Instance:ApplyImpulse(impulse: vector, point: vector?)`
- `Instance:ApplyTorque(torque: vector)`

- `Instance:SetBodyMotion(mode: "dynamic" | "kinematic")`
- `Instance:Rotate(axis: vector, angle: number)`

- `Instance:PlayAnimation(clip: string, fadeSeconds: number?, speed: number?)`
- `Instance:StopAnimation()`
- `Instance:ActiveAnimation()`
- `Instance:AnimationWeight(clip: string)`

- `Instance:PreviewAnimation(clip: string, speed: number?, timeSeconds: number?)`
- `Instance:AnimationPreview()`
- `Instance:AdvancePreview()`
- `Instance:StopPreview()`

---

### Signal

Signals are exclusively available to Instances, and Instances have their own signal lifecycle methods that they can use that aren't documented here. See [the standalone Instance page](instances.md#signals) for more details.

### Constructors(s)

!!! note
    The only way to create a Signal is through Instances. As such, you cannot attach a Signal to anything that's not an Instance.

- `Instance:GetSignal(signalName: string)`

#### Methods

- `signal:Connect(callback: (...unknown))`
- `signal:Emit()`

!!! danger
    Neither `signal:Disconnect()` nor `signal:Wait()` are implemented yet (if ever). Such functionality will have to be implemented by yourself.

---

### Tween

!!! note
    Currently, you can only tween UI instances.

#### Constructor(s)

- `Tween(instance, duration, EasingStyle, properties)`

!!! note
    The types of the constructor arguments are currently unknown.

!!! note "Usable styles"
    - `Cubic`
    - `Quad`
    - `Sine`
    - `Back`
    - `Bounce`
    - `Exponential`
    - `Elastic`
