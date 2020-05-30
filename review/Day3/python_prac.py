fruits = ['사과', '배', '감', '귤']
for fruit in fruits:
    print(fruit)

fruits = ['사과','배','배','감','수박','귤','딸기','사과','배','수박']

count = 0
for fruit in fruits:
	if fruit == '사과':
		count += 1

print(count)

#함수를 정의할 때, def 
#왜 name은 따옴표 안들어가? 매개변수를 정의한 것이기 때문이다! 
def count_fruits(name):
	count = 0
	for fruit in fruits:
		if fruit == name:
			count += 1
	return count

apple_count = count_fruits('사과')
print(apple_count) #사과의 갯수

subak_count = count_fruits('수박')
print(subak_count) #수박의 갯수

gam_count = count_fruits('감')
print(gam_count) #감의 갯수

people = [{'name': 'bob', 'age': 20}, 
          {'name': 'carry', 'age': 38},
          {'name': 'john', 'age': 7}]

# 모든 사람의 이름과 나이를 출력해봅시다.
# 제대로 줄 맞추지 않으면, 원하는 값은 절대 나오지 않는답니다
for person in people:
    print(person['name'], person['age'])

# 이번엔, 반복문과 조건문을 응용한 함수를 만들어봅시다.
# 이름을 받으면, age를 리턴해주는 함수

def age_return(myname):
    for person in people:
        if person['name'] == myname:
            return person['age']
    return '해당하는 이름이 없습니다'

print(age_return('bob'))