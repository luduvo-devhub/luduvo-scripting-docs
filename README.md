# Unnofficial Luduvo Script docs

taken from analysing `LuduvoApp.exe` and bruteforcing some stuff

scripts seem to be attached to entities.
within scripts, `self` refers to the entity, the equivalent of doing `script.Parent` in roblox.

Global Functions:
| function | ran |
|---|---|
| `Update(dt)` | every frame |
| `PhysicsUpdate(dt)` | every physics step, probbaly at a fixed frequency idk|

Globals:
| global | notes |
|---|---|
| `print(s)` | prints to the output, u can currently only see it in studio.log |
| `tick()` |  |
| `wait(t)` | yields the current thread, this should exist |
| `task` | scheduler library |
| `typeof(x)` | Returns the luduvo type name of a value |
| `script` | The current script object |
| `world` | kinda like workspace i think |

# Types:
Still doing research on this

- Vector3
- Vector2
- Instance
- Signal
- Twee
