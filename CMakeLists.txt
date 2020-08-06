cmake_minimum_required(VERSION 3.12)

project(vmtkPythonPakcage)
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake ${CMAKE_MODULE_PATH})

include(ExternalProject)

ExternalProject_add(VMTK
    GIT_REPOSITORY "https://github.com/vmtk/vmtk.git"
    GIT_TAG "v1.4.0"
    SOURCE_DIR "${CMAKE_BINARY_DIR}/VMTK"
    BINARY_DIR "${CMAKE_BINARY_DIR}/VMTK-build"
    USES_TERMINAL_DOWNLOAD 1
    USES_TERMINAL_UPDATE 1
    USES_TERMINAL_CONFIGURE 1
    USES_TERMINAL_BUILD 1
    INSTALL_COMMAND ""
)

install(SCRIPT ${CMAKE_BINARY_DIR}/VMTK-build/cmake_install.cmake)
