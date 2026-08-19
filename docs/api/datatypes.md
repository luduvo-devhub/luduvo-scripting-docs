---
icon: lucide/file-text
---

# Datatypes

## Constructors

| Name                                      | Description                        |
| ----------------------------------------- | ---------------------------------- |
| `Color3(r: number, g: number, b: number)` | Returns a Vector3                  |
| `Vector2(x: number, y: number)`           | Returns a Vector3, with Z set to 0 |

## Types

!!! warning
    This section is incomplete. Feel free to contribute!

### Vector3

#### Constructor(s)

- `Vector3.new(x: number, y: number, z: number)`

#### Constants

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

!!! warning
    See [the standalone Instances page](instances/index.md) for more detail.

#### Constructor(s)

- `Instance.new(className: string)`

!!! note "Creatable classes"
    - `Part`
    - `SpawnLocation`

!!! note
    Instances are automatically parented to the 3D world.

!!! warning
    Unlike Roblox, you cannot get children from dot notation, such as `partA.Child`. You must use `FindFirstChild`, such as `partA:FindFirstChild("Child")`.

!!! danger
    You cannot create instances on the Server.

---

### Signal

!!! warning
    Not much is known about this datatype right now.

#### Methods

- `signal:Connect(callback: (...unknown) -> ())`

!!! note
    `signal:Disconnect()` and `signal:Wait()` probably exist, but we have no way to test for either.

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