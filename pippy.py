import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path


def _remove_unwanted(path: Path) -> None:
    if os.path.exists(f'{path}/build'):
        shutil.rmtree(f'{path}/build')
    contents = os.listdir(path)
    to_delete = [x for x in contents if x.find('.egg-info')+1] #-1 evals True so +1 for False
    for item in to_delete:
        shutil.rmtree(f'{path}/{item}')

        
def main(argv=None) -> int:
    path = Path('.')
    
    parser = argparse.ArgumentParser()
    parser.add_argument('name')
    parser.add_argument('-e', '--editable', action='store_true')
    args = parser.parse_args()
    print(args)
    path = Path('.')
    prev = path

    # since all local packages will exist in some directory above,
    # keep going through parent directory until found
    while args.name not in os.listdir(path):
        path = path.parent.absolute()
        if path == prev: # reached root drive directory
            print(f"Local package {args.name} does not exist.")
            return 1
        prev = path

    pkg_path = f'{path}/{args.name}'
    
    # delete files if they exist from a previous install
    _remove_unwanted(pkg_path)
    
    x = subprocess.run(['pip', 'uninstall', '-y', args.name])
    if args.editable:
        subprocess.run(['pip', 'install', '-e', pkg_path])
    else:
        subprocess.run(['pip', 'install', pkg_path])
    
        
    
    # delete files after install
    _remove_unwanted(pkg_path)
    return 0


if __name__ == '__main__':
    exit(main())
