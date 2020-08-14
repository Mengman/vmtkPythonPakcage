import os
from skbuild import setup, constants, utils
import shlex


def manifest_hook(manifest_list):
    new_manifest_list = []
    for item in manifest_list:
        file_path = utils.to_platform_path(item)
        if not file_path.startswith(constants.CMAKE_INSTALL_DIR()):
            continue
        
        # exculde "header files"
        if "/include/" in file_path:
            continue
        
        if "site-packages" in file_path:
            continue

        if "lib/cmake" in file_path:
            continue

        new_manifest_list.append(item)

    return new_manifest_list


setup(
    name='vmtk-infervision',
    version='1.4.0',
    author='vmtk author',
    packages=["vmtk"],
    package_dir={"vmtk": "vmtk"},
    cmake_args=shlex.split(os.environ.get('VMTK_CMAKE_ARGS', '')),
    description="vmtk",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: C++",
    ],
    cmake_process_manifest_hook=manifest_hook
)
