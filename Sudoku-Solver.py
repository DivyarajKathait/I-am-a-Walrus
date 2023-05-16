from tabnanny import check
from typing import Tuple, List
# No other imports allowed

# PART OF THE DRIVER CODE

def input_sudoku() -> List[List[int]]:
	"""Function to take input a sudoku from stdin and return
	it as a list of lists.
	Each row of sudoku is one line.
	"""
	sudoku= list()
	for _ in range(9):
		row = list(map(int, input().rstrip(" ").split(" ")))
		sudoku.append(row)
	return sudoku

def print_sudoku(sudoku:List[List[int]]) -> None:
	"""Helper function to print sudoku to stdout
	Each row of sudoku in one line.
	"""
	for i in range(9):
		for j in range(9):
			print(sudoku[i][j], end = " ")
		print()

# You have to implement the functions below

def get_block_num(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes a parameter position and returns
	the block number of the block which contains the position.
	"""
	x=pos[0]
	y=pos[1]
	return(((x-1)//3)*3+((y-1)//3)+1)
	# your code goes here

def get_position_inside_block(sudoku:List[List[int]], pos:Tuple[int, int]) -> int:
	"""This function takes parameter position
	and returns the index of the position inside the corresponding block.
	"""
	p1=(pos[0]-1)%3
	p2=(pos[1]-1)%3
	return(p1*3+p2+1)
	# your code goes here


def get_block(sudoku:List[List[int]], x: int) -> List[int]:
	"""This function takes an integer argument x and then
	returns the x^th block of the Sudoku. Note that block indexing is
	from 1 to 9 and not 0-8.
	"""
	t=(x-1)//3
	p=(x-1)%3
	lst=[]
	for a in range(3*t,3*t+3):
		for b in range(3*p,3*p+3):
			lst.append(sudoku[a][b])
	# your code goes here
	return lst
	

def get_row(sudoku:List[List[int]], i: int)-> List[int]:
	"""This function takes an integer argument i and then returns
	the ith row. Row indexing have been shown above.
	"""
	# your code goes here
	return sudoku[i-1]

def get_column(sudoku:List[List[int]], x: int)-> List[int]:
	"""This function takes an integer argument i and then
	returns the ith column. Column indexing have been shown above.
	"""
	ls=[]
	for i in range(9):
		ls.append(sudoku[i][x-1])

	# your code goes here
	return ls

def find_first_unassigned_position(sudoku : List[List[int]]) -> Tuple[int, int]:
	"""This function returns the first empty position in the Sudoku. 
	If there are more than 1 position which is empty then position with lesser
	row number should be returned. If two empty positions have same row number then the position
	with less column number is to be returned. If the sudoku is completely filled then return `(-1, -1)`.
	"""
	for x in range(9):
		for y in range(9):
			if sudoku[x][y]==0:
				return((x+1,y+1))
	return((-1,-1))
		    
	# your code goes here

def valid_list(lst: List[int])-> bool:
	"""This function takes a lists as an input and returns true if the given list is valid. 
	The list will be a single block , single row or single column only. 
	A valid list is defined as a list in which all non empty elements doesn't have a repeating element.
	"""
	# your code goes here
	for x in range (len(lst)):
		if(lst[x]!=0):
			if(lst.count(lst[x])==1):
				continue
			else:
				return False
	return True

def valid_sudoku(sudoku:List[List[int]])-> bool:
	"""This function returns True if the whole Sudoku is valid.
	"""
	
	for x in range(9):
		a=get_block(sudoku,x+1)
		b=get_column(sudoku,x+1)
		c=get_row(sudoku,x+1)
		if (valid_list(a) and valid_list(b) and valid_list(c)):
			continue
		else:
			return False
	
	return True
	# your code goes here


def get_candidates(sudoku:List[List[int]], pos:Tuple[int, int]) -> List[int]:
	"""This function takes position as argument and returns a list of all the possible values that 
	can be assigned at that position so that the sudoku remains valid at that instant.
	"""
	lst=[]
	if(pos==(-1,-1)):
		return
	for x in range(1,10):
		sudoku[pos[0]-1][pos[1]-1]=x
		if(valid_sudoku(sudoku)):
			lst.append(x)
		undo_move(sudoku,pos)
	return lst

	
def make_move(sudoku:List[List[int]], pos:Tuple[int, int], num:int) -> List[List[int]]:
	"""This function fill `num` at position `pos` in the sudoku and then returns
	the modified sudoku.
	"""
	sudoku[pos[0]-1][pos[1]-1]= num
	# your code goes here
	return sudoku

def undo_move(sudoku:List[List[int]], pos:Tuple[int, int]):
	"""This function fills `0` at position `pos` in the sudoku and then returns
	the modified sudoku. In other words, it undoes any move that you 
	did on position `pos` in the sudoku.
	"""
	sudoku[pos[0]-1][pos[1]-1]= 0
	# your code goes here
	return sudoku

def sudoku_solver(sudoku: List[List[int]]) -> Tuple[bool, List[List[int]]]:
	""" This is the main Sudoku solver. This function solves the given incomplete Sudoku and returns 
	true as well as the solved sudoku if the Sudoku can be solved i.e. after filling all the empty positions the Sudoku remains valid.
	It return them in a tuple i.e. `(True, solved_sudoku)`.

	However, if the sudoku cannot be solved, it returns False and the same sudoku that given to solve i.e. `(False, original_sudoku)`
	"""
	# your code goes here
	a=find_first_unassigned_position(sudoku)
	
	ls=get_candidates(sudoku,a)
	while(a!=(-1,-1)):
		for x in ls:
			make_move(sudoku,a,x)
			possible,sudoku =sudoku_solver(sudoku)
			if possible:
				return (True,sudoku)
			undo_move(sudoku,a)
		else:
			return (False,sudoku)
	if(a==(-1,-1)):
		if(valid_sudoku(sudoku)):
			return (True,sudoku)
		return (False,sudoku)

			


	






	# to complete this function, you may define any number of helper functions.
	# However, we would be only calling this function to check correctness.
# PLEASE NOTE:
# We would be importing your functions and checking the return values in the autograder.
# However, note that you must not print anything in the functions that you define above before you 
# submit your code since it may result in undefined behaviour of the autograder.

def in_lab_component(sudoku: List[List[int]]):
	print("Testcases for In Lab evaluation")
	print("Get Block Number:")
	print(get_block_num(sudoku,(4,4)))
	print(get_block_num(sudoku,(7,2)))
	print(get_block_num(sudoku,(2,6)))
	print("Get Block:")
	print(get_block(sudoku,3))
	print(get_block(sudoku,5))
	print(get_block(sudoku,9))
	print("Get Row:")
	print(get_row(sudoku,3))
	print(get_row(sudoku,5))
	print(get_row(sudoku,9))

# Following is the driver code
# you can edit the following code to check your performance.
if __name__ == "__main__":

	# Input the sudoku from stdin
	sudoku = input_sudoku()

	# Try to solve the sudoku
	possible, sudoku = sudoku_solver(sudoku)

	# The following line is for the in-lab component
	#in_lab_component(sudoku)
	# Show the result of the same to your TA to get your code evaulated

	# Check if it could be solved
	if possible:
		print("Found a valid solution for the given sudoku :)")
		print_sudoku(sudoku)

	else:
		print("The given sudoku cannot be solved :(")
		print_sudoku(sudoku)