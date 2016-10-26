import random
import math
def pll_trainer():
    # 2_sided_PLL_trainer
    print "PLL"
    setups = [
    "R' L F2 R L' U F2 D R2 D' F2 R2 U' F2 U R2 U'",
        #Gd    
    "L2 U L2 B2 U B2 U' R2 U L2 U' L R' B2 L R'", 
        #Gd
    "L2 R2 D F2 D2 R2 U B2 U2 R2 D' L R' D2 B2 L' R' U'",
        #U: Y
    "L2 R2 D B2 D2 L2 U F2 U2 L2 D' L' R D2 F2 L' R' U'",
        #U': Y
    "U2 R2 F2 D' B2 D L2 U' L2 U F2 L R' U2 L' R'",
        #Ga
    "U2 R2 F2 D' B2 D L2 U' L2 U F2 L R' U2 L' R' U'",
        #Ga    
    "R L U2 R' L U' F2 L2 U' L2 U L2 F2 D F2 D' ",
        #Gb
    "L2 U' B2 F2 U' R2 U R2 U2 F2 U B' F' R2 B' F L2",
        #U2: V
    "R L U2 R L' F2 U' L2 U L2 D' B2 D F2 R2 U",
        #Gb
    "B2 L2 U' R2 D F2 L2 R2 U2 B2 U' L U L' B2 R D' R' ",
        #E
    "U' R2 D' R2 B2 U' R2 U L2 U' F2 L R' B2 L R' ",
        #Rb
    "L2 D' R2 D2 L2 B2 D' R2 D R2 U' L R' U2 F2 L' R'",
        #U': F
    "L2 D' R2 D2 L2 B2 D' R2 D R2 U' L R' U2 F2 L' R' U'",
        #no AUF: F    
    "L2 U B2 R2 U B2 D' B2 F2 R2 D L R' U2 L' R",
        #Gb
    "B2 R2 F2 D L2 D' F2 R2 U B2 U2 R U R' B2 R U' R' ",
        #E
    "R2 B2 U' F2 U B2 U' F2 U R2 U2",
        #Al
    "U2 R2 U' F2 U B2 U' F2 U B2 R2"
        #Ar    
    ]

    random.shuffle(setups)
    index = 1
    for setup in setups:
        print index,")", setup
        print alg_url(setup)
        print
        index+=1




    #print setups[0]


    #List of hard PLL cases
    
    #A- no auk (side two opp) 
    #A- U2 (front two opp)
    #E- o corners are adj (otherwise G)
    #F - no auk, U' opposite pieces are with bar
    #Ga- U' ((o corners same [1], s edge and corner same [2]) & 1,2 app; 
    #    U2 - 3,4,5,6 checker (A is not) and missing 2 (not R)
    #Gb- no auf (1,6 same and 2,5 not same), 
    #    U' (1,2,4,5,6 checker) 
    #    U2 (3 adj) 
    #    U (4,5 opp and 1,2,3,6 opp) or (1,2,3, opp and 2 adj colors on side)  
    #Gc- U2 (o corners same [1], f edge and corner same [2]) & 1,2 opp; 
    #    U (look at right face)
    #Gd- U' (4 adj) 
    #    U2 (2,3 opp and 3,4,5 opp) 
    #    U (4 adj) 
    #R- U' ((o corners same [1], s edge and corner same [2]) & 1,2 adj;
    #   U2
    #R- U' ((o corners same [1], f edge and corner same [2]) & 1,2 adj; 
    #    no auf (1,2,6 same and 3,5 same) 
    #V- U'  (grab adjacent) 
    #Y- U'  (1,5 same);
    #    U  (2,6 same)  



    #extra Y perms
    
    #"L2 R2 U' L2 D2 F2 D L2 U2 B2 U L R F2 U2 L R'",
        #U': Y
    #"L2 R2 U' R2 D2 B2 D R2 U2 F2 U L R B2 U2 L' R",
        #U: Y
