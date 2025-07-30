
### 📚 강의 개요 (README)
이 저장소는 자율주행 AI의 핵심 기술 중 하나인 '객체 탐지(Object Detection)'를 실제 코드를 통해 깊이 있게 학습하기 위해 만들어졌습니다. 우리는 세계적인 AI 기업 **NVIDIA**가 제공하는 고성능 모델인 **PeopleNet**을 활용하여, 복잡한 환경 속에서 사람, 가방, 얼굴을 실시간으로 탐지하는 파이프라인을 구축해볼 것입니다.

본 문서는 단순히 코드만 제공하는 것이 아니라, **왜(Why)** 이런 절차를 거치는지, 각 코드 라인이 **무엇을(What)** 의미하는지, 그리고 이 기술이 자율주행 시스템에서 **어떻게(How)** 활용되는지에 대한 깊이 있는 통찰을 제공하는 것을 목표로 합니다.

#### 💡 학습 목표
1.  **NVIDIA NGC와 TAO Toolkit 생태계 이해:** 클라우드에서 사전 훈련된(pre-trained) AI 모델을 다운로드하고 활용하는 방법을 배웁니다.
2.  **ONNX 모델과 Inference Runtime:** 특정 딥러닝 프레임워크에 종속되지 않는 표준 모델 형식(ONNX)과 이를 실행하는 `onnxruntime`의 중요성을 이해합니다.
3.  **객체 탐지 파이프라인의 전체 흐름 파악:** 데이터 전처리(Preprocessing), 모델 추론(Inference), 후처리(Post-processing)의 3단계 과정을 코드로 직접 구현하며 마스터합니다.
4.  **모델 최적화 기법의 이해:** PeopleNet에 적용된 **가지치기(Pruning)**와 **양자화(Quantization)**가 왜 엣지 디바이스(자율주행차)에 필수적인지 개념을 학습합니다.

---

### 🧠 [1부] 이론편: NVIDIA PeopleNet 깊이 파헤치기

코드를 살펴보기 전에, 우리가 사용할 강력한 도구인 **NVIDIA PeopleNet**에 대해 자세히 알아보겠습니다.

#### 1. PeopleNet이란?

**PeopleNet**은 NVIDIA가 자사의 **TAO(Train, Adapt, and Optimize) Toolkit**을 사용하여 개발한 고정밀 객체 탐지 모델입니다. 이름에서 알 수 있듯이, **사람(Person)**을 탐지하는 데 특화되어 있으며, 추가로 **가방(Bag)**과 **얼굴(Face)**까지 총 3개의 클래스를 탐지할 수 있습니다.

이 모델은 스마트 시티, 리테일 분석, 그리고 **자율주행** 분야에서 보행자 및 주변 인물을 인식하는 데 매우 효과적으로 사용됩니다.

#### 2. PeopleNet의 기술적 특징

-   **백본 네트워크 (Backbone):** **ResNet-34**를 기반으로 합니다. ResNet은 깊은 신경망에서도 안정적인 학습이 가능하도록 '잔차 연결(Residual Connection)' 개념을 도입한, 컴퓨터 비전 분야의 표준과도 같은 아키텍처입니다. 이를 통해 이미지의 복잡한 특징(feature)을 효과적으로 추출합니다.

-   **탐지 헤드 (Detection Head):** NVIDIA의 **DetectNet_v2** 아키텍처를 사용합니다. 이 구조는 이미지 전체를 일정한 그리드(Grid)로 나누고, 각 그리드 셀이 특정 객체를 포함하는지 여부와 객체의 위치 정보를 예측합니다. 우리가 분석할 코드의 후처리 과정은 바로 이 그리드 기반의 출력을 해석하는 과정입니다.

-   **최적화 (Optimization):** 이것이 PeopleNet의 핵심 경쟁력입니다.
    -   **가지치기 (Pruning):** 모델의 성능에 거의 영향을 주지 않는 불필요한 뉴런(가중치)을 제거하는 기술입니다. 이를 통해 모델의 크기는 대폭 줄어들고, 추론 속도는 빨라집니다.
    -   **양자화 (Quantization):** 기존 32비트 부동소수점(FP32)으로 표현되던 모델 가중치를 8비트 정수(INT8)로 변환하는 기술입니다. 메모리 사용량이 1/4로 줄고, 최신 GPU/NPU의 INT8 연산 가속 기능을 활용해 추론 속도를 극대화할 수 있습니다. 자율주행차와 같은 엣지 디바이스에서는 전력 소모와 연산 속도가 매우 중요하기에, 이 두 기술은 필수적입니다.
    -   우리가 다운로드하는 `pruned_quantized_decrypted_v2.3.4` 버전은 바로 이 두 가지 최적화가 모두 적용된 모델을 의미합니다.

