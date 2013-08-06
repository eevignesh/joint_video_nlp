CC=g++ -g
CFLAGS=-c -Wall
BOOST_DIR=/scail/u/vigneshr/utilities/C_libraries/boost_1_46_1/
IFLAGS=-I $(BOOST_DIR)
#LDFLAGS=-L ./3rd_party/lib -L ./3rd_party/lib/vl_objs/ -L ./3rd_party/lib/opencv -lopencv_core -lopencv_highgui -lopencv_imgproc -lopencv_flann -lavcodec -lavformat -lswscale -lboost_filesystem-mt -lboost_system-mt -lavutil -lpthread -lvl


SOURCES=main2.cpp
EXECFILES=align2

OBJDIR=objs
BINDIR=bin

#LINEAROBJ=blas/blas.a
#blas/daxpy.c blas/dnrm2.c blas/ddot.c blas/dscal.c

OBJECTS=$(SOURCES:.cpp=.o) #$(LINEAROBJ)
	OBJECTS_FULLPATH := $(addprefix $(OBJDIR)/, $(OBJECTS))
	EXECUTABLE := $(addprefix $(BINDIR)/, $(EXECFILES))


all: $(SOURCES) $(EXECUTABLE)

$(EXECUTABLE): $(OBJECTS_FULLPATH)
	    $(CC) $(LDFLAGS) $(IFLAGS) $(OBJECTS_FULLPATH) -o $@

$(OBJDIR)/%.o : %.cpp
	  $(CC) $(CFLAGS) $(IFLAGS) $< -o $@

clean:
	  rm $(OBJDIR)/*.o
		  rm $(BINDIR)/$(EXECFILES)
