cmake_minimum_required(VERSION 3.16)

project(vmtkPythonPakcage)
set(CMAKE_MODULE_PATH ${CMAKE_CURRENT_SOURCE_DIR}/cmake ${CMAKE_MODULE_PATH})

if(NOT DEFINED vmtkPythonPackage_SUPERBUILD)
  set(vmtkPythonPackage_SUPERBUILD 1)
endif()


if (vmtkPythonPackage_SUPERBUILD)
    # Skip git submodules update
    cmake_policy(SET CMP0097 NEW)
    option(VMTK_BUILD_TESTING "Build the VMTK testing libraries" OFF)
    
    if (VMTK_BUILD_TESTING)
        set(VMTK_GIT_SUBMODULES "tests/vmtk-test-data")
    else()
        set(VMTK_GIT_SUBMODULES "")
    endif()

    include(ExternalProject)
    set(install_dir "${CMAKE_INSTALL_PREFIX}/vmtk")
    set(bin_dir "${CMAKE_INSTALL_PREFIX}/bin")
    
    ExternalProject_add(VMTK
        GIT_REPOSITORY "https://github.com/Mengman/vmtk.git"
        GIT_TAG "origin/v1.4.0-vtk-v8.1.2"
        GIT_SUBMODULES ${VMTK_GIT_SUBMODULES}
        SOURCE_DIR "${CMAKE_BINARY_DIR}/VMTK"
        BINARY_DIR "${CMAKE_BINARY_DIR}/VMTK-build"
        USES_TERMINAL_DOWNLOAD 1
        USES_TERMINAL_UPDATE 1
        USES_TERMINAL_CONFIGURE 1
        USES_TERMINAL_BUILD 1
        INSTALL_COMMAND ""
        CMAKE_CACHE_ARGS
            -DVMTK_BUILD_TESTING:BOOL=OFF
    )


    ExternalProject_add(${PROJECT_NAME}
        SOURCE_DIR ${CMAKE_SOURCE_DIR}
        BINARY_DIR ${CMAKE_BINARY_DIR}/${PROJECT_NAME}-build
        CMAKE_CACHE_ARGS
            -DCMAKE_INSTALL_PREFIX:PATH=${CMAKE_INSTALL_PREFIX}
            -DvmtkPythonPackage_SUPERBUILD:BOOL=0
            -DVMTK_BINARY_DIR:PATH=${CMAKE_BINARY_DIR}/VMTK-build
        DOWNLOAD_COMMAND ""
        UPDATE_COMMAND ""
        USES_TERMINAL_CONFIGURE 1
        INSTALL_COMMAND ""
        DEPENDS VMTK
    )

    install(SCRIPT ${CMAKE_BINARY_DIR}/${PROJECT_NAME}-build/cmake_install.cmake)
else()

    install(SCRIPT ${VMTK_BINARY_DIR}/ITK-Build/cmake_install.cmake)
    install(SCRIPT ${VMTK_BINARY_DIR}/VTK-Build/cmake_install.cmake)
    install(SCRIPT ${VMTK_BINARY_DIR}/VMTK-Build/cmake_install.cmake)
endif()