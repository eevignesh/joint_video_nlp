# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 2.6

#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canoncical targets will work.
.SUFFIXES:

# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list

# Suppress display of executed commands.
$(VERBOSE).SILENT:

# A target that is always out of date.
cmake_force:
.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# The program to use to edit the cache.
CMAKE_EDIT_COMMAND = /usr/bin/ccmake

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /scail/u/vigneshr/CVPR2014/codes/C/textAlign

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /scail/u/vigneshr/CVPR2014/codes/C/textAlign/build

# Include any dependencies generated for this target.
include CMakeFiles/align.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/align.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/align.dir/flags.make

CMakeFiles/align.dir/main.cpp.o: CMakeFiles/align.dir/flags.make
CMakeFiles/align.dir/main.cpp.o: ../main.cpp
	$(CMAKE_COMMAND) -E cmake_progress_report /scail/u/vigneshr/CVPR2014/codes/C/textAlign/build/CMakeFiles $(CMAKE_PROGRESS_1)
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Building CXX object CMakeFiles/align.dir/main.cpp.o"
	/usr/lib64/ccache/c++   $(CXX_DEFINES) $(CXX_FLAGS) -o CMakeFiles/align.dir/main.cpp.o -c /scail/u/vigneshr/CVPR2014/codes/C/textAlign/main.cpp

CMakeFiles/align.dir/main.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/align.dir/main.cpp.i"
	/usr/lib64/ccache/c++  $(CXX_DEFINES) $(CXX_FLAGS) -E /scail/u/vigneshr/CVPR2014/codes/C/textAlign/main.cpp > CMakeFiles/align.dir/main.cpp.i

CMakeFiles/align.dir/main.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/align.dir/main.cpp.s"
	/usr/lib64/ccache/c++  $(CXX_DEFINES) $(CXX_FLAGS) -S /scail/u/vigneshr/CVPR2014/codes/C/textAlign/main.cpp -o CMakeFiles/align.dir/main.cpp.s

CMakeFiles/align.dir/main.cpp.o.requires:
.PHONY : CMakeFiles/align.dir/main.cpp.o.requires

CMakeFiles/align.dir/main.cpp.o.provides: CMakeFiles/align.dir/main.cpp.o.requires
	$(MAKE) -f CMakeFiles/align.dir/build.make CMakeFiles/align.dir/main.cpp.o.provides.build
.PHONY : CMakeFiles/align.dir/main.cpp.o.provides

CMakeFiles/align.dir/main.cpp.o.provides.build: CMakeFiles/align.dir/main.cpp.o
.PHONY : CMakeFiles/align.dir/main.cpp.o.provides.build

# Object files for target align
align_OBJECTS = \
"CMakeFiles/align.dir/main.cpp.o"

# External object files for target align
align_EXTERNAL_OBJECTS =

bin/align: CMakeFiles/align.dir/main.cpp.o
bin/align: lib/libTextAlign.a
bin/align: CMakeFiles/align.dir/build.make
bin/align: CMakeFiles/align.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --red --bold "Linking CXX executable bin/align"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/align.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/align.dir/build: bin/align
.PHONY : CMakeFiles/align.dir/build

CMakeFiles/align.dir/requires: CMakeFiles/align.dir/main.cpp.o.requires
.PHONY : CMakeFiles/align.dir/requires

CMakeFiles/align.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/align.dir/cmake_clean.cmake
.PHONY : CMakeFiles/align.dir/clean

CMakeFiles/align.dir/depend:
	cd /scail/u/vigneshr/CVPR2014/codes/C/textAlign/build && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /scail/u/vigneshr/CVPR2014/codes/C/textAlign /scail/u/vigneshr/CVPR2014/codes/C/textAlign /scail/u/vigneshr/CVPR2014/codes/C/textAlign/build /scail/u/vigneshr/CVPR2014/codes/C/textAlign/build /scail/u/vigneshr/CVPR2014/codes/C/textAlign/build/CMakeFiles/align.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/align.dir/depend

