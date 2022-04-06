import _thread
import sys
import os
import msvcrt
'''info'''
__version__ = 'PureOPENS 0.1.3'
__versionInt__ = 0.1
__info__ = 'Made By PureOPENS 2022[4]'
'''main'''
def PromptInput(prompt='',highlight={},promptText={},key={},offset=0):
	os.system('')
	print()
	globals()['wch_list'] = []
	globals()['prompt_list'] = ['']
	globals()['del_index'] = 0
	globals()['if_exit'] = False
	globals()['get_max'] = []
	globals()['my_import'] = []
	globals()['RETURN_STRING'] = ''
	global wch_list,prompt_list,del_index,if_exit,get_max,my_import
	'''global'''
	if promptText != {}:
		for item in promptText:
			get_max.append(promptText[item][0])
		MAX_Char = len(max(get_max,key=len))*2
	else:
		MAX_Char = 0
	for i in promptText:
		key[i] = promptText[i][1]
	def prompt_(wch_list):
		out = ['']
		get_string = ''.join(wch_list).replace('\033[34m','').replace('\033[0m','').replace('\033[35m','').replace('\033[33m','').replace('\033[32m','').replace('\033[31m','')
		for i in promptText:
			if i[::-1] in get_string[::-1]:
				get_index = find_all(get_string[::-1],i[::-1])
				if get_index[0] == 0:
					out = promptText[i]
		length = len(get_string)+1+offset
		gettab = wch_list.count('\t')
		return ['\t'*gettab+' '*length+out[0].replace('\n','')+' '*(MAX_Char-length-len(out[0])-gettab*4)]
	def find_all(string, sub):
		start = 0
		pos = []
		while True:
			start = string.find(sub, start)
			if start == -1:
				return pos
			pos.append(start)
			start += len(sub)
	def pgetwch():
		global wch_list,del_index,prompt_list,if_exit,RETURN_STRING
		sys.stdout.write(f"\033[1A{prompt}{''.join(wch_list)}")
		sys.stdout.flush()
		while True:
			wch = msvcrt.getwch()
			if wch == '\x08':
				'''Del 16'''
				if del_index < len(wch_list):
					del_index += 1
					for i in range(del_index):
						wch_list[-(i+1)] = ' '
					sys.stdout.write(f"\r{prompt}{''.join(wch_list)}\033[s\n{''.join(prompt_list)}{' '* (MAX_Char - len(''.join(prompt_list)))}\033[u")
					sys.stdout.flush()
			elif wch == '\x0d':
				'''Enter 16'''
				sys.stdout.write(f"\r{prompt}{''.join(wch_list)}\033[s\n{''.join(prompt_list)}{' '* (MAX_Char - len(''.join(prompt_list)))}\r")
				sys.stdout.flush()
				prompt_list = ['']
				if_exit = True
				RETURN_STRING = ''.join(wch_list).replace('\033[34m','').replace('\033[0m','').replace('\033[35m','').replace('\033[33m','').replace('\033[32m','').replace('\033[31m','')
				exit()
				wch_list = []
			elif wch == '\x09':
				'''Tab 16'''
				wch_list.append('\t')
			else:
				try:
					if del_index != 0:
						del_index -= 1
						if wch not in highlight:
							wch_list[-(del_index+1)] = wch
						else:
							wch_list[-(del_index+1)] = f'\033[{str(highlight_list[wch])}m{wch}\033[0m'
					else:
						if wch not in highlight:
							wch_list.append(wch)
						else:
							wch_list.append(f'\033[{str(highlight[wch])}m{wch}\033[0m')
				except:
					pass
				sys.stdout.write(f"\r{prompt}{''.join(wch_list)}\033[s\n{''.join(prompt_list)}{' '* (MAX_Char - len(''.join(prompt_list)))}\033[u")
				sys.stdout.flush()
	def pout():
		global prompt_list,wch_list,if_exit,if_exit
		while True:
			get_string = ''.join(wch_list).replace('\033','')
			prompt_list = prompt_(wch_list)
			for i in key:
				if i in get_string:
					m30 = get_string.count('[30m')
					m0 = get_string.count('[0m')
					m33 = get_string.count('[33m')
					m34 = get_string.count('[34m')
					m31 = get_string.count('[31m')
					m32 = get_string.count('[32m')
					m35 = get_string.count('[35m')
					get = find_all(get_string,i)[-1]-m30*4-m0*3-m31*4-m32*4-m33*4-m34*4-m35*4
					for ic in range(get,get+len(i)):
						wch_list[ic] = f'\033[{str(key[i])}m{wch_list[ic]}\033[0m'
	_thread.start_new_thread(pgetwch,())
	_thread.start_new_thread(pout,())
	while 1:
		if if_exit == True:
			return RETURN_STRING[:-del_index]
			break
def PromptPrint(*argv,color='',sep=' ',end=r'\n', file='sys.stdout', flush=False):
	if len(argv) != 0:
		if color != '':
			run = f'print("\033[{color}m{argv[0]}",'
		else:
			run = f'print("{argv[0]}"'
		for i in argv[1:]:
			if type(i) == str:
				run += fr'"{i}",'
			else:
				run += str(i) +','
		if color != '':
			run += '"\033[0m",'
		run += fr'sep="{sep}",end="{end}",file={file},flush={flush}'
		run += ')'
		exec(run)
	else:
		print()
