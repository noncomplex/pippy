Personal utility for pip installing local packages where the package exists
in any parent directory.

## Usage
make pippy.py run without entering `python`/`python3` and `.py` extension
```
pippy {package name}
```
editable install
```
pippy -e {package name}
```

## Windows
add `.PY` to `PATHEXT`

add pippy directory to `PATH`
```
assoc .py=Python.File
ftype Python.File=c:\path to \python.exe "%1" %*
```
