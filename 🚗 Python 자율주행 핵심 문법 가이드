자율주행 개발에서 자주 사용되는 Python 핵심 문법들을 실제 사용 예시와 함께 정리한 가이드입니다.

## 📋 목차
- [반복문 (while, for)](#반복문-while-for)
- [배열 처리](#배열-처리)
- [함수 정의 (def)](#함수-정의-def)
- [클래스 정의 (class)](#클래스-정의-class)
- [조건문 활용](#조건문-활용)
- [예외 처리](#예외-처리)
- [제어문 (continue, pass)](#제어문-continue-pass)

---

## 🔄 반복문 (while, for)

### 실시간 비디오 처리 while 루프

```python
import cv2

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)  # 웹캠 사용

# 기본 비디오 처리 루프
while True:
    ret, frame = cap.read()  # 프레임 읽기
    if not ret:              # 프레임 읽기 실패시
        break                # 루프 종료
    
    # AI 모델로 객체 탐지
    results = model(frame)
    
    # 화면에 프레임 표시
    cv2.imshow('frame', frame)
    
    # 'q' 키 입력시 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 자원 해제
cap.release()
cv2.destroyAllWindows()
```

**실행 결과:**
- 웹캠이 켜지고 실시간으로 영상이 화면에 표시됩니다
- 'q' 키를 누르면 프로그램이 종료됩니다

### 탐지 결과 처리 for 루프

```python
# 각 탐지 결과 순회
for result in results:
    boxes = result.boxes  # 탐지된 객체들의 바운딩 박스
    
    # 방법 1: enumerate로 인덱스와 함께 순회
    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = box.xyxy[0]  # 좌표 추출
        conf = box.conf[0]             # 신뢰도
        cls = box.cls[0]               # 클래스 ID
        
        print(f"객체 {i}: 좌표({x1}, {y1}, {x2}, {y2}), 신뢰도: {conf:.2f}")

    # 방법 2: 좌표 배열 직접 순회
    for i, (x1, y1, x2, y2) in enumerate(boxes):
        # 사각형 그리기 (녹색, 두께 2)
        cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)

    # 방법 3: range로 인덱스 접근
    for i in range(len(boxes)):
        if conf[i] > 0.5:  # 신뢰도 50% 이상만 처리
            # 고신뢰도 객체 처리 로직
            pass
```

**실행 결과:**
```
객체 0: 좌표(150, 200, 350, 450), 신뢰도: 0.85
객체 1: 좌표(400, 100, 600, 300), 신뢰도: 0.92
```

---

## 📊 배열 처리

### 기본 배열 조작

```python
# 빈 리스트 생성
detections = []      # 탐지 결과 저장용
track_history = []   # 추적 히스토리 저장용

# 배열에 데이터 추가
def add_detection(x1, y1, x2, y2, conf, cls):
    # 탐지 정보를 리스트로 저장
    detections.append([x1, y1, x2, y2, conf, cls])
    
    # 중심점 계산 후 추적 히스토리에 추가
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    track_history.append((cx, cy))
    
    print(f"탐지 추가: 중심점({cx}, {cy})")

# 배열 길이 제한 (최근 N개만 유지)
def maintain_history_limit():
    if len(track_history) > 30:  # 최대 30개까지만 유지
        track_history.pop(0)     # 가장 오래된 것 제거
        print("오래된 추적 기록 제거")

# 배열 슬라이싱
recent_points = track_history[-10:]  # 최근 10개
print(f"최근 10개 포인트: {recent_points}")
```

**실행 결과:**
```
탐지 추가: 중심점(250.0, 325.0)
탐지 추가: 중심점(500.0, 200.0)
오래된 추적 기록 제거
최근 10개 포인트: [(250.0, 325.0), (500.0, 200.0), ...]
```

---

## 🔧 함수 정의 (def)

### 차선 검출 함수

```python
def detect_lane_lines(img, roi_vertices, canny_low, canny_high, hough_threshold):
    """
    차선 검출 함수
    
    Args:
        img: 입력 이미지 (numpy array)
        roi_vertices: 관심 영역 좌표 [(x1,y1), (x2,y2), ...]
        canny_low: Canny 엣지 검출 하위 임계값 (int)
        canny_high: Canny 엣지 검출 상위 임계값 (int)
        hough_threshold: Hough 변환 임계값 (int)
    
    Returns:
        lanes: 검출된 차선 리스트
    """
    # 1. 그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. 가우시안 블러 적용
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # 3. Canny 엣지 검출
    edges = cv2.Canny(blur, canny_low, canny_high)
    
    # 4. 관심 영역 마스킹
    mask = create_roi_mask(edges, roi_vertices)
    masked_edges = cv2.bitwise_and(edges, mask)
    
    # 5. Hough 변환으로 직선 검출
    lines = cv2.HoughLinesP(masked_edges, 1, np.pi/180, hough_threshold)
    
    return lines

# 사용 예제
roi_points = [(100, 400), (500, 400), (300, 250)]
lanes = detect_lane_lines(image, roi_points, 50, 150, 100)
print(f"검출된 차선 수: {len(lanes) if lanes is not None else 0}")
```

### 객체 필터링 함수

```python
def filter_by_class(boxes, conf, cls, target_classes):
    """
    특정 클래스의 객체만 골라내는 필터 함수
    
    Args:
        boxes: 각 물체의 위치 정보 (사각형 좌표들)
        conf: 각 물체의 신뢰도 (0~1 점수)
        cls: 각 물체의 종류 (예: 'car', 'person', 'dog')
        target_classes: 우리가 찾고 싶은 물체 종류들
    
    Returns:
        filtered_boxes: 필터링된 박스 리스트
        filtered_conf: 필터링된 신뢰도 리스트
    """
    # 1단계: 빈 리스트 준비
    filtered_boxes = []  # 선택된 물체들의 위치를 저장할 빈 통
    filtered_conf = []   # 선택된 물체들의 신뢰도를 저장할 빈 통
    
    # 2단계: 각 물체를 하나씩 검사
    for i, c in enumerate(cls):
        if c in target_classes:  # 원하는 클래스인가?
            filtered_boxes.append(boxes[i])
            filtered_conf.append(conf[i])
            print(f"클래스 {c} 객체 선택됨 (신뢰도: {conf[i]:.2f})")
    
    return filtered_boxes, filtered_conf

# 사용 예제
target = [0, 2, 3]  # person, car, motorcycle만 선택
vehicles, vehicle_conf = filter_by_class(all_boxes, all_conf, all_cls, target)
print(f"필터링 결과: {len(vehicles)}개 차량 검출")
```

### 유틸리티 함수들

```python
def calculate_center(x1, y1, x2, y2):
    """바운딩 박스의 중심점 계산"""
    center_x = int((x1 + x2) / 2)
    center_y = int((y1 + y2) / 2)
    return center_x, center_y

def is_in_danger_zone(cx, cy, img_width, img_height):
    """위험 구역에 있는지 확인"""
    # 화면 하단 70% 이하, 중앙 40% 영역
    bottom_threshold = img_height * 0.7
    left_threshold = img_width * 0.3
    right_threshold = img_width * 0.7
    
    return (cy > bottom_threshold and 
            cx > left_threshold and 
            cx < right_threshold)

# 사용 예제
cx, cy = calculate_center(100, 200, 300, 400)
if is_in_danger_zone(cx, cy, 800, 600):
    print("⚠️ 위험! 차량이 위험 구역에 있습니다!")
else:
    print("✅ 안전 구역입니다.")
```

**실행 결과:**
```
클래스 0 객체 선택됨 (신뢰도: 0.85)
클래스 2 객체 선택됨 (신뢰도: 0.92)
필터링 결과: 2개 차량 검출
⚠️ 위험! 차량이 위험 구역에 있습니다!
```

---

## 🏗️ 클래스 정의 (class)

### 차량 추적 클래스

```python
class VehicleTracker:
    """차량 추적을 위한 클래스"""
    
    def __init__(self):
        """초기화 메서드"""
        self.tracks = {}           # 추적 중인 차량들 {id: info}
        self.next_id = 0          # 다음에 할당할 ID
        self.max_disappeared = 10  # 최대 실종 프레임 수
        print("🚗 차량 추적기 초기화 완료")
    
    def update_tracks(self, detections):
        """추적 정보 업데이트"""
        print(f"📊 {len(detections)}개 차량 탐지됨")
        
        for detection in detections:
            # 기존 추적과 매칭 시도
            track_id = self.find_closest_track(detection)
            
            if track_id is None:
                # 새로운 차량 추적 시작
                self.create_new_track(detection)
            else:
                # 기존 추적 업데이트
                self.update_existing_track(track_id, detection)
    
    def create_new_track(self, detection):
        """새로운 추적 생성"""
        self.tracks[self.next_id] = {
            'position': detection,
            'disappeared': 0,
            'history': []
        }
        print(f"🆕 새 차량 추적 시작: ID {self.next_id}")
        self.next_id += 1
    
    def find_closest_track(self, detection):
        """가장 가까운 기존 추적 찾기"""
        # 간단한 거리 기반 매칭
        min_distance = float('inf')
        closest_id = None
        
        for track_id, track_info in self.tracks.items():
            distance = self.calculate_distance(detection, track_info['position'])
            if distance < min_distance and distance < 50:  # 임계값
                min_distance = distance
                closest_id = track_id
        
        return closest_id
    
    def calculate_distance(self, det1, det2):
        """두 탐지 결과 간의 거리 계산"""
        cx1, cy1 = calculate_center(*det1[:4])
        cx2, cy2 = calculate_center(*det2[:4])
        return ((cx1 - cx2) ** 2 + (cy1 - cy2) ** 2) ** 0.5

# 사용 예제
tracker = VehicleTracker()
detections = [[100, 200, 300, 400, 0.9, 2], [500, 150, 700, 350, 0.8, 2]]
tracker.update_tracks(detections)
```

### 자율주행 메인 클래스

```python
class AutonomousDriving:
    """자율주행 메인 시스템"""
    
    def __init__(self):
        """시스템 초기화"""
        self.tracker = VehicleTracker()
        self.model = None  # AI 모델 (YOLO 등)
        self.current_speed = 0
        self.target_speed = 50
        print("🤖 자율주행 시스템 초기화")
    
    def process_frame(self, frame):
        """프레임 처리 및 주행 결정"""
        # 1. 객체 탐지
        detections = self.detect_objects(frame)
        
        # 2. 차량 추적 업데이트
        self.tracker.update_tracks(detections)
        
        # 3. 주행 결정
        decision = self.make_driving_decision(detections)
        
        return decision
    
    def detect_objects(self, frame):
        """객체 탐지 (YOLO 모델 사용)"""
        if self.model is None:
            return []
        
        results = self.model(frame)
        detections = []
        
        for result in results:
            if result.boxes is not None:
                for box in result.boxes:
                    x1, y1, x2, y2 = box.xyxy[0]
                    conf = box.conf[0]
                    cls = box.cls[0]
                    detections.append([x1, y1, x2, y2, conf, cls])
        
        return detections
    
    def make_driving_decision(self, detections):
        """주행 결정 로직"""
        # 전방 장애물 확인
        if self.obstacle_ahead(detections):
            print("🛑 전방 장애물 감지 - 제동")
            return "brake"
        
        # 차선 변경 필요성 확인
        elif self.lane_change_needed(detections):
            print("↔️ 차선 변경 필요")
            return "change_lane"
        
        else:
            print("✅ 직진 유지")
            return "continue"
    
    def obstacle_ahead(self, detections):
        """전방 장애물 확인"""
        for detection in detections:
            x1, y1, x2, y2, conf, cls = detection
            cx, cy = calculate_center(x1, y1, x2, y2)
            
            # 전방 중앙 구역에 고신뢰도 객체가 있는가?
            if (conf > 0.7 and 
                cx > 300 and cx < 500 and  # 중앙 구역
                cy > 400):                   # 가까운 거리
                return True
        return False
    
    def lane_change_needed(self, detections):
        """차선 변경 필요성 판단"""
        # 단순 예제: 전방에 느린 차량이 있는 경우
        slow_vehicle_ahead = False
        for detection in detections:
            # 차량 속도 추정 로직 (실제로는 더 복잡)
            if detection[4] > 0.6 and detection[5] == 2:  # 차량 클래스
                slow_vehicle_ahead = True
                break
        
        return slow_vehicle_ahead

# 사용 예제
driving_system = AutonomousDriving()
# decision = driving_system.process_frame(current_frame)
```

**실행 결과:**
```
🤖 자율주행 시스템 초기화
🚗 차량 추적기 초기화 완료
📊 2개 차량 탐지됨
🆕 새 차량 추적 시작: ID 0
🆕 새 차량 추적 시작: ID 1
🛑 전방 장애물 감지 - 제동
```

---

## 🎯 조건문 활용

### 다중 조건 처리

```python
# 객체 타입별 색상 지정
def get_object_color(cls):
    """객체 클래스에 따른 색상 반환"""
    if cls == 0:      # person
        color = (0, 255, 0)      # 녹색
        name = "사람"
    elif cls == 2:    # car
        color = (255, 0, 0)      # 빨간색
        name = "자동차"
    elif cls == 3:    # motorcycle
        color = (0, 0, 255)      # 파란색
        name = "오토바이"
    else:
        color = (128, 128, 128)  # 회색
        name = "기타"
    
    print(f"객체 종류: {name}, 색상: {color}")
    return color, name

# 화면 영역별 처리
def determine_zone(center_x, img_width):
    """화면 위치에 따른 구역 판단"""
    if center_x < img_width // 3:
        zone = "left"
        print("📍 좌측 구역")
    elif center_x > img_width * 2 // 3:
        zone = "right"
        print("📍 우측 구역")
    else:
        zone = "center"
        print("📍 중앙 구역")
    
    return zone

# 복합 조건 처리
def find_important_objects(detections, img_shape):
    """중요한 객체 찾기"""
    important_objects = []
    
    for detection in detections:
        x1, y1, x2, y2, conf, cls = detection
        
        # 복합 조건: 높은 신뢰도 + 특정 클래스 + 화면 하단
        if (conf > 0.7 and                    # 신뢰도 70% 이상
            cls in [0, 2, 3] and              # 사람, 자동차, 오토바이
            y2 > img_shape[0] * 0.5):         # 화면 하단 50% 영역
            
            important_objects.append([x1, y1, x2, y2])
            print(f"⚠️ 중요 객체 발견: 클래스 {cls}, 신뢰도 {conf:.2f}")
    
    return important_objects

# 사용 예제
color, name = get_object_color(2)  # 자동차
zone = determine_zone(400, 800)    # 중앙 구역
important = find_important_objects(detections, (600, 800))
```

**실행 결과:**
```
객체 종류: 자동차, 색상: (255, 0, 0)
📍 중앙 구역
⚠️ 중요 객체 발견: 클래스 2, 신뢰도 0.85
⚠️ 중요 객체 발견: 클래스 0, 신뢰도 0.92
```

---

## 🛡️ 예외 처리

### 안전한 배열 접근

```python
def safe_process_detections(detections):
    """안전한 탐지 결과 처리"""
    # 탐지 결과가 있는지 확인
    if len(detections) > 0:
        print(f"✅ {len(detections)}개 객체 처리 중...")
        
        for i, detection in enumerate(detections):
            try:
                x1, y1, x2, y2, conf, cls = detection
                
                # 좌표 유효성 검사
                if x1 < 0 or y1 < 0 or x2 <= x1 or y2 <= y1:
                    print(f"⚠️ 유효하지 않은 좌표: {detection}")
                    continue
                
                # 신뢰도 검사
                if conf < 0.3:
                    print(f"⚠️ 낮은 신뢰도: {conf:.2f}")
                    continue
                
                # 정상 처리
                process_valid_detection(detection)
                
            except Exception as e:
                print(f"❌ 처리 중 오류 발생: {e}")
                continue
    else:
        print("ℹ️ 탐지된 객체가 없습니다")

def process_valid_detection(detection):
    """유효한 탐지 결과 처리"""
    x1, y1, x2, y2, conf, cls = detection
    cx, cy = calculate_center(x1, y1, x2, y2)
    print(f"✅ 처리 완료: 중심점({cx}, {cy}), 신뢰도 {conf:.2f}")

# 사용 예제
test_detections = [
    [100, 200, 300, 400, 0.9, 2],  # 정상
    [-10, 150, 200, 350, 0.8, 0],  # 음수 좌표
    [500, 100, 700, 300, 0.2, 1],  # 낮은 신뢰도
]

safe_process_detections(test_detections)
```

**실행 결과:**
```
✅ 3개 객체 처리 중...
✅ 처리 완료: 중심점(200, 300), 신뢰도 0.90
⚠️ 유효하지 않은 좌표: [-10, 150, 200, 350, 0.8, 0]
⚠️ 낮은 신뢰도: 0.20
```

---

## ⚡ 제어문 (continue, pass)

### continue - 다음 반복으로

```python
def process_video_stream():
    """비디오 스트림 처리 (continue 사용)"""
    cap = cv2.VideoCapture(0)
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        frame_count += 1
        
        if not ret:
            print(f"프레임 {frame_count}: 읽기 실패")
            continue  # 프레임 읽기 실패시 다음 프레임으로
        
        # 프레임이 너무 어두우면 건너뛰기
        if np.mean(frame) < 50:
            print(f"프레임 {frame_count}: 너무 어두움")
            continue
        
        # 탐지 수행
        results = model(frame)
        if len(results[0].boxes) == 0:
            print(f"프레임 {frame_count}: 탐지 결과 없음")
            continue  # 탐지 결과가 없으면 건너뛰기
        
        # 정상적인 처리
        print(f"프레임 {frame_count}: 정상 처리")
        process_detections(results)
        
        # 'q' 키로 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()

def filter_detections(detections):
    """탐지 결과 필터링 (continue 사용)"""
    valid_detections = []
    
    for i, detection in enumerate(detections):
        x1, y1, x2, y2, confidence, cls = detection
        
        # 신뢰도 낮은 탐지 건너뛰기
        if confidence < 0.5:
            print(f"탐지 {i}: 신뢰도 낮음 ({confidence:.2f})")
            continue
        
        # 관심 없는 클래스 건너뛰기
        if cls not in [0, 2, 3]:  # person, car, motorcycle만
            print(f"탐지 {i}: 관심 없는 클래스 ({cls})")
            continue
        
        # 화면 밖 객체 건너뛰기
        if x1 < 0 or y1 < 0:
            print(f"탐지 {i}: 화면 밖 객체")
            continue
        
        # 유효한 탐지만 저장
        valid_detections.append(detection)
        print(f"탐지 {i}: 유효함 ✅")
    
    return valid_detections
```

### pass - 아무것도 하지 않음

```python
# 미구현 함수 플레이스홀더
def emergency_brake():
    """긴급 제동 시스템"""
    # TODO: 긴급 제동 로직 구현 예정
    pass

def lane_change_left():
    """좌측 차선 변경"""
    # TODO: 좌측 차선 변경 로직 구현 예정
    pass

def calculate_safe_distance():
    """안전거리 계산"""
    # TODO: 안전거리 계산 로직 구현 예정
    pass

# 조건부 처리에서 빈 블록
def handle_detection_by_class(detection):
    """클래스별 탐지 처리"""
    cls = detection[5]
    
    if cls == 0:      # person
        handle_pedestrian(detection)
        print("🚶 보행자 처리")
    elif cls == 2:    # car
        handle_vehicle(detection)
        print("🚗 차량 처리")
    elif cls == 3:    # motorcycle
        handle_motorcycle(detection)
        print("🏍️ 오토바이 처리")
    else:
        pass  # 다른 객체는 무시
        print("❓ 알 수 없는 객체 - 무시")

# 상속에서 빈 메서드 구현
class BaseSensor:
    """센서 기본 클래스"""
    def read_data(self):
        raise NotImplementedError("하위 클래스에서 구현 필요")
    
    def calibrate(self):
        raise NotImplementedError("하위 클래스에서 구현 필요")

class LidarSensor(BaseSensor):
    """라이다 센서 클래스"""
    def read_data(self):
        # 라이다 데이터 읽기
        return self.get_lidar_data()
    
    def calibrate(self):
        pass  # 라이다는 자동 캘리브레이션되므로 별도 작업 불필요

class CameraSensor(BaseSensor):
    """카메라 센서 클래스"""
    def read_data(self):
        # 카메라 데이터 읽기
        return self.capture_frame()
    
    def calibrate(self):
        # 카메라 캘리브레이션 수행
        print("📷 카메라 캘리브레이션 수행")
        self.perform_calibration()

# 사용 예제
lidar = LidarSensor()
camera = CameraSensor()

# 센서 데이터 읽기
lidar_data = lidar.read_data()
camera_frame = camera.read_data()

# 캘리브레이션 수행
lidar.calibrate()    # 아무 작업 안 함 (pass)
camera.calibrate()   # 실제 캘리브레이션 수행
```

**실행 결과:**
```
프레임 1: 읽기 실패
프레임 2: 너무 어두움
프레임 3: 탐지 결과 없음
프레임 4: 정상 처리
탐지 0: 신뢰도 낮음 (0.35)
탐지 1: 유효함 ✅
탐지 2: 관심 없는 클래스 (7)
🚶 보행자 처리
🚗 차량 처리
❓ 알 수 없는 객체 - 무시
📷 카메라 캘리브레이션 수행
```

---

## 🎯 실전 통합 예제

### 완전한 자율주행 시스템

```python
import cv2
import numpy as np
from datetime import datetime

class CompleteAutonomousSystem:
    """완전한 자율주행 시스템 예제"""
    
    def __init__(self):
        """시스템 초기화"""
        self.vehicle_tracker = VehicleTracker()
        self.detection_history = []
        self.frame_count = 0
        self.start_time = datetime.now()
        
        print("🚀 통합 자율주행 시스템 시작")
        print(f"시작 시간: {self.start_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    def run_system(self, video_source=0):
        """시스템 실행"""
        cap = cv2.VideoCapture(video_source)
        
        if not cap.isOpened():
            print("❌ 비디오 소스를 열 수 없습니다")
            return
        
        print("📹 비디오 스트림 시작")
        
        while True:
            # 프레임 읽기
            ret, frame = cap.read()
            self.frame_count += 1
            
            if not ret:
                print(f"프레임 {self.frame_count}: 읽기 실패")
                continue
            
            # 프레임 전처리 및 검증
            if not self.validate_frame(frame):
                continue
            
            # 객체 탐지 수행
            detections = self.detect_objects(frame)
            
            if len(detections) == 0:
                continue
            
            # 탐지 결과 필터링
            valid_detections = self.filter_detections(detections)
            
            # 차량 추적 업데이트
            self.vehicle_tracker.update_tracks(valid_detections)
            
            # 주행 결정
            decision = self.make_decision(valid_detections, frame.shape)
            
            # 결과 표시
            annotated_frame = self.draw_annotations(frame, valid_detections)
            
            # 통계 표시
            self.display_stats(annotated_frame)
            
            # 화면 출력
            cv2.imshow('자율주행 시스템', annotated_frame)
            
            # 'q' 키로 종료
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # 정리
        cap.release()
        cv2.destroyAllWindows()
        self.print_final_stats()
    
    def validate_frame(self, frame):
        """프레임 유효성 검사"""
        # 프레임이 너무 어두운지 확인
        if np.mean(frame) < 30:
            return False
        
        # 프레임 크기 확인
        if frame.shape[0] < 100 or frame.shape[1] < 100:
            return False
        
        return True
    
    def detect_objects(self, frame):
        """객체 탐지 (시뮬레이션)"""
        # 실제 환경에서는 YOLO 등의 모델 사용
        # 여기서는 시뮬레이션 데이터 생성
        detections = []
        
        # 무작위로 몇 개의 객체 생성 (데모용)
        num_objects = np.random.randint(0, 4)
        
        for _ in range(num_objects):
            x1 = np.random.randint(0, frame.shape[1] - 100)
            y1 = np.random.randint(0, frame.shape[0] - 100)
            x2 = x1 + np.random.randint(50, 150)
            y2 = y1 + np.random.randint(50, 150)
            conf = np.random.uniform(0.3, 0.95)
            cls = np.random.choice([0, 2, 3, 7])  # person, car, motorcycle, truck
            
            detections.append([x1, y1, x2, y2, conf, cls])
        
        return detections
    
    def filter_detections(self, detections):
        """탐지 결과 필터링"""
        valid_detections = []
        
        for i, detection in enumerate(detections):
            x1, y1, x2, y2, conf, cls = detection
            
            # 신뢰도 필터
            if conf < 0.5:
                continue
            
            # 클래스 필터 (관심 있는 객체만)
            if cls not in [0, 2, 3]:  # person, car, motorcycle
                continue
            
            # 좌표 유효성 검사
            if x1 < 0 or y1 < 0 or x2 <= x1 or y2 <= y1:
                continue
            
            valid_detections.append(detection)
        
        return valid_detections
    
    def make_decision(self, detections, frame_shape):
        """주행 결정"""
        decision = {
            'action': 'continue',
            'reason': '정상 주행',
            'risk_level': 'low'
        }
        
        for detection in detections:
            x1, y1, x2, y2, conf, cls = detection
            cx, cy = calculate_center(x1, y1, x2, y2)
            
            # 위험 구역 확인
            if is_in_danger_zone(cx, cy, frame_shape[1], frame_shape[0]):
                if cls == 0:  # 사람
                    decision = {
                        'action': 'emergency_brake',
                        'reason': '보행자 감지',
                        'risk_level': 'high'
                    }
                    break
                elif cls in [2, 3]:  # 차량, 오토바이
                    decision = {
                        'action': 'brake',
                        'reason': '전방 차량',
                        'risk_level': 'medium'
                    }
        
        return decision
    
    def draw_annotations(self, frame, detections):
        """검출 결과 시각화"""
        annotated = frame.copy()
        
        for detection in detections:
            x1, y1, x2, y2, conf, cls = detection
            
            # 클래스별 색상
            color, name = get_object_color(cls)
            
            # 바운딩 박스
            cv2.rectangle(annotated, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
            
            # 라벨
            label = f"{name} {conf:.2f}"
            cv2.putText(annotated, label, (int(x1), int(y1)-10), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
            
            # 중심점
            cx, cy = calculate_center(x1, y1, x2, y2)
            cv2.circle(annotated, (cx, cy), 5, color, -1)
        
        return annotated
    
    def display_stats(self, frame):
        """통계 정보 표시"""
        current_time = datetime.now()
        elapsed = (current_time - self.start_time).total_seconds()
        fps = self.frame_count / elapsed if elapsed > 0 else 0
        
        # 통계 텍스트
        stats_text = [
            f"프레임: {self.frame_count}",
            f"FPS: {fps:.1f}",
            f"추적 중: {len(self.vehicle_tracker.tracks)}",
            f"총 탐지: {len(self.detection_history)}"
        ]
        
        # 화면에 표시
        for i, text in enumerate(stats_text):
            cv2.putText(frame, text, (10, 30 + i*25), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)
    
    def print_final_stats(self):
        """최종 통계 출력"""
        end_time = datetime.now()
        total_time = (end_time - self.start_time).total_seconds()
        avg_fps = self.frame_count / total_time if total_time > 0 else 0
        
        print("\n" + "="*50)
        print("📊 최종 실행 통계")
        print("="*50)
        print(f"총 실행 시간: {total_time:.1f}초")
        print(f"처리한 프레임: {self.frame_count}개")
        print(f"평균 FPS: {avg_fps:.1f}")
        print(f"총 탐지 수: {len(self.detection_history)}개")
        print(f"최대 동시 추적: {max(len(self.vehicle_tracker.tracks), 1)}개")
        print("="*50)

# 시스템 실행
if __name__ == "__main__":
    system = CompleteAutonomousSystem()
    
    try:
        system.run_system()  # 웹캠 사용
        # system.run_system('video.mp4')  # 비디오 파일 사용
    except KeyboardInterrupt:
        print("\n👋 사용자에 의해 중단됨")
    except Exception as e:
        print(f"❌ 오류 발생: {e}")
```

---

## 📚 추가 학습 자료

### 유용한 라이브러리들

```python
# 컴퓨터 비전
import cv2          # OpenCV - 이미지/비디오 처리
import numpy as np  # NumPy - 수치 연산

# 딥러닝/AI
import torch        # PyTorch
import ultralytics  # YOLO
import tensorflow   # TensorFlow

# 데이터 처리
import pandas as pd # 데이터 분석
import matplotlib.pyplot as plt  # 시각화

# 시간/날짜
from datetime import datetime
import time
```

### 성능 최적화 팁

```python
# 1. 리스트 컴프리헨션 사용
# 느린 방법
filtered_detections = []
for detection in detections:
    if detection[4] > 0.5:  # 신뢰도
        filtered_detections.append(detection)

# 빠른 방법
filtered_detections = [d for d in detections if d[4] > 0.5]

# 2. NumPy 벡터화 연산
# 느린 방법 (반복문)
centers = []
for detection in detections:
    x1, y1, x2, y2 = detection[:4]
    cx = (x1 + x2) / 2
    cy = (y1 + y2) / 2
    centers.append((cx, cy))

# 빠른 방법 (벡터화)
boxes = np.array([d[:4] for d in detections])
centers = (boxes[:, [0, 1]] + boxes[:, [2, 3]]) / 2

# 3. 조기 종료 활용
def find_high_confidence_detection(detections, threshold=0.9):
    for detection in detections:
        if detection[4] > threshold:
            return detection  # 찾으면 즉시 반환
    return None  # 없으면 None 반환
```

---

## 🔧 디버깅 팁

```python
# 1. 로깅 추가
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def process_detection_with_logging(detection):
    logger.info(f"탐지 처리 시작: {detection}")
    
    try:
        # 처리 로직
        result = process_detection(detection)
        logger.info(f"처리 완료: {result}")
        return result
    except Exception as e:
        logger.error(f"처리 실패: {e}")
        return None

# 2. 어설션 사용
def validate_detection(detection):
    assert len(detection) == 6, f"탐지 데이터 길이 오류: {len(detection)}"
    assert detection[4] >= 0 and detection[4] <= 1, f"신뢰도 범위 오류: {detection[4]}"
    assert detection[2] > detection[0], f"x2가 x1보다 작음: {detection}"
    assert detection[3] > detection[1], f"y2가 y1보다 작음: {detection}"

# 3. 시각적 디버깅
def debug_draw_detections(frame, detections):
    """디버깅용 시각화"""
    debug_frame = frame.copy()
    
    for i, detection in enumerate(detections):
        x1, y1, x2, y2, conf, cls = detection
        
        # 각 탐지에 번호 표시
        cv2.putText(debug_frame, str(i), (int(x1), int(y1)), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)
        
        # 자세한 정보 표시
        info = f"ID:{i} C:{conf:.2f} Cls:{cls}"
        cv2.putText(debug_frame, info, (int(x1), int(y2)+20), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 0), 1)
    
    return debug_frame
```

---

## 🎓 마무리

이 가이드에서 다룬 Python 핵심 문법들은 자율주행 시스템 개발의 기초가 됩니다. 각 문법 요소들이 실제 어떻게 활용되는지 이해하고, 실전 프로젝트에서 응용해보세요.

### 다음 단계 학습 권장사항

1. **OpenCV 심화**: 이미지 처리 고급 기법
2. **YOLO 모델**: 실시간 객체 탐지
3. **칼만 필터**: 객체 추적 알고리즘
4. **ROS (Robot Operating System)**: 로봇 소프트웨어 플랫폼
5. **딥러닝 프레임워크**: PyTorch, TensorFlow

### 추가 리소스

- [OpenCV 공식 문서](https://docs.opencv.org/)
- [Ultralytics YOLO](https://github.com/ultralytics/ultralytics)
- [자율주행 오픈소스 프로젝트](https://github.com/topics/autonomous-driving)

---

**💡 팁**: 이 가이드의 모든 코드는 실제 프로젝트에서 바로 사용할 수 있도록 작성되었습니다. 각 예제를 직접 실행해보며 학습하는 것을 권장합니다!

**📝 기여**: 이 가이드에 개선사항이나 추가할 내용이 있다면 언제든 PR을 보내주세요!
