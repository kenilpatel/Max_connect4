import sys
class boardconfig:
	def __init__(self,board=[[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],column=[5,5,5,5,5,5,5],player1moves=[],player2moves=[]):
		self.evaltable=[[3, 4, 5, 7, 5, 4, 3], [4, 6, 8, 10, 8, 6, 4], [5, 8, 11, 13, 11, 8, 5], [5, 8, 11, 13, 11, 8, 5], [4, 6, 8, 10, 8, 6, 4], [3, 4, 5, 7, 5, 4, 3]]
		self.board=board
		self.minx=0
		self.maxx=6
		self.miny=0
		self.maxy=5
		self.player1moves=player1moves
		self.player2moves=player2moves
		self.column=column
	def print1(self):
		for x in range(self.miny,self.maxy+1): 
			print(self.board[x])  
		print("\n")
	def write(self,x,y="computer.txt",z="human.txt"): 
		if(x=="c"):
			boards=""
			for i in self.board:
				for j in i:
					boards=boards+str(j)
				boards=boards+"\n"
			boards=boards+"2"
			f=open(y,"w")
			f.write(boards)
		elif(x=="h"):
			boards=""
			for i in self.board:
				for j in i:
					boards=boards+str(j)
				boards=boards+"\n"
			boards=boards+"1"
			f=open(z,"w")
			f.write(boards)
	def printreturn(self):
		return self.board
	def full(self):
		if(self.column==[-1,-1,-1,-1,-1,-1,-1]):
			return True
		else:
			return False
	def valid(self,col):
		col=col-1 
		if(col>=0 and col<=6):
			if(self.column[col]!=-1):
				return True
			else:
				return False
		else:
			return False
	def returnconfig(self):
		return self.board,self.column,self.player1,self.player2
	def makemove(self,player1,player2,col):
		col=col-1
		if(player1):
			if(self.column[col]!=-1):
				b=[]
				pm1=[]
				pm2=[]
				for i in self.player1moves:
					pm1.append(i)
				for i in self.player2moves:
					pm2.append(i)
				cd=[]
				for i in self.column:
					cd.append(i)
				for i in self.board:
					dummy=[]
					for j in i:
						dummy.append(j)
					b.append(dummy)
				b[self.column[col]][col]=1 
				pm1.append([self.column[col],col])
				cd[col]=cd[col]-1 
				return b,cd,pm1,pm2 
			else:
				return False
		elif(player2):
			if(self.column[col]!=-1):
				b=[]
				pm1=[]
				pm2=[]
				cd=[]
				for i in self.player1moves:
					pm1.append(i)
				for i in self.player2moves:
					pm2.append(i)
				for i in self.column:
					cd.append(i)
				for i in self.board:
					dummy=[]
					for j in i:
						dummy.append(j)
					b.append(dummy)
				b[self.column[col]][col]=2 
				pm2.append([self.column[col],col])
				cd[col]=cd[col]-1 
				return b,cd,pm1,pm2 
			else:
				return False
		else:
			return False
	def returnutil(self):
		sum=0
		for i in self.player1moves:
			sum=sum+self.evaltable[i[0]][i[1]]
		for i in self.player2moves:
			sum=sum-self.evaltable[i[0]][i[1]]
		return sum
	def returnutil1(self):
		sum=0
		for i in self.player1moves:
			sum=sum-self.evaltable[i[0]][i[1]]
		for i in self.player2moves:
			sum=sum+self.evaltable[i[0]][i[1]]
		return sum 
	def horizontal_four1(self,inpx,inpy): 
		x=inpx
		count=0  
		score=0
		while(x>=self.minx and count<=4): 
			if(x+3<=self.maxx and x+3>=inpx): 
				flag=1
				for i in range(0,4):
					if(x+i!=inpx): 
						if(self.board[inpy][x+i]!=1):
							flag=0 
							break
				if(flag==1):
					score=score+1 
			x=x-1
			count=count+1  
		return score
	def horizontal_four2(self,inpx,inpy): 
		x=inpx
		count=0  
		score=0
		while(x>=self.minx and count<=4): 
			if(x+3<=self.maxx and x+3>=inpx): 
				flag=1
				for i in range(0,4):
					if(x+i!=inpx): 
						if(self.board[inpy][x+i]!=2):
							flag=0 
							break
				if(flag==1):
					score=score+1 
			x=x-1
			count=count+1  
		return score
	def vertical_four1(self,inpx,inpy): 
		y=inpy
		count=0
		score=0
		while(y>=self.miny and count<=4): 
			if(y+3<=self.maxy and y+3>=inpy): 
				flag=1
				for i in range(0,4):
					if(y+i!=inpy): 
						if(self.board[y+i][inpx]!=1):
							flag=0 
							break 
				if(flag==1):
					score=score+1 
			y=y-1
			count=count+1  
		return score
	def vertical_four2(self,inpx,inpy): 
		y=inpy
		count=0
		score=0
		score=0
		while(y>=self.miny and count<=4): 
			if(y+3<=self.maxy and y+3>=inpy): 
				flag=1
				for i in range(0,4):
					if(y+i!=inpy): 
						if(self.board[y+i][inpx]!=2):
							flag=0 
							break 
				if(flag==1):
					score=score+1 
			y=y-1
			count=count+1  
		return score
	def diagonal_four11(self,inpx,inpy): 
		y=inpy
		x=inpx
		count=0 
		score=0
		while(y>=self.miny and x>=self.minx and count<=4): 
			if(y+3<=self.maxy and x+3<=self.maxx and y+3>=inpy and x+3>=inpx):
				flag=1 
				for i in range(0,4):
					if(y+i!=inpy and x+i!=inpx): 
						if(self.board[y+i][x+i]!=1):
							flag=0 
							break 
				if(flag==1):
					score=score+1  
			y=y-1
			x=x-1
			count=count+1  
		return score
	def diagonal_four12(self,inpx,inpy): 
		y=inpy
		x=inpx
		count=0 
		score=0
		while(y>=self.miny and x>=self.minx and count<=4): 
			if(y+3<=self.maxy and x+3<=self.maxx and y+3>=inpy and x+3>=inpx):
				flag=1 
				for i in range(0,4):
					if(y+i!=inpy and x+i!=inpx): 
						if(self.board[y+i][x+i]!=2):
							flag=0 
							break 
				if(flag==1):
					score=score+1  
			y=y-1
			x=x-1
			count=count+1  
		return score
	def diagonal_four21(self,inpx,inpy): 
		y=inpy
		x=inpx
		count=0 
		score=0
		while(y>=self.miny and x<=self.maxx and count<=4): 
			if(y+3<=self.maxy and x-3>=self.minx and y+3>=inpy and x+3>=inpx): 
				flag=1 
				for i in range(0,4):
					if(y+i!=inpy and x-i!=inpx): 
						if(self.board[y+i][x-i]!=1):
							flag=0 
							break 
				if(flag==1):
					score=score+1  
			y=y-1
			x=x+1
			count=count+1 
		return score
	def diagonal_four22(self,inpx,inpy): 
		y=inpy
		x=inpx
		count=0 
		score=0
		while(y>=self.miny and x<=self.maxx and count<=4): 
			if(y+3<=self.maxy and x-3>=self.minx and y+3>=inpy and x+3>=inpx): 
				flag=1 
				for i in range(0,4):
					if(y+i!=inpy and x-i!=inpx): 
						if(self.board[y+i][x-i]!=2):
							flag=0 
							break 
				if(flag==1):
					score=score+1  
			y=y-1
			x=x+1
			count=count+1 
		return score
	def score(self):
		p1=0
		p2=0
		for i in self.player1moves:
			p1=p1+self.vertical_four1(i[1],i[0])+self.horizontal_four1(i[1],i[0])+self.diagonal_four11(i[1],i[0])+self.diagonal_four21(i[1],i[0]) 
		for i in self.player2moves:
			p2=p2+self.vertical_four2(i[1],i[0])+self.horizontal_four2(i[1],i[0])+self.diagonal_four12(i[1],i[0])+self.diagonal_four22(i[1],i[0]) 
		p1=int(p1/4)
		p2=int(p2/4)
		return p1,p2 

def minmax(board,depth,alpha,beta,maxmin,j):
	if(board.full() and j==0): 
		p1,p2=board.score()
		return board.returnutil()+p1*500-p2*500,board
	elif(depth==0 or board.full()): 
		p1,p2=board.score()
		return board.returnutil()+p1*500-p2*500
	if maxmin:
		maxval=-99999
		move=None 
		for i in range(1,8): 
			if(board.valid(i)):
				b,cd,pm1,pm2=board.makemove(True,False,i)
				b1=boardconfig(b,cd,pm1,pm2)  
				eval=minmax(b1,depth-1,alpha,beta,False,j+1) 
				if(eval>maxval):
					move=b1
					maxval=eval
				if(alpha<eval):
					alpha=eval
				if(beta<=alpha): 
					break 
		if(j==0): 
			return maxval,move
		return maxval
	else:
		minval=99999
		move=None 
		for i in range(1,8):
			if(board.valid(i)):
				b,cd,pm1,pm2=board.makemove(False,True,i)
				b1=boardconfig(b,cd,pm1,pm2) 
				eval=minmax(b1,depth-1,alpha,beta,True,j+1) 
				if(minval>eval):
					move=b1
					minval=eval
				if(beta>eval):
					beta=eval
				if(beta<=alpha): 
					break 
		if(j==0): 
			return minval,move
		return minval

def minmax1(board,depth,alpha,beta,maxmin,j):
	if(board.full() and j==0): 
		p1,p2=board.score()
		return board.returnutil1()+p1*500-p2*500,board
	elif(depth==0 or board.full()): 
		p1,p2=board.score()
		return board.returnutil1()+p1*500-p2*500
	if maxmin:
		maxval=-99999
		move=None 
		for i in range(1,8): 
			if(board.valid(i)):
				b,cd,pm1,pm2=board.makemove(False,True,i)
				b1=boardconfig(b,cd,pm1,pm2)  
				eval=minmax(b1,depth-1,alpha,beta,False,j+1) 
				if(eval>maxval):
					move=b1
					maxval=eval
				if(alpha<eval):
					alpha=eval
				if(beta<=alpha): 
					break 
		if(j==0): 
			return maxval,move
		return maxval
	else:
		minval=99999
		move=None 
		for i in range(1,8):
			if(board.valid(i)):
				b,cd,pm1,pm2=board.makemove(True,False,i)
				b1=boardconfig(b,cd,pm1,pm2) 
				eval=minmax(b1,depth-1,alpha,beta,True,j+1) 
				if(minval>eval):
					move=b1
					minval=eval
				if(beta>eval):
					beta=eval
				if(beta<=alpha): 
					break 
		if(j==0): 
			return minval,move
		return minval

if(sys.argv[1]=="interactive"): 
	depth=int(sys.argv[4])
	try:
		f=open(sys.argv[2],"r") 
		lines=f.readlines() 
		board=[]
		pm1=[]
		pm2=[]
		col=[5,5,5,5,5,5,5]
		nextmove=1
		for i in range(0,len(lines)):
			if(i!=len(lines)-1):
				l=[]
				for j in range(0,len(lines[i])): 
					if(lines[i][j]=="1"):
						l.append(int(lines[i][j]))
						pm1.append([i,j])
						col[j]=col[j]-1
					if(lines[i][j]=="0"):
						l.append(int(lines[i][j]))
					if(lines[i][j]=="2"):
						l.append(int(lines[i][j]))
						pm2.append([i,j])
						col[j]=col[j]-1
				board.append(l) 
			else:
				nextmove=i
		move=boardconfig(board,col,pm1,pm2)
	except Exception: 
		board=[]
		pm1=[]
		pm2=[]
		col=[5,5,5,5,5,5,5]
		move=boardconfig()
	  
	while(move.full()!=True):
		if(sys.argv[3]=="computer-next"):	 
			print("---------------------------")
			print("\n")
			print("Current Board\n")
			move.print1()
			p1,p2=move.score()
			print("Computer Score(1):",p1)
			print("Human Score(2):",p2)
			print("\n")
			print("---------------------------") 
			max,move=minmax(move,depth,-9999,9999,True,0)
			print("---------------------------")
			print("\n")
			print("Current Board\n")
			move.write("c")
			move.print1()
			p1,p2=move.score()
			print("Computer Score(1):",p1)
			print("Human Score(2):",p2)
			print("\n")
			print("---------------------------") 
			if(move.full()==True):
				break
			x=int(input("enter column number:"))
			while(move.valid(x)==False):
				x=int(input("enter valid column number:"))
			b,cd,pm1,pm2=move.makemove(False,True,x)
			move=boardconfig(b,cd,pm1,pm2)
			print("---------------------------")
			print("\n")
			print("Current Board\n")
			move.print1()
			move.write("h")
			p1,p2=move.score()
			print("Computer Score(1):",p1)
			print("Human Score(2):",p2)
			print("\n")
			print("---------------------------") 
		else:
			print("---------------------------")
			print("\n")
			print("Current Board\n")
			move.print1()
			p1,p2=move.score()
			print("Computer Score(1):",p1)
			print("Human Score(2):",p2)
			print("\n")
			print("---------------------------")  
			x=int(input("enter column number:"))
			while(move.valid(x)==False):
				x=int(input("enter valid column number:"))
			b,cd,pm1,pm2=move.makemove(False,True,x)
			move=boardconfig(b,cd,pm1,pm2)
			print("---------------------------")
			print("\n")
			print("Current Board\n")
			move.print1()
			move.write("h")
			p1,p2=move.score()
			print("Computer Score(1):",p1)
			print("Human Score(2):",p2)
			print("\n")
			print("---------------------------") 
			if(move.full()==True):
				break 
			max,move=minmax(move,depth,-9999,9999,True,0)
			print("---------------------------")
			print("\n")
			print("Current Board\n")
			move.write("c")
			move.print1()
			p1,p2=move.score()
			print("Computer Score(1):",p1)
			print("Human Score(2):",p2)
			print("\n")
			print("---------------------------") 
	if(move.full()==True):
		print("---------------------------")
		print("\n")
		print("Current Board\n")
		move.print1()
		p1,p2=move.score()
		print("Computer Score(1):",p1)
		print("Human Score(2):",p2)
		print("\n")
		print("---------------------------")
		print("Board is full")
elif(sys.argv[1]=="one-move"):
	depth=int(sys.argv[4])
	try:
		f=open(sys.argv[2],"r") 
		lines=f.readlines() 
		board=[]
		pm1=[]
		pm2=[]
		col=[5,5,5,5,5,5,5]
		nextmove=1
		for i in range(0,len(lines)):
			if(i!=len(lines)-1):
				l=[]
				for j in range(0,len(lines[i])): 
					if(lines[i][j]=="1"):
						l.append(int(lines[i][j]))
						pm1.append([i,j])
						col[j]=col[j]-1
					if(lines[i][j]=="0"):
						l.append(int(lines[i][j]))
					if(lines[i][j]=="2"):
						l.append(int(lines[i][j]))
						pm2.append([i,j])
						col[j]=col[j]-1
				board.append(l)  
			elif(i==len(lines)-1):
				nextmove=int(lines[i]) 
		move=boardconfig(board,col,pm1,pm2)
		if(move.full()!=True):
			print("---------------------------")
			print("\n")
			print("Current Board\n")
			move.print1()
			p1,p2=move.score()
			print("Player 1:",p1)
			print("Player 2:",p2)
			print("\n")
			print("---------------------------")
			if(nextmove==1):
				max,move=minmax(move,depth,-9999,9999,True,0)
				move.write("c",y=sys.argv[3])
			elif(nextmove==2):
				max,move=minmax(move,depth,-9999,9999,False,0)
				move.write("h",z=sys.argv[3])
			print("---------------------------")
			print("\n")
			print("Current Board\n")
			move.print1()
			p1,p2=move.score()
			print("Player 1:",p1)
			print("Player 2:",p2)
			print("\n")
			print("---------------------------")
		else:
			print("---------------------------")
			print("\n")
			print("Current Board\n")
			move.print1()
			p1,p2=move.score()
			print("Player 1:",p1)
			print("Player 2:",p2)
			print("\n")
			print("---------------------------")
			print("Board is full")
	except Exception:
		print("exception") 