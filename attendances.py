	attendances = {}
class Student(object):
	def call(self, name):
		if name in attendances.values():
			pass
		else:
			attendances[len(attendances)] = name
	def print_attendances_list(self):
		#print(attendances.values())
		i = 0
		for i in attendances.keys():
			print(attendances.get(i))
			i = i + 1