from unittest import main, TestCase
import operator

#implementing zip
def my_zip(*a) :
	if not a :
		return []
	return map(lambda *x : x, *a)

x = [2,3,4]
y = [5,6,7]

assert list(my_zip(x, y)) == [(2,5), (3,6), (4,7)]



#implement map
def my_map(f, a) :
	return (f(x) for x in a)

a_list = [2,3,4]
assert list(my_map(lambda x : x + 1, a_list)) == [3,4,5]




#run some tests
class TestTests (TestCase) :
	def test_1 (self) :
		assert 1 == 1

	def test_2 (self) :
		assert 2 == 2
main()





#implementing iter
class my_list (self) :
	def __init__ (self) :
		self.a = []

	def __iter__ (self) :
		return (v for v in self.a)

	def __append__ (self, v) :
		self.a.append(v)


#implementing another iter
class my_list2 (self) :
	class iterator :
		def __init__ (self, x) :
			self.x = x
			self.i = 0

		def __iter__ (self) :
			return self

		def __next__ (self) :
			if self.i == len(self.x.a) :
				raise StopIteration
			v = self.a[self.i]
			self.i += 1
			return v

	def __init__ (self) :
		self.a = []

	def __iter__ (self) :
		return my_list2.iterator(self)

	def append (self, v) :
		self.a.append(v)


#testing first iter
def test(c) :
	x = c()
	x.append(2)
	x.append(3)
	x.append(4)
	assert not hasattr(x, "__next__")
	assert	   hasattr(x, "__iter__")

	p = iter(x)
	assert     hasattr(x, "__next__")

	assert next(p) == 2
	assert next(p) == 3
	assert next(p) == 4

	try:
		assert next(p) == 5
	except StopIteration :
		pass

test(my_list)




#testing second iter
def test2(c) :
        x = c()
        x.append(2)
        x.append(3)
        x.append(4)
        assert not hasattr(x, "__next__")
        assert     hasattr(x, "__iter__")

        p = iter(x)
        assert     hasattr(x, "__next__")

        assert next(p) == 2
        assert next(p) == 3
        assert next(p) == 4

        try:
                assert next(p) == 5
        except StopIteration :
                pass

test(my_list2)



#implementing count
def my_count(x = 0, s = 1) :
	return (lambda x : x + s)

x = my_count()
assert next(x) == 0
assert next(x) == 1
assert next(x) == 2

y = my_count(2, 10)
assert next(x) == 2
assert next(x) == 12
assert next(x) == 22



#implement reduce
def my_reduce(f, a, s) :
	if (not a) and (s is None) :
		raise TypeError("reduce() of empty sequence with no initial value")
	it = iter(a)
	if s is None :
		s = next(it)
	for v in it :
		s = f(s, v)
	return s

x = [2,3,4]
assert my_reduce(operator.add, x) == 9
assert my_reduce(operator.add, x, 1) == 10
	



#implement filter
def my_filter(f, a) :
	return (f(x) for x in a)

x = [2,3,4]
assert my_filter(lambda x : x % 2, x) == 3
assert my_filter(lambda x : x % 2 == 0, x) == [2,4]




