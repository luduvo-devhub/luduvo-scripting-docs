---
icon: lucide/box
---

# Components

Components are data that can be attached to [Instances](../instances.md) to define their behavior, appearance, relationship between other Instances, and more. More often than not, Components store their data in the form of table items called "fields".

!!! warning
    In Luduvo Studio, the values you see in the Editor are different from the actual components that you will be accessing in your scripts. For some reason, the Editor mixes, shuffles, renames, and otherwise reorganizes components and some their fields into new groups such as **Transform**, **Data**, **Physics**, **Color**, **Material**, and more. While they proclaim that these are "Components", they do not accurately represent the actual internal component names. For example, the Editor's "Transform" Component really is a combination of separate `Position`, `Rotation`, and `Scale` Components. "Transform" is not a real component name.

## Script access

Every Component can be used as an exact, case-sensitive filter with [`game.World.Query`](../query.md), `Query:With`, `Query:Without`,`game.World.Each`, `Instance:HasComponent`, `Instance:AddComponent`, and `Instance:RemoveComponent`, subject to the component's write scope.

Currently, only 4 Components expose fields that can be accessed through a Query:

| Query column | Luau type | Scope |
| --- | --- | :---: |
| `query.Position[i]` | `vector` | read/write |
| `query.Scale[i]` | `vector` | read/write |
| `query.BrickColor[i]` | `vector` | read/write |
| `query.Velocity[i]` | `vector` | read-only |

All other built-ins only can act as a filter in a Query. Some Components still have other means of indirect access though a separate Instance/game-service property or method, but many do not. You cannot access components through an Instance directly like `Instance.Component.field`.

## Custom data

Currently, you cannot make your own custom components. Components are hard coded into the engine, and `AddComponent` can only attach Components from a giant lookup table. However, Luduvo itself defines two built-in Components as being "custom":

```luau
type PlayerSpawnerComponent = {
    character: string,
    respawnDelay: number,
}

type ToolComponent = {
    equipped: number, -- U8, clamped to 0 through 255
}
```

These 2 custom components are the only Components that get exposed to Query as a table of fields rather than a single value. 

If you need to store custom data directly on an Instance, you can still use [Instance Attributes](../instances.md#attributes).

## Types of Components

While internally all components are formatted the same (assuming they store data), Query selectively exposes some of their fields in different ways.

### Value-Based Components

Value-based components are components that are so simple that they can be represented by a single value. When you access a value-based component in Queries, you directly read and write to the component itself instead of needing to access a nested field. Not all simple components are value-based, but some built-in components are.

For example, [`Position`](Position.md){ data-preview } is a value-based component that can be expressed as a single `Vector3` value. As such, accessing it in Queries looks like this:

```luau
for i = 1, query.count do
    local position = query.Position[i]
    print(position)
    query.Position[i] += Vector3.new(1, 2, 3)
end
```

### Field-Based Components

!!! note
    Currently, only components marked as "custom" ([`Tool`](Tool.md){ data-preview } and [`PlayerSpawner`](PlayerSpawner.md){ data-preview }) can be accessed as field-based components.

Field-based components are components that have fields that must be directly named to be accessed and modified. When you access a field-based component in Queries, you need to use dot notation to specify what field you want to access before you are able to read or write to it.

For example, take [`Tool`](Tool.md){ data-preview }:

```luau
for i = 1, query.count do
    local equipped = query.Tool.equipped[i]
    if equipped then
        print("A player is holding a tool!")
    end
end
```

### Tag Components

Tag components are special components that intentionally do not have any fields. They function as markers that other systems check the existence (or lack thereof) to preform specific actions.

For example, Instances marked with an [`Anchored`](Anchored.md){ data-preview } Component tag will be purposely ignored by physics systems.

## Built-in component names

- [Admin](Admin.md)
- [AmbientLight](AmbientLight.md)
- [Anchored](Anchored.md)
- [Attachment](Attachment.md)
- [AutoLocomotion](AutoLocomotion.md)
- [AutoRotate](AutoRotate.md)
- [BodyPart](BodyPart.md)
- [BrickColor](BrickColor.md)
- [Character](Character.md)
- [CharacterAnimation](CharacterAnimation.md)
- [CharacterAppearance](CharacterAppearance.md)
- [CharacterPhysics](CharacterPhysics.md)
- [CharacterPose](CharacterPose.md)
- [CharacterRig](CharacterRig.md)
- [Collider](Collider.md)
- [CollisionGroup](CollisionGroup.md)
- [CoreMenuAction](CoreMenuAction.md)
- [CoreMenuPage](CoreMenuPage.md)
- [CoreSettingBind](CoreSettingBind.md)
- [DisplayName](DisplayName.md)
- [Exposure](Exposure.md)
- [Health](Health.md)
- [HumanoidState](HumanoidState.md)
- [Identity](Identity.md)
- [Kinematic](Kinematic.md)
- [LensFlare](LensFlare.md)
- [Light](Light.md)
- [LightShadowOff](LightShadowOff.md)
- [LimbAttachment](LimbAttachment.md)
- [Locked](Locked.md)
- [Locomotion](Locomotion.md)
- [Mesh](Mesh.md)
- [Name](Name.md)
- [NoContactFriction](NoContactFriction.md)
- [Position](Position.md)
- [PrefabAnchor](PrefabAnchor.md)
- [PrefabInstance](PrefabInstance.md)
- [PrefabNodeId](PrefabNodeId.md)
- [RenderDisabled](RenderDisabled.md)
- [RigidBody](RigidBody.md)
- [Rotation](Rotation.md)
- [Scale](Scale.md)
- [ShadowOff](ShadowOff.md)
- [Shape](Shape.md)
- [SkyBackground](SkyBackground.md)
- [SpawnPoint](SpawnPoint.md)
- [SpotCone](SpotCone.md)
- [StableId](StableId.md)
- [Stars](Stars.md)
- [SunLight](SunLight.md)
- [SunShadows](SunShadows.md)
- [SurfaceAppearance](SurfaceAppearance.md)
- [SurfaceMaterial](SurfaceMaterial.md)
- [SwingTwistJoint](SwingTwistJoint.md)
- [Transparency](Transparency.md)
- [UIClickable](UIClickable.md)
- [UIClips](UIClips.md)
- [UICorner](UICorner.md)
- [UIDisabled](UIDisabled.md)
- [UIFrame](UIFrame.md)
- [UIHidden](UIHidden.md)
- [UIListLayout](UIListLayout.md)
- [UIOrder](UIOrder.md)
- [UIRect](UIRect.md)
- [UIRoot](UIRoot.md)
- [UIScrollingFrame](UIScrollingFrame.md)
- [UISlider](UISlider.md)
- [UISliderState](UISliderState.md)
- [UIStroke](UIStroke.md)
- [UITextInput](UITextInput.md)
- [UITextSource](UITextSource.md)
- [UITextStyle](UITextStyle.md)
- [UIToggle](UIToggle.md)
- [UIToggleOn](UIToggleOn.md)
- [Velocity](Velocity.md)
- [WorldConfig](WorldConfig.md)
