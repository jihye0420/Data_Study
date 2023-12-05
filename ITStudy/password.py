# def password_test():
#     password = input("비밀번호를 입력하세요: ")
#     while not password:
#         password = input("다시 비밀번호를 입력하세요: ")
#     return password


# returned = password_test()

"""
1. python console로 붙여넣고 실행해서 변수 값 확인
2. 디버깅
3. doctest
"""
def count_words(words):
    count = 0
    for word in words:
        if "kim" in word.lower():
            count += 1
    return count

words = ["Kim", "kimchi", "gim"]
print(count_words(words))