#### 3. 생태계: NGC, TAO, 그리고 ONNX

-   **NVIDIA NGC (NVIDIA GPU Cloud):** AI 및 HPC(고성능 컴퓨팅)를 위한 소프트웨어 허브입니다. 개발자들은 NGC에서 PeopleNet과 같이 즉시 사용 가능한 사전 훈련 모델, 컨테이너, SDK 등을 손쉽게 다운로드할 수 있습니다.
-   **ONNX (Open Neural Network Exchange):** 딥러닝 모델을 위한 개방형 표준 형식입니다. TensorFlow, PyTorch 등 다양한 프레임워크에서 훈련된 모델을 ONNX 형식으로 변환하면, `onnxruntime`과 같은 단일 추론 엔진으로 어디서든 실행할 수 있습니다. 이는 모델의 배포와 이식성을 크게 향상시킵니다. 우리가 사용할 `.onnx` 파일이 바로 이것입니다.

---

### 💻 [2부] 실전편: PeopleNet 객체 탐지 코드 상세 분석

이제 제공된 코드를 한 줄 한 줄 분석하며, 이론이 실제 어떻게 구현되는지 살펴보겠습니다.

#### STEP 1: 환경 설정 및 모델 다운로드

이 단계는 PeopleNet을 실행하기 위한 기반 환경을 구축하는 과정입니다.

```bash
# 시스템 패키지 매니저 업데이트 및 필수 도구 설치
!apt update && apt install -y unzip wget ffmpeg

# 1. NVIDIA NGC CLI 다운로드 및 준비
# NGC(NVIDIA의 모델 허브)에 접근하기 위한 커맨드 라인 인터페이스(CLI)를 다운로드합니다.
!wget -q https://ngc.nvidia.com/downloads/ngccli_reg_linux.zip
!unzip -o ngccli_reg_linux.zip
!chmod +x ngc-cli/ngc # 실행 권한 부여

# 2. NGC CLI 설정 (API Key 입력 필요)
# NGC 웹사이트에서 API 키를 발급받아 붙여넣어야 합니다. 이를 통해 인증된 사용자만 모델을 다운로드할 수 있습니다.
!./ngc-cli/ngc config set

# 3. PeopleNet 모델 다운로드
# NGC 레지스트리에서 'nvidia/tao/peoplenet' 모델의 특정 버전을 다운로드합니다.
# 'pruned_quantized_decrypted': 가지치기, 양자화가 적용된, 암호 해제된 버전이라는 의미입니다.
!./ngc-cli/ngc registry model download-version nvidia/tao/peoplenet:pruned_quantized_decrypted_v2.3.4

# 4. 파이썬 라이브러리 설치
# onnxruntime: ONNX 모델을 실행하기 위한 런타임
# yt-dlp: 테스트용 유튜브 영상을 다운로드하기 위한 도구
# opencv-python: 이미지/영상 처리를 위한 필수 라이브러리
# numpy: 다차원 배열 연산을 위한 핵심 라이브러리
!pip install onnxruntime yt-dlp opencv-python numpy
```

#### STEP 2: Python 클래스 `DebugNVIDIAPeopleNet` 분석

이 클래스는 PeopleNet 모델을 로드하고, 영상을 처리하여 객체를 탐지하는 모든 로직을 담고 있습니다.

##### `__init__(self)`: 클래스 초기화

```python
def __init__(self):
    print("🚀 디버깅 NVIDIA PeopleNet 시작...")

    # 모델 경로를 하드코딩합니다. 실제 환경에서는 설정 파일로 분리하는 것이 좋습니다.
    self.model_path = "/workspace/peoplenet_vpruned_quantized_decrypted_v2.3.4/resnet34_peoplenet_int8.onnx"
    # 모델이 탐지할 수 있는 클래스 정의. 순서가 매우 중요합니다.
    self.classes = ['person', 'bag', 'face']
    # 시각화를 위한 BGR 색상 정의 (OpenCV 기준)
    self.colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255)]  # 사람:녹색, 가방:파랑, 얼굴:빨강

    # 모델 로드를 시도합니다.
    self.setup_model()
```
-   **핵심:** 객체 탐지 시스템에 필요한 기본 설정(모델 경로, 클래스 이름, 시각화 색상)을 정의합니다.

##### `setup_model(self)` & `find_model(self)`: 모델 로딩 및 검증

