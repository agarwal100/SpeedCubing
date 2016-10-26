import random
def inverse_move(move):
	move
	return inverse_move
def setup_from_alg(cases):
	premoves = []
	for case in cases:
		premoves.append("")
		for character in range(len(case),0,-1):
			premoves[0]= character+premoves[0]
def print_setup_from_alg(cases):
	cases = setup_from_alg(cases)
	random.shuffle(cases)
	for i in range(1,len(cases)+1):

		print i,"",cases[i-1]



easy_tcll_cases = ["R' F R F' R' F R F'",
 	"y' R' U2 R U' y R U' R'",
	"y' U2 R' U' R U R' U' R",
	"R U R' U F' R U' R' F2",
	"R' U' F R F' U R2 U' R'",
	"U' R U R' U' R2 U R2 U' R2",
	"y' U R' U2 R' F R F' R",
	"U R U R' U' y' R2 U' R2 U R2",
	"R U' R' U R U' R'",
	"R U' R2 F R F'",
	"R U' R' U2 R U2 R'",
	"R' F R F' U R U' R'"]


print_setup_from_alg(easy_tcll_cases)