def oll_trainer(if_auf_isRandom=None):
    #if argument is true, uses random AUF, else predetermined
    setups=[]
    if if_auf_isRandom:
        print "Oll with Random AUF"
        setups=[
        "F' L F L' R U2 L' U2 L U2 R'",
        "L' U2 L U2 L F' L' F",
        "R' U2 R B' R B R' U R' U R",
        "R' U' R F U R U' R' F' U' R' U R",
        "F' U' L' U L F U F' U' L' U L F",
        "F R' F' R2 U R2 D' R U R' D R2 U' R'",
        "R U2 R' U' R U R' F R' F' R2 U2 R'",
        "R U R' F' U' R U R' U R U2 R' F R U' R'",
        "F U R U' R' F' R U R' U R U2 R'",
        "B' R B R' U' R' U' R U R' U R",
        "R U R' F' U' F R U' R'",
        "B L' B' L U L U L' U' L U' L'",
        "F R2 D R' U R D' R2 U' F'",
        "R U' R' U R U R' U' F' U F U' R U R'",
        "R' U' F R' F' R F U R U' R' F' R",
        "F R' F' R U2 R U' R' U R U2 R'",
        "R' U2 R U R' U R F R U R' U' F'",
        "F R U R' U' R U' R' U R U R' F'",
        "F' L' U' L U F2 U R U' R' U R U' R' F'",
        "B' R' U R U R' U' R U' R' U R B"]
    else:
        print "OLL without random AUF"
        setups=[
        "F' L F L' R U2 L' U2 L U2 R'",
        "L' U2 L U2 L F' L' F",
        "R' U2 R B' R B R' U R' U R U2",
        "R' U' R F U R U' R' F' U' R' U R U'",
        "F' U' L' U L F U F' U' L' U L F U'",
        "F R' F' R2 U R2 D' R U R' D R2 U' R' U",
        "R U2 R' U' R U R' F R' F' R2 U2 R'",
        "R U R' F' U' R U R' U R U2 R' F R U' R'",
        "F U R U' R' F' R U R' U R U2 R' U2",
        "B' R B R' U' R' U' R U R' U R U'",
        "R U R' F' U' F R U' R' U'",
        "B L' B' L U L U L' U' L U' L'",
        "F R2 D R' U R D' R2 U' F' U'",
        "R U' R' U R U R' U' F' U F U' R U R'",
        "R' U' F R' F' R F U R U' R' F' R U2",
        "F R' F' R U2 R U' R' U R U2 R' U2",
        "R' U2 R U R' U R F R U R' U' F' U2",
        "F R U R' U' R U' R' U R U R' F' U",
        "F' L' U' L U F2 U R U' R' U R U' R' F' U",
        "B' R' U R U R' U' R U' R' U R B U'"]
        
    auf = ["U","U'","U2"] 
    
    random.shuffle(setups)
    
    index = 1
    if if_auf_isRandom: 
        for setup in setups:
            print index,")", setup,random.choice(auf)
            print
            index+=1
    else:
        for setup in setups:
            print index,")", setup
            print alg_url(setup)
            print
            index+=1

def coll_trainer(if_auf_isRandom=None):   
    print "COLL"
    setups=[
    "R' U2 R U R' U' R U R' U R",
    "R U2 R' U L' U2 R U R' U' R U' L R'",
    "F U2 R U' R U2 R' U' R U' R2 U2 F'",
    "R' U' R' F R F' R' F R F' R' F R F' U R",
    "L' U2 L2 U L2 U L2 U2 L'",
    "F' U' L' U L U' L' U L2 F L' U' L' U L",
    "R' U2 R U2 R2 F' R U R U' R' F U R",
    "L' U R U' L U R2 U' R U' R' U2 R",
    "L U L' U L U R' U L' U' R",
    "F R2 U' R U2 R U R' U R' U R2 F'"  ]  
    
    auf = ["U","U'","U2"] 
      
    random.shuffle(setups)
    index = 1
    for setup in setups:
        print index,")", setup,random.choice(auf)
        print alg_url(setup)
        print
        index+=1
