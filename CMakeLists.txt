cmake_minimum_required(VERSION 3.0.0)
project(test VERSION 0.1.0)

set(TARGET_PREFIX r2d2_)
set(BUILD_ROOT_DIR r2d2_)

set(Boost_USE_STATIC_LIBS OFF) 
set(Boost_USE_MULTITHREADED ON)  
set(Boost_USE_STATIC_RUNTIME OFF) 

# Allow use of relative source paths:
cmake_policy(SET CMP0076 NEW)

# Link to targets in other directories:
cmake_policy(SET CMP0079 NEW)

set (CMAKE_CXX_STANDARD 17)

include_directories(${TRIPLET_INCLUDE_DIRS}) 

function(configure_target_output TARGET_NAME)
    set_target_properties(${TARGET_NAME}
        PROPERTIES
        ARCHIVE_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/arc/"
        LIBRARY_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/lib/"
        RUNTIME_OUTPUT_DIRECTORY "${CMAKE_BINARY_DIR}/bin/"
    )
endfunction()

include_directories("./src/cpp")

# Configure Core:
set(TARGET_CORE "${TARGET_PREFIX}core")
add_library(${TARGET_CORE} SHARED)
add_subdirectory("./src/cpp/core")
configure_target_output(${TARGET_CORE})


# Configure Runtime:
set(TARGET_RUNTIME "${TARGET_PREFIX}runtime")
add_executable(${TARGET_RUNTIME})
target_link_libraries(${TARGET_RUNTIME} ${TARGET_CORE})
add_subdirectory("./src/cpp/runtime")
configure_target_output(${TARGET_RUNTIME})





set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})
