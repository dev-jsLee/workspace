# def solution(my_string, overwrite_string, s):
#     #   문자열 my_string, overwrite_string과 정수 s가 주어집니다.
#     answer = ''
#     #   첫글자부터 s-1번째 글자까지를 먼저 answer에 붙인다.
#     answer += my_string[:s]
#     #   덮어쓰려는 문자열을 그 뒤에 붙인다.
#     answer += overwrite_string
#     #   남은 부분, 즉 앞선 부분의 길이 만큼을 제외한 글자부터 맨 뒤까지의 원래 내용을 붙인다.
#     # answer += my_string[s+len(overwrite_string):]
#     answer += my_string[len(answer):]
#     #   문자열 my_string의 인덱스 s부터 overwrite_string의 길이만큼을
#     #   문자열 overwrite_string으로 바꾼 문자열을
#     #   return 하는 solution 함수를 작성해 주세요.
#     return answer



def solution(my_string, overwrite_string, s):
    #   문자열 my_string, overwrite_string과 정수 s가 주어집니다.
    answer = ''
    # ms_li = list(my_string)
    # for i, e in enumerate(ms_li[s:s+len(overwrite_string)]):
    #     ms_li[s+i] = overwrite_string[i]
    # answer = ''.join(ms_li)
    print(my_string[s:s + len(overwrite_string)])
    print(overwrite_string)
    my_string.replace(str(my_string[s:s + len(overwrite_string)]), overwrite_string)

    return my_string

my_string =         "He11oWor1d"
overwrite_string =  "lloWorl"
s = 2

print(solution(my_string, overwrite_string, s)) #  == "HelloWorld"
print(solution("Program29b8UYP", "merS123", 7)) # == "ProgrammerS123"