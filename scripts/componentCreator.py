"""Generate the built-in component reference pages."""

from pathlib import Path

COMPONENTS = {
    # Tab autocomplete generated most of these. Will revisit soon(tm)
    "Position": "stores where an Instance is located in the world",
    "Rotation": "stores an Instance's rotation",
    "Scale": "stores an Instance's size",
    "Name": "stores the name shown in Studio's Outliner",
    "Velocity": "stores an Instance's linear velocity",
    "Shape": "selects an Instance's primitive shape",
    "Collider": "selects an Instance's collider shape",
    "RigidBody": "stores an Instance's physical material properties",
    "Anchored": "marks an Instance as unaffected by physics",
    "CollisionGroup": "assigns an Instance to a collision group",
    "Kinematic": "marks an Instance's physics body as kinematic",
    "Locked": "marks an Instance as locked",
    "BrickColor": "stores an Instance's color",
    "Transparency": "stores an Instance's transparency",
    "ShadowOff": "disables an Instance's rendered shadow",
    "SurfaceMaterial": "stores an Instance's surface material",
    "Mesh": "stores an Instance's mesh asset",
    "SurfaceAppearance": "stores an Instance's surface texture assets",
    "SpawnPoint": "marks an Instance as a player spawn point",
    "StableId": "stores an engine-assigned stable identifier",
    "PrefabInstance": "records which prefab an Instance came from",
    "PrefabNodeId": "identifies an Instance's node within a prefab",
    "PrefabAnchor": "marks an Instance as a prefab anchor",
    "Character": "marks an Instance as a character",
    "CharacterPhysics": "opts an Instance into character physics",
    "CharacterAnimation": "opts an Instance into character animation",
    "Health": "stores character health state",
    "Locomotion": "stores character locomotion state",
    "HumanoidState": "stores the current humanoid state",
    "AutoRotate": "opts a character into automatic rotation",
    "NoContactFriction": "disables contact friction for an Instance",
    "CharacterRig": "marks an Instance as a character rig",
    "AutoLocomotion": "opts a character into automatic locomotion",
    "LimbAttachment": "stores limb attachment data",
    "SwingTwistJoint": "stores swing-twist joint settings",
    "BodyPart": "identifies a character body part",
    "CharacterAppearance": "stores character appearance asset references",
    "CharacterPose": "stores character pose data",
    "Identity": "stores a user identity reference",
    "DisplayName": "stores a user's display name identifier",
    "Admin": "marks an identity as an administrator",
    "RenderDisabled": "disables rendering for an Instance",
    "Attachment": "stores an attachment type and target",
    "UIRect": "stores a UI element's rectangle and sizing behavior",
    "UIOrder": "stores a UI element's draw and layout order",
    "UIHidden": "hides a UI element and its descendants",
    "UIFrame": "stores a UI frame's fill",
    "UIStroke": "stores a UI element's border style",
    "UICorner": "stores a UI element's corner radius",
    "UIClips": "clips UI descendants to the Instance's rectangle",
    "UITextStyle": "stores text color, alignment, and rendering settings",
    "UITextSource": "stores authored UI text",
    "UITextInput": "stores editable-text settings",
    "UIRoot": "marks the root of a UI overlay",
    "UIClickable": "opts a UI element into pointer hit-testing",
    "UIListLayout": "stores list layout and margin settings",
    "UIScrollingFrame": "stores a scrolling frame's canvas size",
    "UISlider": "stores a slider's visual style",
    "UISliderState": "stores a slider's steps and current index",
    "UIToggle": "stores a toggle's visual style",
    "UIToggleOn": "marks a toggle as on",
    "UIDisabled": "marks a UI control as disabled",
    "CoreMenuAction": "stores a core-menu action",
    "CoreSettingBind": "binds a core-menu control to a setting operation",
    "CoreMenuPage": "stores a core-menu page identifier",
    "Light": "stores a local light's color, intensity, and range",
    "SpotCone": "stores a spotlight's inner and outer cone angles",
    "LightShadowOff": "disables shadows for a local light",
    "SunLight": "stores the world's directional sunlight settings",
    "AmbientLight": "stores the world's ambient-light settings",
    "SkyBackground": "stores the world's sky-background settings",
    "SunShadows": "stores the world's sunlight shadow settings",
    "Exposure": "stores the world's exposure range",
    "Stars": "stores the world's star luminance",
    "LensFlare": "stores the world's lens-flare settings",
    "WorldConfig": "stores the world's physics and visibility settings",
    "Tool": "stores the world's tool settings",
    "PlayerSpawner": "stores the world's player spawner settings",
}


