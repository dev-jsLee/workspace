# 상속
# 상속이라는 것은 상위 개념을 적용받은 하위 개념을 만들 때
# 사용하는 것이다.(하향식)
# 상속을 하는 클래스는 부모 클래스라고 부르며,
# 상속을 함으로써 상속받는 자식 클래스는
# 부모 클래스가 정의한 속성, 메서드 등등을
# 그대로 (재)사용할 수 있게 된다.

# 혹은 상속받은 것을 수정하거나
# 자식 클래스만의 새로운 무언가를 추가할 수도 있다.

# 부모 클래스, 슈퍼 클래스, 상위 클래스
# 상위 클래스를 먼저 만들고 하위 클래스를 만드는 것을
# 하향식 클래스 작성이라고 부른다.
# 이런 방식은 기초 개념(공통 개념)을 정립한 후
# 구체적인 개념을 추가하는 방식에서 주로 쓰인다.
class Person:
    def __init__(self, name) -> None:
        self.name = name
        pass

    def walk(self, floor:str):
        """
        floor: 어디를 걷고 있는 설명해보자.
        """
        print(f"{self.name}이(가) {floor} 위로 걸어갑니다.")

# 자식 클래스, 서브 클래스, 하위 클래스
# 부모 클래스로부터 속성, 메서드(init 제외)를 그대로 가져와서
# 사용할 수 있는 클래스를 말한다.
# 부모 클래스로부터 상속받은 정보를 수정해서 사용하거나
# 새로운 자신만의 속성이나 기능(메서드)을 추가할 수 있다.
# 상속받은 내용은 재작성할 필요가 없기 때문에
# 개발시간을 단축할 수 있다(생산성 향상)

# 같은 부모 클래스를 상속받은 자식 클래스들은
# 부모 클래스가 정의한 메서드를 모두 가지고 있기 때문에
# 일괄적인, 일관적인 관리와 사용이 가능하다.
class Male(Person):
    def __init__(self, name) -> None:
        # super().__init__(name)
        self.name = name
    
    def walk(self, floor: str):
        # return super().walk(floor)
        # 재정의(override)
        # 부모 클래스에 정의된 메서드를
        # 가리고 스스로가 만든 내용으로 변경하는 것
        print(f"{self.name} 님이 {floor} 위로 걸어갑니다.")

class Female(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
    
    def walk(self, floor: str):
        # return super().walk(floor)
        print(f"{self.name}씨가 {floor}로 된 복도를 걸어갑니다.")

if __name__ == "__main__":
    # m = Male("홍길동")
    # f = Female("홍순자")
    # people: list[Person] = [m, f]
    # 다형성
    # 자식 클래스가 부모 클래스로부터 상속받음으로써
    # 속성과 메서드 뿐만 아니라 부모 클래스라는 "타입"도
    # 상속 받는다.
    # for p in people:
    #     print(p.name)
    #     p.walk("대리석")

    # 원시 타입과 참조 타입
    # 원시타입은 값 그 자체가 들어가 있는 저장공간을 의미한다.
    # 변수에 원시타입의 값을 담아서 다른 변수에 담으면
    # 값만 복사된다.
    num = 3
    num2 = num + 5 # 8
    num += 2    # num == 5
    print(num2) # 8
    # 기존 num을 사용한 것에 대해서
    # 이후에 num의 값을 바꿔도
    # 이전 연산에 영향을 주지 않는다.

    # 참조 타입(클래스)
    # 참조 타입은 값이 위치한 주소값을 담고 있기 때문에
    # 다른 변수에 대입하면 값이 아니라 주소값을 전달한다.
    # 이때 주소값을 가진다는 것은 "참조한다"라고 표현하며
    # 참조 대상이 같은 경우(주소값이 같다면)
    # 같은 대상을 바라보고 있는 것이기 때문에
    # 같은 주소값을 가졌다면 같은 값에 접근할 수 있다.
    철수네집 = Person("철수")
    철수엄마네집 = 철수네집

    # 주소값이 같은지 확인
    print(f"철수네집: {철수네집}")
    print(f"철수엄마네집: {철수엄마네집}")
    print("=============")
    철수네집.name = "홍길동"
    print(f"철수name:\n{철수네집.name}\n")
    print(f"철수엄마name:\n{철수엄마네집.name}")