def alg_url(alg):
    transformed_alg=""
    for char in alg:
       
        if char== "'":
            transformed_alg= transformed_alg +"-"
        elif (char== " "):
            transformed_alg= transformed_alg +"_"
        elif (char== "2"):
            transformed_alg= transformed_alg +"2"    
        else:    
            transformed_alg= transformed_alg + char
            #transformed_alg= transformed_alg +"_"
    return  "https://alg.cubing.net/?setup=" + transformed_alg 

def f2l_trainer():   
    print "F2L"
    setups=[
    "R' U R2 F R' F' U R'",
    "R U R' F U R' F' R",
    "L' U' L F' U' L F L'",
    "F U' F R' F2 R",
    "F' U F' L F2 L'",
    "R' U R y R U R' U2"]  
    
   
      
    random.shuffle(setups)
    index = 1
    for setup in setups:
        print index,")", setup
       
        print alg_url(setup)+ "&stage=F2L"                           
        print 
        index+=1
# def inverse_move(move):
#   move
#   if move==:

#   return inverse_move
def setup_from_alg(case):
    # print "original case",case
    premoves = ""
    
    for ind in range(len(case)-1,-1,-1):
        # print ind
        if ind==-1:
            print "negative 1"
            breank
        if case[ind] == "'" or case[ind] == "2":
            x=2
        elif case[ind] == " ": 
            premoves= premoves+" "
        
        else:
            
            if ind+1< len(case) and case[ind+1]== "'":
                premoves= premoves+case[ind]
            elif ind+1< len(case) and case[ind+1]== "2":
                premoves= premoves+case[ind]+"2"
                        
            else: 
                premoves= premoves+case[ind]+"'"
        
    return premoves               