# Each tuple is (runtime field name, serialized type, note). These are native
# serialization fields, not generic Luau properties.
def fields(names: str, stored_type: str):
    return [(name, stored_type, "") for name in names.split()]


FIELDS = {
    "Position": fields("x y z", "number"),
    "Rotation": [(axis, "f32", "Quaternion component") for axis in "xyzw"],
    "Scale": fields("x y z", "number"),
    "Name": [("id", "u32", "Interned string ID; shown as Name")],
    "Velocity": fields("x y z", "number"),
    "Shape": [("kind", "u8", "Editor label: Type")],
    "Collider": [("kind", "u8", "Editor label: Collider")],
    "RigidBody": fields(
        "friction restitution density linearDamping angularDamping", "f32"
    ),
    "CollisionGroup": [("index", "u8", "Editor label: Group")],
    "BrickColor": fields("r g b", "number"),
    "Transparency": [("value", "f32", "")],
    "SurfaceMaterial": [("type", "u64", "Runtime enum value")],
    "Mesh": [("id", "u64", "Asset ID; exposed to Luau as MeshId")],
    "SurfaceAppearance": fields(
        "albedo normal metallic_roughness occlusion emissive underlay", "u64 asset ID"
    ),
    "StableId": [("value", "u64", "")],
    "PrefabInstance": [("id", "u32", "Interned prefab ID; editor label: PrefabId")],
    "PrefabNodeId": [("value", "u32", "Interned ID")],
    "Health": fields("health maxHealth", "f32"),
    "Locomotion": fields("walkSpeed jumpPower hipHeight maxSlopeAngle", "f32"),
    "HumanoidState": [("current", "u8", "Enum")]
    + fields("timer no_floor_timer launch_vx launch_vz tilt_dot", "f32"),
    "LimbAttachment": fields("joint.x joint.y joint.z pivot.x pivot.y pivot.z", "f32"),
    "SwingTwistJoint": fields(
        "anchor.x anchor.y anchor.z twistAxis.x twistAxis.y twistAxis.z planeAxis.x planeAxis.y planeAxis.z restAxis.x restAxis.y restAxis.z planeConeDeg normalConeDeg twistMinDeg twistMaxDeg frictionTorque",
        "f32",
    ),
    "BodyPart": [("type", "u8", "Enum; editor label: Part")],
    "CharacterAppearance": fields(
        "body[0] body[1] body[2] body[3] body[4] body[5] face shirt pants",
        "u64 asset ID",
    ),
    "CharacterPose": [("part", "168-byte record", "")],
    "Identity": [("user_id", "u64", "Editor label: User Id")],
    "DisplayName": [("id", "u32", "Interned string ID; editor label: NameId")],
    "Attachment": [("slot", "u8", ""), ("is_root", "u8", "Boolean")],
    "UIRect": fields(
        "position.x.scale position.x.offset position.y.scale position.y.offset size.x.scale size.x.offset size.y.scale size.y.offset max.x.scale max.x.offset max.y.scale max.y.offset anchor_x anchor_y",
        "f32",
    )
    + [("size_mode[0]", "u8", "X-axis enum"), ("size_mode[1]", "u8", "Y-axis enum")],
    "UIOrder": [
        ("z_index", "u16", "Editor label: Z Index"),
        ("layout_order", "u16", "Editor label: Layout Order"),
    ],
    "UIFrame": fields("fill.r fill.g fill.b fill.a", "f32"),
    "UIStroke": fields("color.r color.g color.b color.a width", "f32"),
    "UICorner": [("radius", "f32", "Pixels")],
    "UITextStyle": fields(
        "color.r color.g color.b color.a outline_color.r outline_color.g outline_color.b outline_color.a font_size outline_width",
        "f32",
    )
    + [
        ("h_align", "u8", "Enum"),
        ("v_align", "u8", "Enum"),
        ("no_translate", "u8", "Boolean"),
        ("bold", "u8", "Boolean"),
    ],
    "UITextSource": [("id", "u32", "Interned string ID; editor label: TextId")],
    "UITextInput": [
        ("placeholder", "u32", "Interned string ID"),
        ("max_length", "u32", ""),
    ]
    + fields("cursor_color.r cursor_color.g cursor_color.b cursor_color.a", "f32")
    + [("password", "u8", "Boolean")],
    "UIListLayout": [
        ("axis", "u8", "Enum"),
        ("align", "u8", "Enum"),
        ("spacing", "f32", ""),
        ("margins[0]", "f32", "Editor label: Margin Left"),
        ("margins[1]", "f32", "Editor label: Margin Top"),
        ("margins[2]", "f32", "Editor label: Margin Right"),
        ("margins[3]", "f32", "Editor label: Margin Bottom"),
    ],
    "UIScrollingFrame": fields(
        "canvas_size.x.scale canvas_size.x.offset canvas_size.y.scale canvas_size.y.offset",
        "f32",
    ),
    "UISlider": fields(
        "track_color.r track_color.g track_color.b track_color.a fill_color.r fill_color.g fill_color.b fill_color.a thumb_color.r thumb_color.g thumb_color.b thumb_color.a track_thickness thumb_size",
        "f32",
    ),
    "UISliderState": [("steps", "u8", ""), ("index", "u8", "Editor label: Value")],
    "UIToggle": fields(
        "off_color.r off_color.g off_color.b off_color.a on_color.r on_color.g on_color.b on_color.a knob_color.r knob_color.g knob_color.b knob_color.a knob_inset",
        "f32",
    ),
    "CoreMenuAction": [("action", "u8", "Enum")],
    "CoreSettingBind": [("setting", "u8", "Enum"), ("op", "u8", "Enum")],
    "CoreMenuPage": [("page", "u8", "Enum")],
    "Light": fields("r g b intensity range", "f32"),
    "SpotCone": fields("innerAngle outerAngle", "f32"),
    "SunLight": fields("azimuth elevation r g b intensity", "f32"),
    "AmbientLight": fields("r g b intensity", "f32") + [("source", "u8", "Enum")],
    "SkyBackground": [("mode", "u8", "Enum")] + fields("r g b skyContribution", "f32"),
    "SunShadows": [("mode", "u8", "Enum"), ("fill", "f32", "")],
    "Exposure": fields("evMin evMax", "f32"),
    "Stars": [("luminance", "f32", "")],
    "LensFlare": fields("intensity scale r g b ghostIntensity", "f32"),
    "WorldConfig": fields(
        "fallenPartsDestroyHeight gravity sleepVelocityThreshold viewRadius", "f32"
    ),
    "Tool": fields("equipped", "Boolean"),
    "PlayerSpawner": [("character", "respawnDelay", ""), ("Enum", "number", "")],
}

