#coding: utf-8
def deprecated(n):
	def decorator(f):
		def autre_fonction(*param, **param2):
			try:
				raise DeprecationWarning("Deprecated since v" + str(n))
			except DeprecationWarning as dw:
				print('[DeprecationWarning/WARNING] :')
				for dwarg in dw.args:
					print("\t" + dwarg)

		return autre_fonction

	return decorator