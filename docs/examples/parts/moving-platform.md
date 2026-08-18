# Moving Platform

## Difficulty

This is a **medium** tutorial. It involves the use of Luau's [type solver](https://luau.org/types/), aswell as `table.sort` and lerping. It also involves using [Script Handles](../../api/scripts.md#script-handles).

## Setup

You need to create a [Script Handles](../../api/scripts.md#script-handles) and attach it to the Part.

You will then need to create as many slots as you need in in the Script Handles: `Pos1`, `Pos2`, ..., `PosN`, with `N` being your final number.

## Code

```luau linenums="1"
local SPEED = 5 --(1)!
local REACH_THRESHOLD = 0.05 --(2)!

type platformPosition = { --(3)!
    order: number,
    position: Vector3,
    orientation: Vector3,
}

local positions = {} :: { platformPosition }

for _, value in handles do --(4)!
    local name = value.Name
    local split = string.split(name, "Pos") --(5)!

    local order = tonumber(split[2]) or 1 --(6)!

    table.insert(positions, {
        order = order,
        position = value.Position,
        orientation = value.Orientation,
    })
end

table.sort(positions, function(a: platformPosition, b: platformPosition) --(7)!
    return a.order < b.order
end)

local platformPosition = self.Position --(8)!
local platformOrientation = self.Orientation

local currentIndex = 1 --(9)!

function Update(dt: number)
    local currentPosition = positions[currentIndex]

    local toTarget = currentPosition.position - platformPosition --(10)!
    local distance = toTarget.Magnitude

    local step = SPEED * dt --(11)!

    if distance <= step or distance <= REACH_THRESHOLD then --(12)!
        platformPosition = currentPosition.position
        platformOrientation = currentPosition.orientation

        currentIndex += 1

        if currentIndex > #positions then --(13)!
            currentIndex = 1
        end
    else
        local direction = toTarget / distance -- normalize --(14)!

        platformPosition += direction * step --(15)!

        local alpha = math.clamp(SPEED * dt, 0, 1)

        platformOrientation = platformOrientation:Lerp(currentPosition.orientation, alpha)
    end

    self.Position = platformPosition
    self.Orientation = platformOrientation
end
```

1. This line creates the `SPEED` variable, in studs per second. This controls how fast the platform travels between positions.
2. This is the distance, in studs, at which the platform is considered to have "arrived" at its target.
3. This creates a type for each stop the platform will visit: an `order` number (for sorting), and the `position`/`orientation` it should move to.
4. This loop runs once for every handle found in the Script Handles, using their name (for `order`) and position/orientation.
5. This splits the handle's name around the text `"Pos"`, so a handle named `Pos1` becomes `{ "", "1" }`. We want the second element, which is used as the `order`.
6. The `order`, or `split[2]`, is a string, so `tonumber` converts it to an actual number for sorting later. If it isn't a valid number, it defaults to `1`.
7. `table.sort` reorders `positions` so the platform visits them in ascending `order`, regardless of what order the handles were found in.
8. These two lines cache the platform's starting position and orientation. This is the running "current" position that gets moved on each `Update`.
9. This tracks which entry in `positions` the platform is currently moving toward.
10. `toTarget` is the vector from where the platform currently is to where it needs to go. `.Magnitude` gives the remaining distance.
11. `step` is how far the platform should move this frame, based on `SPEED` and `dt`. Multiplying the speed by `dt` ensures it moves smoothly despite lag.
12. If the remaining distance is smaller than this frame's step (or under the threshold), moving the full `step` would overshoot the target.
13. If the platform just reached the last position in the list, this wraps `currentIndex` back to `1`, so the platform loops back to the start.
14. Dividing `toTarget` by its own `distance` produces a unit vector. This is needed so `step` controls the distance moved.
15. The platform moves `step` studs along `direction` this frame, producing linear motion instead of an eased curve.