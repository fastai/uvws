#!/usr/bin/env python

import tomllib, re, shutil
from pathlib import Path

path = Path('pyproject.toml')

def get_project_name(path):
    data = tomllib.loads((path/'pyproject.toml').read_text())
    return data.get('project', {}).get('name') or ''

def add_missing_projects(toml_path, project_list):
    "Add projects to sources section if they don't exist"
    if not path.exists(): shutil.copy('pyproject.tmpl', path)
    content = toml_path.read_text()
    data = tomllib.loads(content)
    sources = data['tool']['uv']['sources']

    missing = [o for o in project_list if o and o not in sources]
    for proj in missing: sources[proj] = {"workspace": True}

    sources_str = '\n'.join([f'{k} = {{workspace = true}}' for k in sources])
    new_content = re.sub(r'\[tool\.uv\.sources\].*?(?=\n\[|\Z)', f'[tool.uv.sources]\n{sources_str}\n', content, flags=re.DOTALL)
    toml_path.write_text(new_content)
    return missing

projects = [get_project_name(d) for d in Path().iterdir() if (d/'pyproject.toml').exists()]
np = add_missing_projects(path, projects)
if np: print(f"uv add {' '.join(np)}")
else: print("No new packages")

