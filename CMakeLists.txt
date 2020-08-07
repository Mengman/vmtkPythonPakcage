cmake_minimum_required(VERSION 3.12)

project(vmtkPythonPakcage)
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake ${CMAKE_MODULE_PATH})

if(NOT DEFINED vmtkPythonPackage_SUPERBUILD)
  set(vmtkPythonPackage_SUPERBUILD 1)
endif()


if (vmtkPythonPackage_SUPERBUILD)
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
            -DUSE_SYSTEM_ITK=ON
            -DUSE_SYSTEM_VTK=ON
            -DVMTK_USE_SUPERBUILD=OFF
            -DCMAKE_INSTALL_PREFIX:PATH=${CMAKE_INSTALL_PREFIX}
            -DCMAKE_PREFIX_PATH=/root/libs
    )


    ExternalProject_add(${PROJECT_NAME}
        SOURCE_DIR ${CMAKE_SOURCE_DIR}
        BINARY_DIR ${CMAKE_BINARY_DIR}/${PROJECT_NAME}-build
        CMAKE_CACHE_ARGS:
            -DCMAKE_INSTALL_PREFIX:PATH=${CMAKE_INSTALL_PREFIX}
            -DvmtkPythonPackage_SUPERBUILD:BOOL=0
        DOWNLOAD_COMMAND ""
        UPDATE_COMMAND ""
        USES_TERMINAL_CONFIGURE 1
        INSTALL_COMMAND ""
        DEPENDS VMTK
    )

    install(SCRIPT ${CMAKE_BINARY_DIR}/${PROJECT_NAME}-build/cmake_install.cmake)

endif()