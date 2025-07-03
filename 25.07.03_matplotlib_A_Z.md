# 📊 Matplotlib 자율주행 시각화 완벽 가이드

## 🎯 시각화가 자율주행에서 중요한 이유

자율주행 시스템을 개발할 때 가장 중요한 것 중 하나는 **데이터를 눈으로 직접 확인**하는 것입니다. 센서에서 들어오는 수많은 숫자들을 그래프와 그림으로 변환하면, 우리는 차량이 주변 환경을 어떻게 인식하고 있는지 한눈에 파악할 수 있습니다.

예를 들어, LiDAR 센서가 수집한 수천 개의 포인트들을 단순히 숫자로만 보면 아무것도 이해할 수 없지만, 3D 산점도로 그려보면 앞에 있는 차량이나 보행자를 즉시 식별할 수 있습니다. 이것이 바로 Matplotlib이 자율주행 개발에서 핵심적인 역할을 하는 이유입니다.

---

## 📌 목차

- [환경 설정](#-환경-설정)
- [기본 그래프 작성](#1-기본-그래프-작성-센서-데이터-시각화)
- [센서 데이터 시각화](#2-센서-데이터-전용-시각화)
- [실시간 데이터 처리](#3-실시간-데이터-시각화)
- [고급 시각화 기법](#4-고급-시각화-기법)
- [자율주행 실전 예제](#5-자율주행-실전-시각화-예제)
- [성능 최적화](#6-성능-최적화-및-실용-팁)
- [마무리](#-마무리)

---

## 🛠 환경 설정

자율주행 시각화를 위해 필요한 라이브러리들을 설치해보겠습니다. 각 라이브러리는 특별한 역할을 담당합니다.

```bash
# 핵심 시각화 라이브러리
pip install matplotlib numpy

# 추가 유용한 라이브러리들
pip install seaborn pandas  # 더 아름다운 그래프와 데이터 처리
pip install pillow          # 이미지 처리
```

이제 개발 환경을 설정해보겠습니다. 주피터 노트북을 사용한다면 다음 명령어를 실행하면 그래프가 노트북 내부에 바로 표시됩니다.

```python
# 주피터 노트북에서 그래프를 바로 보기 위한 설정
%matplotlib inline

# 필요한 라이브러리 임포트
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.animation import FuncAnimation
import seaborn as sns

# 한글 폰트 설정 (한국어 제목과 라벨 사용을 위해)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# 그래프 품질 향상을 위한 설정
plt.rcParams['figure.dpi'] = 100
plt.rcParams['savefig.dpi'] = 300
```

---

## 1. 기본 그래프 작성: 센서 데이터 시각화

자율주행 시스템에서 가장 기본이 되는 것은 시간에 따른 센서 값의 변화를 추적하는 것입니다. 차량의 속도, 조향각, 가속도 등이 시간에 따라 어떻게 변하는지 살펴보겠습니다.

### 1.1 차량 주행 데이터 시각화

```python
# 시뮬레이션된 차량 주행 데이터 생성
# 실제 자율주행 시스템에서는 이 데이터들이 센서와 ECU에서 실시간으로 들어옵니다
time_seconds = np.linspace(0, 60, 300)  # 1분간 0.2초 간격으로 데이터 수집
vehicle_speed = 30 + 10 * np.sin(time_seconds * 0.1) + np.random.normal(0, 1, 300)  # km/h
steering_angle = 15 * np.sin(time_seconds * 0.05) + np.random.normal(0, 2, 300)     # 도
acceleration = np.gradient(vehicle_speed) * 5 + np.random.normal(0, 0.5, 300)      # m/s²

# 그래프 생성: 하나의 창에 여러 그래프를 배치
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))

# 첫 번째 그래프: 차량 속도
ax1.plot(time_seconds, vehicle_speed, 'b-', linewidth=2, alpha=0.8, label='차량 속도')
ax1.set_ylabel('속도 (km/h)', fontsize=12)
ax1.set_title('자율주행 차량 주행 데이터 분석', fontsize=14, fontweight='bold')
ax1.grid(True, alpha=0.3)
ax1.legend()

# 두 번째 그래프: 조향각
ax2.plot(time_seconds, steering_angle, 'r-', linewidth=2, alpha=0.8, label='조향각')
ax2.set_ylabel('조향각 (도)', fontsize=12)
ax2.grid(True, alpha=0.3)
ax2.legend()

# 세 번째 그래프: 가속도
ax3.plot(time_seconds, acceleration, 'g-', linewidth=2, alpha=0.8, label='가속도')
ax3.set_xlabel('시간 (초)', fontsize=12)
ax3.set_ylabel('가속도 (m/s²)', fontsize=12)
ax3.grid(True, alpha=0.3)
ax3.legend()

# 그래프 간격 조정
plt.tight_layout()
plt.show()
```

이 코드를 실행하면 차량의 주행 상태를 한눈에 파악할 수 있는 세 개의 그래프가 세로로 정렬되어 나타납니다. 각 그래프는 서로 다른 색상을 사용하여 구분하기 쉽게 만들었습니다.

### 1.2 산점도로 상관관계 분석

자율주행에서는 여러 센서 데이터 간의 상관관계를 파악하는 것이 중요합니다. 예를 들어, 속도와 조향각의 관계를 보면 안전한 주행 패턴을 분석할 수 있습니다.

```python
# 속도와 조향각의 상관관계 분석
plt.figure(figsize=(10, 6))

# 산점도 생성: 각 점은 특정 시점의 속도와 조향각을 나타냄
scatter = plt.scatter(vehicle_speed, np.abs(steering_angle), 
                     c=acceleration, cmap='viridis', alpha=0.6, s=30)

# 컬러바 추가: 가속도를 색상으로 표현
colorbar = plt.colorbar(scatter)
colorbar.set_label('가속도 (m/s²)', fontsize=12)

plt.xlabel('차량 속도 (km/h)', fontsize=12)
plt.ylabel('조향각 절댓값 (도)', fontsize=12)
plt.title('속도-조향각 상관관계 분석 (가속도별 색상 구분)', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)

# 추세선 추가
z = np.polyfit(vehicle_speed, np.abs(steering_angle), 1)
p = np.poly1d(z)
plt.plot(vehicle_speed, p(vehicle_speed), "r--", alpha=0.8, linewidth=2, label='추세선')
plt.legend()

plt.tight_layout()
plt.show()
```

이 산점도를 통해 우리는 흥미로운 패턴을 발견할 수 있습니다. 일반적으로 속도가 높을 때는 조향각이 작아지는 경향이 있는데, 이는 고속 주행 시 안전을 위해 급격한 조향을 피하는 자율주행 알고리즘의 특성을 반영합니다.

---

## 2. 센서 데이터 전용 시각화

자율주행 차량의 핵심은 다양한 센서들입니다. 각 센서의 특성에 맞는 시각화 방법을 살펴보겠습니다.

### 2.1 LiDAR 데이터 시각화

LiDAR는 레이저를 사용하여 주변 환경의 3차원 포인트 클라우드를 생성합니다. 이 데이터를 효과적으로 시각화하는 방법을 알아보겠습니다.

```python
# LiDAR 포인트 클라우드 시뮬레이션
# 실제 LiDAR에서는 수만 개의 포인트가 생성되지만, 여기서는 이해를 위해 간단히 구현
np.random.seed(42)  # 재현 가능한 결과를 위한 시드 설정

# 차량 앞쪽 180도 스캔 영역 시뮬레이션
angles = np.linspace(-np.pi/2, np.pi/2, 180)  # -90도에서 90도까지
distances = 10 + 5 * np.sin(angles * 3) + np.random.normal(0, 0.5, 180)  # 기본 거리 + 노이즈

# 극좌표를 직교좌표로 변환
x_coords = distances * np.cos(angles)
y_coords = distances * np.sin(angles)

# 일부 포인트에 장애물 추가 (예: 앞쪽 차량)
obstacle_indices = np.where((np.abs(angles) < 0.3) & (distances < 8))
distances[obstacle_indices] = 3 + np.random.normal(0, 0.1, len(obstacle_indices[0]))

# 업데이트된 좌표 계산
x_coords = distances * np.cos(angles)
y_coords = distances * np.sin(angles)

# LiDAR 데이터 시각화
plt.figure(figsize=(12, 8))

# 포인트 클라우드 그리기
plt.scatter(x_coords, y_coords, c=distances, cmap='plasma', s=20, alpha=0.8)
plt.colorbar(label='거리 (m)')

# 차량 위치 표시 (원점)
plt.plot(0, 0, 'ro', markersize=10, label='차량 위치')

# 스캔 범위 표시
scan_range = 15
plt.plot([0, scan_range * np.cos(-np.pi/2)], [0, scan_range * np.sin(-np.pi/2)], 'k--', alpha=0.5)
plt.plot([0, scan_range * np.cos(np.pi/2)], [0, scan_range * np.sin(np.pi/2)], 'k--', alpha=0.5)

plt.xlabel('X 좌표 (m)', fontsize=12)
plt.ylabel('Y 좌표 (m)', fontsize=12)
plt.title('LiDAR 포인트 클라우드 시각화', fontsize=14, fontweight='bold')
plt.axis('equal')  # 축 비율을 1:1로 맞춤
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()
```

이 시각화를 통해 차량 앞쪽에 있는 장애물의 위치와 거리를 명확히 확인할 수 있습니다. 색상이 진할수록 가까운 객체를 나타냅니다.

### 2.2 카메라 이미지와 객체 검출 결과

자율주행 시스템에서 카메라는 차선, 표지판, 다른 차량 등을 인식하는 데 사용됩니다. 객체 검출 결과를 원본 이미지 위에 표시하는 방법을 살펴보겠습니다.

```python
# 가상의 카메라 이미지와 객체 검출 결과 시뮬레이션
def create_mock_camera_image():
    """가상의 도로 이미지 생성"""
    # 640x480 크기의 기본 이미지 (하늘색 배경)
    image = np.ones((480, 640, 3)) * 0.7
    
    # 도로 영역 (회색)
    image[300:480, :] = [0.4, 0.4, 0.4]
    
    # 차선 (흰색)
    image[350:360, 100:150] = [1.0, 1.0, 1.0]  # 왼쪽 차선
    image[350:360, 490:540] = [1.0, 1.0, 1.0]  # 오른쪽 차선
    
    # 앞차 시뮬레이션 (빨간색 사각형)
    image[250:320, 280:360] = [0.8, 0.2, 0.2]
    
    return image

# 검출된 객체 정보 (실제로는 YOLO, SSD 등의 알고리즘에서 생성)
detected_objects = [
    {'name': '차량', 'bbox': [280, 250, 80, 70], 'confidence': 0.95},
    {'name': '차선', 'bbox': [100, 350, 50, 10], 'confidence': 0.88},
    {'name': '차선', 'bbox': [490, 350, 50, 10], 'confidence': 0.91}
]

# 이미지 생성 및 시각화
image = create_mock_camera_image()

plt.figure(figsize=(12, 8))
plt.imshow(image)

# 검출된 객체에 바운딩 박스 그리기
for obj in detected_objects:
    x, y, w, h = obj['bbox']
    confidence = obj['confidence']
    name = obj['name']
    
    # 바운딩 박스 그리기
    rect = plt.Rectangle((x, y), w, h, linewidth=2, 
                        edgecolor='yellow', facecolor='none')
    plt.gca().add_patch(rect)
    
    # 객체 이름과 신뢰도 표시
    plt.text(x, y-5, f'{name} ({confidence:.2f})', 
             bbox=dict(boxstyle="round,pad=0.3", facecolor='yellow', alpha=0.7),
             fontsize=10, color='black')

plt.title('자율주행 카메라 객체 검출 결과', fontsize=14, fontweight='bold')
plt.axis('off')  # 축 숨기기
plt.tight_layout()
plt.show()
```

이 시각화를 통해 자율주행 시스템이 카메라 이미지에서 어떤 객체들을 인식했는지, 그리고 각 인식 결과의 신뢰도가 얼마나 되는지 한눈에 확인할 수 있습니다.

### 2.3 GPS 경로 시각화

GPS 데이터를 지도상에 표시하여 차량의 이동 경로를 시각화하는 것은 자율주행 시스템의 성능을 평가하는 데 매우 중요합니다.

```python
# 가상의 GPS 경로 데이터 생성
# 실제로는 차량의 GPS 수신기에서 이 데이터가 들어옵니다
def generate_gps_path():
    """곡선 경로를 포함한 GPS 좌표 생성"""
    t = np.linspace(0, 4*np.pi, 100)
    
    # 기본 좌표 (서울 시청 근처로 가정)
    base_lat = 37.5665
    base_lon = 126.9780
    
    # 곡선 경로 생성 (실제 도로를 따라 이동하는 패턴)
    lat_offset = 0.01 * np.sin(t * 0.5) + 0.002 * np.random.normal(0, 1, 100)
    lon_offset = 0.01 * t / (4*np.pi) + 0.002 * np.random.normal(0, 1, 100)
    
    latitudes = base_lat + lat_offset
    longitudes = base_lon + lon_offset
    
    return latitudes, longitudes

# GPS 경로 데이터 생성
lats, lons = generate_gps_path()

# 시간별 속도 데이터 (색상 표현용)
speeds = 20 + 15 * np.sin(np.linspace(0, 2*np.pi, 100)) + np.random.normal(0, 3, 100)

# GPS 경로 시각화
plt.figure(figsize=(14, 10))

# 경로를 속도별로 색상 구분하여 표시
scatter = plt.scatter(lons, lats, c=speeds, cmap='RdYlBu_r', s=30, alpha=0.8)
plt.colorbar(scatter, label='속도 (km/h)')

# 경로 연결선 그리기
plt.plot(lons, lats, 'k-', alpha=0.3, linewidth=1)

# 시작점과 끝점 표시
plt.plot(lons[0], lats[0], 'go', markersize=10, label='시작점')
plt.plot(lons[-1], lats[-1], 'ro', markersize=10, label='끝점')

# 중요한 지점들 표시 (예: 급감속 지점)
slow_points = np.where(speeds < 15)[0]
if len(slow_points) > 0:
    plt.scatter(lons[slow_points], lats[slow_points], 
                c='red', s=80, marker='x', label='급감속 지점')

plt.xlabel('경도 (Longitude)', fontsize=12)
plt.ylabel('위도 (Latitude)', fontsize=12)
plt.title('자율주행 차량 GPS 경로 분석', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.legend()

# 축 비율을 지리적으로 정확하게 맞춤
plt.axis('equal')
plt.tight_layout()
plt.show()
```

이 시각화를 통해 차량이 어떤 경로로 이동했는지, 어느 구간에서 속도가 변했는지 명확히 파악할 수 있습니다. 급감속 지점이 표시되어 있어 위험한 상황이 발생했던 위치를 쉽게 식별할 수 있습니다.

---

## 3. 실시간 데이터 시각화

자율주행 시스템에서는 센서 데이터가 실시간으로 들어오기 때문에, 이를 실시간으로 시각화하는 기술이 매우 중요합니다.

### 3.1 실시간 센서 데이터 모니터링

```python
# 실시간 데이터 시각화를 위한 클래스 정의
class RealTimeMonitor:
    def __init__(self):
        self.fig, (self.ax1, self.ax2) = plt.subplots(2, 1, figsize=(12, 8))
        
        # 데이터 저장용 리스트
        self.time_data = []
        self.speed_data = []
        self.steering_data = []
        
        # 그래프 초기화
        self.speed_line, = self.ax1.plot([], [], 'b-', linewidth=2)
        self.steering_line, = self.ax2.plot([], [], 'r-', linewidth=2)
        
        # 축 설정
        self.ax1.set_xlim(0, 50)
        self.ax1.set_ylim(0, 80)
        self.ax1.set_ylabel('속도 (km/h)')
        self.ax1.set_title('실시간 차량 상태 모니터링')
        self.ax1.grid(True, alpha=0.3)
        
        self.ax2.set_xlim(0, 50)
        self.ax2.set_ylim(-30, 30)
        self.ax2.set_ylabel('조향각 (도)')
        self.ax2.set_xlabel('시간 (초)')
        self.ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        
    def update_data(self, current_time, speed, steering):
        """새로운 데이터 포인트 추가"""
        self.time_data.append(current_time)
        self.speed_data.append(speed)
        self.steering_data.append(steering)
        
        # 최근 50초 데이터만 유지
        if len(self.time_data) > 250:  # 0.2초 간격이므로 50초 = 250개
            self.time_data.pop(0)
            self.speed_data.pop(0)
            self.steering_data.pop(0)
            
        # 그래프 업데이트
        self.speed_line.set_data(self.time_data, self.speed_data)
        self.steering_line.set_data(self.time_data, self.steering_data)
        
        # 축 범위 자동 조정
        if len(self.time_data) > 0:
            self.ax1.set_xlim(max(0, self.time_data[-1] - 50), self.time_data[-1] + 5)
            self.ax2.set_xlim(max(0, self.time_data[-1] - 50), self.time_data[-1] + 5)
        
        plt.draw()
        plt.pause(0.01)

# 실시간 모니터링 시뮬레이션
monitor = RealTimeMonitor()

# 실시간 데이터 시뮬레이션 (실제로는 센서에서 데이터가 들어옴)
for i in range(100):
    current_time = i * 0.5
    
    # 가상의 센서 데이터 생성
    speed = 40 + 20 * np.sin(current_time * 0.1) + np.random.normal(0, 2)
    steering = 15 * np.sin(current_time * 0.05) + np.random.normal(0, 3)
    
    monitor.update_data(current_time, speed, steering)

plt.show()
```

이 실시간 모니터링 시스템을 통해 차량의 상태를 실시간으로 추적할 수 있습니다. 그래프는 자동으로 스크롤되면서 최신 데이터를 보여줍니다.

### 3.2 대시보드 형태의 종합 모니터링

```python
# 자율주행 차량 대시보드 시각화
def create_dashboard():
    """종합 모니터링 대시보드 생성"""
    fig = plt.figure(figsize=(16, 10))
    
    # 그리드 레이아웃 설정
    gs = fig.add_gridspec(3, 3, hspace=0.3, wspace=0.3)
    
    # 현재 상태 데이터 (실제로는 실시간으로 업데이트됨)
    current_speed = 45.2
    current_steering = -12.5
    battery_level = 78
    engine_temp = 85
    
    # 1. 속도계 (게이지 형태)
    ax1 = fig.add_subplot(gs[0, 0])
    angles = np.linspace(0, np.pi, 100)
    speed_angle = np.pi * (current_speed / 80)  # 최대 80km/h
    
    ax1.plot(np.cos(angles), np.sin(angles), 'k-', linewidth=3)
    ax1.plot([0, np.cos(speed_angle)], [0, np.sin(speed_angle)], 'r-', linewidth=4)
    ax1.set_xlim(-1.2, 1.2)
    ax1.set_ylim(-0.2, 1.2)
    ax1.set_aspect('equal')
    ax1.set_title(f'속도: {current_speed:.1f} km/h', fontsize=12, fontweight='bold')
    ax1.axis('off')
    
    # 2. 조향각 표시
    ax2 = fig.add_subplot(gs[0, 1])
    steering_visual = np.zeros((10, 20))
    center_col = 10
    steering_col = int(center_col + current_steering / 5)  # 조향각을 픽셀로 변환
    steering_col = max(0, min(19, steering_col))
    steering_visual[:, steering_col] = 1
    
    ax2.imshow(steering_visual, cmap='RdYlBu_r', aspect='auto')
    ax2.set_title(f'조향각: {current_steering:.1f}°', fontsize=12, fontweight='bold')
    ax2.set_xticks([])
    ax2.set_yticks([])
    
    # 3. 배터리 상태
    ax3 = fig.add_subplot(gs[0, 2])
    battery_colors = ['red' if battery_level < 20 else 'yellow' if battery_level < 50 else 'green']
    ax3.bar(['배터리'], [battery_level], color=battery_colors[0], alpha=0.7)
    ax3.set_ylim(0, 100)
    ax3.set_title(f'배터리: {battery_level}%', fontsize=12, fontweight='bold')
    ax3.set_ylabel('충전량 (%)')
    
    # 4. 최근 경로 (GPS 트래킹)
    ax4 = fig.add_subplot(gs[1, :])
    
    # 가상의 최근 경로 데이터
    recent_x = np.linspace(0, 100, 50) + np.random.normal(0, 2, 50)
    recent_y = 10 * np.sin(recent_x * 0.1) + np.random.normal(0, 1, 50)
    
    ax4.plot(recent_x, recent_y, 'b-', linewidth=2, alpha=0.7)
    ax4.scatter(recent_x[-1], recent_y[-1], c='red', s=100, label='현재 위치')
    ax4.set_title('최근 주행 경로', fontsize=12, fontweight='bold')
    ax4.set_xlabel('X 좌표 (m)')
    ax4.set_ylabel('Y 좌표 (m)')
    ax4.grid(True, alpha=0.3)
    ax4.legend()
    
    # 5. 센서 상태 히트맵
    ax5 = fig.add_subplot(gs[2, 0])
    sensor_status = np.random.rand(4, 4)  # 4x4 센서 그리드
    sensor_names = ['LiDAR', 'Camera', 'Radar', 'GPS']
    
    im = ax5.imshow(sensor_status, cmap='RdYlGn', aspect='auto')
    ax5.set_title('센서 상태', fontsize=12, fontweight='bold')
    ax5.set_xticks(range(4))
    ax5.set_yticks(range(4))
    ax5.set_xticklabels(['A', 'B', 'C', 'D'])
    ax5.set_yticklabels(sensor_names)
    