TAG_COMPONENTS = {
    "Anchored",
    "Kinematic",
    "Locked",
    "ShadowOff",
    "SpawnPoint",
    "PrefabAnchor",
    "Character",
    "CharacterPhysics",
    "CharacterAnimation",
    "AutoRotate",
    "NoContactFriction",
    "CharacterRig",
    "AutoLocomotion",
    "Admin",
    "RenderDisabled",
    "UIHidden",
    "UIClips",
    "UIRoot",
    "UIClickable",
    "UIToggleOn",
    "UIDisabled",
    "LightShadowOff",
}

QUERY_VALUES = {
    "Position": ("vector", "read/write"),
    "Scale": ("vector", "read/write"),
    "BrickColor": ("vector", "read/write"),
    "Velocity": ("vector", "read-only"),
    "Tool": {"equipped": ("boolean", "read/write")},
    "PlayerSpawner": {"character": ("enum", "read/write"), "respawnDelay": ("number", "read/write")},
}

OTHER_ROUTES = {
    "Position": "`Instance.Position: vector`",
    "Rotation": "`Instance.Orientation: vector`",
    "Scale": "`Instance.Size: vector`",
    "Name": "`Instance.Name: string`",
    "Velocity": "`Instance.Velocity: vector` and the velocity methods",
    "Shape": "`Instance.Kind: string`",
    "RigidBody": "`Instance.Density`, `Friction`, `Restitution`, `LinearDamping`, and `AngularDamping`",
    "Anchored": "`Instance.Anchored: boolean`",
    "CollisionGroup": "`Instance.CollisionGroup: string`",
    "Kinematic": "`Instance:SetBodyMotion(...)`",
    "BrickColor": "`Instance.Color: vector`",
    "Transparency": "`Instance.Transparency: number`",
    "Mesh": "`Instance.MeshId: number`",
    "SurfaceAppearance": "`Instance.TextureId`, `EmissiveTextureId`, and `UnderlayTextureId`",
    "SpawnPoint": "`Instance.SpawnPoint: boolean`",
    "CharacterAnimation": "the Instance animation methods",
    "SwingTwistJoint": "`Instance:GetSwingTwistJoint()` and `SetSwingTwistJoint(...)`",
    "Identity": "`Instance:GetIdentity().userId`",
    "DisplayName": "`Instance:GetIdentity().displayName`",
    "Admin": "`Instance:GetIdentity().isAdmin`",
    "UIClickable": "`Instance.Activated: Signal`",
    "SunLight": "`game.Lighting.Sun`",
    "AmbientLight": "`game.Lighting.Ambient`",
    "SkyBackground": "`game.Lighting.Sky`",
    "SunShadows": "`game.Lighting.Shadows`",
    "Exposure": "`game.Lighting.Exposure`",
    "Stars": "`game.Lighting.Stars`",
    "LensFlare": "`game.Lighting.Flare`",
    "WorldConfig": "`game.Physics.Gravity` and `game.Physics.FallenPartsDestroyHeight`",
}


