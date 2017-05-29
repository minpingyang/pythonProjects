# a = [1,2,3,("b",1)]
# print (a)
# print (type(a))

# line ='work'
# print ("You typed%s" % line)
# line = line + "h"
# num = int(line)
# print ("You typed the number%s"% num)






def perfect_interleave(lst1,lst2,lst3):
	if len(lst1) != len(lst2) or len(lst1) != len(lst3):
		raise Exception('Should input same size list')
	elif len(lst1) == 0 or len(lst2) == 0 or len(lst3) == 0 :
		return []
	else:
		return [lst1[0],lst2[0],lst3[0]] + perfect_interleave(lst1[1:],lst2[1:],lst3[1:])
	

# print(perfect_interleave([],['a','b','c'],['I','II','III']))
print(perfect_interleave(['1','2','3'],['a','b','c'],['I','II','III']))




# a = 123
# b = "this is a great course"
# c = 24.44
# d = ["try","me"]
# e = {2,'a'}
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))





# firefly =["1"]
# firefly.append(["2","3"])
# print(firefly)
# ['1', ['2', '3']]
# firefly.extend(["2","3"])
# print(firefly)



# browncoats = ["Zoe", "Malcolm"]
# crew = ["Hoban", "Kaylee"]
# passengers = ["River", "Shepherd", "Simon", "Inara"]
# cargo = ["Contrabrand"]
# print (len(passengers))
# print (len(cargo))
# print('hello')
# firefly = browncoats + crew + passengers

# print (firefly)

# firefly = firefly + cargo*2
# print (firefly)
# firefly[0]
# print(22)
# print(firefly[-3])
# print(22)
# print (firefly[1:3])

# print("1111")
# print(firefly[1:3][0]);
# print("111")

# if 'River' in firefly:
#     print (firefly)
# if 'River' not in browncoats:
#     print ('moo')