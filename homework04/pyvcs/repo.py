import os
import pathlib
import typing as tp


def repo_find(workdir: tp.Union[str, pathlib.Path] = ".") -> pathlib.Path:
    gitdir = os.environ.get("GIT_DIR", default=".pyvcs")
    dir = pathlib.Path(workdir)
    while str(dir.absolute()) != "/":
        if (dir / gitdir).exists():
            return dir / gitdir
        dir = dir.parent
    if (dir / gitdir).exists():
        return dir / gitdir
    raise Exception("Not a git repository")

def repo_create(workdir: tp.Union[str, pathlib.Path]) -> pathlib.Path:
    gitdir = os.environ.get("GIT_DIR", default=".pyvcs")
    dir = pathlib.Path(workdir)
    if not dir.is_dir():
        raise Exception(f"{workdir} is not a directory")
    os.makedirs(dir / gitdir / "refs" / "heads")
    os.makedirs(dir / gitdir / "refs" / "tags")
    os.makedirs(dir / gitdir / "objects")
    with (dir / gitdir / "HEAD").open("w") as f:
        f.write("ref: refs/heads/master\n")
    with (dir / gitdir / "config").open("w") as f:
        f.write(
            "[core]\n\trepositoryformatversion = 0\n\tfilemode = true\n\tbare = false\n\tlogallrefupdates = false\n"
        )
    with (dir / gitdir / "description").open("w") as f:
        f.write("Unnamed pyvcs repository.\n")
    return dir / gitdir
