# miminum version of cmake required
cmake_minimum_required (VERSION 2.6)

# project name
project(TextAlignment)

# set the version
set(TextAlignment_VERSION_MAJOR 1)
set(TextAlignment_VERSION_MINOR 0)

# set the directory for the boost library
set(Boost_INCLUDE_DIR /scail/u/vigneshr/utilities/C_libraries/boost_1_46_1/)

# add executable files and library files
add_executable(align main.cpp)
add_library(TextAlign textAlign.cpp)

# add include directories, even for boost
include_directories(${Boost_INCLUDE_DIR})
include_directories("${PROJECT_SOURCE_DIR}/include")

# link to the text alignment library
target_link_libraries(align TextAlign)

# set the target directories
set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)
set(ARCHIVE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
