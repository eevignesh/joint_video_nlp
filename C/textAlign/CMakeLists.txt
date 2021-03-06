# miminum version of cmake required
cmake_minimum_required (VERSION 2.6)

# project name
project(TextAlignment)

# set the version
set(TextAlignment_VERSION_MAJOR 1)
set(TextAlignment_VERSION_MINOR 0)

set(CMAKE_LIBRARY_PATH ${CMAKE_LIBRARY_PATH}
  "/scail/u/vigneshr/utilities/C_libraries/boost_1_46_1/stage/lib/")
set(CMAKE_INCLUDE_PATH ${CMAKE_INCLUDE_PATH}
  "/scail/u/vigneshr/utilities/C_libraries/boost_1_46_1/")


# set the directory for the boost library
find_package(Boost 1.46.1 COMPONENTS regex)

IF (Boost_FOUND) 
   ADD_DEFINITIONS( "-DHAS_BOOST" )
ELSE()
    message(STATUS "Boost couldn't be found, adding it manually")
    set(Boost_INCLUDE_DIR /scail/u/vigneshr/utilities/C_libraries/boost_1_46_1/)
ENDIF()

# add executable files and library files
add_executable(align align.cpp)
add_library(TvParser tvParser.cpp)

# add include directories, even for boost
include_directories(${Boost_INCLUDE_DIR})
include_directories("${PROJECT_SOURCE_DIR}/include")

# link to the text alignment library
target_link_libraries(align TvParser ${Boost_REGEX_LIBRARY})

# set the target directories
set(LIBRARY_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)
set(ARCHIVE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/lib)
set(EXECUTABLE_OUTPUT_PATH ${PROJECT_BINARY_DIR}/bin)
