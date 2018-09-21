

with open('file.txt') as f:
	
	#
	# 何らかの処理を行う
	#
	
	print(f.closed)

print(f.closed)


# with文を抜ける時、自動的にファイルはクローズされる
# そのため、以下のような構文と同じような意味を持つ

f = open('file.txt')

try:
	
	#
	# 何らかの処理を行う
	#
	pass

except:
	pass

finally:
	f.close()

