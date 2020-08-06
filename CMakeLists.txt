cmake_minimum_required(VERSION 3.12)

project(vmtkPythonPakcage)
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake ${CMAKE_MODULE_PATH})

include(ExternalProject)

set(install_dir "${CMAKE_INSTALL_PREFIX}/vmtk")
set(bin_dir "${CMAKE_INSTALL_PREFIX}/bin")

ExternalProject_add(VMTK
    GIT_REPOSITORY "https://github.com/Mengman/vmtk.git"
    GIT_TAG "origin/v1.4.1"
    SOURCE_DIR "${CMAKE_BINARY_DIR}/VMTK"
    BINARY_DIR "${CMAKE_BINARY_DIR}/VMTK-build"
    USES_TERMINAL_DOWNLOAD 1
    USES_TERMINAL_UPDATE 1
    USES_TERMINAL_CONFIGURE 1
    USES_TERMINAL_BUILD 1
    INSTALL_COMMAND ""
    CMAKE_ARGS
        -DCMAKE_INSTALL_PREFIX:PATH=${CMAKE_INSTALL_PREFIX}
        -DCMAKE_INSTALL_RPATH=${install_dir}
        -DVMTK_INSTALL_LIB_DIR=${install_dir}
        -DVMTK_INSTALL_BIN_DIR=${install_bin}
        -DVMTK_MODULE_INSTALL_LIB_DIR=${install_dir}
        -DVTK_VMTK_INSTALL_LIB_DIR=${install_dir}
        -DVTK_VMTK_MODULE_INSTALL_LIB_DIR=${install_dir}
        -DVTK_VMTK_INSTALL_BIN_DIR=${install_bin}
        -DVMTK_SCRIPTS_INSTALL_LIB_DIR=${install_dir}
        -DVMTK_SCRIPTS_INSTALL_BIN_DIR=${install_bin}
        -DPYPES_MODULE_INSTALL_LIB_DIR=${install_dir}
        -DPYPES_INSTALL_BIN_DIR=${install_bin}
)


ExternalProject_add(${PROJECT_NAME}
    SOURCE_DIR ${CMAKE_SOURCE_DIR}
    BINARY_DIR ${CMAKE_BINARY_DIR}/${PROJECT_NAME}-build
    DOWNLOAD_COMMAND ""
    UPDATE_COMMAND ""
    USES_TERMINAL_CONFIGURE 1
    INSTALL_COMMAND ""
    DEPENDS VMTK
)

install(SCRIPT ${CMAKE_BINARY_DIR}/${PROJECT_NAME}-build/cmake_install.cmake)
