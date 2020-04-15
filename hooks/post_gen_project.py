import json
import shutil
import subprocess


def exec(command, **kwargs):
    subprocess.call(command.split(**kwargs))


exec("poetry install")
with open("./labextensions.json") as f:
    extensions = " ".join(
        [f"{extension}@{version}" for extension, version in json.load(f).items()]
    )
exec(f"./.venv/bin/jupyter labextension install {extensions}")
exec("./.venv/bin/jupyter labextension list")
shutil.move("overrides.json", "./.venv/share/jupyter/lab/settings")
