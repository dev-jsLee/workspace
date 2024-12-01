# 학생 클래스를 만들어서
class Student():
    # 수학점수, 영어점수, 국어점수를 입력받아
    def __init__(self, math, kor, eng) -> None:
        # 각각 self math, eng, kor 변수에 담아서
        self.math = math
        self.kor = kor
        self.eng = eng

    def get_math(self) -> int:
        return self.math
    
    def set_math(self, math):
        self.math = math
        return

if __name__ == "__main__":
    # 객체 생성 kim
    # math=80, kor=70, eng=85
    kim = Student(math=80, kor=70, eng=85)
    # 객체에 접근하여 math 점수 출력
    print(kim.get_math()) # 80

    # 객체에 접근하여 메서드 사용하기
    kim.set_math(100)
    print(kim.get_math()) # 100