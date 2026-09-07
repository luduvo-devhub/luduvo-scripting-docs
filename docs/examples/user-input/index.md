---
icon: lucide/mouse
---

!!! note
    This page is under construction! [PRs](../index.md) to contribute example code tutorials (or anything else really) are welcome.

# User Input

Currently, Luduvo has two methods of input:

- [`Instance.Activated`](../../api/instances.md#built-in-signals) for accepted UI-control activation on the client.
- [`Instance:GetMoveIntent()`](../../api/instances.md#user-data) for character movement detection (server-side only).

True input handling (mouse, keyboard, gamepad, etc.) is currently not implemented.