def easy_tcll_trainer(needs_inverse=False):   

    print "Easy TCLL"
    algs=[
    "R' F R F' R' F R F'",
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
    setups=[
    "R' F R F' R' F R F'",
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
    if needs_inverse:
        print "INVERSED"
        print "---------"
        i=0
        for alg in algs:
            setups[i] = [setups[i],setup_from_alg(alg)]
            i+=1
        #random.shuffle(setups)
        
        index = 1
        print "setups"
        for setup in setups:
            print index,")", setup[1],"                                            solution:",setup[0]
            # print setup[1]
            print 
            #print alg_url(setup)                         
            print 
            index+=1
        
        
    else:   
        random.shuffle(setups)
        index = 1
        for setup in setups:
            print index,")", setup
            print 
            #print alg_url(setup)                         
            print 
            index+=1
#easy_tcll_trainer(True)
def tcll_trainer(needs_inverse=False,plus_sets="TCLL_plus",minus_sets="TCLL_minus"):   

    print "TCLL"
    tcll_plus={
        "Hammer":[
        "R' F R F' R' F R F'",
        "y' R' U2 R U' y R U' R'",
        "F2 R' F2 R2 U' R' U2 F",
        "U2  L' U' L F' L' U L U2 F'",
        "U R' U R U' R U' R2 F R2 F'",
        "U R U R' F R F' R U R' U R'"
        ],
         
        "Spaceship":[
        "y' U2 R' U' R U R' U' R'",
        "U R' F R F' R' F R U R U' R' F''",
        "U R U' R' U R2 U' R' F R' F''",
        "R U' R' U2 R U' R' U' R' F R F''",
        "U R U2' R' U R' F R F' R U' R''",
        "U2 R' F2 R U' R' F2 R2 U R' F2'"
        ],

        "Stollery":[
        "R U R' U F' R U' R' F2",
        "U2 R' F R U' F' R U2 R' F2", 
        "U R U' R' U' R U' R'  U R' F R F'",
        "R U R' F R U R' U' R' F' R",
        "y U R' U' R U2 R' F2 R' F R2",
        "R' U' F R F' U R2 U' R'"],

         
        "Pinwheel": [
        "x R2 U' R' U R U' R' U x' U' R U' R",
        "R' F' U' F R2 U' R U2 R",
        "R U' R2' y R U' R' U' R U' R'",
        ],

        "TwoFace":[
        "U' R U R' U' R2 U R2 U' R2",
        "y' U R' U2 R' F R F' R",
        "x R U R' U' R' F R' F' U x'",
        "U R U R' U' y' R2 U' R2 U R2",
        ],

        "Turtle":[
        "R U' R' U R U' R'",
        "y R' U' R' F2 R U R' F' R' F R",
        "R' F R2 U R' F' R U' R' F'",
        "y' U' R U R' U' R' U2 F R2 F'",
        "U2 R' F R F' U2 R U2 R'",
        "U' R U2 F' U' F2 R2 F' R2",
        ],
         
        "PinwheelPoser":[
        "y R U R' U' R U2 R' F' R U R' F'",
        "U' R' F R F' R' F R2 U R' U' F'",
        "U' R' U2 R2 U' F R F' U2 R",
        "U2 R' F R F2 U' F",
        "R U' R2 F R F'",
        "U2 F' U R' F2 R F",
        ],
         
        "Gun":[
        "R U' R' U2 R U2 R'",
        "y U' F' R' F2 R F' R' F R2 U' R'",
        "R' F R F' U R U' R'",
        "R U' R' U R U2 R' (F R' F' R)",
        "y' R2' F R F' R U R' U R",
        "U R U2 R' F R F' R U R2",
        ],
        "TCLL_plus": [
        "R' F R F' R' F R F'",
        "y' R' U2 R U' y R U' R'",
        "F2 R' F2 R2 U' R' U2 F",
        "U2  L' U' L F' L' U L U2 F'",
        "U R' U R U' R U' R2 F R2 F'",
        "U R U R' F R F' R U R' U R'",
        "y' U2 R' U' R U R' U' R'",
        "U R' F R F' R' F R U R U' R' F''",
        "U R U' R' U R2 U' R' F R' F''",
        "R U' R' U2 R U' R' U' R' F R F''",
        "U R U2' R' U R' F R F' R U' R''",
        "U2 R' F2 R U' R' F2 R2 U R' F2'",
        "R U R' U F' R U' R' F2",
        "U2 R' F R U' F' R U2 R' F2", 
        "U R U' R' U' R U' R'  U R' F R F'",
        "R U R' F R U R' U' R' F' R",
        "y U R' U' R U2 R' F2 R' F R2",
        "R' U' F R F' U R2 U' R'",
        "x R2 U' R' U R U' R' U x' U' R U' R",
        "R' F' U' F R2 U' R U2 R",
        "R U' R2' y R U' R' U' R U' R'",
        "U' R U R' U' R2 U R2 U' R2",
        "y' U R' U2 R' F R F' R",
        "x R U R' U' R' F R' F' U x'",
        "U R U R' U' y' R2 U' R2 U R2",
        "R U' R' U R U' R'",
        "y R' U' R' F2 R U R' F' R' F R",
        "R' F R2 U R' F' R U' R' F'",
        "y' U' R U R' U' R' U2 F R2 F'",
        "U2 R' F R F' U2 R U2 R'",
        "U' R U2 F' U' F2 R2 F' R2",
        "y R U R' U' R U2 R' F' R U R' F'",
        "U' R' F R F' R' F R2 U R' U' F'",
        "U' R' U2 R2 U' F R F' U2 R",
        "U2 R' F R F2 U' F",
        "R U' R2 F R F'",
        "U2 F' U R' F2 R F",
        "R U' R' U2 R U2 R'",
        "y U' F' R' F2 R F' R' F R2 U' R'",
        "R' F R F' U R U' R'",
        "R U' R' U R U2 R' (F R' F' R)",
        "y' R2' F R F' R U R' U R",
        "U R U2 R' F R F' R U R2"
        ],
    }
    tcll_minus={
    "Hammer":[
    "x U R' U' R U R' U' R x'",
    "y L F' L' F L F' L' F",
    "R U' R U' R' F R' F' R U' R'",
    "U' R U R' F R' F' R U' R U2 R'",
    "U' R U2 R' y' U R' U R",
    "U' R' F R F U' y' R2 U R2",
    "U' F R U R' U' R' F' R2 U R'",
    ],
     
    "Spaceship":[
    "R U R' U' R U R'",
    "U2 F R U R' U' R' F' R F R' F' R",
    "U2 R U R' U' F R' F R U R' F R",
    "y U R' F R2 U' R' U' R' F R F",
    "U F U2 L' U' L F L' U L",
    "y L' U2 L U' L F' L' F L' U L",
    "R U R' U' F R' F2 R U' R' F2 R",
    ],

    "Stollery":[ 
    "U2 F2 R U R' F U' R U' R'",
    "F2 R U2 R' F U L' U' L ",
    "F R' F' U R2 U R2' U' R",
    "R' F R U R U' R' F' R U' R'",
    "U2 F R' F' R2 U R2' F' R U' R' F2 R",
    "U R2 U' R' F R' F' U' R U' R'",
    ],
     
    "Pinwheel":[
    ],
    "TwoFace":[
    "R2 U R2 U' R2 U R U' R'",
    "U' R F R F' R' U' R U R'",
    "R U' R' U2 R U' F R F' U R'",
    "R U' R' U2 R U' F R F' U R'",
    ],
    "Turtle":[
    "U' y L' U L U' L' U L",
    "y' U' R' U' R U' R' U R",
    "y' U R' U R U' R2' F R F' R U' R' U2 R",
    "U2 R F' R' F' U R' U2 R F'",
    "U2 R U R' U y L' U2 L",
    "U' R U2 R' U2 F R' F' R",
    "R U' R' U2 R U R2 F R F'",
    ],
    "Pinwheel poser":[
    "R2 F U' R U F2 U R'",
    "U F U R U' R2 F' R F R' F' R ",
    "y' U' x' R' F R2 U' R' U",
    "U F R' F' R2 U R'",
    "U R U R' F R' F' R U2 R U' R'",
    "F' R' F2 R U' F",
    ],

    "Gun":[
    "U2 R F2 R F2 R' F2 R U' R'"
    ]
}


    algs=[]
    setups=[] 
    
    for alg_set in plus_sets: 
        algs.extend(tcll_plus[alg_set])
        setups.extend(tcll_plus[alg_set])
    for alg_set in minus_sets:     
        algs.extend(tcll_minus[alg_set])
        setups.extend(tcll_minus[alg_set])
       
    if needs_inverse:
        print "INVERSED"
        print "---------"
        i=0
        for alg in algs:
            setups[i] = [setups[i],setup_from_alg(alg)]
            i+=1
        #random.shuffle(setups)
        
        index = 1
        print "setups"
        for setup in setups:
            print index,")", setup[1],"                                            solution:",setup[0]
            # print setup[1]
            print 
            #print alg_url(setup)                         
            print 
            index+=1
        
        
    else:   
        random.shuffle(setups)
        index = 1
        for setup in setups:
            print index,")", setup
            print 
            #print alg_url(setup)                         
            print 
            index+=1     
tcll_trainer(True,["Hammer","Spaceship"],["Hammer"])              
def parse_qq_into_list(times):
    list_of_times = [""]
    for char in times:
        if char == "(" or char == ")" or char == " " or char =="+":
            None
        elif char == ",":
            list_of_times.append("")
        else:
            list_of_times[-1]=list_of_times[-1]+char
    list_of_times_float=[]        
    for time in list_of_times:
        list_of_times_float.append(float(time))
            
    return list_of_times_float
    
def averageOfao5s(times):
    sub10s=0.0
    list_of_averages=[]
    list_of_times = parse_qq_into_list(times)
    for i in range(0,len(list_of_times)-4):
        #finds fives solves
        five_solves = list_of_times[i:i+5]
        slow_solve = min(five_solves)
        fast_solve = max(five_solves)
        #removes fastest and slowest
        five_solves.remove(slow_solve)
        five_solves.remove(fast_solve)
        ao5 = sum(five_solves)/3
        list_of_averages.append(ao5)
        if ao5<10.0:
            sub10s+=1
        
    
    sum_of_avg = sum(list_of_averages)
    num_of_avg = len(list_of_times)-4
    #Calculates interals
    fastafs=0
    low10s=0
    high10s=0
    low11s=0
    high11s=0
    slowafs=0
    for time in list_of_averages:
        
        if time<10.0:
            fastafs+=1
        elif time<10.5:
            low10s+=1
        elif time<11.0:
            high10s+=1
        elif time<11.5:
            low11s+=1
        elif time<12.0:
            high11s+=1
        else:
            slowafs+=1
    print "--INTERVALS--"
    print "     sub10s:",fastafs
    print "10.00-10.50:",low10s
    print "10.50-11.00:",high10s
    print "11.00-11.50:",low11s
    print "11.50-12.00:",high11s
    print " shon times:",slowafs
    print
    #Calculates streak
    allstreak=[]
    
    if list_of_averages[0]>=10.0:
        allstreak.append(1)
    else:
        allstreak.append(-1)
    for k in range(1,len(list_of_averages)):
        
        if list_of_averages[k-1]>=10.0:
            if list_of_averages[k]>=10.0:
                allstreak[-1]+=1
            else: 
                allstreak.append(-1)
        else:
            if list_of_averages[k]<10.0:
                allstreak[-1]-=1
            else: 
                allstreak.append(1)
    print "--STREAKS--"
    print "all streaks:", allstreak        
    #Calculates sub10 streak 
    sub10streak=[0]
    for count in allstreak:
        #print count
        if count == 0:
            sub10streak[-1]+=1
        else:
            sub10streak.append(0)
    
    #Calculates sup10 streak        
    sub10streak = [-x for x in allstreak if x <= 0] 
    sup10streak = [x for x in allstreak if x > 0] 
    print "sub10 streak:",sub10streak
    print "streaks without a sub10:",sup10streak 
    print
    print"--RESULTS--"
    #Calculates SUB10s
    print "SUB 10s: "+ str(int(sub10s)) + " out of "+ str(num_of_avg) + "= " + str((sub10s/num_of_avg)*100)+ "%"
    print
    #Calculates average of ao5s
    print "avg of ao5's: " +str(sum_of_avg/num_of_avg)
    print
    #Recalculate when removing times (5%)
    five_percent = int(round(.05*len(list_of_averages)))
    for j in range(0,five_percent):
        list_of_averages.remove(min(list_of_averages))
        list_of_averages.remove(max(list_of_averages))
    sum_of_avg5percent = sum(list_of_averages)
    num_of_avg5percent = len(list_of_times)-4-(2*five_percent)
    print "avg of ao5's - 5%: "+ str(sum_of_avg5percent / num_of_avg5percent)
    print
    
    
##################
#PLACE TESTS HERE
#################
#pll_trainer()  
#oll_trainer()  
#oll_trainer(True)
#coll_trainer()  
#f2l_trainer()     
#string_times = "10.00, 10.00, 10.00, 10.00, 9.00, 9.00, 10.00, 10.00, 10.00, 10.00"
string_times ="(8.24), 10.51, 9.59, 10.19, (8.55), 9.81, 9.21, 11.26, 9.36, 12.99, 11.64, 11.08, 9.76, 9.13, 10.11, 10.34, 11.01, (7.49), 10.32, 10.31, 11.04+, 10.15, 11.17, 11.22+, 11.29, 10.83, 9.16, 9.88, 9.19, 11.56, 11.01, 10.17, 10.98, 10.66, 10.21, (6.97), 10.62, 11.01, 9.66, 12.22, 9.77, 11.69, 10.83, 9.75, 10.21, 8.89, 11.52, (14.28), 12.32, (13.29), 8.92, 10.79, 10.11, 10.23, 11.31, 9.12, 10.60, 9.02, 9.20, 9.71, 10.11, 9.70, (15.73), 9.15, 8.82, 9.90, 10.61, 8.91, 9.63, 9.83, 9.92, 9.49, 10.26, 11.40, 11.85, 9.48, 12.72, 8.73, 9.26, (13.05), 12.59, 9.06, 10.77, 11.11, 10.18, 11.69+, 9.74, 10.40, 10.71, (14.01), 10.16, 9.60, 10.29, 11.58, 9.47, 12.12, 10.82, 12.38, (8.61), 9.50"
#averageOfao5s(string_times)
# print "qq ao100:"



# print 
# print
# print
# print
# print
# print "RACE TO SUB-10!!!"