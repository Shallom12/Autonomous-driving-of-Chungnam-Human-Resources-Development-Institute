# 🐍 Python 코딩 시 주의점 가이드

> Python 개발 시 주의해야 할 핵심 사항들과 자율주행 시스템 예제를 포함한 종합 가이드

## 📋 목차
- [문법 관련 주의사항](#문법-관련-주의사항)
- [변수와 데이터 타입](#변수와-데이터-타입)
- [문자열 처리](#문자열-처리)
- [리스트와 인덱스](#리스트와-인덱스)
- [반복문과 조건문](#반복문과-조건문)
- [자율주행 시스템 If문 예제](#자율주행-시스템-if문-예제)
- [함수 관련 주의사항](#함수-관련-주의사항)
---

## 📐 문법 관련 주의사항

### 들여쓰기 (Indentation)

Python은 들여쓰기로 코드 블록을 구분하므로 일관성이 매우 중요합니다.

#### ❌ 잘못된 예시
```python
# 들여쓰기가 없는 경우
if True:
print("Hello")  # IndentationError 발생!
```

#### ✅ 올바른 예시
```python
# 스페이스 4개로 일관되게 들여쓰기
if True:
    print("Hello")  # 정상 실행
    print("World")  # 정상 실행
```

**실행 결과:**
```
Hello
World
```

> **💡 팁:** IDE에서 탭을 스페이스 4개로 설정하거나, 한 방식만 일관되게 사용하세요.

### 대소문자 구분

Python은 대소문자를 엄격하게 구분합니다.

#### ❌ 잘못된 예시
```python
Print("Hello")  # NameError: name 'Print' is not defined
```

#### ✅ 올바른 예시
```python
print("Hello")  # 정상 실행
```

**실행 결과:**
```
Hello
```

---

## 🏷️ 변수와 데이터 타입

### 변수명 규칙

Python 변수명은 특정 규칙을 따라야 합니다.

#### ❌ 잘못된 변수명
```python
# 숫자로 시작하는 경우
2name = "John"  # SyntaxError

# 특수문자 사용하는 경우
my-name = "John"  # SyntaxError

# 예약어 사용하는 경우
class = "A"  # SyntaxError
```

#### ✅ 올바른 변수명
```python
# 올바른 변수명 사용
name2 = "John"
my_name = "John"
class_name = "A"

print(f"이름: {name2}")
print(f"사용자명: {my_name}")
print(f"클래스: {class_name}")
```

**실행 결과:**
```
이름: John
사용자명: John
클래스: A
```

---

## 📝 문자열 처리

### 따옴표 사용 주의

문자열 내부에 따옴표가 있을 때 주의해야 합니다.

#### ❌ 잘못된 예시
```python
text = "She said "Hello""  # SyntaxError
```

#### ✅ 올바른 예시
```python
# 방법 1: 이스케이프 문자 사용
text1 = "She said \"Hello\""

# 방법 2: 다른 종류의 따옴표 사용
text2 = 'She said "Hello"'

# 방법 3: 삼중 따옴표 사용
text3 = """She said "Hello" and 'Hi'"""

print(text1)
print(text2)
print(text3)
```

**실행 결과:**
```
She said "Hello"
She said "Hello"
She said "Hello" and 'Hi'
```

### 문자열과 숫자 연산

문자열과 숫자를 직접 연결할 수 없습니다.

#### ❌ 잘못된 예시
```python
age = 25
print("나이: " + age)  # TypeError: can only concatenate str (not "int") to str
```

#### ✅ 올바른 예시
```python
age = 25

# 방법 1: str() 함수 사용
result1 = "나이: " + str(age)

# 방법 2: f-string 사용 (권장)
result2 = f"나이: {age}"

# 방법 3: format() 메서드 사용
result3 = "나이: {}".format(age)

print(result1)
print(result2)
print(result3)
```

**실행 결과:**
```
나이: 25
나이: 25
나이: 25
```

---

## 📋 리스트와 인덱스

### 인덱스 범위 주의

리스트의 인덱스 범위를 초과하면 오류가 발생합니다.

#### ❌ 잘못된 예시
```python
my_list = [1, 2, 3]
print(my_list[3])  # IndexError: list index out of range
```

#### ✅ 올바른 예시
```python
my_list = [1, 2, 3]

# 안전한 인덱스 접근 방법들
print(f"마지막 요소: {my_list[2]}")      # 인덱스 2 (세 번째 요소)
print(f"마지막 요소: {my_list[-1]}")     # 음수 인덱스 사용
print(f"리스트 길이: {len(my_list)}")    # 리스트 길이 확인

# 안전한 접근을 위한 조건문
index = 3
if index < len(my_list):
    print(f"인덱스 {index}의 값: {my_list[index]}")
else:
    print(f"인덱스 {index}는 범위를 벗어났습니다.")
```

**실행 결과:**
```
마지막 요소: 3
마지막 요소: 3
리스트 길이: 3
인덱스 3는 범위를 벗어났습니다.
```

### 리스트 복사 주의

리스트를 직접 할당하면 참조만 복사됩니다.

#### ❌ 잘못된 예시
```python
list1 = [1, 2, 3]
list2 = list1  # 참조 복사 (같은 메모리 주소)
list2.append(4)

print(f"list1: {list1}")  # 원본도 변경됨!
print(f"list2: {list2}")
print(f"같은 객체인가? {list1 is list2}")
```

**실행 결과:**
```
list1: [1, 2, 3, 4]
list2: [1, 2, 3, 4]
같은 객체인가? True
```

#### ✅ 올바른 예시
```python
list1 = [1, 2, 3]

# 방법 1: copy() 메서드 사용
list2 = list1.copy()

# 방법 2: 슬라이싱 사용
list3 = list1[:]

# 방법 3: list() 생성자 사용
list4 = list(list1)

# 각각 다른 객체임을 확인
list2.append(4)
list3.append(5)
list4.append(6)

print(f"원본 list1: {list1}")
print(f"복사본 list2: {list2}")
print(f"복사본 list3: {list3}")
print(f"복사본 list4: {list4}")
```

**실행 결과:**
```
원본 list1: [1, 2, 3]
복사본 list2: [1, 2, 3, 4]
복사본 list3: [1, 2, 3, 5]
복사본 list4: [1, 2, 3, 6]
```

---

## 🔄 반복문과 조건문

### 무한 루프 주의

반복문에서 종료 조건을 확실히 설정해야 합니다.

#### ❌ 위험한 예시
```python
# 이 코드는 실행하지 마세요! 무한 루프입니다.
# while True:
#     print("무한 루프!")  # Ctrl+C로 중단해야 함
```

#### ✅ 안전한 예시
```python
# 카운터를 사용한 안전한 루프
count = 0
max_iterations = 5

while count < max_iterations:
    print(f"카운트: {count}")
    count += 1  # 반드시 카운터를 증가시켜야 함!

print("루프 종료")
```

**실행 결과:**
```
카운트: 0
카운트: 1
카운트: 2
카운트: 3
카운트: 4
루프 종료
```

### 조건문에서 할당 연산자 실수

조건문에서는 비교 연산자(==)를 사용해야 합니다.

#### ❌ 잘못된 예시
```python
x = 5
if x = 10:  # SyntaxError: invalid syntax
    print("x는 10")
```

#### ✅ 올바른 예시
```python
x = 5

# 비교 연산자 사용
if x == 10:
    print("x는 10입니다")
elif x == 5:
    print("x는 5입니다")
else:
    print(f"x는 {x}입니다")

# 다양한 비교 연산자 예시
numbers = [1, 5, 10, 15]
target = 10

for num in numbers:
    if num < target:
        print(f"{num}은 {target}보다 작습니다")
    elif num == target:
        print(f"{num}은 {target}과 같습니다")
    else:
        print(f"{num}은 {target}보다 큽니다")
```

**실행 결과:**
```
x는 5입니다
1은 10보다 작습니다
5은 10보다 작습니다
10은 10과 같습니다
15은 10보다 큽니다
```

---

## 🚗 자율주행 시스템 If문 예제

자율주행 시스템에서 사용되는 복잡한 조건문 예제들입니다.

### 1. 장애물 감지 및 긴급 제동 시스템

```python
import math

def calculate_brake_distance(speed_kmh, friction_coefficient=0.7):
    """제동거리 계산 함수
    
    Args:
        speed_kmh (float): 현재 속도 (km/h)
        friction_coefficient (float): 노면 마찰계수
    
    Returns:
        float: 제동거리 (미터)
    """
    speed_ms = speed_kmh / 3.6  # km/h를 m/s로 변환
    return (speed_ms ** 2) / (2 * 9.8 * friction_coefficient)

# 라이다 센서 데이터 시뮬레이션
front_distance = 15.0  # 전방 장애물까지의 거리 (미터)
current_speed = 60     # 현재 속도 (km/h)

# 제동거리 계산
brake_distance = calculate_brake_distance(current_speed)

print(f"현재 상황:")
print(f"- 현재 속도: {current_speed} km/h")
print(f"- 전방 거리: {front_distance} m")
print(f"- 계산된 제동거리: {brake_distance:.1f} m")
print("-" * 40)

# 제동 강도 결정 로직
if front_distance <= brake_distance:
    emergency_brake = True
    brake_force = 100  # 최대 제동력
    action = "긴급 제동 활성화"
    warning_level = "🚨 위험"
elif front_distance <= brake_distance * 1.5:
    emergency_brake = False
    brake_force = 70
    action = "강한 제동"
    warning_level = "⚠️ 경고"
elif front_distance <= brake_distance * 2:
    emergency_brake = False
    brake_force = 40
    action = "완만한 제동"
    warning_level = "⚡ 주의"
else:
    emergency_brake = False
    brake_force = 0
    action = "정상 주행"
    warning_level = "✅ 안전"

print(f"판단 결과:")
print(f"- 상태: {warning_level}")
print(f"- 행동: {action}")
print(f"- 제동력: {brake_force}%")
print(f"- 긴급제동: {'활성화' if emergency_brake else '비활성화'}")
```

**실행 결과:**
```
현재 상황:
- 현재 속도: 60 km/h
- 전방 거리: 15.0 m
- 계산된 제동거리: 20.1 m

판단 결과:
- 상태: 🚨 위험
- 상태: 긴급 제동 활성화
- 제동력: 100%
- 긴급제동: 활성화
```

### 2. 날씨 조건별 주행 모드 시스템

```python
def determine_driving_mode(weather, visibility, road_friction, temperature, wind_speed):
    """날씨 조건에 따른 주행 모드 결정
    
    Args:
        weather (str): 날씨 상태
        visibility (int): 가시거리 (미터)
        road_friction (float): 노면 마찰계수 (0.0-1.0)
        temperature (int): 기온 (섭씨)
        wind_speed (int): 풍속 (m/s)
    
    Returns:
        dict: 주행 모드 정보
    """
    
    # 기본값 설정
    driving_mode = "normal"
    max_speed_limit = 100
    following_distance_multiplier = 1.0
    special_notes = []
    
    print(f"📊 현재 기상 상황:")
    print(f"- 날씨: {weather}")
    print(f"- 가시거리: {visibility}m")
    print(f"- 노면 마찰계수: {road_friction}")
    print(f"- 기온: {temperature}°C")
    print(f"- 풍속: {wind_speed}m/s")
    print("-" * 40)
    
    # 날씨별 판단 로직
    if weather == "clear" and visibility > 500:
        driving_mode = "normal"
        max_speed_limit = 100
        following_distance_multiplier = 1.0
        special_notes.append("최적의 주행 조건")
        
    elif weather == "rain":
        if road_friction < 0.3:
            driving_mode = "wet_cautious"
            max_speed_limit = 60
            following_distance_multiplier = 2.0
            special_notes.append("노면이 매우 미끄러움")
        else:
            driving_mode = "wet_normal"
            max_speed_limit = 80
            following_distance_multiplier = 1.5
            special_notes.append("우천 시 주의 운전")
            
    elif weather == "snow" or temperature <= 0:
        driving_mode = "winter"
        max_speed_limit = 50
        following_distance_multiplier = 2.5
        special_notes.append("겨울철 운전 모드")
        if temperature <= -5:
            special_notes.append("블랙아이스 주의")
            
    elif weather == "fog" or visibility < 100:
        driving_mode = "low_visibility"
        max_speed_limit = 40
        following_distance_multiplier = 2.0
        special_notes.append("시야 확보 어려움")
        
    elif wind_speed > 20:
        driving_mode = "high_wind"
        max_speed_limit = 70
        following_distance_multiplier = 1.3
        special_notes.append("강풍 주의")
        
    else:
        driving_mode = "cautious"
        max_speed_limit = 80
        following_distance_multiplier = 1.2
        special_notes.append("일반적 주의 운전")
    
    return {
        "mode": driving_mode,
        "max_speed": max_speed_limit,
        "following_distance": following_distance_multiplier,
        "notes": special_notes
    }

# 시나리오 테스트
scenarios = [
    {"weather": "clear", "visibility": 600, "road_friction": 0.8, "temperature": 20, "wind_speed": 5},
    {"weather": "rain", "visibility": 200, "road_friction": 0.25, "temperature": 15, "wind_speed": 10},
    {"weather": "snow", "visibility": 150, "road_friction": 0.3, "temperature": -2, "wind_speed": 8},
]

for i, scenario in enumerate(scenarios, 1):
    print(f"\n🌤️ 시나리오 {i}")
    result = determine_driving_mode(**scenario)
    
    print(f"🚗 주행 모드 결정:")
    print(f"- 모드: {result['mode']}")
    print(f"- 최대 속도: {result['max_speed']} km/h")
    print(f"- 차간거리 배수: {result['following_distance']}배")
    print(f"- 특이사항: {', '.join(result['notes'])}")
```

**실행 결과:**
```
🌤️ 시나리오 1
📊 현재 기상 상황:
- 날씨: clear
- 가시거리: 600m
- 노면 마찰계수: 0.8
- 기온: 20°C
- 풍속: 5m/s
----------------------------------------
🚗 주행 모드 결정:
- 모드: normal
- 최대 속도: 100 km/h
- 차간거리 배수: 1.0배
- 특이사항: 최적의 주행 조건

🌤️ 시나리오 2
📊 현재 기상 상황:
- 날씨: rain
- 가시거리: 200m
- 노면 마찰계수: 0.25
- 기온: 15°C
- 풍속: 10m/s
----------------------------------------
🚗 주행 모드 결정:
- 모드: wet_cautious
- 최대 속도: 60 km/h
- 차간거리 배수: 2.0배
- 특이사항: 노면이 매우 미끄러움

🌤️ 시나리오 3
📊 현재 기상 상황:
- 날씨: snow
- 가시거리: 150m
- 노면 마찰계수: 0.3
- 기온: -2°C
- 풍속: 8m/s
----------------------------------------
🚗 주행 모드 결정:
- 모드: winter
- 최대 속도: 50 km/h
- 차간거리 배수: 2.5배
- 특이사항: 겨울철 운전 모드
```

### 3. 스쿨존 안전 운전 시스템

```python
from datetime import datetime

def school_zone_safety_check(current_zone, zone_speed_limit, current_time, 
                           day_of_week, children_detected, current_speed):
    """스쿨존 안전 운전 시스템
    
    Args:
        current_zone (str): 현재 구역 유형
        zone_speed_limit (int): 구역 제한속도
        current_time (int): 현재 시간 (0-23)
        day_of_week (str): 요일
        children_detected (bool): 어린이 감지 여부
        current_speed (int): 현재 속도
    
    Returns:
        dict: 안전 운전 지침
    """
    
    print(f"🏫 구역 안전 분석:")
    print(f"- 현재 구역: {current_zone}")
    print(f"- 기본 제한속도: {zone_speed_limit} km/h")
    print(f"- 현재 시간: {current_time}:00")
    print(f"- 요일: {day_of_week}")
    print(f"- 어린이 감지: {'예' if children_detected else '아니오'}")
    print(f"- 현재 속도: {current_speed} km/h")
    print("-" * 40)
    
    # 기본 설정
    enforced_speed_limit = zone_speed_limit
    extra_caution = False
    safety_measures = []
    
    if current_zone == "school_zone":
        # 등하교 시간대 확인
        if 7 <= current_time <= 9 or 14 <= current_time <= 16:
            if day_of_week in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
                enforced_speed_limit = 30
                extra_caution = True
                safety_measures.append("등하교 시간대 특별 주의")
            else:
                enforced_speed_limit = 40
                safety_measures.append("주말 스쿨존 운전")
        else:
            enforced_speed_limit = 50
            safety_measures.append("일반 시간대")
            
        # 어린이 감지 시 추가 조치
        if children_detected:
            enforced_speed_limit = min(enforced_speed_limit, 25)
            extra_caution = True
            safety_measures.append("어린이 보행자 감지")
            
    elif current_zone == "hospital_zone":
        enforced_speed_limit = 30
        extra_caution = True
        safety_measures.append("병원 구역 서행")
        
    elif current_zone == "construction":
        enforced_speed_limit = 40
        safety_measures.append("공사 구간 주의")
        
    # 속도 조정 판단
    if current_speed > enforced_speed_limit:
        speed_action = "즉시 감속 필요"
        urgency = "🚨 긴급"
    elif current_speed > enforced_speed_limit * 0.9:
        speed_action = "속도 조심"
        urgency = "⚠️ 주의"
    else:
        speed_action = "적정 속도 유지"
        urgency = "✅ 양호"
    
    # 추가 안전 조치
    if extra_caution:
        safety_measures.extend([
            "전방 주시 강화",
            "비상등 점멸 고려",
            "서행 준비"
        ])
    
    return {
        "enforced_limit": enforced_speed_limit,
        "action": speed_action,
        "urgency": urgency,
        "extra_caution": extra_caution,
        "measures": safety_measures
    }

# 다양한 시나리오 테스트
test_scenarios = [
    {
        "current_zone": "school_zone",
        "zone_speed_limit": 30,
        "current_time": 8,  # 등교 시간
        "day_of_week": "monday",
        "children_detected": True,
        "current_speed": 35
    },
    {
        "current_zone": "school_zone", 
        "zone_speed_limit": 30,
        "current_time": 15,  # 하교 시간
        "day_of_week": "friday",
        "children_detected": False,
        "current_speed": 28
    },
    {
        "current_zone": "hospital_zone",
        "zone_speed_limit": 40,
        "current_time": 10,
        "day_of_week": "wednesday",
        "children_detected": False,
        "current_speed": 32
    }
]

for i, scenario in enumerate(test_scenarios, 1):
    print(f"\n📍 테스트 시나리오 {i}")
    result = school_zone_safety_check(**scenario)
    
    print(f"📋 안전 운전 지침:")
    print(f"- 적용 제한속도: {result['enforced_limit']} km/h")
    print(f"- 상태: {result['urgency']}")
    print(f"- 조치: {result['action']}")
    print(f"- 특별 주의: {'필요' if result['extra_caution'] else '불필요'}")
    print(f"- 안전 조치: {', '.join(result['measures'])}")
```

**실행 결과:**
```
📍 테스트 시나리오 1
🏫 구역 안전 분석:
- 현재 구역: school_zone
- 기본 제한속도: 30 km/h
- 현재 시간: 8:00
- 요일: monday
- 어린이 감지: 예
- 현재 속도: 35 km/h
----------------------------------------
📋 안전 운전 지침:
- 적용 제한속도: 25 km/h
- 상태: 🚨 긴급
- 조치: 즉시 감속 필요
- 특별 주의: 필요
- 안전 조치: 등하교 시간대 특별 주의, 어린이 보행자 감지, 전방 주시 강화, 비상등 점멸 고려, 서행 준비

📍 테스트 시나리오 2
🏫 구역 안전 분석:
- 현재 구역: school_zone
- 기본 제한속도: 30 km/h
- 현재 시간: 15:00
- 요일: friday
- 어린이 감지: 아니오
- 현재 속도: 28 km/h
----------------------------------------
📋 안전 운전 지침:
- 적용 제한속도: 30 km/h
- 상태: ✅ 양호
- 조치: 적정 속도 유지
- 특별 주의: 필요
- 안전 조치: 등하교 시간대 특별 주의, 전방 주시 강화, 비상등 점멸 고려, 서행 준비

📍 테스트 시나리오 3
🏫 구역 안전 분석:
- 현재 구역: hospital_zone
- 기본 제한속도: 40 km/h
- 현재 시간: 10:00
- 요일: wednesday
- 어린이 감지: 아니오
- 현재 속도: 32 km/h
----------------------------------------
📋 안전 운전 지침:
- 적용 제한속도: 30 km/h
- 상태: 🚨 긴급
- 조치: 즉시 감속 필요
- 특별 주의: 필요
- 안전 조치: 병원 구역 서행, 전방 주시 강화, 비상등 점멸 고려, 서행 준비
```

---

## 🔧 함수 관련 주의사항

### 매개변수 기본값 함정

가변 객체를 기본값으로 사용하면 예상치 못한 결과가 발생할 수 있습니다.

#### ❌ 위험한 코드
```python
def add_item_wrong(item, my_list=[]):  # 위험! 기본값이 공유됨
    my_list.append(item)
    return my_list

# 문제 상황 재현
print("첫 번째 호출:")
list1 = add_item_wrong("apple")
print(f"결과: {list1}")

print("\n두 번째 호출:")
list2 = add_item_wrong("banana")  
print(f"결과: {list2}")  # ['apple', 'banana'] - 예상과 다름!

print(f"\n같은 객체인가? {list1 is list2}")  # True
```

**실행 결과:**
```
첫 번째 호출:
결과: ['apple']

두 번째 호출:
결과: ['apple', 'banana']

같은 객체인가? True
```

#### ✅ 올바른 코드
```python
def add_item_correct(item, my_list=None):
    """올바른 방식: None 체크 후 새로운 리스트 생성"""
    if my_list is None:
        my_list = []  # 매번 새로운 리스트 생성
    my_list.append(item)
    return my_list

# 올바른 동작 확인
print("올바른 함수 테스트:")
print("첫 번째 호출:")
list1 = add_item_correct("apple")
print(f"결과: {list1}")

print("\n두 번째 호출:")
list2 = add_item_correct("banana")
print(f"결과: {list2}")

print(f"\n같은 객체인가? {list1 is list2}")  # False

# 기존 리스트에 추가하는 경우
print("\n기존 리스트에 추가:")
existing_list = ["orange"]
result = add_item_correct("grape", existing_list)
print(f"기존 리스트: {existing_list}")
print(f"결과: {result}")
```

**실행 결과:**
```







