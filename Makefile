TARGET = game.out

CXX = clang++

BIN_DIR = bin
SRC_DIR = src
OBJ_DIR = obj

SOURCES := $(wildcard $(SRC_DIR)/*.cpp)
OBJECTS := $(SOURCES:$(SRC_DIR)/%.cpp=$(OBJ_DIR)/%.o)

SDL_INCLUDE = -I/usr/local/include
SDL_LIB = -L/usr/local/lib -lSDL2 -lSDL2_image -Wl,-rpath=/usr/local/lib

CXX_FLAGS = -c -Wall -Wextra -Werror -std=c++11 $(SDL_INCLUDE)
LD_FLAGS = $(SDL_LIB)


all: $(OBJECTS) $(BIN_DIR)/$(TARGET)
		
$(BIN_DIR)/$(TARGET): $(OBJECTS)
	@$(CXX) $^ $(LD_FLAGS) -o $@
	@echo "done linking"

$(OBJECTS): $(OBJ_DIR)/%.o : $(SRC_DIR)/%.cpp
	@$(CXX) $< $(CXX_FLAGS) -o $@
	@echo "compiled "$<

.PHONEY: clean
clean:
	@rm -f $(OBJECTS)
	@echo "done cleaning up"

.PHONEY: remove
remove: clean
	@rm -f $(BIN_DIR)/$(TARGET)
	@echo "removed executable"
