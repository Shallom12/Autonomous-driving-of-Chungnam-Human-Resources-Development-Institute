# 🚗 자율주행 개발을 위한 Python 핵심 문법 가이드

> 자율주행 시스템 개발에서 가장 많이 사용되는 Python 문법들을 실제 예시와 함께 정리한 가이드입니다.

## 📋 목차

- [반복문 (Loops)](#반복문-loops)
- [배열 처리 (Array Processing)](#배열-처리-array-processing)
- [함수 정의 (Function Definition)](#함수-정의-function-definition)
- [클래스 정의 (Class Definition)](#클래스-정의-class-definition)
- [조건문 활용 (Conditional Statements)](#조건문-활용-conditional-statements)
- [제어문 (Control Statements)](#제어문-control-statements)
- [예외 처리 (Exception Handling)](#예외-처리-exception-handling)

---

## 🔄 반복문 (Loops)

### 실시간 비디오 처리 - while 루프

실시간으로 카메라에서 영상을 받아와 객체를 탐지하는 메인 루프입니다.

```python
# 기본 비디오 처리 루프
while True:
    ret, frame = cap.read()          # 카메라에서 프레임 읽기
    if not ret:                      # 프레임 읽기 실패시 종료
        break
    
    results = model(frame)           # AI 모델로 객체 탐지
    cv2.imshow('frame', frame)       # 화면에 출력
    
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 'q' 키 누르면 종료
        break
```

### 탐지 결과 처리 - for 루프

AI 모델이 탐지한 객체들을 하나씩 처리하는 방법들입니다.

```python
# 각 탐지 결과 순회
for result in results:
    boxes = result.boxes
    for i, box in enumerate(boxes):
        x1, y1, x2, y2 = box.xyxy[0]    # 바운딩 박스 좌표
        conf = box.conf[0]              # 신뢰도
        cls = box.cls[0]                # 클래스 (차량, 사람 등)
```

```python
# 좌표 배열 순회 - 더 간단한 방법
for i, (x1, y1, x2, y2) in enumerate(boxes):
    cv2.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
```

```python
# range로 인덱스 접근 - 조건부 처리할 때 유용
for i in range(len(boxes)):
    if conf[i] > 0.5:               # 신뢰도 50% 이상만 처리
        # 처리 로직
        pass
```

---

## 📊 배열 처리 (Array Processing)

### 기본 배열 조작

자율주행에서 탐지 결과나 트래킹 히스토리를 관리할 때 사용하는 배열 처리 방법들입니다.

```python
# 빈 리스트 생성
detections = []                      # 탐지 결과 저장
track_history = []                   # 객체 이동 경로 저장

# 배열에 추가
detections.append([x1, y1, x2, y2, conf, cls])  # 탐지 정보 추가
track_history.append((cx, cy))                   # 중심점 좌표 추가

# 배열 길이 제한 (최근 N개만 유지) - 메모리 효율성
if len(track_history) > 30:
    track_history.pop(0)             # 가장 오래된 데이터 제거

# 배열 슬라이싱 - 최근 데이터만 분석
recent_points = track_history[-10:]  # 최근 10개 포인트
```

---

## ⚙️ 함수 정의 (Function Definition)

### 차선 검출 함수

복잡한 이미지 처리 로직을 재사용 가능한 함수로 만드는 예시입니다.

```python
def detect_lane_lines(img, roi_vertices, canny_low, canny_high, hough_threshold):
    """
    차선 검출 함수
    
    Args:
        img: 입력 이미지
        roi_vertices: 관심 영역 좌표 [(x1,y1), (x2,y2), ...]
        canny_low: Canny 엣지 검출 하위 임계값
        canny_high: Canny 엣지 검출 상위 임계값
        hough_threshold: Hough 변환 임계값
    
    Returns:
        차선이 그려진 이미지
    """
    # 차선 검출 로직 구현
    pass
```

#### 🔍 함수 인자 상세 설명

1. **img**: 차선을 검출할 입력 이미지
2. **roi_vertices**: 관심 영역(ROI) 좌표들 - 도로 부분만 집중 분석
3. **canny_low**: Canny 엣지 검출의 하위 임계값 - 약한 엣지 감지
4. **canny_high**: Canny 엣지 검출의 상위 임계값 - 강한 엣지 감지
5. **hough_threshold**: Hough 변환 임계값 - 직선 검출 민감도

### 객체 필터링 함수

원하는 종류의 객체만 골라내는 실용적인 함수입니다.

```python
def filter_by_class(boxes, conf, cls, target_classes):
    """
    특정 클래스의 객체만 골라내는 필터 함수
    우리가 원하는 물체만 골라내는 역할을 합니다.
    """
    filtered_boxes = []              # 선택된 물체들의 위치 저장
    filtered_conf = []               # 선택된 물체들의 신뢰도 저장
    
    for i, c in enumerate(cls):      # 각 클래스를 하나씩 검사
        if c in target_classes:      # 원하는 클래스인지 확인
            filtered_boxes.append(boxes[i])
            filtered_conf.append(conf[i])
    
    return filtered_boxes, filtered_conf
```

### 유틸리티 함수들

```python
def calculate_center(x1, y1, x2, y2):
    """바운딩 박스의 중심점 계산"""
    return int((x1 + x2) / 2), int((y1 + y2) / 2)

def is_in_danger_zone(cx, cy, img_width, img_height):
    """객체가 위험 구역에 있는지 판단"""
    return (cy > img_height * 0.7 and 
            cx > img_width * 0.3 and 
            cx < img_width * 0.7)
```

---

## 🏗️ 클래스 정의 (Class Definition)

### 차량 추적 클래스

여러 프레임에 걸쳐 동일한 객체를 추적하는 클래스입니다.

```python
class VehicleTracker:
    def __init__(self):
        """초기화 - 추적 시스템 설정"""
        self.tracks = {}             # 추적 중인 객체들 {id: 위치정보}
        self.next_id = 0             # 다음에 할당할 ID
        self.max_disappeared = 10    # 몇 프레임 사라지면 추적 중단
    
    def update_tracks(self, detections):
        """새로운 탐지 결과로 추적 정보 업데이트"""
        for detection in detections:
            track_id = self.find_closest_track(detection)
            if track_id is None:
                self.create_new_track(detection)    # 새 객체 추적 시작
            else:
                self.update_existing_track(track_id, detection)  # 기존 추적 업데이트
```

### 자율주행 메인 클래스

전체 자율주행 시스템을 관리하는 메인 클래스입니다.

```python
class AutonomousDriving:
    def __init__(self):
        self.tracker = VehicleTracker()
        
    def process_frame(self, frame):
        """한 프레임을 처리하고 주행 결정을 내림"""
        detections = self.detect_objects(frame)      # 객체 탐지
        self.tracker.update_tracks(detections)       # 객체 추적
        decision = self.make_driving_decision(detections)  # 주행 결정
        return decision

    def make_driving_decision(self, detections):
        """탐지 결과를 바탕으로 주행 결정"""
        if self.obstacle_ahead(detections):
            return "brake"                           # 앞에 장애물 → 제동
        elif self.lane_change_needed(detections):
            return "change_lane"                     # 차선 변경 필요
        else:
            return "continue"                        # 직진 계속
```

---

## 🎯 조건문 활용 (Conditional Statements)

### 다중 조건 처리

객체 타입에 따라 다른 색상으로 표시하는 예시입니다.

```python
# 객체 타입별 처리
if cls == 0:           # person (사람)
    color = (0, 255, 0)     # 초록색
elif cls == 2:         # car (자동차)
    color = (255, 0, 0)     # 빨간색
elif cls == 3:         # motorcycle (오토바이)
    color = (0, 0, 255)     # 파란색
else:
    color = (128, 128, 128) # 회색 (기타)
```

### 영역별 처리

화면을 3등분하여 객체가 어느 영역에 있는지 판단합니다.

```python
# 영역별 처리
if center_x < img.shape[1] // 3:
    zone = "left"                    # 좌측 영역
elif center_x > img.shape[1] * 2 // 3:
    zone = "right"                   # 우측 영역
else:
    zone = "center"                  # 중앙 영역
```

### 복합 조건

여러 조건을 동시에 만족하는 중요한 객체를 선별합니다.

```python
# 복합 조건 - 중요한 객체 선별
if (conf > 0.7 and                          # 높은 신뢰도
    cls in [0, 2, 3] and                     # 특정 클래스 (사람, 차량, 오토바이)
    y2 > img.shape[0] * 0.5):               # 화면 하단 (가까운 거리)
    
    important_objects.append([x1, y1, x2, y2])  # 중요 객체로 분류
```

---

## 🎮 제어문 (Control Statements)

### continue - 다음 반복으로

조건에 맞지 않는 경우 현재 반복을 건너뛰고 다음으로 넘어갑니다.

```python
# 프레임 처리에서 continue 사용
while True:
    ret, frame = cap.read()
    if not ret:
        continue                    # 프레임 읽기 실패시 다음 프레임으로
    
    # 프레임이 너무 어두우면 건너뛰기
    if np.mean(frame) < 50:
        continue
    
    # 탐지 결과가 없으면 건너뛰기
    results = model(frame)
    if len(results[0].boxes) == 0:
        continue
    
    # 정상적인 처리
    process_detections(results)
```

```python
# 탐지 결과 필터링에서 continue 사용
for i, detection in enumerate(detections):
    confidence = detection.conf
    if confidence < 0.5:
        continue                    # 신뢰도가 낮으면 건너뛰기
    
    # 관심 없는 클래스 건너뛰기
    if detection.cls not in [0, 2, 3]:    # person, car, motorcycle만
        continue
    
    # 화면 밖 객체 건너뛰기
    if detection.x1 < 0 or detection.y1 < 0:
        continue
    
    process_valid_detection(detection)    # 유효한 탐지만 처리
```

pass - 아무것도 하지 않음
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
실행 결과:
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

🎯 실전 통합 예제
완전한 자율주행 시스템
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

📚 추가 학습 자료
유용한 라이브러리들
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
성능 최적화 팁
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

🔧 디버깅 팁
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

🎓 마무리
이 가이드에서 다룬 Python 핵심 문법들은 자율주행 시스템 개발의 기초가 됩니다. 각 문법 요소들이 실제 어떻게 활용되는지 이해하고, 실전 프로젝트에서 응용해보세요.
다음 단계 학습 권장사항
1. OpenCV 심화: 이미지 처리 고급 기법
2. YOLO 모델: 실시간 객체 탐지
3. 칼만 필터: 객체 추적 알고리즘
4. ROS (Robot Operating System): 로봇 소프트웨어 플랫폼
5. 딥러닝 프레임워크: PyTorch, TensorFlow
추가 리소스
* OpenCV 공식 문서
* Ultralytics YOLO
* 자율주행 오픈소스 프로젝트

---
