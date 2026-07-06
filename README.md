# Unofficial Luduvo Script docs

>[!WARNING]
> Everything documented here is **untested** and may not work in an actual script, most of this is inferring what i'm seeing from analysing the executable. 


## Scripts
scripts seem to be attached to entities.
within scripts, `self` refers to the entity, the equivalent of doing `script.Parent` in roblox.

## Script Handles
You can access handles of the entity that the script is attached to via the `handles` global

```lua
for i,v in pairs(handles) do
    print(i,v)
end
```

## Global Functions:
| function | ran |
|---|---|
| `Update(dt)` | every frame |
| `PhysicsUpdate(dt)` | every physics step, probbaly at a fixed frequency idk|

## Globals:
| global | notes |
|---|---|
| `tick()` |  |
| `typeof(x)` | Returns the luduvo type name of a value |
| `world` | equivalent to roblox's workspace maybe |
| `handles` | the handles of the entity the script is attached to |
| `self` | the entity instance that the script is attached to |

## Types:
Still doing research on this

### Vector3
#### Constructor
- `Vector3.new(x, y, z)`

#### Constants
- `Vector3.zero`
- `Vector3.one`
- `Vector3.xAxis`
- `Vector3.yAxis`
- `Vector3.zAxis`

#### Methods
- `v:Magnitude()`
- `v:Unit()`
- `v:Dot(v2)`
- `v:Cross(v2)`
- `v:Lerp(v2, t)`
#
### Vector2
Currently researching
#
### UDim2
Currently researching
#
### Instance
#### Constructor
- `Instance.new(className)`

#### Methods
- `inst:Destroy()`
- `inst:FindFirstChild()`
- `inst:GetChildren()`
- `inst:IsDescendantOf()`

#### Properties
For all Instances:
- `Name`
- `Parent`
- `ClassName`

For Part Instances:
- `Position`
- `Size`
- `Rotation`
- `Orientation`
- `Scale`
- `Anchored`
- `Velocity`

UI Instances:
- `Image`
- `ImageColor`
- `ImageTransparency`
- `SliceCenter`
- `CanvasSize`
- `CanvasPosition`
  
Misc:
- `NetworkID`
- `StableID`
- `RigidBody`
- `CharacterMoveIntent`
- `RemoteEntity`

#### Events

For user interface instances?
- `MouseButton1Click`
- `MouseButton1Down`
- `MouseButton1Up`
- `MouseEnter`
- `MouseLeave`
- `MouseWheel`
 

#### Example:
```lua
local part = Instance.new("Part")
part.Position = Vector3.new(0,30,0)
part.Parent = world
```
#
### Signal
`signal:Connect(callback)`
stuff like `sig:Disconnect()` or `sig:Wait` proabably do exist but I can't find anything about them rn
#
### Tween
You can only tween UI instances

Tween(Instnace, Duration, EasyingStyle, properties)

styles:
- quad
- cubic
- sine
- exponential
- back
- bounce
- elastic