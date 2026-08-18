# Spinning Part

## Difficulty

This is an **easy** tutorial.

## Setup

No setup is required. All you need to do is attach this to an existing Part.

## Code

```luau linenums="1"
local speed = 25 --(1)!

function Update(dt: number) --(2)!
    self.Orientation += --(3)!
        Vector3.new(0, 0, speed * dt) --(4)!
end
```

1. This line creates the `speed` variable, and gives it a value of `25`. This will be used later, on line 5.
2. As mentioned in [Globals/Lifetime Functions](../../api/globals.md#lifetime-functions), this fires every frame.
3. This line gets the current rotation of the Instance that the script is attached to.
4. This line creates a new Vector3, with the X and Y set to 0, with the Z axis being set to `speed * dt`. Multiplying the speed by `dt` ensures it rotates smoothly despite lag.