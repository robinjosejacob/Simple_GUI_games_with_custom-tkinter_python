from cProfile import run
import random

box = [101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125]
box1 = box[:]
random.shuffle(box1)

def show_matix():
    box_matrix = [box1[i:i+5] for i in range(0,len(box1),5)]
    for num in box_matrix:
        print(num)

run_flag = 1
rounds_counts = 1
score_board = ["","$","$","$","$","$"]
score_index = 0
score_count = "=====>"

# flag = [run_status,done_status]
r1,r2,r3,r4,r5 = [1,0],[1,0],[1,0],[1,0],[1,0]
c1,c2,c3,c4,c5 = [1,0],[1,0],[1,0],[1,0],[1,0]
d1,d2 = [1,0],[1,0]

print("\nWelcome\n")
name = str(input("Enter your name : "))
disp_score = str(input("Do you want to dispaly score board with game [Y/N] : "))

while(run_flag):
    print("\n=============================================\n")
    print("Number of rounds : " + str(rounds_counts) + "\n")
    show_matix()
   
    a = int(input("\nEnter the number : "))

    for i in range(len(box1)):
        if box1[i] == a:
            input_val = i

    box1[input_val] = "/"

    ############ Checking #############
    for j in range(len(box1)):
        if (r1[0]==1) and (box1[0] and box1[1] and box1[2] and box1[3] and box1[4] =="/"):
            r1[0]=0
        if (r2[0]==1) and (box1[5] and box1[6] and box1[7] and box1[8] and box1[9] =="/"):
            r2[0]=0
        if(r3[0]==1) and (box1[10] and box1[11] and box1[12] and box1[13] and box1[14] =="/"):
            r3[0]=0
        if(r4[0]==1) and (box1[15] and box1[16] and box1[17] and box1[18] and box1[19] =="/"):
            r4[0]=0
        if(r5[0]==1) and (box1[20] and box1[21] and box1[22] and box1[23] and box1[24] =="/"):
            r5[0]=0
        if(c1[0]==1) and (box1[0] and box1[5] and box1[10] and box1[15] and box1[20] =="/"):
            c1[0]=0
        if(c2[0]==1) and (box1[1] and box1[6] and box1[11] and box1[16] and box1[21] =="/"):
            c2[0]=0
        if(c3[0]==1) and (box1[2] and box1[7] and box1[12] and box1[17] and box1[22] =="/"):
            c3[0]=0
        if(c4[0]==1) and (box1[3] and box1[8] and box1[13] and box1[18] and box1[23] =="/"):
            c4[0]=0
        if(c5[0]==1) and (box1[4] and box1[9] and box1[14] and box1[19] and box1[24] =="/"):
            c5[0]=0
        if(d1[0]==1) and (box1[0] and box1[6] and box1[12] and box1[18] and box1[24] =="/"):
            d1[0]=0
        if(d2[0]==1) and (box1[4] and box1[8] and box1[12] and box1[16] and box1[20] =="/"):
            d2[0]=0
        
    if (r1[0]==0 and r1[1]==0) or (r2[0]==0 and r2[1]==0) or (r3[0]==0 and r3[1]==0) or (r4[0]==0 and r4[1]==0) or (r5[0]==0 and r5[1]==0) or (c1[0]==0 and c1[1]==0)  or (c2[0]==0 and c2[1]==0) or (c3[0]==0 and c3[1]==0) or (c4[0]==0 and c4[1]==0) or (c5[0]==0 and c5[1]==0) or (d1[0]==0 and d1[1]==0) or (d2[0]==0 and d2[1]==0):
        score_index = score_index + 1

    if r1[0]==0:
        r1[1]=1
    if r2[0]==0:
        r2[1]=1
    if r3[0]==0:
        r3[1]=1
    if r4[0]==0:
        r4[1]=1
    if r5[0]==0:
        r5[1]=1
    if c1[0]==0:
        c1[1]=1
    if c2[0]==0:
        c2[1]=1
    if c3[0]==0:
        c3[1]=1
    if c4[0]==0:
        c4[1]=1
    if c5[0]==0:
        c5[1]=1
    if d1[0]==0:
        d1[1]=1
    if d2[0]==0:
        d2[1]=1
    
    if score_index==1:
        score_count="B"
    elif score_index==2:
        score_count="I"
    elif score_index==3:
        score_count="N"
    elif score_index==4:
        score_count="G"
    elif score_index==5:
        score_count="O"
    
    if score_index <= 5:
        score_board[score_index] = score_count
    else:
        run_flag = 0

    if disp_score == 'Y' or disp_score == 'y' or disp_score == 'YES' or disp_score == 'yes' :
        print("\nscore : " + str(score_board))

    rounds_counts = rounds_counts+1

if run_flag == 0 and score_index == 5 :
    print("\n\n\n===============================================\n")
    show_matix()
    print("\n===============================================\n")
    print("************* Congratulations " + name + "*******\n")
    print("\n\n\n===============================================\n")

