# 클래스는 객체를 생성하는 틀, 설계도
# 객체는 클래스로부터 메모리에 생성된 실체
# 객체는 속성과 기능(동작)으로 구성 (속성: 인스턴스 변수, 기눙: 메서드 정의)

class Travel:              # 클래스 선언
    INDIVIDUAL = 1         # 클래스 변수 선언
    PACKAGE = 0           
    # 생성되는 객체의 속성(인스턴스 변수)를 초기화하는 생성자 메서드
    def __init__(self, travelCode, cityName, flight, travelType, maxPeople, reserved):
        # 객체의 인스턴스 변수 선언과 초기화
        self.travelCode = travelCode
        self.cityName = cityName
        self.flight = flight
        self.travelType = travelType
        self.maxPeople = maxPeople
        self.reserved = reserved

    # object로 부터 상속받은 메서드를 재정의(override)
    def __str__(self):
        info = self.travelCode + '\t' + self.cityName + '\t' + self.flight + '\t'
        if self.travelType == Travel.INDIVIDUAL:
            info += '개별자유여행'
        else:
            info += '패키지여행'
        info += '\t' + str(self.maxPeople) + '명\t' + str(self.reserved) + '명'
        return info

travel1 = Travel('TRV001', '뭰휀', '독일항공', Travel.INDIVIDUAL, 10, 0)
print(travel1) # TRV001  뭰휀    독일항공        개별자유여행    10명    0명

class TravelBiz:
    def __init__(self):
        self.travels = []
    
    def printAllTravels(self):
        for t in self.travels:
            print(t)
            
    def printIndividualTravels(self):
        for t in self.travels:
            if t.travelType == Travel.INDIVIDUAL:
                print(t)
    
    def printPackageTravels(self):
        for t in self.travels:
            if t.travelType == Travel.PACKAGE:
                print(t)
    
    def reservedTravel(self, travelCode, resereCount):
        for t in self.travels:
            if t.travelCode == travelCode:
                t.reserved += resereCount
                break
        else:
            print('여행코드가 존재하지 않습니다.')
    
    def printTravelListTitle(self):
        print('-------------------------------------------------------')
        print('여행코드   도시명   항공편   여행유형   최대인원   예약인원')
        print('-------------------------------------------------------')

def printMenu():
    print('-------------------------------------------------------')
    print('1. 전체 여행 상품 조회')
    print('2. 개별 여행 상품 조회')
    print('3. 패키지 여행 상품 조회')
    print('4. 여행 상품 예약')
    print('9. 종료')
    print('-------------------------------------------------------')
    

if __name__ == '__main__' :
    biz = TravelBiz()
    biz.travels.append(Travel("TRV001", "뭔휀", "독일항공", Travel.INDIVIDUAL, 10, 0))
    biz.travels.append(Travel("TRV002", "프랑스", "에어프랑스", Travel.INDIVIDUAL, 20, 0))
    biz.travels.append(Travel("TRV003", "LA", "델타항공", Travel.PACKAGE, 12, 0))
    biz.travels.append(Travel("TRV004", "후쿠오카", "대한항공", Travel.INDIVIDUAL, 15, 0))
    biz.travels.append(Travel("TRV005", "상해", "남방항공", Travel.PACKAGE, 10, 0))

    while True:
        printMenu()
        menu = int(input(' ## 메뉴 입력: '))
        if menu == 1:
            biz.printTravelListTitle()
            biz.printAllTravels()
        elif menu == 2:
            biz.printTravelListTitle()
            biz.printIndividualTravels()
        elif menu == 3:
            biz.printTravelListTitle()
            biz.printPackageTravels()
        elif menu == 4:
            biz.reservedTravel()
        elif menu == 9:
            break
        else:
            print(' ## 잘못된 메뉴번호 입니다.')
            continue
        print()
        input(' ## 엔터를 입력하세요.')
        print()
        