```python
def setup_model(self):
    try:
        if not os.path.exists(self.model_path):
            # 경로에 모델이 없으면, 다른 경로에서 찾아보는 find_model() 호출 (코드 견고성 향상)
            self.find_model() 
            return

        # onnxruntime을 사용하여 모델을 로드합니다. 'CPUExecutionProvider'는 CPU에서 추론하겠다는 의미입니다.
        # 자율주행차에서는 ['CUDAExecutionProvider']를 사용하여 NVIDIA GPU 가속을 활용합니다.
        self.session = ort.InferenceSession(self.model_path, providers=['CPUExecutionProvider'])

        # 모델의 입력/출력 노드 정보를 가져옵니다.
        # 이는 모델에게 어떤 형태의 데이터를 넣어주고, 어떤 형태의 결과를 받을지 알려줍니다.
        input_info = self.session.get_inputs()[0]
        output_info = self.session.get_outputs()
        self.input_name = input_info.name
        self.output_names = [output.name for output in output_info]
        
        # 모델이 요구하는 입력 형태 (Batch, Channel, Height, Width)를 출력하여 확인
        print(f"📊 입력: {input_info.name}, 형태: {input_info.shape}")

        self.model_loaded = True
        self.test_model() # 로드 직후, 더미 데이터로 테스트하여 모델이 정상 동작하는지 확인
    except Exception as e:
        print(f"❌ 모델 로드 실패: {e}")
        self.model_loaded = False
```
-   **핵심:** `onnxruntime.InferenceSession`을 통해 `.onnx` 파일을 메모리에 올리고 추론할 준비를 합니다. 모델의 입출력 구조를 파악하는 것은 매우 중요하며, 이는 `preprocess_frame`과 `postprocess_debug` 함수 설계의 기준이 됩니다.

##### `preprocess_frame(self, frame)`: 전처리 단계

```python
def preprocess_frame(self, frame):
    # 1. 리사이즈: 모델의 입력 크기(960x544)에 맞게 이미지 크기를 조절합니다.
    resized = cv2.resize(frame, (960, 544))
    # 2. 색상 공간 변환: OpenCV의 기본 BGR을 모델이 학습한 RGB 순서로 변경합니다.
    rgb_frame = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    # 3. 정규화: 픽셀 값을 0~255에서 0.0~1.0 사이로 변환합니다. 이는 모델의 안정적인 성능을 돕습니다.
    normalized = rgb_frame.astype(np.float32) / 255.0
    # 4. 차원 순서 변경 (HWC -> CHW): (Height, Width, Channel)을 (Channel, Height, Width) 순서로 바꿉니다.
    #    대부분의 딥러닝 프레임워크는 CHW 형식을 표준으로 사용합니다.
    chw_frame = np.transpose(normalized, (2, 0, 1))
    # 5. 배치 차원 추가: (CHW)를 (1, CHW)로 변경합니다. 모델은 항상 여러 이미지를 묶은 '배치' 단위로 입력받기 때문입니다.
    batch_frame = np.expand_dims(chw_frame, axis=0)
    return batch_frame
```
-   **핵심:** 원본 이미지를 AI 모델이 "이해"할 수 있는 표준화된 숫자 행렬(Tensor)로 변환하는 과정입니다. 이 5단계는 컴퓨터 비전 모델링의 정석과도 같습니다.

##### `detect_people(self, frame, debug=True)`: 추론 단계

```python
def detect_people(self, frame, debug=True):
    # ... (모델 로드 확인) ...
    # 1. 전처리
    input_data = self.preprocess_frame(frame)
    # 2. 추론 (Inference)
    #    핵심적인 부분! 전처리된 데이터를 모델에 입력하고, 출력을 받습니다.
    outputs = self.session.run(self.output_names, {self.input_name: input_data})
    if debug:
        print(f"🤖 추론 완료. 출력 텐서 형태: {outputs[0].shape}")
    # 3. 후처리
    detections = self.postprocess_debug(outputs, frame.shape, debug=debug)
    return detections
```
-   **핵심:** `session.run()` 한 줄이 바로 AI 모델이 수많은 연산을 통해 이미지 속에서 특징을 찾아내는 과정입니다. 이 함수의 입력은 전처리된 텐서, 출력은 모델의 예측 결과 텐서입니다.

##### `postprocess_debug(self, outputs, original_shape, debug=True)`: 후처리 단계

이 부분이 가장 복잡하지만, 모델의 출력을 해석하는 핵심적인 로직을 담고 있습니다.

