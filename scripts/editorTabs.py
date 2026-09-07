from pathlib import Path

TABS = [
    "Animation",
    "Assets",
    "Entity Report",
    "Learn Luduvo",
    "Outliner",
    "Profiler",
    "Properties",
    "Viewport",
    "Welcome",
    "Script Editor",
    "Index"
]


if __name__ == "__main__":
    output = Path(__file__).resolve().parents[1] / "docs" / "editor" / "tabs"
    for tab in TABS:
        (output / f"{tab.lower().replace(' ', '-')}.md").write_text(
f"""---
icon: lucide/app-window
---

# {tab}

!!! note
    This page is under construction! [PRs](../../index.md) are welcome.
""", encoding="utf-8", newline="\n")
