from colorama import Fore
from random import randint as r
from random import choice
# from keyboard import get
from os import system
from time import sleep

#==========
import sys,tty,termios
class _Getch:
    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(3)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

def get():
        inkey = _Getch()
        while(1):
                k=inkey()
                if k!='':break
        if k=='\x1b[A':
                return "up"
        elif k=='\x1b[B':
                return "down"
        elif k=='\x1b[C':
                return "right"
        elif k=='\x1b[D':
                return "left"
        else:
                return "not an arrow key!"

# if __name__ == "__main__":
# 	for i in range(10):
# 		print(get())

#=======

file_name = 'scores.txt'

class Game2048:
	def __init__(self):
		self.score_list = open(file_name).readlines()
		self.highest_score = 0 if not self.score_list else self.score_list[0].split()[-1]
		print('Welcome to 2048 Game!')
		self.name = input('Enter your name: ')
		self.board = [[' ' for i in range(4)] for i in range(4)]
		self.spaces = [[]]
		self.m = []
		self.start()
	def navbar(self):
		print(f'Record: {self.highest_score}  {"by "+self.score_list[0].split()[1] if self.highest_score else ""}')

	def start(self):
		while not self.finished():
			system("clear")
			self.navbar()
			self.put()
			self.score()
			self.show()
			key = get()
			self.move(key)
	def score(self):
		self.m = []
		for i in self.board:
			self.m+=i
		self.m = max(filter(lambda x: x!=' ',self.m))
		print(f'Your Highest Score: {self.m}')

	def move(self,key):
		if key == 'down':
			self.down()
		if key == 'up':
			self.up()
		if key == 'left':
			self.left()
		if key == 'right':
			self.right()

	def up(self):
		for j in range(4):
			ustun = []
			for i in range(4):
				if str(self.board[i][j]) !=' ':
					ustun += [self.board[i][j]]
			[4,4]
			k = 0
			while k<len(ustun)-1:
				if ustun[k]==ustun[k+1]:
					ustun[k+1] *= 2
					ustun.pop(k)
				k+=1
			m=0
			for i in ustun:
				self.board[m][j] = i
				m += 1
			while m<4:
				self.board[m][j] = ' '
				m+=1
	def down(self):
		for j in range(4):
			ustun=[]
			for i in range(4):
				if self.board[i][j] !=' ':
					ustun += [self.board[i][j]]
			n = len(ustun)-1
			while n>0:
				if ustun[n]==ustun[n-1]:
					ustun[n-1] *= 2
					ustun.pop(n)
					n -= 2
				else:
					n -= 1
			m = 3
			for i in ustun[::-1]:
				self.board[m][j] = i
				m -= 1
			while m>-1:
				self.board[m][j] = ' '
				m-=1
	def left(self):
		for i in range(4):
			qator = []
			for j in range(4):
				if str(self.board[i][j]) !=' ':
					qator += [self.board[i][j]]
			k = len(qator)-1
			while k>0:
				if qator[k]==qator[k-1]:
					qator[k-1] *= 2
					qator.pop(k)
					k-=2
				else:
					k-=1
			m=0
			for j in qator:
				self.board[i][m] = j
				m += 1
			while m<4:
				self.board[i][m] = ' '
				m+=1
	def right(self):
		for i in range(4):
			qator = []
			for j in range(4):
				if str(self.board[i][j]) !=' ':
					qator += [self.board[i][j]]
			k = 0
			while k<len(qator)-1:
				if qator[k]==qator[k+1]:
					qator[k+1] *= 2
					qator.pop(k)
				k+=1
			m=3
			for j in qator[::-1]:
				self.board[i][m] = j
				m -= 1
			while m>-1:
				self.board[i][m] = ' '
				m-=1

	def put(self):
		self.find()
		if self.spaces:
			x,y = choice(self.spaces)
			self.board[x][y] = 2**r(1,2)

	def find(self):
		res = []
		for i in range(4):
			for j in range(4):
				if self.board[i][j] == ' ':
					res+= [(i,j)]
		self.spaces = res
	def finished(self):
		val = sum([x.count(' ') for x in self.board])
		if val == 0:
			self.score_list.append(f'. {self.name} {self.m}')
			self.score_list.sort(key=lambda p: int(p.split()[-1]),reverse=True)
			self.score_list = list(map(lambda p: ' '.join(p.split()[1:]),self.score_list))
			self.score_list = list(filter(lambda p: len(p.split())>1,self.score_list))
			f = open(file_name,'w')
			for i,person in enumerate(self.score_list):
				f.write(f'{i+1}. {person}\n')
			print(Fore.RED+f'{"="*10}\nTop Scores\n{"="*10}')
			for i,person in enumerate(self.score_list[:5]):
				print(Fore.YELLOW+f'{i+1}. {person}')
			return True
		return False

	def show(self):
		line = "+------"*4+'+'
		print(Fore.WHITE+line)
		for i in range(4):
			for j in range(4):
				c = ' '*(5-len(str(self.board[i][j])))
				print(Fore.WHITE+f'|{c}',end='')
				if self.board[i][j] == ' ':
					print(Fore.WHITE+self.board[i][j],end=' ')
				if self.board[i][j] == 2:
					print(Fore.WHITE+str(self.board[i][j]),end=' ')
				if self.board[i][j] == 4:
					print(Fore.BLUE+str(self.board[i][j]),end=' ')
				if self.board[i][j] == 8:
					print(Fore.RED+str(self.board[i][j]),end=' ')
				if self.board[i][j] == 16:
					print(Fore.GREEN+str(self.board[i][j]),end=' ')
				if self.board[i][j] == 32:
					print(Fore.YELLOW+str(self.board[i][j]),end=' ')
				if self.board[i][j] == 64:
					print(Fore.MAGENTA+str(self.board[i][j]),end=' ')
				if self.board[i][j] == 128:
					print(Fore.WHITE+str(self.board[i][j]),end=' ')
				if self.board[i][j] == 256:
					print(Fore.BLUE+str(self.board[i][j]),end=' ')
				if self.board[i][j] == 512:
					print(Fore.RED+str(self.board[i][j]),end=' ')
				if self.board[i][j] == 1024:
					print(Fore.GREEN+str(self.board[i][j]),end=' ')
				if self.board[i][j] == 2048:
					print(Fore.YELLOW+str(self.board[i][j]),end=' ')
				if self.board[i][j] == 4096:
					print(Fore.MAGENTA+str(self.board[i][j]),end=' ')

			print(Fore.WHITE+f'|\n{line}')


if __name__ == "__main__":
	Game2048()
