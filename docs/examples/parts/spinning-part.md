# Spinning Part

## Setup

No setup is required. All you need to do is attach this to an existing Part.

## Code

```lua linenums="1"
local speed = 5 --(1)!

function Update(dt: number) --(2)!
    self.Rotation = --(3)!
        self.Rotation +
        Vector3.new(0, 0, speed * dt) --(4)!
end
```

1. This line creates the `speed` variable, and gives it a value of `5`. This will be used later, on line 6.
2. As mentioned in [Globals/Lifetime Functions](../../api/globals.md#lifetime-functions), this fires every frame.
3. This line gets the current rotation of the Instance that the script is attached to.
4. This line creates a new Vector3, with the X and Y set to 0, with the Z axis being set to `speed * dt`. Multiplying the speed by `dt` ensures it rotates smoothly despite lag.