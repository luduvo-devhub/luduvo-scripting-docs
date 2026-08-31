---
icon: lucide/box
---

!!! note
    This is a stub and currently a work in progress. Contribute, or come back later for updates!

# Character

Characters are Luduvo's prefab for creating visible, controllable characters in a game. Currently, this is prefab is used to create player characters under the hood, but you can also use the Character prefab to create NPCs or custom character models since very little details on the character's appearance or behavior are hardcoded into the prefab itself.

## Constructor(s)

- `Prefab.spawn("Character")`

## Components

### Removable

- `Transform`
- `Data`
- `PrefabInstance`
- `Velocity`
- `Shape`
- `Physics`
- `CollisionGroup`
- `Color`
- `Health`
- `Locomotion`
- `HumanoidState`
- `BodyPart`

### Permanent

- `Character`
- `CharacterRig`
- `CharacterAnimation`
- `CharacterPhysics`
- `AutoRotate`
- `AutoLocomotion`
- `Attributes`
