##
## EPITECH PROJET, 2022
## Multigrains
## File description:
## Makefile
##

PROJECT	=	Multigrains

NAME = 307multigrains

SRC_DIR	=	src/
WIN_SRC_DIR	=	src\\

TEST_SRC	=	./tests/


#############################################################

PRINT	=	printf "$(PROJECT):\t" ; printf

RESET	=	\033[0m
RED		=	\033[0;31m
GREEN	=	\033[0;32m
YELLOW	=	\033[0;33m
BLUE	=	\033[0;34m
MAGENTA	=	\033[0;35m
CYAN	=	\033[1;36m

#############################################################

all:	$(NAME)

$(NAME):
ifeq ($(OS),Windows_NT)
	@echo $(PROJECT):	 Building $(NAME)
	@pip install pyinstaller
	@copy $(WIN_SRC_DIR)main.py . && \
	pyinstaller --onefile main.py && \
	move .\dist\main.exe $(NAME).exe && \
	del main.py && \
	(@echo Done; exit 0) || \
	(@echo Fail; exit 1)
else
	@ $(PRINT) "$(BLUE)Building $(NAME)$(RESET)\n"
	@ cp $(SRC_DIR)main.py ./ && \
	mv main.py $(NAME) && \
	chmod +x $(NAME) && \
	(printf "$(GREEN)Done$(RESET)\n" ; exit 0) || \
	(printf "$(RED)Fail$(RESET)\n" ; exit 1)
endif

clean:
ifeq ($(OS),Windows_NT)
	@echo $(PROJECT):	 Deleting pycache
	@-del *.spec
	@-del .coverage
	@-rmdir /s /q build dist .pytest_cache
	@echo Done
else
	@ $(PRINT) "$(YELLOW)Deleting pycache$(RESET)\n"
	@-rm -r $(SRC_DIR)__pycache__
	@-rm .coverage
	@-rm -r .pytest_cache
	@ $(PRINT) "$(GREEN)Done$(RESET)\n"
endif

fclean: clean
ifeq ($(OS),Windows_NT)
	@echo $(PROJECT):	 Deleting $(NAME)
	@-del $(NAME).exe
else
	@ $(PRINT) "$(YELLOW)%-40b$(RESET)\n" "Deleting $(NAME)"
	@-rm $(NAME)
	@ $(PRINT) "$(GREEN)Done$(RESET)\n"
endif

re: fclean all

tests_run:
	@pip install pytest coverage pytest-cov
	@pytest -v -vv --cov=./src/ $(TEST_SRC)

.PHONY: all $(NAME) clean fclean re tests_run