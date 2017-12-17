def moveTower(height,A, B, C):
    
    def moveDisk(fp,tp):
        print("moving disk from",fp,"to",tp)
        
    if height >= 1:
        moveTower(height-1,A,C,B)
        moveDisk(A,B)
        moveTower(height-1,C,B,A)
    

moveTower(4,"A","C","B") #from, to, with
	

