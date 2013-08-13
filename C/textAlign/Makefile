LDFLAGS=-L /scail/u/vigneshr/utilities/C_libraries/boost_1_46_1/stage/lib/ -lboost_regex
IFLAGS=-I /scail/u/vigneshr/utilities/C_libraries/boost_1_46_1/

SOURCES=temp.cpp
OBJECTS=temp.o
EXECFILES=temp

all: $(SOURCES) $(EXECFILES)

$(EXECFILES): $(OBJECTS)
		g++ -g $(LDFLAGS) $(IFLAGS) $(OBJECTS) -o $@

%.o: %.cpp
		g++ -c -w $(IFLAGS) $< -o $@

clean:
	rm ./temp.o
	rm ./temp