def render_fields(name: str) -> str:
    if name in TAG_COMPONENTS:
        return "This is a [tag component](index.md#tag-components){ data-preview } and has no stored fields."

    rows = FIELDS[name]
    table = ["| Field | Stored type | Notes |", "| --- | --- | --- |"]
    for field, stored_type, note in rows:
        table.append(f"| `{field}` | `{stored_type}` | {note} |")

    return "\n".join(table)


def render(name: str, responsibility: str) -> str:
    if name in QUERY_VALUES and isinstance(QUERY_VALUES[name], tuple):
        value_type, access = QUERY_VALUES[name]
        query_text = f"As a [Value-Based Component](index.md#value-based-components){{ data-preview }}, Queries expose `query.{name}[i]` as `{value_type}` ({access})."
    elif name in QUERY_VALUES and isinstance(QUERY_VALUES[name], dict):
        query_text = f"As a [Field-Based Component](index.md#field-based-components){{ data-preview }}, Queries expose `query.{name}.fieldName` as the type specified in the Stored Fields section. All fields have read/write access."
    else:
        query_text = "While this component can be used as a filter in Queries, it currently does not expose any of its fields to Queries."

    route = OTHER_ROUTES.get(name)
    if route:
        if name in QUERY_VALUES:
            route_text = f"It can also be accessed via {route}."
        else:
            route_text = f"However, it can be accessed via {route}."
    else:
        route_text = "There is no other way to access this component in scripts."

    return f"""---
icon: lucide/box
---

!!! note
    Studio's property groups and the scripting component API are different. A
    label shown in the Properties panel is not automatically a component name or
    a Luau field.

# {name}

`{name}` is a (case-sensitive) built-in component name that {responsibility}.
You can use it with [`game.World.Query`](../query.md){{ data-preview }},
`Query:With`, `Query:Without`, [`game.World.Each`](../query.md){{ data-preview }},
and the Instance component methods.

## Script access

{query_text} {route_text}

Inspector fields are serialization/editor metadata and are not automatically
available as Luau fields. See [Components](index.md){{ data-preview }} for that
distinction and [Instances](../instances.md){{ data-preview }} for fixed property
types and write scope.

## Stored fields
{"""
!!! note
    Currently, these fields are not directly available as editable Luau. As such, they are reported as the types they are stored as in the engine itself instead of Luau types.
""" if not QUERY_VALUES.get(name) and name not in TAG_COMPONENTS else ""}
{render_fields(name)}

"""


def main() -> None:
    missing = set(COMPONENTS) - TAG_COMPONENTS - set(FIELDS)
    extra = (TAG_COMPONENTS | set(FIELDS)) - set(COMPONENTS)
    if missing or extra:
        raise RuntimeError(
            f"Component field coverage mismatch: missing={missing}, extra={extra}"
        )

    output = Path(__file__).resolve().parents[1] / "docs" / "api" / "components"
    for component, responsibility in COMPONENTS.items():
        (output / f"{component}.md").write_text(
            render(component, responsibility), encoding="utf-8", newline="\n"
        )


if __name__ == "__main__":
    main()
