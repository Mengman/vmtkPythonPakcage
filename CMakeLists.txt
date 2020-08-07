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
            -DBUILDNAME:STRING=${BUILDNAME}
            -DSITE:STRING=${SITE}
            -DMAKECOMMAND:STRING=${MAKECOMMAND}
            -DCMAKE_BUILD_TYPE:STRING=${CMAKE_BUILD_TYPE}
            -DCMAKE_CXX_COMPILER:STRING=${CMAKE_CXX_COMPILER}
            -DBUILD_EXAMPLES:BOOL=${BUILD_EXAMPLES}
            -DBUILD_SHARED_LIBS:BOOL=${BUILD_SHARED_LIBS}
            -DBUILD_DOCUMENTATION:BOOL=${BUILD_DOCUMENTATION}
            -DBUILD_TESTING:BOOL=${BUILD_TESTING}
            -DCMAKE_EXE_LINKER_FLAGS:STRING=${CMAKE_EXE_LINKER_FLAGS}
            -DCMAKE_SHARED_LINKER_FLAGS:STRING=${CMAKE_SHARED_LINKER_FLAGS}
            -DCMAKE_CXX_FLAGS:STRING=${CMAKE_CXX_FLAGS}
            -DCMAKE_OSX_ARCHITECTURES:STRING=${CMAKE_OSX_ARCHITECTURES}
            -DCMAKE_INSTALL_PREFIX:PATH=${CMAKE_INSTALL_PREFIX}
            -DCMAKE_C_FLAGS:STRING=${CMAKE_C_FLAGS}
            -DVMTK_USE_SUPERBUILD:BOOL=OFF
            -DVTK_VMTK_WRAP_PYTHON:BOOL=${VTK_VMTK_WRAP_PYTHON}
            -DVTK_VMTK_CONTRIB:BOOL=ON
            -DVMTK_CONTRIB_SCRIPTS:BOOL=ON
            -DVTK_ENABLE_VTKPYTHON:BOOL=ON
            -DVMTK_SCRIPTS_ENABLED:BOOL=ON
            -DVMTK_ENABLE_DISTRIBUTION:BOOL=OFF
            -DVMTK_MINIMAL_INSTALL:BOOL=OFF
            -DVMTK_BUILD_TETGEN:BOOL=ON
            -DVMTK_WITH_LIBRARY_VERSION:BOOL=OFF
            -DVMTK_BUILD_STREAMTRACER:BOOL=ON
            -DVTK_VMTK_USE_COCOA:BOOL=ON
            -DVMTK_USE_RENDERING:STRING=ON
            -DVTK_REQUIRED_OBJCXX_FLAGS:STRING=OFF
            -DPYTHON_INCLUDE_DIR=${PYTHON_INCLUDE_DIR}
            -DPYTHON_EXECUTABLE=${PYTHON_EXECUTABLE}
            -DCMAKE_BUILD_WITH_INSTALL_RPATH=OFF
            -DPYTHON_LIBRARY=${PYTHON_LIBRARY}
            -DCMAKE_INSTALL_RPATH=${CMAKE_INSTALL_PREFIX};@rpath
            
            -DVMTK_SCRIPTS_INSTALL_LIB_DIR=${install_dir}
            -DVMTK_SCRIPTS_INSTALL_BIN_DIR=${bin_dir}
            
            -DPYPES_MODULE_INSTALL_LIB_DIR=${install_dir}
            -DPYPES_INSTALL_BIN_DIR=${bin_dir}

            -DVTK_VMTK_INSTALL_LIB_DIR=${install_dir}
            -DVTK_VMTK_MODULE_INSTALL_LIB_DIR=${install_dir}
            -DVTK_VMTK_INSTALL_INCLUDE_DIR=${CMAKE_INSTALL_PREFIX}/include/vmtk
            -DVTK_VMTK_INSTALL_BIN_DIR=${bin_dir}

            -DVMTK_CONTRIB_SCRIPTS_INSTALL_BIN_DIR=${bin_dir}
            -DVMTK_CONTRIB_SCRIPTS_INSTALL_LIB_DIR=${install_dir}

            -DCMAKE_MACOSX_RPATH=ON
            -DCMAKE_INSTALL_RPATH_USE_LINK_PATH=TRUE
            -DCMAKE_PREFIX_PATH=/root/libs
        INSTALL_DIR "${SUPERBUILD_INSTALL_PREFIX}/vmtk"
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
    set(components "PythonRuntimeLibraries;RuntimeExecutables")

    message(STATUS "Adding install rules for components:")

    foreach(component IN LISTS components)
        message(STATUS "  ${component}")

        install(CODE "
        unset(CMAKE_INSTALL_COMPONENT)
        set(COMPONENT \"${component}\")
        set(CMAKE_INSTALL_DO_STRIP 1)
        include(\"${VMTK_BINARY_DIR}/cmake_install.cmake\")
        unset(CMAKE_INSTALL_COMPONENT)
        ")
    endforeach()

    install(CODE "include(\"${VMTK_BINARY_DIR}/cmake_install.cmake\")")
endif()