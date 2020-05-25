#/usr/bin/env

"""a string"""

str = "hello python"

print("{} in {} ? {}".format('e', str, 'e' in str))

a_list = ['a', 'b', 1, 2.0, False, True]

print('{} in {} ? {}'.format(1, a_list, 1 in a_list))

a_tuple = ( 'SONY', 'LG', 'SAMSUNG', 'sony', 'sony' )

print('{} in {} ? {}'.format('SONY', a_tuple, 'SONY' in a_tuple))

a_set = {'A', 'B', 'C'}

print('{} in {} ? {}'.format('A', a_set, 'A' in a_set))

a_dictionary = { 'name': 'a', 'age': 1 }

print('{} in {} ? {}'.format('name', a_dictionary, 'name' in a_dictionary))

"""Magic"""

x = 2
print("id(2) = {}".format(id(2)))
print("id(x = 2) = {}".format(id(x)))

def printHello():
  print('Hello Python')

a = printHello

a()


def func_a():
  the_global = 'a'
  print(the_global)
  def func_b():
    global the_global
    the_global = 'b'
    print(the_global)
  
  func_b()

the_global = 'the global'
func_a()
print(the_global)

def fibo(n):
  arr = []

  for i in range(n):
    if i == 0 or i == 1:
      arr.append(1)
    else:
      arr.append(arr[i - 2] + arr[i - 1])

  return arr

arr = fibo(8)
print(arr)

print(list(range(0, 22, 2)))

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

# program to display student's marks from record
student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Arthur': 77}

for student in marks:
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')    