```python
def postprocess_debug(self, outputs, original_shape, debug=True):
    detections = []
    # PeopleNet은 2개의 출력을 주지만, 첫 번째 출력이 객체 탐지 결과를 담고 있습니다.
    # 출력의 형태는 (1, 3, 34, 60): (Batch, Class, Grid_H, Grid_W)
    predictions = outputs[0][0]  # 배치 차원 제거 -> (3, 34, 60)
    orig_h, orig_w = original_shape[:2]
    num_classes, grid_h, grid_w = predictions.shape

    # 각 클래스(person, bag, face)에 대해 반복
    for class_idx in range(num_classes):
        class_name = self.classes[class_idx]
        class_pred = predictions[class_idx]  # (34, 60) 크기의 그리드(히트맵)

        # confidence가 특정 임계값(threshold)을 넘는 위치를 찾습니다.
        # 이 코드는 디버깅을 위해 여러 임계값을 테스트합니다.
        thresholds = [0.1, 0.2, 0.3, 0.4, 0.5]
        for threshold in thresholds:
            # np.where는 조건에 맞는 요소의 인덱스를 반환합니다.
            high_positions = np.where(class_pred > threshold)

            if len(high_positions[0]) > 0:
                # 객체가 탐지된 경우
                # (y_idx, x_idx)는 그리드 상의 좌표
                y_idx = high_positions[0][0]
                x_idx = high_positions[1][0]
                confidence = float(class_pred[y_idx, x_idx])

                # 그리드 좌표를 원본 이미지 비율 좌표로 변환
                center_x = (x_idx + 0.5) / grid_w
                center_y = (y_idx + 0.5) / grid_h

                # 이 코드의 단순화된 부분: 바운딩 박스 크기를 클래스별로 고정값으로 사용.
                # 원래 DetectNet_v2는 바운딩 박스의 크기(w, h)도 함께 예측합니다.
                # (수업에서는 이 부분을 개선하는 과제를 내줄 수 있습니다.)
                if class_name == 'person': box_w, box_h = 0.12, 0.20
                # ... (bag, face 크기 설정) ...

                # 비율 좌표를 원본 이미지의 픽셀 좌표로 최종 변환
                x1 = int((center_x - box_w/2) * orig_w)
                # ... (y1, x2, y2 계산) ...

                detections.append({'bbox': [x1, y1, x2, y2], ...})
                break # 하나의 임계값에서 성공하면 다음 클래스로 넘어감

    # NMS (Non-Maximum Suppression): 겹치는 바운딩 박스 중 가장 신뢰도 높은 것만 남김
    if detections:
        detections = self.simple_nms(detections)

    return detections
```
-   **핵심:** 모델이 출력한 숫자 그리드(히트맵)를 사람이 이해할 수 있는 정보(바운딩 박스 좌표, 클래스 이름, 신뢰도)로 변환하는 과정입니다. 그리드 좌표계 -> 비율 좌표계 -> 픽셀 좌표계로 변환하는 로직과 NMS의 필요성을 이해하는 것이 중요합니다.

---

### 🚀 결론 및 심화 학습 제안

본 튜토리얼을 통해 우리는 NVIDIA의 최신 AI 모델을 가져와, 실세계 문제(객체 탐지)에 적용하는 전체 과정을 경험했습니다.

-   **환경 설정:** NGC CLI를 통해 클라우드에서 모델을 다운로드했습니다.
-   **모델 로딩:** ONNX와 `onnxruntime`을 사용해 프레임워크 독립적인 추론 환경을 구축했습니다.
-   **파이프라인 구현:** **전처리-추론-후처리** 3단계를 코드로 명확히 구현했습니다.
-   **이론과 실제의 연결:** ResNet, DetectNet_v2, 양자화, NMS 등의 이론적 개념이 실제 코드에서 어떻게 동작하는지 확인했습니다.

#### 다음 단계는?

1.  **GPU 가속:** `providers=['CPUExecutionProvider']`를 `['CUDAExecutionProvider']`로 변경하여 GPU를 사용했을 때, 추론 속도가 얼마나 향상되는지 직접 측정해보세요.
2.  **후처리 개선:** 현재 고정된 바운딩 박스 크기를 사용하는 `postprocess_debug` 함수를 개선해보세요. DetectNet_v2는 보통 Coverage 맵과 Bbox 맵을 함께 출력합니다. 모델의 두 번째, 세 번째 출력을 분석하여 실제 예측된 크기를 사용하도록 코드를 수정해보세요.
3.  **다른 모델 적용:** NGC에는 PeopleNet 외에도 차량을 탐지하는 `TrafficCamNet`, `DashCamNet` 등 다양한 모델이 있습니다. 오늘 배운 파이프라인 구조를 재활용하여 다른 모델을 테스트해보세요.
4.  **실시간 처리:** 현재는 정지된 프레임을 테스트했습니다. `cv2.VideoCapture(0)`를 사용하여 웹캠 영상을 실시간으로 입력받고, 화면에 탐지 결과를 바로 출력하는 프로그램을 작성해보세요. (FPS 측정 포함)

이 과정을 통해 학생 여러분은 자율주행 AI 개발자로서 한 걸음 더 나아갈 수 있을 것입니다. 질문이 있다면 언제든지 토론을 시작해주세요.
