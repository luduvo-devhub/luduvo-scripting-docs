import re
from pathlib import Path

TOML_PATH = Path("zensical.toml")

PREFAB_NAMES = {
    "playerspawner": "PlayerSpawner",
    "spawnlocation": "SpawnLocation",
}

TABS = {
    "animation": "Animation",
    "assets": "Assets",
    "entity-report": "Entity Report",
    "learn-luduvo": "Learn Luduvo",
    "outliner": "Outliner",
    "profiler": "Profiler",
    "properties": "Properties",
    "viewport": "Viewport",
    "welcome": "Welcome",
    "script-editor": "Script Editor",
}


SECTIONS = [
    {
        "key": "Components",
        "dir": Path("docs/api/components"),
        "rel": "api/components",
        "marker": "COMPONENTS",
        "display": lambda stem: stem,
    },
    {
        "key": "Prefabs",
        "dir": Path("docs/api/prefabs"),
        "rel": "api/prefabs",
        "marker": "PREFABS",
        "display": lambda stem: PREFAB_NAMES.get(
            stem, stem[0].upper() + stem[1:] if stem else stem
        ),
    },
    {
        "key": "Tabs",
        "dir": Path("docs/editor/tabs"),
        "rel": "editor/tabs",
        "marker": "TABS",
        "display": lambda stem: TABS.get(
            stem, stem[0].upper() + stem[1:] if stem else stem
        ),
    },
]


def build_list(section):
    files = sorted(
        f for f in section["dir"].glob("*.md")
        if f.name.lower() != "index.md"
    )

    lines = [f'{{ "{section["key"]}" = [']
    lines.append(f'    "{section["rel"]}/index.md",')
    lines.append("")
    for f in files:
        name = section["display"](f.stem)
        rel_path = f'{section["rel"]}/{f.name}'
        lines.append(f'    {{ "{name}" = "{rel_path}" }},')
    lines.append("  ] },")
    return "\n".join(lines), len(files)


def main():
    toml_text = TOML_PATH.read_text(encoding="utf-8")

    for section in SECTIONS:
        start_tag = f"# NAVGEN -- {section['marker']}"
        end_tag = f"# NAVGEN -- {section['marker']} END"

        pattern = re.compile(
            re.escape(start_tag) + r".*?" + re.escape(end_tag),
            re.DOTALL,
        )

        if not pattern.search(toml_text):
            print(f"Could not find markers for {section['key']} "
                  f"({start_tag} / {end_tag}). Skipping.")
            continue

        new_entry, count = build_list(section)
        replacement = f"{start_tag}\n{new_entry}\n  {end_tag}"

        toml_text = pattern.sub(replacement, toml_text, count=1)
        print(f'Updated {section["key"]} entry with {count} file(s).')

    TOML_PATH.write_text(toml_text, encoding="utf-8")


if __name__ == "__main__":
    main()
