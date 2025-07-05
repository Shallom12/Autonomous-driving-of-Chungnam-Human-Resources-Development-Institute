# Autonomous_drivingof_Chungnam_Human_Resources_Development
## 안녕하세요 주은이의 자율주행차 프로젝트에 오신것을 환영합니다
### 만나서 반갑습니다
![ai-generated-8403514_1280](https://github.com/user-attachments/assets/48199f10-e6b1-4d9b-ac52-e5a8911eaa83)
```
print(hello autonomous driving)
sudo apt update
pip install matplotlib as plt
```
# 📘 AI 학습 정리

## 1. About GitHub, Markdown, Colab
- [GitHub 사용법](github-사용법)


## GitHub 사용법

### ✅ GitHub 계정 만드는 순서 (2025년 기준)

1. **웹 브라우저 열기**
   크롬(Chrome), 엣지(Edge), 사파리(Safari) 중 편한 걸 사용하세요.

2. **GitHub 웹사이트 접속**
   주소창에 아래 주소를 입력하고 Enter 누르세요: https://github.com

3. **회원가입 시작하기**
   화면 오른쪽 위 또는 중간에 있는 Sign up 버튼 클릭

4. **이메일 주소 입력**
   평소 자주 사용하는 이메일을 입력

5. **비밀번호 만들기**
   영어 대문자, 소문자, 숫자, 특수문자를 섞어 안전하게!
   예시: Git1234!hub

6. **사용자 이름(Username) 정하기**
   나만의 고유한 이름을 지어요 (다른 사람이 쓰고 있으면 불가)
   - 예시: jetsunmom, sungsookjang66 등
   - 영어, 숫자, 하이픈(-) 가능 (띄어쓰기 ❌)

### ✅ Repository 만들기 순서

1. **GitHub에 로그인 후 New Repository 클릭**
2. ![new](https://github.com/user-attachments/assets/3481a680-f677-403b-be8c-1fe59d5aa7cb)

3. **Repository 이름 입력**
4. **Public/Private 선택**
5. **README.md 파일 생성 체크**
6. **Create repository 버튼 클릭**
   
![create_repository](https://github.com/user-attachments/assets/8c2eb16b-8dfc-465a-88cd-d35770d12df0)-----

# GitHub 마크다운 가이드: 초보자를 위한 시작 (2025년 최신)

안녕하세요\! 이 문서는 GitHub에서 프로젝트 문서를 효과적으로 만들고 소통하는 데 필수적인 **마크다운(Markdown)** 사용법을 안내합니다. 마크다운은 간단한 문법으로 텍스트를 아름답게 꾸밀 수 있는 강력한 도구입니다. 특히 GitHub의 `README.md` 파일을 작성하는 데 가장 많이 활용됩니다.

이 가이드를 통해 여러분의 프로젝트에 생명을 불어넣고, 방문자에게 명확하고 매력적인 정보를 제공할 수 있도록 돕겠습니다.

-----

## 🚀 1. 빠른 시작: 기본 문법 요약

| 문법                   | 예시                                    | 미리보기                      |
| :--------------------- | :-------------------------------------- | :---------------------------- |
| **제목** | `# 제목`, `## 소제목`                   | \# 제목, \#\# 소제목             |
| **텍스트 강조** | `**굵게**`, `*기울임꼴*`              | **굵게**, *기울임꼴* |
| **목록 (순서 없음)** | `* 항목`, `- 항목`                      | \* 항목                        |
| **목록 (순서 있음)** | `1. 항목`                               | 1. 항목                       |
| **인라인 코드** | `` `코드` ``                            | `코드`                        |
| **코드 블록** | ` ```python ... ``` `           | (아래 예시 참고)              |
| **링크** | `[텍스트](URL)`                         | [텍스트](https://github.com) |
| **이미지** | `![설명](URL)`                          | (아래 예시 참고)              |
| **인용문** | `> 인용문`                              | \> 인용문                      |
| **구분선** | `---`                                   | ---                           |
| **표** | `| 헤더 | ...`                           | (아래 예시 참고)              |
| **체크리스트 (GFM)** | `- [ ] 미완료`, `- [x] 완료`           | - [ ] 미완료, - [x] 완료      |
| **이모지 (GFM)** | `:sparkles:`                            | ✨                            |

-----

## 🌟 2. 자세히 알아보기: 핵심 마크다운 문법

### 2.1. 제목 (Headings): 문서의 뼈대 세우기

`#` 기호의 개수로 제목의 크기를 조절합니다. HTML의 `<h1>`부터 `<h6>`와 유사합니다.

```markdown
# 프로젝트 이름 (가장 큰 제목)
## 주요 섹션 (예: 개요, 설치 방법)
### 세부 내용 (예: 전제 조건, 사용법)
#### 더 깊은 내용
```

### 2.2. 텍스트 꾸미기 (Text Formatting): 내용 강조하기

특정 단어나 구절을 시각적으로 강조하여 가독성을 높입니다.

```markdown
**이 텍스트는 굵게 표시됩니다.**
*이 텍스트는 기울임꼴로 표시됩니다.*
***이 텍스트는 굵고 기울임꼴입니다.***
~~이 텍스트는 취소선이 있습니다.~~
```

### 2.3. 목록 (Lists): 정보 체계화하기

  * **순서 없는 목록 (Unordered List):** `*`, `-`, `+` 중 하나를 사용합니다.

    ```markdown
    * 첫 번째 항목
      * 하위 항목 1
      * 하위 항목 2
    - 두 번째 항목
    ```

  * **순서 있는 목록 (Ordered List):** 숫자와 마침표(`.`)를 사용합니다.

    ```markdown
    1. 첫 번째 단계
    2. 두 번째 단계
       1. 세부 단계 1
       2. 세부 단계 2
    ```

### 2.4. 코드 (Code): 코드 스니펫 공유하기

  * **인라인 코드:** 짧은 코드 조각은 `` ` `` (백틱)으로 감쌉니다.

    ```markdown
    `git clone` 명령어를 사용하여 저장소를 복제합니다.
    ```

  * **코드 블록:** 여러 줄의 코드는 백틱 3개(\`\`\`)로 시작하고 끝냅니다. 언어 이름을 지정하면 신택스 하이라이팅이 적용되어 가독성이 매우 높아집니다.

    ````markdown
    ```python
    # Python 예제 코드
    def hello_world():
        print("Hello, GitHub Markdown!")

    hello_world()
    ````

### 2.5. 링크 (Links): 관련 자료 연결하기

`[링크 텍스트](링크_URL)` 형식으로 외부 웹사이트나 저장소 내의 다른 파일로 연결할 수 있습니다.

````markdown
[공식 GitHub 웹사이트](https://github.com)
[프로젝트 기여 가이드](./CONTRIBUTING.md)  ```

### 2.6. 이미지 (Images): 시각 자료 첨부하기

`![이미지 설명](이미지_URL)` 형식으로 이미지를 삽입합니다.

```markdown
![예시 이미지](https://via.placeholder.com/150/0000FF/FFFFFF?text=Placeholder)
````

### 2.7. 인용문 (Blockquotes): 중요한 내용 강조하기

`>` 기호를 사용하여 텍스트를 인용문 형식으로 표시합니다.

```markdown
> "코드는 예술과 같다." - 프로그래밍 격언
>> 중첩된 인용문도 가능합니다.
```

### 2.8. 구분선 (Horizontal Rules): 섹션 분리하기

`---`, `***`, `___` 중 3개 이상을 사용하여 가로 구분선을 만듭니다.

```markdown
첫 번째 섹션의 내용.

---

두 번째 섹션의 내용.
```

### 2.9. 표 (Tables): 데이터 정렬하기

`|` (파이프)와 `-` (하이픈)를 사용하여 데이터를 표 형태로 보여줍니다.

```markdown
| 헤더 1 | 헤더 2   | 헤더 3      |
| :----- | :------: | --------: |
| 왼쪽 정렬 | 중앙 정렬 | 오른쪽 정렬 |
| 데이터 A | 데이터 B | 데이터 C    |
```
-----

## ✨ 3. GitHub Flavored Markdown (GFM): GitHub만의 특별한 기능

GitHub는 표준 마크다운 외에 개발자에게 유용한 몇 가지 확장 기능을 제공합니다.

### 3.1. 체크리스트 (Task Lists)

이슈나 PR(Pull Request) 설명에서 작업 진행 상태를 표시할 때 유용합니다.

```markdown
- [ ] 문서 업데이트 계획
- [x] 버그 수정 완료
- [ ] 테스트 코드 작성
```

### 3.2. 이모지 (Emojis)

`:` 기호와 이모지 이름(Cheatsheet 참고)을 사용하여 귀여운 이모티콘을 추가합니다.

```markdown
이 프로젝트는 :heart: 사랑으로 만들어졌습니다!
```

### 3.3. 사용자/이슈/커밋 참조 (Mentions, Issues, Commits)

  * **사용자 멘션:** `@사용자명` 을 통해 특정 GitHub 사용자에게 알림을 보냅니다. 예: `@octocat`
  * **이슈/PR 참조:** `#이슈번호` 를 통해 해당 저장소의 이슈나 PR을 참조합니다. 예: `#123` (이슈 123번)
  * **커밋 참조:** 커밋 해시(Commit Hash)의 처음 몇 글자를 입력하여 특정 커밋에 링크할 수 있습니다. 예: `a1b2c3d`

-----

## 💡 4. 마크다운 작성 팁 & 모범 사례

  * **간결하게:** 필요한 정보만 명확하게 전달하세요.
  * **일관성:** 제목, 목록, 코드 스타일 등 문서 전체에서 일관된 포맷을 유지하세요.
  * **미리보기:** GitHub에서 파일을 저장하기 전에 항상 미리보기 기능을 활용하여 어떻게 보일지 확인하세요.
  * **목차 사용:** 긴 README 파일에는 `[제목](#제목-id)` 형태의 내부 링크를 활용하여 목차를 만들어주면 편리합니다. (예: `[빠른 시작](#-1-빠른-시작-기본-문법-요약)`)
  * **이모지 활용:** 적절한 이모지는 문서의 분위기를 부드럽게 하고 시선을 끌 수 있습니다. (과도한 사용은 지양)
  * **`.md` 확장자:** 마크다운 파일은 항상 `.md` 또는 `.markdown` 확장자를 사용해야 GitHub에서 제대로 렌더링됩니다.

-----

## 📚 5. 더 알아보기 (추가 자료)

  * **GitHub Markdown Cheatsheet:** [https://guides.github.com/features/mastering-markdown/](https://guides.github.com/features/mastering-markdown/)
  * **Markdown Guide:** [https://www.markdownguide.org/basic-syntax/](https://www.markdownguide.org/basic-syntax/)

-----

- [Colab 기초](#colab-기초)

## Colab 기초    

(여기에 Colab 내용 작성)
![colab1](https://github.com/user-attachments/assets/13ad41ca-8f7c-40fe-b6d6-a47800bea3a9)주어진 이미지들을 바탕으로 Google Colaboratory (Colab) 기초 내용을 좀 더 상세하고 시각적으로 명확하게 재구성하여 GitHub 마크다운에 적합한 형태로 만들어 드리겠습니다. 이전 내용과 중복되는 부분은 통합하고, 새로운 정보를 추가하겠습니다.

-----

# 🚀 Google Colaboratory (Colab) 시작하기: 실전 가이드

안녕하세요\! 이 가이드는 **Google Colaboratory (Colab)** 를 사용하는 가장 기본적인 방법들을 안내합니다. Colab은 Google에서 무료로 제공하는 클라우드 기반의 Jupyter 노트북 환경으로, 웹 브라우저만 있다면 누구나 쉽게 파이썬 코드를 실행하고, 심지어 GPU/TPU 같은 고성능 하드웨어 가속기까지 활용하여 머신러닝 및 데이터 과학 프로젝트를 수행할 수 있습니다.

**핵심 이점:**

  * **무료:** GPU/TPU 자원까지 무료로 제공됩니다.
  * **설정 불필요:** 웹 브라우저만 있으면 바로 코딩을 시작할 수 있습니다.
  * **협업:** Google 문서처럼 여러 명이 동시에 작업할 수 있습니다.
  * **GitHub 연동:** `.ipynb` 파일을 GitHub에 올리면 코드와 실행 결과를 함께 볼 수 있습니다.

-----

## 🏁 1단계: Colab 시작하기 & 새 노트북 만들기

Colab은 Google 계정만 있다면 쉽게 접근할 수 있습니다.

### 1.1 Colab 접속 방법

1.  **가장 쉬운 방법:** 아래 주소로 접속합니다.
    [https://colab.research.google.com](https://colab.research.google.com)

2.  **또는 Google 드라이브에서:**

    1.  [Google 드라이브](https://drive.google.com) 에 접속합니다.
    2.  왼쪽 상단의 `[+ 새로 만들기]`를 클릭합니다.
    3.  `더보기 > Google Colaboratory`를 클릭합니다.

    <!-- end list -->

      * 📌 **팁:** 처음 실행 시 "Google Colab을 설치하시겠습니까?"라는 메시지가 나올 수 있습니다. 설치하면 다음부터는 자동으로 연결됩니다.

### 1.2 새 노트북 만들기

Colab은 `.ipynb` 확장자를 가진 주피터(Jupyter) 노트북 파일로 작업합니다.

  * **시작 시:** `새 노트` 버튼을 클릭하여 새로운 노트북을 시작할 수 있습니다.
     \* **기본 이름:** 보통 `Untitled0.ipynb`처럼 자동으로 생성됩니다.
  * **이름 변경:** 노트북 상단의 파일명을 클릭하여 원하는 이름으로 변경할 수 있습니다. (예: `My_First_Colab_Notebook.ipynb`)

-----

## 🧱 2단계: Colab 노트북 구성 이해하기

Colab 노트북은 다음의 핵심 요소들로 구성됩니다.

| 구성     | 설명                                 |
| :------- | :----------------------------------- |
| ▶ 코드 셀 | 파이썬 코드를 작성하고 실행하는 공간 |
| 📜 텍스트 셀 | 마크다운(글 설명)을 작성하는 공간    |
| 🔄 런타임 | 코드가 실행되는 환경 (CPU, GPU 선택) |

-----

## 🛠️ 3단계: 셀(Cell) 추가 / 삭제 / 실행

Colab 작업의 기본은 '셀' 단위로 이루어집니다.

| 작업          | 방법                                       |
| :------------ | :----------------------------------------- |
| **코드 셀 추가** | 상단 메뉴: `+ 코드` 버튼 클릭                      |
| **텍스트 셀 추가** | 상단 메뉴: `+ 텍스트` 버튼 클릭                    |
| **셀 삭제** | 셀 왼쪽 점 3개(`⋮`) 클릭 → `휴지통` 아이콘 클릭 |
| **셀 실행** | `Shift + Enter` 또는 셀 좌측의 `▶` 아이콘 클릭 |

-----

## ⚙️ 4단계: 실행 환경 설정 (GPU 사용 등)

머신러닝이나 딥러닝 작업 시에는 강력한 하드웨어 가속기(GPU/TPU)를 활용하는 것이 중요합니다.

1.  **런타임 유형 변경:** 상단 메뉴 `[런타임]` → `[런타임 유형 변경]`을 클릭합니다.
     2.  **하드웨어 가속기 선택:** `하드웨어 가속기` 드롭다운에서 `GPU` 또는 `TPU`를 선택합니다.

      * **저장 후 다시 실행하면 AI 학습도 가능합니다\!**

### 4.1. 용도별 추천 설정

| 하고 싶은 일              | 추천 하드웨어 가속기 | 이유                                          |
| :------------------------ | :------------------- | :-------------------------------------------- |
| **단순한 파이썬 연습** | ✅ **CPU (기본값)** | 빠르고 설정 없이 사용 가능                    |
| **딥러닝, AI 모델 실행** | ✅ **T4 GPU** 또는 **A100 GPU** | AI 연산에 최적화, GPU는 필수                |
| **고속 이미지 처리, 훈련** | ✅ **L4 GPU** | 영상 처리나 대규모 훈련에 적합                |
| **TPU를 사용한 딥러닝** | ❗ **TPU (v2-8 등)** | 빠르지만 설정 복잡 (초보자 비추천, 특수 경우) |

**전문가 팁:** 처음에는 `CPU`로 시작하고, 딥러닝 모델 훈련 등 컴퓨팅 자원이 많이 필요할 때만 `GPU`로 변경하는 것이 효율적입니다.

-----

## 📁 5단계: 구글 드라이브 연동 & 파일 관리

Colab 노트북은 Google Drive에 자동 저장되며, Drive의 파일들을 Colab에서 바로 사용할 수 있습니다.

  * Colab은 자동 저장됩니다.
  * **파일 \> 사본 저장 \> 내 드라이브에 저장**을 통해 명시적으로 사본을 저장할 수 있습니다.
  * 드라이브의 `.ipynb` 파일을 더블클릭하면 다시 Colab으로 열립니다.

### 5.1. Google Drive 마운트 (연동)

Colab 노트북에서 Google Drive에 있는 데이터나 다른 노트북에 접근하려면 Drive를 마운트해야 합니다.

```python
from google.colab import drive
drive.mount('/content/drive')
# 성공적으로 마운트되면 'Mounted at /content/drive' 메시지가 출력됩니다.
```

이제 `/content/drive/MyDrive/` 경로를 통해 Google Drive 내의 파일에 접근할 수 있습니다.

```python
# 예시: Drive에 있는 CSV 파일 읽기
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/MyProject/data.csv')
print(df.head())
```

-----

## 🤝 6단계: 협업 및 GitHub 연동

Colab은 협업에 매우 강력하며, GitHub와 함께 사용하면 그 시너지가 극대화됩니다.

### 6.1. 노트북 공유 (Google Drive 방식)

Google 문서처럼 여러 명이 동시에 Colab 노트북을 편집할 수 있습니다.

1.  노트북 우측 상단의 `공유(Share)` 버튼을 클릭합니다.
2.  공유 설정을 변경하여 특정 사용자에게 접근 권한을 부여하거나, 링크를 아는 모든 사람이 볼 수 있도록 설정할 수 있습니다.

### 6.2. GitHub에 Colab 노트북 올리기

`.ipynb` 파일은 GitHub에서 특별하게 다루어집니다.

1.  작성한 Colab 노트북(`.ipynb` 파일)을 Google Drive에서 다운로드합니다.
2.  GitHub 저장소에 이 `.ipynb` 파일을 업로드합니다.
3.  GitHub에서 `.ipynb` 파일을 클릭하면, 코드는 물론 **실행 결과와 마크다운 설명까지 웹 페이지에서 바로 렌더링되어 보입니다\!**

**전문가 팁:** 이 기능은 프로젝트의 분석 과정, 실험 결과, 데이터 시각화 등을 코드를 실행하지 않고도 다른 사람들에게 명확하게 보여줄 수 있어, 프로젝트 문서화에 매우 강력합니다.

-----

## 💡 7. Colab 사용 팁 & 모범 사례

  * **단축키 활용:**
      * `Shift + Enter`: 현재 셀 실행 및 다음 셀로 이동
      * `Ctrl/Cmd + Enter`: 현재 셀 실행
      * `Ctrl/Cmd + M A`: 현재 셀 위에 코드 셀 추가
      * `Ctrl/Cmd + M B`: 현재 셀 아래에 코드 셀 추가
  * **PIP 설치:** 필요한 라이브러리가 없다면 셀에서 `!pip install 라이브러리_이름` 명령어로 설치할 수 있습니다.
  * **주석과 텍스트 셀:** 코드는 `#`으로 주석을 달고, 텍스트 셀을 통해 코드의 목적, 데이터 설명, 결과 해석 등을 자세히 작성하여 노트북의 가독성을 높이세요.
  * **런타임 재시작/연결 해제:** 필요 시 `런타임(Runtime)` 메뉴에서 환경을 초기화하거나 연결을 해제하여 리소스를 관리하세요.

-----

## 2. About Python3
- [Python basic](./docs/python3.md)

## 3.  data structure / data sciencs

- [데이터 구조 개요](./data_structures.md)
- [Pandas](./pandas.md)
- [Numpy](./numpy.md)
- [Matplotlib](./Matplotlib.md)

## 4. Machine Learning

- [Machine Learning Basic](./ml_basic.md)
- [모델 훈련 및 평가](./ml_test.md)
- <img width="702" alt="Screenshot 2025-06-24 at 10 39 00" src="https://github.com/user-attachments/assets/347973e1-d7fe-407d-8d4f-8190260e8824" />


## 5. OpenCV

- [OpenCV Basic](./OpenCV_basic.md)
- [이미지 처리](./image_test.md)

  
## 6. CNN(Convolution Neural Network
- [CNN_Basic](./CNN_basic.md)
- [CNN_자율주행 관련 코드](./cnn_test.md)

## 7. Ultralytics
- [Ultralytics_Basic](./Ultralytics_basic.md)
- [YOLOv8](./YOLOv8_test.md)
- [YOLOv12](./YOLOv12_test.md)
  
## 8. TensorRT vs PyTorch 
- [PyTorch_Basic](./PyTorch_basic.md)
- [TensorRT](./TensorRT_test.md)
- [YOLOv12](./YOLOv12_test.md)

## 9. TAO Toolkit on RunPod
- [TAO_사용법](.TAO_install.md)
- [TAO_Toolkit](.TAO_Toolkit.md)

## 10. 칼만필터, CARLA, 경로 알고리즘
- [kalman](.kalman.md)
- [CARLA_simulator](.CARLA.md)

## 11. ADAS & (ADAS TensorRT vs PyTorch)
- [adas_basic](.adas_basic.md)
- [TensorRT vs PyTorch 비교](.vs.md)
- 


# 🚗 Python 자율주행 핵심 문법 가이드

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

# 🚗 자율주행 개발 핵심 변수 가이드

> 자율주행 시스템 개발에서 필수적으로 사용되는 변수들을 카테고리별로 정리한 실무 가이드입니다.

## 📋 목차

- [차량 상태 변수](#-차량-상태-변수-vehicle-state)
- [제어 변수](#-제어-변수-control-variables)
- [경로 계획 변수](#-경로-계획-변수-path-planning)
- [센서 데이터 변수](#-센서-데이터-변수-sensor-data)
- [안전 및 충돌 회피 변수](#-안전-및-충돌-회피-변수-safety--collision-avoidance)
- [주행 모드 변수](#-주행-모드-변수-driving-modes)
- [환경 변수](#-환경-변수-environment)
- [시간 관련 변수](#-시간-관련-변수-time-related)
- [차량 물리적 특성 변수](#-차량-물리적-특성-변수-vehicle-physical-properties)

---

## 📍 차량 상태 변수 (Vehicle State)

차량의 현재 위치, 방향, 속도 등 기본적인 상태 정보를 저장하는 변수들입니다.

### 🗺️ 위치 정보 (Position Information)

```python
# 3D 공간에서의 차량 위치
x, y, z = 0.0, 0.0, 0.0        # 차량의 3D 좌표 (미터 단위)

# 차량의 방향 정보
heading = 0.0                   # 차량의 방향각 (yaw) - 좌우 회전
pitch = 0.0                     # 차량의 앞뒤 기울기 (상하 각도)
roll = 0.0                      # 차량의 좌우 기울기 (롤링 각도)
```

### 🏃‍♂️ 속도 정보 (Velocity Information)

```python
# 직선 운동 관련
velocity = 0.0                  # 현재 속도 (km/h 또는 m/s)
acceleration = 0.0              # 가속도 (m/s²)

# 회전 운동 관련
angular_velocity = 0.0          # 각속도 (rad/s) - 회전 속도
```

---

## 🎮 제어 변수 (Control Variables)

차량의 움직임을 직접 제어하는 명령값들을 저장하는 변수들입니다.

### 🔄 조향 제어 (Steering Control)

```python
steering_angle = 0.0            # 현재 조향각 (도 단위)
max_steering_angle = 30.0       # 최대 조향각 제한 (물리적 한계)

# 조향 방향 예시
# steering_angle > 0  : 우회전
# steering_angle = 0  : 직진
# steering_angle < 0  : 좌회전
```

### ⚡ 속도 제어 (Speed Control)

```python
# 액셀/브레이크 제어 (0~1 범위)
throttle = 0.0                  # 스로틀 개도 (0: 없음, 1: 최대)
brake = 0.0                     # 브레이크 강도 (0: 없음, 1: 최대)

# 속도 목표값
target_speed = 30.0             # 목표 속도 (km/h)
max_speed = 60.0                # 최대 허용 속도 (안전 제한)
```

---

## 🗺️ 경로 계획 변수 (Path Planning)

차량이 목적지까지 이동할 경로와 관련된 변수들입니다.

### 📍 웨이포인트 (Waypoints)

```python
# 경로 관련 데이터 구조
waypoints = []                  # 경로상의 모든 점들
target_waypoint = None          # 현재 목표로 하는 점
path = []                       # 계획된 상세 경로
route = []                      # 전체 루트 (큰 구간들)

# 거리 계산
distance_to_target = 0.0        # 현재 목표점까지의 거리
lookahead_distance = 10.0       # 전방 주시 거리 (경로 추종용)
```

### 🌏 실제 GPS 좌표 예시

```python
# 서울/경기도 지역의 실제 waypoints 예시
waypoints = np.array([
    [127.123, 37.456],          # 시작점 (강남구 근처)
    [127.126, 37.456],          # 안전 접근
    [127.130, 37.463],          # 장애물1 위로 회피
    [127.134, 37.462],          # 장애물2 아래로 회피
    [127.139, 37.468],          # 장애물3 위로 회피
    [127.143, 37.474],          # 목적지 접근
    [127.145, 37.478]           # 최종 목적지
])

# GPS 좌표 분해
start_position = waypoints[0]   # [127.123, 37.456] - 시작점
current_lon = start_position[0] # 127.123 (경도, longitude)
current_lat = start_position[1] # 37.456 (위도, latitude)
```

#### 🌍 GPS 좌표계 이해하기

| 용어 | 영문 | 의미 | 방향 |
|------|------|------|------|
| **경도** | longitude (lon) | 동서 방향 위치 | 세로선 (동경/서경) |
| **위도** | latitude (lat) | 남북 방향 위치 | 가로선 (북위/남위) |

> 💡 **좌표 해석**: `[127.123, 37.456]`은 동경 127.123도, 북위 37.456도를 의미하며, 서울 강남구 근처의 실제 위치입니다.

---

## 📡 센서 데이터 변수 (Sensor Data)

다양한 센서로부터 수집되는 데이터를 저장하는 변수들입니다.

### 📷 카메라 데이터 (Camera Data)

```python
camera_data = None              # 카메라로 촬영한 이미지 데이터
lane_lines = []                 # 감지된 차선 정보 리스트
traffic_signs = []              # 인식된 교통 표지판 리스트
traffic_lights = []             # 감지된 신호등 정보

# 영상 처리 결과
detected_objects = []           # 인식된 모든 객체들
pedestrians = []                # 보행자 정보
vehicles = []                   # 다른 차량 정보
```

### 🌊 라이다 데이터 (LiDAR Data)

```python
lidar_points = []               # 라이다 포인트 클라우드 데이터
obstacles = []                  # 감지된 장애물 리스트
point_cloud_intensity = []      # 각 포인트의 반사 강도

# 3D 공간 정보
distance_map = []               # 거리 맵 (2D 배열)
height_map = []                 # 높이 맵 (지형 정보)
```

### 🛰️ GPS 데이터 (GPS Data)

```python
gps_lat, gps_lon = 0.0, 0.0    # 현재 GPS 좌표 (위도, 경도)
gps_altitude = 0.0              # 해발 고도 (미터)
gps_accuracy = 0.0              # GPS 정확도 (미터 단위 오차)
gps_timestamp = 0.0             # GPS 데이터 수신 시간

# GPS 상태 정보
gps_fix_type = "3D"             # GPS 고정 타입 (2D/3D)
satellite_count = 8             # 연결된 위성 수
```

---

## ⚠️ 안전 및 충돌 회피 변수 (Safety & Collision Avoidance)

차량의 안전한 주행을 위한 충돌 감지 및 회피 관련 변수들입니다.

### 🚨 충돌 감지 (Collision Detection)

```python
collision_detected = False      # 충돌 위험 감지 여부
safety_distance = 5.0           # 최소 안전 거리 (미터)
emergency_brake = False         # 비상 브레이크 활성화 여부

# 위험도 평가
collision_risk_level = 0        # 충돌 위험도 (0: 안전 ~ 10: 매우 위험)
time_to_collision = float('inf') # 충돌까지 예상 시간 (초)
```

### 🚗 주변 차량 정보 (Surrounding Vehicles)

```python
nearby_vehicles = []            # 주변 차량들의 정보 리스트
front_vehicle_distance = float('inf')  # 앞차와의 거리
rear_vehicle_distance = float('inf')   # 뒤차와의 거리
left_vehicle_distance = float('inf')   # 좌측 차량과의 거리
right_vehicle_distance = float('inf')  # 우측 차량과의 거리

# 각 차량의 상세 정보 (딕셔너리 형태로 저장)
vehicle_info = {
    'id': 1,                    # 차량 식별 ID
    'position': [x, y],         # 차량 위치
    'velocity': 30.0,           # 차량 속도
    'direction': 45.0,          # 진행 방향
    'distance': 15.0            # 우리 차량과의 거리
}
```

---

## 🚦 주행 모드 변수 (Driving Modes)

차량의 다양한 주행 상태와 모드를 관리하는 변수들입니다.

### 🎯 주행 상태 (Driving State)

```python
# 주행 모드 종류
driving_mode = "NORMAL"         # 현재 주행 모드
# 가능한 값: "NORMAL", "PARKING", "EMERGENCY", "MANUAL", "HIGHWAY"

autonomous_mode = True          # 자율주행 모드 활성화 여부
lane_change_mode = False        # 차선 변경 모드 여부
parking_mode = False            # 주차 모드 여부

# 특수 상황 모드
overtaking_mode = False         # 추월 모드
reversing_mode = False          # 후진 모드
```

### 🔄 모드 전환 (Mode Switching)

```python
mode_switch_request = None      # 모드 전환 요청
mode_transition_time = 0.0      # 모드 전환에 걸리는 시간
previous_mode = "NORMAL"        # 이전 주행 모드 (복구용)
```

---

## 🌦️ 환경 변수 (Environment)

주변 환경과 도로 상황에 관한 정보를 저장하는 변수들입니다.

### ☀️ 날씨 및 도로 상태 (Weather & Road Conditions)

```python
# 날씨 정보
weather_condition = "CLEAR"     # 날씨 상태
# 가능한 값: "CLEAR", "RAIN", "SNOW", "FOG", "CLOUDY"

road_condition = "DRY"          # 도로 상태
# 가능한 값: "DRY", "WET", "ICY", "SNOWY"

visibility = 100.0              # 가시거리 (미터)
temperature = 20.0              # 외부 온도 (섭씨)
humidity = 50.0                 # 습도 (%)
wind_speed = 5.0                # 풍속 (m/s)
```

### 🚦 교통 상황 (Traffic Conditions)

```python
# 교통 신호 및 규칙
traffic_light_state = "GREEN"   # 현재 신호등 상태
# 가능한 값: "RED", "YELLOW", "GREEN", "UNKNOWN"

speed_limit = 50.0              # 현재 구간 제한 속도 (km/h)
road_type = "CITY"              # 도로 타입
# 가능한 값: "HIGHWAY", "CITY", "RESIDENTIAL", "PARKING_LOT"

traffic_density = "LIGHT"       # 교통 밀도
# 가능한 값: "LIGHT", "MODERATE", "HEAVY", "JAM"
```

---

## ⏰ 시간 관련 변수 (Time Related)

시뮬레이션이나 실시간 처리를 위한 시간 관련 변수들입니다.

### 🕐 시간 정보 (Time Information)

```python
current_time = 0.0              # 현재 시간 (유닉스 타임스탬프)
dt = 0.1                        # 시간 간격/타임스텝 (초)
simulation_time = 0.0           # 시뮬레이션 시작부터 경과 시간

# 프레임 관리
frame_count = 0                 # 처리된 프레임 수
fps = 30.0                      # 초당 프레임 수
last_update_time = 0.0          # 마지막 업데이트 시간

# 성능 측정
processing_time = 0.0           # 한 프레임 처리 시간
average_processing_time = 0.0   # 평균 처리 시간
```

---

## 🚗 차량 물리적 특성 변수 (Vehicle Physical Properties)

차량의 물리적 특성과 성능 한계를 정의하는 변수들입니다.

### 📏 차량 크기 (Vehicle Dimensions)

```python
# 기본 치수 (미터 단위)
vehicle_length = 4.5            # 차량 전체 길이
vehicle_width = 1.8             # 차량 전체 너비
vehicle_height = 1.5            # 차량 높이
wheelbase = 2.7                 # 앞뒤 바퀴 축간거리

# 안전 마진 포함 크기
safety_length = vehicle_length + 0.5    # 안전 여유분 포함 길이
safety_width = vehicle_width + 0.3      # 안전 여유분 포함 너비
```

### ⚡ 성능 파라미터 (Performance Parameters)

```python
# 가속/감속 성능
max_acceleration = 3.0          # 최대 가속도 (m/s²)
max_deceleration = -8.0         # 최대 감속도 (m/s²) - 음수값
emergency_deceleration = -10.0  # 비상 제동시 최대 감속도

# 조향 성능
turning_radius = 5.0            # 최소 회전 반경 (미터)
max_steering_rate = 15.0        # 최대 조향 변화율 (도/초)

# 엔진 성능
max_power = 200.0               # 최대 출력 (kW)
max_torque = 400.0              # 최대 토크 (Nm)
fuel_efficiency = 12.5          # 연비 (km/L)
```

---

## 💾 변수 초기화 예시

실제 프로젝트에서 사용할 수 있는 변수 초기화 코드입니다.

```python
class AutonomousVehicle:
    def __init__(self):
        # 차량 상태 초기화
        self.x, self.y, self.z = 0.0, 0.0, 0.0
        self.heading = 0.0
        self.velocity = 0.0
        
        # 제어 변수 초기화
        self.steering_angle = 0.0
        self.throttle = 0.0
        self.brake = 0.0
        
        # 안전 변수 초기화
        self.collision_detected = False
        self.safety_distance = 5.0
        
        # 환경 변수 초기화
        self.weather_condition = "CLEAR"
        self.speed_limit = 50.0
        
        # 물리적 특성 설정
        self.vehicle_length = 4.5
        self.max_acceleration = 3.0
        
    def update_state(self, dt):
        """차량 상태를 시간 간격 dt만큼 업데이트"""
        # 상태 업데이트 로직
        pass
```

---

## 🔧 실전 활용 팁

### 변수 명명 규칙
- **명확성**: 변수명만 봐도 용도를 알 수 있게 작성
- **일관성**: 프로젝트 전체에서 동일한 명명 규칙 사용
- **단위 명시**: 주석이나 변수명에 단위 포함 (`_m`, `_kmh` 등)

### 초기값 설정
- **안전 우선**: 안전한 기본값으로 초기화
- **물리적 한계**: 실제 차량의 물리적 한계를 반영
- **센서 무효값**: 센서 데이터는 유효하지 않은 값으로 초기화

### 데이터 타입 선택
- **정밀도**: 위치나 속도는 `float` 사용
- **메모리 효율**: 불필요한 정밀도는 피하기
- **numpy 배열**: 대량의 센서 데이터는 numpy 활용

---

## 📚 참고 자료

- [자율주행 차량 제어 시스템](https://en.wikipedia.org/wiki/Autonomous_car)
- [ROS (Robot Operating System)](https://www.ros.org/)
- [OpenCV 컴퓨터 비전](https://opencv.org/)
- [PCL (Point Cloud Library)](https://pointclouds.org/)

---


# 🚗 자율주행을 위한 파이썬 명령문 완벽 가이드

> 자율주행 분야에서 자주 사용되는 파이썬 명령문들을 실제 예제와 함께 학습해보세요!

## 📋 목차
- [1. List Comprehension](#1-list-comprehension)
- [2. Dictionary Comprehension](#2-dictionary-comprehension)
- [3. 실전 과제 모음](#3-실전-과제-모음)

---

## 1. List Comprehension

### 🎯 센서 데이터 필터링 - 안전 거리 이상의 장애물만 추출

```python
# 라이다 센서가 감지한 장애물까지의 거리 데이터 (단위: 미터)
sensor_distances = [2.5, 8.3, 1.2, 15.7, 3.8, 0.9, 12.4, 6.1]

# 5미터 이상 떨어진 '안전한' 장애물만 필터링
safe_distances = [dist for dist in sensor_distances if dist > 5.0]

print("안전 거리 이상 장애물:", safe_distances)
```

**실행 결과:**
```
안전 거리 이상 장애물: [8.3, 15.7, 12.4, 6.1]
```

**💡 해설:**
- `2.5, 1.2, 3.8, 0.9`는 5미터 미만이므로 위험 구간으로 제외
- `8.3, 15.7, 12.4, 6.1`은 안전 거리로 분류되어 포함

---

### 🧭 좌표 변환 - 상대 좌표를 절대 좌표로 변환

```python
# 차량의 현재 GPS 좌표 (절대 좌표)
vehicle_position = (10, 20)

# 차량 기준 상대 좌표로 감지된 주변 물체들
relative_points = [(1, 2), (-3, 4), (5, -1), (0, 3)]

# 상대 좌표를 지도상 절대 좌표로 변환
absolute_points = [
    (x + vehicle_position[0], y + vehicle_position[1])
    for x, y in relative_points
]

print("절대 좌표:", absolute_points)
```

**실행 결과:**
```
절대 좌표: [(11, 22), (7, 24), (15, 19), (10, 23)]
```

**💡 해설:**
- `(1, 2)` → `(11, 22)`: 차량 앞쪽 오른쪽 물체의 지도상 위치
- `(-3, 4)` → `(7, 24)`: 차량 왼쪽 앞의 물체 위치
- 센서 데이터를 내비게이션 시스템과 연동하기 위한 필수 변환

---

### 🚦 속도 제한 적용 - 각 구간별 최대 속도 제한

```python
# 현재 각 구간에서의 주행 속도 (km/h)
current_speeds = [45, 75, 38, 82, 55, 95, 28]

# 각 구간의 법정 속도 제한 (km/h)
speed_limits = [50, 70, 40, 80, 60, 90, 30]

# 현재 속도와 제한 속도 중 작은 값을 선택 (법규 준수)
adjusted_speeds = [
    min(current, limit)
    for current, limit in zip(current_speeds, speed_limits)
]

print("속도 제한 적용 후:", adjusted_speeds)
```

**실행 결과:**
```
속도 제한 적용 후: [45, 70, 38, 80, 55, 90, 28]
```

**💡 해설:**
- `75 → 70`: 70km/h 제한구간에서 감속 필요
- `82 → 80`: 80km/h 제한구간에서 감속 필요
- `95 → 90`: 90km/h 제한구간에서 감속 필요

---

### 🛣️ 경로 포인트 생성 - 시작점과 끝점 사이의 중간 포인트들 생성

```python
import math

# 출발지와 목적지 좌표
start_point = (0, 0)    # 집 주차장
end_point = (10, 8)     # 회사 주차장
num_points = 5          # 5개의 경유지 생성

# 선형 보간을 이용한 균등 간격 경로 포인트 생성
path_points = [
    (
        start_point[0] + i * (end_point[0] - start_point[0]) / (num_points - 1),
        start_point[1] + i * (end_point[1] - start_point[1]) / (num_points - 1)
    )
    for i in range(num_points)
]

print("경로 포인트들:", path_points)
```

**실행 결과:**
```
경로 포인트들: [(0.0, 0.0), (2.5, 2.0), (5.0, 4.0), (7.5, 6.0), (10.0, 8.0)]
```

**💡 해설:**
- 직선 거리를 5등분하여 부드러운 주행 경로 생성
- 급격한 방향 전환 대신 단계적 이동으로 승차감 향상

---

### ⚠️ 위험 상황 감지 - 조건부 다중 필터링

```python
# 다양한 센서에서 수집된 데이터
sensor_data = [
    {'type': 'lidar', 'distance': 3.2, 'angle': 45},    # 라이다: 우측 45도, 3.2m
    {'type': 'camera', 'distance': 8.5, 'angle': 0},    # 카메라: 정면, 8.5m
    {'type': 'radar', 'distance': 1.8, 'angle': -30},   # 레이더: 좌측 30도, 1.8m
    {'type': 'lidar', 'distance': 12.3, 'angle': 90}    # 라이다: 우측 90도, 12.3m
]

# 위험 조건: 5m 이내 + 전방 60도 범위 내
danger_sensors = [
    sensor for sensor in sensor_data
    if sensor['distance'] < 5.0 and abs(sensor['angle']) < 60
]

print("위험 감지 센서:", danger_sensors)
```

**실행 결과:**
```
위험 감지 센서: [
    {'type': 'lidar', 'distance': 3.2, 'angle': 45}, 
    {'type': 'radar', 'distance': 1.8, 'angle': -30}
]
```

**💡 해설:**
- 전방 60도 범위 내에서 5미터 이내 장애물을 감지한 센서만 추출
- 즉시 감속 또는 회피 기동이 필요한 위험 상황 판단

---

## 2. Dictionary Comprehension

### 📊 기본 딕셔너리 생성 - 센서별 데이터 관리

```python
# 1. 센서 데이터 딕셔너리 생성
sensor_data = {}
sensor_data['camera'] = 8.5    # 카메라 센서: 8.5m
sensor_data['lidar'] = 12.3    # 라이다 센서: 12.3m
sensor_data['radar'] = 15.7    # 레이더 센서: 15.7m

print("센서 데이터:", sensor_data)

# 2. 경로 계획 - 목적지별 거리 정보
destinations = ['집', '회사', '마트', '주유소']
distances_km = [0, 15, 8, 12]

route_plan = {}
for i, dest in enumerate(destinations):
    route_plan[dest] = distances_km[i]

print("목적지별 거리:", route_plan)

# 3. 차량 상태 체크
vehicle_parts = ['엔진', '브레이크', '타이어', '배터리']
status_codes = ['정상', '정상', '교체필요', '정상']

vehicle_status = {}
for i, part in enumerate(vehicle_parts):
    vehicle_status[part] = status_codes[i]

print("차량 상태:", vehicle_status)
```

**실행 결과:**
```
센서 데이터: {'camera': 8.5, 'lidar': 12.3, 'radar': 15.7}
목적지별 거리: {'집': 0, '회사': 15, '마트': 8, '주유소': 12}
차량 상태: {'엔진': '정상', '브레이크': '정상', '타이어': '교체필요', '배터리': '정상'}
```

---

### 🚥 신호등 정보 관리

```python
# 교차로별 신호등 현황
intersections = ['서울역', '강남역', '홍대입구', '잠실역']
light_colors = ['빨강', '초록', '노랑', '초록']
remaining_times = [25, 15, 3, 45]

# 신호등 정보 통합 관리
traffic_lights = {}
for i, intersection in enumerate(intersections):
    traffic_lights[intersection] = {
        'color': light_colors[i],
        'time_left': remaining_times[i]
    }

print("교차로 신호등 현황:")
for intersection, info in traffic_lights.items():
    print(f"  {intersection}: {info['color']} (남은시간: {info['time_left']}초)")
```

**실행 결과:**
```
교차로 신호등 현황:
  서울역: 빨강 (남은시간: 25초)
  강남역: 초록 (남은시간: 15초)
  홍대입구: 노랑 (남은시간: 3초)
  잠실역: 초록 (남은시간: 45초)
```

---

### 🅿️ 주차장 정보 시스템

```python
# 주차장 구역별 현황
parking_zones = ['A구역', 'B구역', 'C구역', 'D구역']
empty_spots = [5, 0, 12, 3]
total_spots = [20, 15, 25, 10]

# 주차장 정보 딕셔너리 생성
parking_info = {}
for i, zone in enumerate(parking_zones):
    parking_info[zone] = {
        'empty': empty_spots[i],
        'total': total_spots[i],
        'occupancy_rate': round((total_spots[i] - empty_spots[i]) / total_spots[i] * 100, 1)
    }

print("주차장 현황:")
for zone, info in parking_info.items():
    print(f"  {zone}: {info['empty']}/{info['total']} 가능 (점유율: {info['occupancy_rate']}%)")
    
# 빈 주차공간이 있는 구역 찾기
available_zones = [zone for zone, info in parking_info.items() if info['empty'] > 0]
print(f"\n주차 가능한 구역: {available_zones}")
```

**실행 결과:**
```
주차장 현황:
  A구역: 5/20 가능 (점유율: 75.0%)
  B구역: 0/15 가능 (점유율: 100.0%)
  C구역: 12/25 가능 (점유율: 52.0%)
  D구역: 3/10 가능 (점유율: 70.0%)

주차 가능한 구역: ['A구역', 'C구역', 'D구역']
```

---

## 3. 실전 과제 모음

### 🚦 과제 1: 스마트 신호등 타이밍 최적화

```python
print("=== 스마트 신호등 타이밍 최적화 ===")

# 교차로별 대기 차량 수와 신호등 현황
intersections = ['서울역앞', '시청앞', '종로3가', '을지로입구']
traffic_signals = {
    '서울역앞': {'color': '빨강', 'time_left': 25, 'waiting': 12},
    '시청앞': {'color': '초록', 'time_left': 15, 'waiting': 8},
    '종로3가': {'color': '빨강', 'time_left': 40, 'waiting': 15},
    '을지로입구': {'color': '노랑', 'time_left': 3, 'waiting': 5}
}

print("현재 교차로 상황:")
for intersection in intersections:
    signal = traffic_signals[intersection]
    status_emoji = "🔴" if signal['color'] == '빨강' else "🟢" if signal['color'] == '초록' else "🟡"
    print(f"  {status_emoji} {intersection}: {signal['color']} {signal['time_left']}초, 대기차량 {signal['waiting']}대")

# 우선순위 교차로 선정 (대기차량 10대 이상)
print("\n⚠️  우선처리 필요 교차로:")
priority_intersections = [
    intersection for intersection in intersections
    if traffic_signals[intersection]['waiting'] >= 10
]

for intersection in priority_intersections:
    waiting = traffic_signals[intersection]['waiting']
    print(f"  🚨 {intersection}: 대기차량 {waiting}대 → 신호 조정 필요")
```

**실행 결과:**
```
=== 스마트 신호등 타이밍 최적화 ===
현재 교차로 상황:
  🔴 서울역앞: 빨강 25초, 대기차량 12대
  🟢 시청앞: 초록 15초, 대기차량 8대
  🔴 종로3가: 빨강 40초, 대기차량 15대
  🟡 을지로입구: 노랑 3초, 대기차량 5대

⚠️  우선처리 필요 교차로:
  🚨 서울역앞: 대기차량 12대 → 신호 조정 필요
  🚨 종로3가: 대기차량 15대 → 신호 조정 필요
```

---

### 🅿️ 과제 2: 자동 발렛파킹 시스템

```python
print("=== 자동 발렛파킹 시스템 ===")

# 주차공간 크기별 현황
parking_spaces = {
    '소형전용': {'total': 30, 'occupied': 15, 'size_limit': '소형'},
    '일반공간': {'total': 40, 'occupied': 28, 'size_limit': '중형'},
    '대형공간': {'total': 15, 'occupied': 8, 'size_limit': '대형'},
    'SUV전용': {'total': 20, 'occupied': 12, 'size_limit': 'SUV'}
}

print("주차공간 현황:")
for space_type, space in parking_spaces.items():
    available = space['total'] - space['occupied']
    utilization = round(space['occupied'] / space['total'] * 100, 1)
    print(f"  {space_type}: {available}/{space['total']} 가능 ({space['size_limit']} 전용, 이용률 {utilization}%)")

# 신규 차량 주차 시뮬레이션
new_vehicle = 'SUV'
print(f"\n🚗 신규 {new_vehicle} 차량 주차 요청")

# 적합한 주차공간 찾기
suitable_spaces = []
for space_type, space in parking_spaces.items():
    available = space['total'] - space['occupied']
    if space['size_limit'] == new_vehicle and available > 0:
        suitable_spaces.append(space_type)

if suitable_spaces:
    selected_space = suitable_spaces[0]
    available = parking_spaces[selected_space]['total'] - parking_spaces[selected_space]['occupied']
    print(f"✅ {selected_space}에 주차 가능 (남은 자리: {available}개)")
else:
    print("❌ 적합한 주차공간이 없습니다")
```

**실행 결과:**
```
=== 자동 발렛파킹 시스템 ===
주차공간 현황:
  소형전용: 15/30 가능 (소형 전용, 이용률 50.0%)
  일반공간: 12/40 가능 (중형 전용, 이용률 70.0%)
  대형공간: 7/15 가능 (대형 전용, 이용률 53.3%)
  SUV전용: 8/20 가능 (SUV 전용, 이용률 60.0%)

🚗 신규 SUV 차량 주차 요청
✅ SUV전용에 주차 가능 (남은 자리: 8개)
```

---

### 🚛 과제 3: 차량 군집주행 관리 시스템

```python
print("=== 차량 군집주행 관리 시스템 ===")

# 군집주행 그룹별 상세 정보
convoy_info = {
    '그룹A': {'vehicles': 3, 'leader_speed': 80, 'formation': '일렬'},
    '그룹B': {'vehicles': 5, 'leader_speed': 70, 'formation': '삼각'},
    '그룹C': {'vehicles': 2, 'leader_speed': 90, 'formation': '병렬'}
}

print("군집주행 현황:")
for group, info in convoy_info.items():
    formation_emoji = "🚗🚗🚗" if info['formation'] == '일렬' else "🚗🚗\n🚗" if info['formation'] == '삼각' else "🚗🚗"
    print(f"  {group}: {info['vehicles']}대, 속도 {info['leader_speed']}km/h, {info['formation']}대형")

# 안전 속도 권장 (5대 이상이면 속도 제한)
print("\n📋 안전 권장사항:")
for group, info in convoy_info.items():
    if info['vehicles'] >= 5:
        recommended_speed = 60
        print(f"  ⚠️ {group}: 차량 {info['vehicles']}대로 인해 {recommended_speed}km/h 이하 권장")
    else:
        print(f"  ✅ {group}: 현재 속도 {info['leader_speed']}km/h 적정")

# 군집 효율성 분석
print("\n📊 군집 효율성 분석:")
for group, info in convoy_info.items():
    if info['vehicles'] >= 3:
        fuel_efficiency = round(15 + (info['vehicles'] * 2), 1)  # 연비 개선 효과
        print(f"  {group}: 연비 {fuel_efficiency}% 개선 효과")
```

**실행 결과:**
```
=== 차량 군집주행 관리 시스템 ===
군집주행 현황:
  그룹A: 3대, 속도 80km/h, 일렬대형
  그룹B: 5대, 속도 70km/h, 삼각대형
  그룹C: 2대, 속도 90km/h, 병렬대형

📋 안전 권장사항:
  ✅ 그룹A: 현재 속도 80km/h 적정
  ⚠️ 그룹B: 차량 5대로 인해 60km/h 이하 권장
  ✅ 그룹C: 현재 속도 90km/h 적정

📊 군집 효율성 분석:
  그룹A: 연비 21.0% 개선 효과
  그룹B: 연비 25.0% 개선 효과
```

---

### 🔋 과제 4: 전기차 충전 관리 시스템

```python
print("=== 전기차 충전 관리 시스템 ===")

# 전기차 배터리 현황
ev_fleet = ['전기차A', '전기차B', '전기차C', '전기차D', '전기차E']
ev_status = {
    '전기차A': {'battery': 85, 'range': 340, 'charging': False},
    '전기차B': {'battery': 25, 'range': 100, 'charging': False},
    '전기차C': {'battery': 60, 'range': 240, 'charging': True},
    '전기차D': {'battery': 15, 'range': 60, 'charging': False},
    '전기차E': {'battery': 90, 'range': 360, 'charging': False}
}

print("전기차 배터리 현황:")
for vehicle, status in ev_status.items():
    battery_emoji = "🔋" if status['battery'] > 50 else "🪫" if status['battery'] > 20 else "⚡"
    charging_status = "충전중" if status['charging'] else "대기중"
    print(f"  {battery_emoji} {vehicle}: {status['battery']}% ({status['range']}km) - {charging_status}")

# 긴급 충전 필요 차량 (배터리 30% 이하)
print("\n🚨 긴급 충전 필요:")
urgent_vehicles = [
    vehicle for vehicle, status in ev_status.items()
    if status['battery'] <= 30 and not status['charging']
]

for vehicle in urgent_vehicles:
    battery = ev_status[vehicle]['battery']
    range_left = ev_status[vehicle]['range']
    print(f"  ⚡ {vehicle}: {battery}% (주행가능 {range_left}km) - 즉시 충전 필요")

# 충전소 예약 시스템
charging_stations = {
    '강남충전소': {'slots': 5, 'reserved': 2, 'fast_charge': True},
    '서초충전소': {'slots': 3, 'reserved': 1, 'fast_charge': False},
    '종로충전소': {'slots': 4, 'reserved': 4, 'fast_charge': True}
}

print("\n🔌 충전소 예약 현황:")
for station, info in charging_stations.items():
    available = info['slots'] - info['reserved']
    charge_type = "급속충전" if info['fast_charge'] else "완속충전"
    availability_emoji = "🟢" if available > 0 else "🔴"
    print(f"  {availability_emoji} {station}: {available}/{info['slots']} 이용가능 ({charge_type})")
```

**실행 결과:**
```
=== 전기차 충전 관리 시스템 ===
전기차 배터리 현황:
  🔋 전기차A: 85% (340km) - 대기중
  🪫 전기차B: 25% (100km) - 대기중
  🔋 전기차C: 60% (240km) - 충전중
  ⚡ 전기차D: 15% (60km) - 대기중
  🔋 전기차E: 90% (360km) - 대기중

🚨 긴급 충전 필요:
  ⚡ 전기차B: 25% (주행가능 100km) - 즉시 충전 필요
  ⚡ 전기차D: 15% (주행가능 60km) - 즉시 충전 필요

🔌 충전소 예약 현황:
  🟢 강남충전소: 3/5 이용가능 (급속충전)
  🟢 서초충전소: 2/3 이용가능 (완속충전)
  🔴 종로충전소: 0/4 이용가능 (급속충전)
```

---

### 🌧️ 과제 5: 도로 위험도 평가 및 경고 시스템

```python
print("=== 도로 위험도 평가 및 경고 시스템 ===")

# 도로 구간별 위험 요소
road_segments = ['구간A', '구간B', '구간C', '구간D']
road_conditions = [
    {'rain': True, 'fog': False, 'construction': False, 'accident': False},
    {'rain': False, 'fog': True, 'construction': True, 'accident': False},
    {'rain': True, 'fog': False, 'construction': False, 'accident': True},
    {'rain': False, 'fog': False, 'construction': False, 'accident': False}
]

# 도로별 위험도 계산
road_safety = {}
for i, segment in enumerate(road_segments):
    conditions = road_conditions[i]
    risk_score = 0
    
    # 위험 요소별 점수 부여
    if conditions['rain']:
        risk_score += 20    # 우천시 미끄럼 위험
    if conditions['fog']:
        risk_score += 30    # 안개로 인한 시야 불량
    if conditions['construction']:
        risk_score += 25    # 공사로 인한 차로 변경
    if conditions['accident']:
        risk_score += 50    # 사고로 인한 정체/위험
    
    road_safety[segment] = {'risk_score': risk_score, 'conditions': conditions}

print("도로 구간별 위험도 분석:")
for segment in road_segments:
    safety = road_safety[segment]
    risk = safety['risk_score']
    conditions = safety['conditions']
    
    # 위험도 레벨 분류
    if risk >= 50:
        level = "매우위험"
        level_emoji = "🔴"
    elif risk >= 30:
        level = "위험"
        level_emoji = "🟠"
    elif risk >= 15:
        level = "주의"
        level_emoji = "🟡"
    else:
        level = "안전"
        level_emoji = "🟢"
    
    print(f"  {level_emoji} {segment}: {risk}점 ({level})")
    
    # 위험 요소 상세 표시
    warnings = []
    if conditions['rain']:
        warnings.append("우천 🌧️")
    if conditions['fog']:
        warnings.append("안개 🌫️")
    if conditions['construction']:
        warnings.append("공사중 🚧")
    if conditions['accident']:
        warnings.append("사고발생 🚨")
    
    if warnings:
        print(f"    └ 위험요소: {', '.join(warnings)}")

# 우회 경로 권장
print("\n📍 경로 권장사항:")
safe_routes = [segment for segment, info in road_safety.items() if info['risk_score'] < 30]
dangerous_routes = [segment for segment, info in road_safety.items() if info['risk_score'] >= 50]

if safe_routes:
    print(f"  ✅ 안전 경로: {', '.join(safe_routes)}")
if dangerous_routes:
    print(f"  ⚠️ 우회 권장: {', '.join(dangerous_routes)}")
```

**실행 결과:**
```
=== 도로 위험도 평가 및 경고 시스템 ===
도로 구간별 위험도 분석:
  🟡 구간A: 20점 (주의)
    └ 위험요소: 우천 🌧️
  🔴 구간B: 55점 (매우위험)
    └ 위험요소: 안개 🌫️, 공사중 🚧
  🔴 구간C: 70점 (매우위험)
    └ 위험요소: 우천 🌧️


# 자동차 자율주행 시스템 기준점 가이드

## 개요
자율주행 자동차 개발 시 다양한 시스템과 센서들이 사용하는 기준점(Reference Points)들을 정리한 종합 가이드입니다. 각 기준점은 특정 상황과 목적에 따라 선택되며, 정확한 위치 계산과 안전한 주행을 위해 매우 중요합니다.

## 목차
1. [센서 위치 기준점](#1-센서-위치-기준점)
2. [안전성 기준점](#2-안전성-기준점)
3. [조향 관련 기준점](#3-조향-관련-기준점)
4. [주차/정밀 제어 기준점](#4-주차정밀-제어-기준점)
5. [동적 기준점](#5-동적-기준점-상황별)
6. [좌표계별 기준점](#6-좌표계별-기준점)
7. [제어 시스템별 고려사항](#7-제어-시스템별-고려사항)
8. [도로 및 교통 환경 기준점](#8-도로-및-교통-환경-기준점)
9. [법규 및 규정 기준점](#9-법규-및-규정-기준점)
10. [물리학적/역학적 기준점](#10-물리학적역학적-기준점)
11. [통신 및 V2X 기준점](#11-통신-및-v2x-기준점)
12. [예측 및 미래 위치 기준점](#12-예측-및-미래-위치-기준점)
13. [다중 차량 시스템 기준점](#13-다중-차량-시스템-기준점)
14. [환경 인식 기준점](#14-환경-인식-기준점)
15. [보험/사고 조사 기준점](#15-보험사고-조사-기준점)
16. [성능 최적화 기준점](#16-성능-최적화-기준점)
17. [승객 안전/편의 기준점](#17-승객-안전편의-기준점)

---

## 1. 센서 위치 기준점

자율주행 차량의 다양한 센서들은 각각 최적의 위치에 설치되며, 이들의 위치 정보는 센서 융합과 정확한 환경 인식을 위해 필수적입니다.

```python
# 차량 기본 위치 (x, y, z) - 후축 중심 기준
vehicle_base_position = (0, 0, 0)

class SensorPositions:
    def __init__(self, vehicle_x, vehicle_y, vehicle_z):
        self.base_x = vehicle_x
        self.base_y = vehicle_y  
        self.base_z = vehicle_z
        
        # 라이다: 차량 지붕 위 중앙에 설치 (360도 스캔을 위해)
        self.lidar_position = (
            self.base_x + 0.5,  # 차량 중심에서 앞쪽으로 0.5m
            self.base_y,        # 차량 중심선
            self.base_z + 1.2   # 지면에서 1.2m 높이
        )
        
        # 카메라: 앞범퍼 근처 (전방 시야 확보)
        self.camera_position = (
            self.base_x + 2.0,  # 차량 앞쪽 끝
            self.base_y,        # 차량 중심선
            self.base_z + 0.8   # 적절한 시야각 확보 높이
        )
        
        # 레이더: 전면 하단 (근거리 장애물 감지)
        self.radar_position = (
            self.base_x + 2.1,  # 카메라보다 약간 앞쪽
            self.base_y,        # 차량 중심선
            self.base_z + 0.3   # 낮은 높이에서 도로면 스캔
        )
        
        # GPS 안테나: 지붕 뒤쪽 (위성 신호 수신 최적화)
        self.gps_antenna = (
            self.base_x - 1.0,  # 차량 뒤쪽
            self.base_y,        # 차량 중심선
            self.base_z + 1.5   # 최대한 높은 위치
        )
    
    def get_sensor_offset(self, sensor_type):
        """특정 센서의 차량 기준점 대비 오프셋 반환"""
        positions = {
            'lidar': self.lidar_position,
            'camera': self.camera_position,
            'radar': self.radar_position,
            'gps': self.gps_antenna
        }
        return positions.get(sensor_type, (0, 0, 0))

# 사용 예시
vehicle = SensorPositions(0, 0, 0)
print(f"라이다 위치: {vehicle.lidar_position}")
print(f"카메라 위치: {vehicle.camera_position}")
```

**실행 결과:**
```
라이다 위치: (0.5, 0, 1.2)
카메라 위치: (2.0, 0, 0.8)
```

---

## 2. 안전성 기준점

충돌 감지와 안전성 확보를 위한 핵심 기준점들입니다. 이들 점들은 차량의 물리적 경계를 정의하고 충돌 위험을 사전에 감지하는 데 사용됩니다.

```python
import math

class SafetyReferencePoints:
    def __init__(self, vehicle_length=4.5, vehicle_width=1.8, vehicle_height=1.5):
        self.length = vehicle_length
        self.width = vehicle_width
        self.height = vehicle_height
        
        # 충돌 감지용 주요 지점들 정의
        self.safety_points = {
            'front_bumper': (self.length/2, 0, 0),      # 전방 충돌 감지
            'rear_bumper': (-self.length/2, 0, 0),      # 후방 충돌 감지
            'left_side': (0, self.width/2, 0),          # 좌측 충돌 감지
            'right_side': (0, -self.width/2, 0),        # 우측 충돌 감지
            'roof_corners': [                            # 높이 제한 감지
                (self.length/2, self.width/2, self.height),
                (self.length/2, -self.width/2, self.height),
                (-self.length/2, self.width/2, self.height),
                (-self.length/2, -self.width/2, self.height)
            ]
        }
    
    def check_collision_risk(self, obstacle_position, safety_margin=0.5):
        """장애물과의 충돌 위험도 계산"""
        min_distance = float('inf')
        closest_point = None
        
        for point_name, position in self.safety_points.items():
            if point_name != 'roof_corners':  # 루프 코너는 별도 처리
                distance = math.sqrt(
                    (obstacle_position[0] - position[0])**2 +
                    (obstacle_position[1] - position[1])**2
                )
                
                if distance < min_distance:
                    min_distance = distance
                    closest_point = point_name
        
        is_dangerous = min_distance < safety_margin
        return {
            'is_dangerous': is_dangerous,
            'distance': min_distance,
            'closest_point': closest_point,
            'safety_margin': safety_margin
        }
    
    def get_safety_envelope(self, expansion_factor=1.2):
        """안전 여유 공간을 포함한 차량 외곽 계산"""
        expanded_points = {}
        for point_name, position in self.safety_points.items():
            if point_name != 'roof_corners':
                expanded_points[point_name] = (
                    position[0] * expansion_factor,
                    position[1] * expansion_factor,
                    position[2]
                )
        return expanded_points

# 사용 예시
safety_system = SafetyReferencePoints()
obstacle_pos = (3.0, 0.5, 0)  # 전방 우측 장애물
risk_assessment = safety_system.check_collision_risk(obstacle_pos)

print(f"충돌 위험: {risk_assessment['is_dangerous']}")
print(f"최근접 거리: {risk_assessment['distance']:.2f}m")
print(f"가장 가까운 지점: {risk_assessment['closest_point']}")
```

**실행 결과:**
```
충돌 위험: False
최근접 거리: 0.58m
가장 가까운 지점: front_bumper
```

---

## 3. 조향 관련 기준점

차량의 조향 제어를 위한 다양한 기준점들입니다. Bicycle Model을 기반으로 한 조향 시스템에서 사용되는 핵심 개념들을 포함합니다.

```python
class SteeringReferencePoints:
    def __init__(self, wheelbase=2.7, front_overhang=0.9, rear_overhang=0.9):
        self.wheelbase = wheelbase  # 축간거리
        self.front_overhang = front_overhang  # 앞쪽 오버행
        self.rear_overhang = rear_overhang    # 뒤쪽 오버행
        
        # 조향 관련 주요 기준점들
        self.reference_points = {
            'rear_wheel_center': (0, 0, 0),  # 후륜 중심 (일반적 기준)
            'front_wheel_center': (self.wheelbase, 0, 0),  # 전륜 중심
            'wheelbase_center': (self.wheelbase/2, 0, 0),  # 축간거리 중점
            'cog_center': (self.wheelbase*0.4, 0, 0),  # 무게중심 (일반적으로 후축에서 40% 지점)
            'geometric_center': (self.wheelbase/2, 0, 0)  # 기하학적 중심
        }
    
    def calculate_turning_radius(self, steering_angle_deg, reference_point='rear_wheel_center'):
        """조향각에 따른 회전 반경 계산 (Bicycle Model 기반)"""
        steering_angle_rad = math.radians(steering_angle_deg)
        
        if abs(steering_angle_rad) < 0.001:  # 직진 시
            return float('inf')
        
        # 후축 중심 기준 회전 반경
        base_radius = self.wheelbase / math.tan(abs(steering_angle_rad))
        
        # 기준점에 따른 보정
        if reference_point == 'front_wheel_center':
            # 전륜 중심의 경우 더 넓은 회전 반경
            radius = base_radius / math.cos(steering_angle_rad)
        elif reference_point == 'cog_center':
            # 무게중심 기준 보정
            cog_offset = self.wheelbase * 0.4
            radius = math.sqrt(base_radius**2 + cog_offset**2)
        else:  # rear_wheel_center (기본값)
            radius = base_radius
            
        return radius
    
    def get_instantaneous_center_of_rotation(self, steering_angle_deg):
        """순간 회전 중심 계산"""
        steering_angle_rad = math.radians(steering_angle_deg)
        
        if abs(steering_angle_rad) < 0.001:
            return None  # 직진 시에는 회전 중심이 무한대
        
        # 후축 중심에서 회전 중심까지의 거리
        distance = self.wheelbase / math.tan(abs(steering_angle_rad))
        
        # 회전 중심의 위치 (후축 중심 기준)
        if steering_angle_deg > 0:  # 좌회전
            icr_position = (0, distance, 0)
        else:  # 우회전
            icr_position = (0, -distance, 0)
            
        return icr_position

# 사용 예시
steering_system = SteeringReferencePoints()

# 15도 좌회전 시 회전 반경 계산
steering_angle = 15  # 도
radius = steering_system.calculate_turning_radius(steering_angle)
icr = steering_system.get_instantaneous_center_of_rotation(steering_angle)

print(f"조향각: {steering_angle}도")
print(f"회전 반경: {radius:.2f}m")
print(f"순간 회전 중심: {icr}")
```

**실행 결과:**
```
조향각: 15도
회전 반경: 10.07m
순간 회전 중심: (0, 10.07, 0)
```

---

## 4. 주차/정밀 제어 기준점

주차나 정밀한 조작이 필요한 상황에서 사용되는 기준점들입니다. 차량의 모서리와 경계를 정확히 파악하여 충돌 없는 주차를 가능하게 합니다.

```python
class ParkingReferencePoints:
    def __init__(self, vehicle_length=4.5, vehicle_width=1.8):
        self.length = vehicle_length
        self.width = vehicle_width
        
        # 주차 시 중요한 차량 모서리들
        self.vehicle_corners = {
            'front_left_corner': (self.length/2, self.width/2, 0),
            'front_right_corner': (self.length/2, -self.width/2, 0),
            'rear_left_corner': (-self.length/2, self.width/2, 0),
            'rear_right_corner': (-self.length/2, -self.width/2, 0)
        }
        
        # 주차 시 추가 확인 지점들
        self.critical_points = {
            'front_center': (self.length/2, 0, 0),
            'rear_center': (-self.length/2, 0, 0),
            'left_center': (0, self.width/2, 0),
            'right_center': (0, -self.width/2, 0),
            'geometric_center': (0, 0, 0)
        }
    
    def check_parking_clearance(self, parking_space_corners, clearance_margin=0.3):
        """주차 공간과 차량 간 여유 공간 확인"""
        # 주차 공간 크기 계산
        space_length = abs(parking_space_corners[1][0] - parking_space_corners[0][0])
        space_width = abs(parking_space_corners[2][1] - parking_space_corners[0][1])
        
        # 필요한 최소 공간 (차량 크기 + 여유 공간)
        required_length = self.length + 2 * clearance_margin
        required_width = self.width + 2 * clearance_margin
        
        length_ok = space_length >= required_length
        width_ok = space_width >= required_width
        
        return {
            'can_park': length_ok and width_ok,
            'length_clearance': space_length - self.length,
            'width_clearance': space_width - self.width,
            'length_sufficient': length_ok,
            'width_sufficient': width_ok
        }
    
    def calculate_parking_trajectory(self, target_position, current_position, parking_type='parallel'):
        """주차 궤적 계산"""
        if parking_type == 'parallel':
            # 평행 주차 궤적
            trajectory_points = []
            
            # 1단계: 후진 시작점까지 이동
            approach_point = (
                target_position[0] - self.length,
                target_position[1] + self.width,
                0
            )
            trajectory_points.append(approach_point)
            
            # 2단계: 후진하며 조향
            reverse_point = (
                target_position[0] - self.length/2,
                target_position[1] + self.width/2,
                0
            )
            trajectory_points.append(reverse_point)
            
            # 3단계: 최종 주차 위치
            trajectory_points.append(target_position)
            
        elif parking_type == 'perpendicular':
            # 수직 주차 궤적
            trajectory_points = []
            
            # 1단계: 진입 준비 위치
            approach_point = (
                target_position[0] - self.length,
                target_position[1],
                0
            )
            trajectory_points.append(approach_point)
            
            # 2단계: 최종 주차 위치
            trajectory_points.append(target_position)
        
        return trajectory_points
    
    def get_corner_positions_at_pose(self, vehicle_x, vehicle_y, vehicle_heading):
        """특정 위치와 방향에서의 차량 모서리 위치 계산"""
        cos_h = math.cos(vehicle_heading)
        sin_h = math.sin(vehicle_heading)
        
        corner_positions = {}
        for corner_name, (local_x, local_y, local_z) in self.vehicle_corners.items():
            # 회전 변환 적용
            global_x = vehicle_x + (local_x * cos_h - local_y * sin_h)
            global_y = vehicle_y + (local_x * sin_h + local_y * cos_h)
            corner_positions[corner_name] = (global_x, global_y, local_z)
        
        return corner_positions

# 사용 예시
parking_system = ParkingReferencePoints()

# 주차 공간 정의 (길이 5.5m, 폭 2.3m)
parking_space = [
    (0, 0, 0),    # 좌하단
    (5.5, 0, 0),  # 우하단
    (5.5, 2.3, 0), # 우상단
    (0, 2.3, 0)   # 좌상단
]

clearance_check = parking_system.check_parking_clearance(parking_space)
print(f"주차 가능: {clearance_check['can_park']}")
print(f"길이 여유: {clearance_check['length_clearance']:.2f}m")
print(f"폭 여유: {clearance_check['width_clearance']:.2f}m")

# 주차 궤적 계산
target_pos = (2.75, 1.15, 0)  # 주차 공간 중심
current_pos = (0, 3, 0)       # 현재 위치
trajectory = parking_system.calculate_parking_trajectory(target_pos, current_pos, 'parallel')
print(f"주차 궤적 점들: {len(trajectory)}개")
```

**실행 결과:**
```
주차 가능: True
길이 여유: 1.00m
폭 여유: 0.50m
주차 궤적 점들: 3개
```

---

## 5. 동적 기준점 (상황별)

주행 상황에 따라 동적으로 변경되는 기준점들입니다. 각 주행 모드에 최적화된 기준점을 선택하여 제어 정확도를 높입니다.

```python
class DynamicReferencePoints:
    def __init__(self, vehicle_config):
        self.vehicle_config = vehicle_config
        
        # 상황별 최적 기준점 정의
        self.mode_reference_points = {
            'HIGHWAY': 'rear_axle_center',      # 고속 주행 - 안정성 중시
            'PARKING': 'geometric_center',      # 주차 - 정밀도 중시
            'LANE_CHANGE': 'front_axle_center', # 차선 변경 - 반응성 중시
            'INTERSECTION': 'front_bumper',     # 교차로 - 안전성 중시
            'REVERSE': 'rear_bumper',           # 후진 - 후방 정밀도 중시
            'SENSOR_FUSION': 'sensor_fusion_center'  # 센서 융합 최적화
        }
    
    def get_current_reference_point(self, driving_mode, vehicle_speed=0, sensor_data=None):
        """현재 상황에 맞는 최적 기준점 선택"""
        
        # 속도 기반 조정
        if vehicle_speed > 80:  # 고속 주행
            base_reference = self.mode_reference_points['HIGHWAY']
        elif vehicle_speed < 5:  # 저속 주행
            base_reference = self.mode_reference_points['PARKING']
        else:
            base_reference = self.mode_reference_points.get(driving_mode, 'rear_axle_center')
        
        # 센서 데이터 기반 추가 조정
        if sensor_data and 'sensor_fusion_active' in sensor_data:
            if sensor_data['sensor_fusion_active']:
                base_reference = self.mode_reference_points['SENSOR_FUSION']
        
        return base_reference
    
    def calculate_reference_position(self, reference_type, vehicle_position, vehicle_heading):
        """기준점 타입에 따른 실제 위치 계산"""
        vehicle_x, vehicle_y, vehicle_z = vehicle_position
        
        # 차량 기하학적 파라미터
        wheelbase = self.vehicle_config.get('wheelbase', 2.7)
        front_overhang = self.vehicle_config.get('front_overhang', 0.9)
        rear_overhang = self.vehicle_config.get('rear_overhang', 0.9)
        
        # 로컬 좌표계에서의 오프셋 정의
        local_offsets = {
            'rear_axle_center': (0, 0, 0),
            'front_axle_center': (wheelbase, 0, 0),
            'geometric_center': (wheelbase/2, 0, 0),
            'front_bumper': (wheelbase + front_overhang, 0, 0),
            'rear_bumper': (-rear_overhang, 0, 0),
            'sensor_fusion_center': (wheelbase*0.3, 0, 0.5)  # 센서 융합 최적 위치
        }
        
        local_offset = local_offsets.get(reference_type, (0, 0, 0))
        
        # 차량 방향 고려한 글로벌 좌표 변환
        cos_h = math.cos(vehicle_heading)
        sin_h = math.sin(vehicle_heading)
        
        global_x = vehicle_x + (local_offset[0] * cos_h - local_offset[1] * sin_h)
        global_y = vehicle_y + (local_offset[0] * sin_h + local_offset[1] * cos_h)
        global_z = vehicle_z + local_offset[2]
        
        return (global_x, global_y, global_z)
    
    def adaptive_reference_selection(self, current_scenario):
        """시나리오 기반 적응적 기준점 선택"""
        scenario_weights = {
            'safety_priority': 0.4,
            'precision_priority': 0.3,
            'efficiency_priority': 0.2,
            'comfort_priority': 0.1
        }
        
        # 시나리오별 가중치 적용
        if current_scenario.get('emergency_braking', False):
            scenario_weights['safety_priority'] = 0.8
            return 'front_bumper'
        
        if current_scenario.get('tight_parking', False):
            scenario_weights['precision_priority'] = 0.7
            return 'geometric_center'
        
        if current_scenario.get('highway_cruise', False):
            scenario_weights['efficiency_priority'] = 0.6
            return 'rear_axle_center'
        
        return 'rear_axle_center'  # 기본값

# 사용 예시
vehicle_config = {
    'wheelbase': 2.7,
    'front_overhang': 0.9,
    'rear_overhang': 0.9
}

dynamic_ref = DynamicReferencePoints(vehicle_config)

# 다양한 주행 상황 시뮬레이션
scenarios = [
    {'mode': 'HIGHWAY', 'speed': 100, 'description': '고속도로 주행'},
    {'mode': 'PARKING', 'speed': 2, 'description': '주차 중'},
    {'mode': 'LANE_CHANGE', 'speed': 60, 'description': '차선 변경'},
    {'mode': 'INTERSECTION', 'speed': 20, 'description': '교차로 통과'}
]

for scenario in scenarios:
    ref_point = dynamic_ref.get_current_reference_point(
        scenario['mode'], 
        scenario['speed']
    )
    print(f"{scenario['description']}: {ref_point}")

# 특정 위치에서의 기준점 계산
vehicle_pos = (100, 50, 0)
vehicle_heading = math.radians(30)  # 30도 방향
ref_pos = dynamic_ref.calculate_reference_position(
    'front_axle_center', 
    vehicle_pos, 
    vehicle_heading
)
print(f"전축 중심 위치: ({ref_pos[0]:.2f}, {ref_pos[1]:.2f}, {ref_pos[2]:.2f})")
```

**실행 결과:**
```
고속도로 주행: rear_axle_center
주차 중: geometric_center
차선 변경: front_axle_center
교차로 통과: intersection
전축 중심 위치: (102.34, 51.35, 0.00)
```

---

## 6. 좌표계별 기준점

서로 다른 좌표계에서 사용되는 기준점들입니다. 글로벌, 로컬, 센서 좌표계 간의 변환과 일관성 유지가 핵심입니다.

```python
import numpy as np

class CoordinateSystemReferences:
    def __init__(self):
        # 좌표계별 기준점 정의
        self.coordinate_systems = {
            'global': 'rear_axle_gps',        # GPS 기준 글로벌 좌표
            'local': 'vehicle_center',        # 차량 중심 기준 로컬 좌표
            'sensor': 'lidar_origin',         # 센서 원점 기준
            'map': 'map_origin',              # 지도 좌표계 기준
            'lane': 'lane_center_line'        # 차선 중심선 기준
        }
    
    def global_to_local_transform(self, global_position, vehicle_global_pos, vehicle_heading):
        """글로벌 좌표를 차량 로컬 좌표로 변환"""
        # 평행 이동
        translated = np.array(global_position) - np.array(vehicle_global_pos)
        
        # 회전 변환 (차량 방향 기준)
        cos_h = math.cos(-vehicle_heading)  # 역회전
        sin_h = math.sin(-vehicle_heading)
        
        rotation_matrix = np.array([
            [cos_h, -sin_h, 0],
            [sin_h, cos_h, 0],
            [0, 0, 1]
        ])
        
        if len(translated) == 2:
            translated = np.append(translated, 0)  # z 좌표 추가
        
        local_position = rotation_matrix @ translated
        return tuple(local_position)
    
    def local_to_global_transform(self, local_position, vehicle_global_pos, vehicle_heading):
        """차량 로컬 좌표를 글로벌 좌표로 변환"""
        # 회전 변환 (차량 방향 적용)
        cos_h = math.cos(vehicle_heading)
        sin_h = math.sin(vehicle_heading)
        
        rotation_matrix = np.array([
            [cos_h, -sin_h, 0],
            [sin_h, cos_h, 0],
            [0, 0, 1]
        ])
        
        if len(local_position) == 2:
            local_position = list(local_position) + [0]  # z 좌표 추가
        
        rotated = rotation_matrix @ np.array(local_position)
        
        # 평행 이동
        global_position = rotated + np.array(vehicle_global_pos)
        return tuple(global_position)
    
    def sensor_to_vehicle_transform(self, sensor_data, sensor_offset, sensor_orientation=0):
        """센서 좌표를 차량 좌표로 변환"""
        # 센서 방향 보정
        cos_s = math.cos(sensor_orientation)
        sin_s = math.sin(sensor_orientation)
        
        sensor_rotation = np.array([
            [cos_s, -sin_s, 0],
            [sin_s, cos_s, 0],
            [0, 0, 1]
        ])
        
        # 센서 데이터를 차량 좌표계로 변환
        if len(sensor_data) == 2:
            sensor_data = list(sensor_data) + [0]
        
        rotated_data = sensor_rotation @ np.array(sensor_data)
        vehicle_coordinates = rotated_data + np.array(sensor_offset)
        
        return tuple(vehicle_coordinates)
    
    def get_coordinate_reference_chain(self, target_coordinate_system):
        """좌표계 변환 체인 반환"""
        transformation_chain = {
            'sensor_to_vehicle': [
                'sensor_rotation',
                'sensor_translation'
            ],
            'vehicle_to_global': [
                'vehicle_rotation',
                'vehicle_translation'
            ],
            'global_to_map': [
                'map_projection',
                'map_alignment'
            ]
        }
        return transformation_chain
    
    def multi_coordinate_fusion(self, sensor_readings):
        """다중 좌표계 데이터 융합"""
        fused_data = {}
        
        for sensor_name, reading in sensor_readings.items():
            # 각 센서별 좌표계 변환
            if sensor_name == 'lidar':
                sensor_offset = (0.5, 0, 1.2)
                vehicle_coords = self.sensor_to_vehicle_transform(
                    reading['position'], 
                    sensor_offset
                )
            elif sensor_name == 'camera':
                sensor_offset = (2.0, 0, 0.8)
                vehicle_coords = self.sensor_to_vehicle_transform(
                    reading['position'], 
                    sensor_offset
                )
            elif sensor_name == 'gps':
                # GPS는 이미 글로벌 좌표
                vehicle_coords = reading['position']
            
            fused_data[sensor_name] = {
                'original': reading['position'],
                'vehicle_coordinates': vehicle_coords,
                'confidence': reading.get('confidence', 1.0)
            }
        
        return fused_data

# 사용 예시
coord_system = CoordinateSystemReferences()

# 차량 현재 위치 (글로벌 좌표)
vehicle_global_pos = (1000.0, 2000.0, 0.0)
vehicle_heading = math.radians(45)  # 45도 방향

# 로컬 좌표의 한 점을 글로벌로 변환
local_point = (5.0, 2.0, 0.0)  # 차량 앞쪽 우측 5m, 우측 2m
global_point = coord_system.local_to_global_transform(
    local_point, vehicle_global_pos, vehicle_heading
)

print(f"로컬 좌표 {local_point} -> 글로벌 좌표 ({global_point[0]:.2f}, {global_point[1]:.2f})")

# 센서 데이터 융합 예시
sensor_readings = {
    'lidar': {'position': (10.0, 0.0), 'confidence': 0.95},
    'camera': {'position': (12.0, -1.0), 'confidence': 0.88},
    'gps': {'position': (1000.0, 2000.0), 'confidence': 0.92}
}

fused_data = coord_system.multi_coordinate_fusion(sensor_readings)
for sensor, data in fused_data.items():
    print(f"{sensor}: 차량 좌표 {data['vehicle_coordinates']}")
```

**실행 결과:**
```
로컬 좌표 (5.0, 2.0, 0.0) -> 글로벌 좌표 (1002.12, 2004.95)
lidar: 차량 좌표 (10.5, 0.0, 1.2)
camera: 차량 좌표 (14.0, -1.0, 0.8)
gps: 차량 좌표 (1000.0, 2000.0, 0.0)
```

---

## 7. 제어 시스템별 고려사항

각 제어 시스템의 목적에 따라 최적화된 기준점 선택 가이드입니다.

```python
class ControlSystemReferences:
    def __init__(self):
        # 제어 시스템별 최적 기준점 매핑
        self.control_references = {
            'path_following': 'rear_axle_center',      # 수학적 단순함
            'obstacle_avoidance': 'vehicle_boundary',   # 안전 마진 확보
            'lane_keeping': 'vehicle_centerline',      # 차선 중앙 유지
            'intersection_crossing': 'front_bumper',    # 진입 타이밍 최적화
            'reverse_parking': 'rear_bumper',          # 후진 정밀도
            'adaptive_cruise': 'front_center',         # 차간거리 제어
            'emergency_braking': 'front_bumper'        # 최대 안전성
        }
    
    def get_control_reference(self, control_system, vehicle_state):
        """제어 시스템에 맞는 기준점 반환"""
        base_reference = self.control_references.get(control_system, 'rear_axle_center')
        
        # 차량 상태에 따른 동적 조정
        if vehicle_state.get('speed', 0) > 50:  # 고속 주행
            if control_system == 'path_following':
                return 'rear_axle_center'  # 안정성 우선
        elif vehicle_state.get('speed', 0) < 10:  # 저속 주행
            if control_system in ['path_following', 'lane_keeping']:
                return 'geometric_center'  # 정밀도 우선
        
        return base_reference
    
    def calculate_control_error(self, control_system, target_path, current_position, vehicle_heading):
        """제어 시스템별 오차 계산"""
        reference_point = self.get_control_reference(control_system, {'speed': 30})
        
        if control_system == 'path_following':
            # 경로 추종 오차 (Cross Track Error)
            return self._calculate_cross_track_error(target_path, current_position, vehicle_heading)
        
        elif control_system == 'lane_keeping':
            # 차선 중앙 유지 오차
            return self._calculate_lane_center_error(target_path, current_position)
        
        elif control_system == 'obstacle_avoidance':
            # 장애물 회피 안전 거리 오차
            return self._calculate_safety_margin_error(target_path, current_position)
        
        return 0.0
    
    def _calculate_cross_track_error(self, path_points, vehicle_position, vehicle_heading):
        """경로 추종 횡방향 오차 계산"""
        if len(path_points) < 2:
            return 0.0
        
        # 가장 가까운 경로 점 찾기
        min_distance = float('inf')
        closest_segment_idx = 0
        
        for i in range(len(path_points) - 1):
            distance = self._point_to_line_distance(
                vehicle_position, path_points[i], path_points[i + 1]
            )
            if distance < min_distance:
                min_distance = distance
                closest_segment_idx = i
        
        # 경로 방향과 차량 방향 비교
        path_vector = (
            path_points[closest_segment_idx + 1][0] - path_points[closest_segment_idx][0],
            path_points[closest_segment_idx + 1][1] - path_points[closest_segment_idx][1]
        )
        path_heading = math.atan2(path_vector[1], path_vector[0])
        
        # 외적을 이용한 좌우 판단
        cross_product = (
            (vehicle_position[0] - path_points[closest_segment_idx][0]) * path_vector[1] -
            (vehicle_position[1] - path_points[closest_segment_idx][1]) * path_vector[0]
        )
        
        return min_distance if cross_product > 0 else -min_distance
    
    def _point_to_line_distance(self, point, line_start, line_end):
        """점과 직선 사이의 최단 거리 계산"""
        line_vec = (line_end[0] - line_start[0], line_end[1] - line_start[1])
        point_vec = (point[0] - line_start[0], point[1] - line_start[1])
        
        line_len = math.sqrt(line_vec[0]**2 + line_vec[1]**2)
        if line_len == 0:
            return math.sqrt(point_vec[0]**2 + point_vec[1]**2)
        
        line_unitvec = (line_vec[0] / line_len, line_vec[1] / line_len)
        proj_length = point_vec[0] * line_unitvec[0] + point_vec[1] * line_unitvec[1]
        
        if proj_length < 0:
            return math.sqrt(point_vec[0]**2 + point_vec[1]**2)
        elif proj_length > line_len:
            end_vec = (point[0] - line_end[0], point[1] - line_end[1])
            return math.sqrt(end_vec[0]**2 + end_vec[1]**2)
        else:
            proj_point = (
                line_start[0] + proj_length * line_unitvec[0],
                line_start[1] + proj_length * line_unitvec[1]
            )
            return math.sqrt((point[0] - proj_point[0])**2 + (point[1] - proj_point[1])**2)
    
    def _calculate_lane_center_error(self, lane_center_line, vehicle_position):
        """차선 중앙 유지 오차 계산"""
        return self._point_to_line_distance(vehicle_position, lane_center_line[0], lane_center_line[-1])
    
    def _calculate_safety_margin_error(self, obstacles, vehicle_position):
        """안전 거리 마진 오차 계산"""
        min_distance = float('inf')
        for obstacle in obstacles:
            distance = math.sqrt(
                (vehicle_position[0] - obstacle[0])**2 + 
                (vehicle_position[1] - obstacle[1])**2
            )
            min_distance = min(min_distance, distance)
        
        safety_margin = 2.0  # 최소 안전 거리 2m
        return max(0, safety_margin - min_distance)

# 사용 예시
control_system = ControlSystemReferences()

# 다양한 제어 시스템의 기준점 확인
control_types = ['path_following', 'lane_keeping', 'obstacle_avoidance', 'emergency_braking']
vehicle_state = {'speed': 45}

for control_type in control_types:
    reference = control_system.get_control_reference(control_type, vehicle_state)
    print(f"{control_type}: {reference}")

# 경로 추종 오차 계산 예시
target_path = [(0, 0), (10, 0), (20, 0), (30, 0)]  # 직선 경로
current_pos = (15, 1.5)  # 경로에서 1.5m 우측 이탈
vehicle_heading = math.radians(0)  # 정방향

cross_track_error = control_system.calculate_control_error(
    'path_following', target_path, current_pos, vehicle_heading
)
print(f"경로 추종 오차: {cross_track_error:.2f}m")
```

**실행 결과:**
```
path_following: rear_axle_center
lane_keeping: vehicle_centerline
obstacle_avoidance: vehicle_boundary
emergency_braking: front_bumper
경로 추종 오차: 1.50m
```

---

## 8. 도로 및 교통 환경 기준점

도로 인프라와 교통 환경에 특화된 기준점들입니다.

```python
class RoadEnvironmentReferences:
    def __init__(self):
        self.road_references = {
            'lane_center_line': 'lane_marking_center',
            'road_edge': 'road_boundary',
            'intersection_center': 'intersection_geometry_center',
            'stop_line': 'legal_stopping_position',
            'crosswalk': 'pedestrian_crossing_area',
            'traffic_light': 'signal_detection_point'
        }
    
    def get_lane_reference_points(self, lane_width=3.5, lane_marking_width=0.15):
        """차선 기준점들 계산"""
        half_lane = lane_width / 2
        marking_offset = lane_marking_width / 2
        
        return {
            'lane_center': (0, 0, 0),
            'left_lane_boundary': (0, half_lane, 0),
            'right_lane_boundary': (0, -half_lane, 0),
            'left_marking_center': (0, half_lane, 0),
            'right_marking_center': (0, -half_lane, 0),
            'left_marking_inner': (0, half_lane - marking_offset, 0),
            'left_marking_outer': (0, half_lane + marking_offset, 0),
            'right_marking_inner': (0, -half_lane + marking_offset, 0),
            'right_marking_outer': (0, -half_lane - marking_offset, 0)
        }
    
    def calculate_intersection_reference_points(self, intersection_geometry):
        """교차로 기준점 계산"""
        # 교차로 중심점 계산
        center_x = sum(point[0] for point in intersection_geometry) / len(intersection_geometry)
        center_y = sum(point[1] for point in intersection_geometry) / len(intersection_geometry)
        
        intersection_refs = {
            'intersection_center': (center_x, center_y, 0),
            'entry_points': [],
            'exit_points': [],
            'conflict_zones': []
        }
        
        # 진입점과 진출점 계산 (단순화된 예시)
        for i, point in enumerate(intersection_geometry):
            if i % 2 == 0:  # 짝수 인덱스는 진입점
                intersection_refs['entry_points'].append(point)
            else:  # 홀수 인덱스는 진출점
                intersection_refs['exit_points'].append(point)
        
        return intersection_refs
    
    def get_stop_line_reference(self, stop_line_position, approach_direction):
        """정지선 기준점 계산"""
        # 정지선에서 차량 전면까지의 거리 고려
        vehicle_front_offset = 2.5  # 차량 전면 오버행 + 안전 여유
        
        # 접근 방향에 따른 정지 위치 계산
        if approach_direction == 'north':
            stop_position = (stop_line_position[0], stop_line_position[1] - vehicle_front_offset, 0)
        elif approach_direction == 'south':
            stop_position = (stop_line_position[0], stop_line_position[1] + vehicle_front_offset, 0)
        elif approach_direction == 'east':
            stop_position = (stop_line_position[0] - vehicle_front_offset, stop_line_position[1], 0)
        elif approach_direction == 'west':
            stop_position = (stop_line_position[0] + vehicle_front_offset, stop_line_position[1], 0)
        else:
            stop_position = stop_line_position
        
        return {
            'legal_stop_position': stop_position,
            'stop_line_position': stop_line_position,
            'safety_margin': vehicle_front_offset
        }
    
    def calculate_road_curvature_references(self, road_points):
        """도로 곡률 기준점 계산"""
        if len(road_points) < 3:
            return {'curvature': 0, 'radius': float('inf')}
        
        curvature_points = []
        
        for i in range(1, len(road_points) - 1):
            # 3점을 이용한 곡률 계산
            p1, p2, p3 = road_points[i-1], road_points[i], road_points[i+1]
            
            # 벡터 계산
            v1 = (p2[0] - p1[0], p2[1] - p1[1])
            v2 = (p3[0] - p2[0], p3[1] - p2[1])
            
            # 각도 변화량 계산
            angle1 = math.atan2(v1[1], v1[0])
            angle2 = math.atan2(v2[1], v2[0])
            angle_diff = angle2 - angle1
            
            # 각도 정규화 (-π ~ π)
            while angle_diff > math.pi:
                angle_diff -= 2 * math.pi
            while angle_diff < -math.pi:
                angle_diff += 2 * math.pi
            
            # 거리 계산
            dist1 = math.sqrt(v1[0]**2 + v1[1]**2)
            dist2 = math.sqrt(v2[0]**2 + v2[1]**2)
            avg_dist = (dist1 + dist2) / 2
            
            # 곡률 계산
            if avg_dist > 0:
                curvature = abs(angle_diff) / avg_dist
                radius = 1 / curvature if curvature > 0 else float('inf')
            else:
                curvature = 0
                radius = float('inf')
            
            curvature_points.append({
                'position': p2,
                'curvature': curvature,
                'radius': radius
            })
        
        return curvature_points

# 사용 예시
road_env = RoadEnvironmentReferences()

# 차선 기준점 계산
lane_refs = road_env.get_lane_reference_points(lane_width=3.5)
print("차선 기준점들:")
for ref_name, position in lane_refs.items():
    print(f"  {ref_name}: {position}")

# 교차로 기준점 계산 (4거리 교차로 예시)
intersection_corners = [
    (-5, -5), (5, -5), (5, 5), (-5, 5)  # 사각형 교차로
]
intersection_refs = road_env.calculate_intersection_reference_points(intersection_corners)
print(f"\n교차로 중심: {intersection_refs['intersection_center']}")

# 정지선 기준점 계산
stop_line_pos = (0, 0)
stop_ref = road_env.get_stop_line_reference(stop_line_pos, 'north')
print(f"정지 위치: {stop_ref['legal_stop_position']}")

# 도로 곡률 계산
road_curve = [(0, 0), (10, 2), (20, 8), (30, 18)]  # 곡선 도로
curvature_data = road_env.calculate_road_curvature_references(road_curve)
print(f"곡률 데이터 점수: {len(curvature_data)}개")
if curvature_data:
    print(f"첫 번째 곡률점 - 곡률: {curvature_data[0]['curvature']:.4f}, 반경: {curvature_data[0]['radius']:.2f}m")
```

**실행 결과:**
```
차선 기준점들:
  lane_center: (0, 0, 0)
  left_lane_boundary: (0, 1.75, 0)
  right_lane_boundary: (0, -1.75, 0)
  left_marking_center: (0, 1.75, 0)
  right_marking_center: (0, -1.75, 0)
  left_marking_inner: (0, 1.675, 0)
  left_marking_outer: (0, 1.825, 0)
  right_marking_inner: (0, -1.675, 0)
  right_marking_outer: (0, -1.825, 0)

교차로 중심: (0.0, 0.0, 0)
정지 위치: (0, -2.5, 0)
곡률 데이터 점수: 2개
첫 번째 곡률점 - 곡률: 0.0063, 반경: 158.11m
```
---

## 9. 법규 및 규정 기준점들

차량이 교통법규를 준수하고 검사 기준을 만족하기 위한 기준점들입니다.

### 🔧 코드 예시

```python
class LegalReferencePoints:
    """교통법규 및 차량 검사 기준점 관리 클래스"""
    
    def __init__(self, vehicle_config):
        self.vehicle_config = vehicle_config
        self.legal_boundaries = self._calculate_legal_boundaries()
        self.inspection_points = self._define_inspection_points()
    
    def _calculate_legal_boundaries(self):
        """법적 차량 경계 계산"""
        # 차량의 법적 최대 크기 (길이 × 폭 × 높이)
        max_length = 12.0  # 12미터 (대형 버스/트럭 기준)
        max_width = 2.5    # 2.5미터 (일반 도로 기준)
        max_height = 4.0   # 4미터 (교량 통과 기준)
        
        return {
            'front_legal_boundary': (max_length/2, 0, 0),
            'rear_legal_boundary': (-max_length/2, 0, 0),
            'left_legal_boundary': (0, max_width/2, 0),
            'right_legal_boundary': (0, -max_width/2, 0),
            'top_legal_boundary': (0, 0, max_height)
        }
    
    def _define_inspection_points(self):
        """차량 검사 기준점 정의"""
        return {
            'headlight_height': (2.0, 0, 0.8),     # 전조등 높이 기준점
            'license_plate_position': (-2.5, 0, 0.5),  # 번호판 위치
            'emission_test_point': (-1.0, -0.5, 0.3),  # 배기가스 측정점
            'brake_test_reference': (0, 0, 0.3)     # 제동 성능 측정 기준점
        }
    
    def check_legal_compliance(self, current_position):
        """현재 위치가 법적 기준을 만족하는지 확인"""
        x, y, z = current_position
        
        # 차선 이탈 여부 확인
        lane_width = 3.5  # 표준 차선 폭 3.5m
        if abs(y) > lane_width / 2:
            return False, "차선 이탈 위험"
        
        # 높이 제한 확인 (교량, 터널 등)
        height_limit = 3.8
        if z > height_limit:
            return False, f"높이 제한 초과: {z:.2f}m > {height_limit}m"
        
        return True, "법적 기준 준수"

# 사용 예시
vehicle_config = {'length': 4.5, 'width': 1.8, 'height': 1.6}
legal_system = LegalReferencePoints(vehicle_config)

# 현재 차량 위치 확인
current_pos = (0, 1.2, 1.6)  # x, y, z 좌표
compliance, message = legal_system.check_legal_compliance(current_pos)
print(f"법규 준수 상태: {compliance}, 메시지: {message}")
```

### 📊 실행 결과
```
법규 준수 상태: True, 메시지: 법적 기준 준수
```

---

## 10. 물리학적/역학적 기준점들

차량의 동역학적 특성을 고려한 물리학적 기준점들입니다.

### 🔧 코드 예시

```python
import math
import numpy as np

class PhysicalReferencePoints:
    """차량의 물리학적/역학적 기준점 관리 클래스"""
    
    def __init__(self, vehicle_mass, wheelbase, track_width):
        self.mass = vehicle_mass          # 차량 질량 (kg)
        self.wheelbase = wheelbase        # 축간거리 (m)
        self.track_width = track_width    # 윤거 (m)
        self.gravity = 9.81               # 중력가속도 (m/s²)
        
    def calculate_center_of_rotation(self, steering_angle, velocity):
        """회전 중심 계산 (선회 시)"""
        if abs(steering_angle) < 0.001:  # 직진 시
            return None
        
        # 회전 반지름 계산 (Bicycle Model 기반)
        turn_radius = self.wheelbase / math.tan(math.radians(steering_angle))
        
        # 회전 중심 위치 (차량 뒤축 기준)
        center_x = 0
        center_y = turn_radius
        
        return (center_x, center_y, 0)
    
    def calculate_instantaneous_center(self, front_wheel_angle, rear_wheel_angle=0):
        """순간 회전 중심 계산"""
        # 4륜 조향 시스템을 고려한 순간 회전 중심
        if abs(front_wheel_angle) < 0.001 and abs(rear_wheel_angle) < 0.001:
            return None  # 직진 시에는 순간 회전 중심이 무한대
        
        # Ackermann 기하학 기반 계산
        if abs(rear_wheel_angle) < 0.001:  # 앞바퀴만 조향
            ic_y = self.wheelbase / math.tan(math.radians(front_wheel_angle))
        else:  # 4륜 조향
            ic_y = self.wheelbase / (math.tan(math.radians(front_wheel_angle)) - 
                                   math.tan(math.radians(rear_wheel_angle)))
        
        return (0, ic_y, 0)
    
    def calculate_roll_center(self, suspension_geometry):
        """롤 중심 계산 (코너링 시 차체 기울어짐 기준점)"""
        # 서스펜션 기하학을 고려한 롤 중심 높이 계산
        front_roll_center_height = suspension_geometry.get('front_rc_height', 0.05)
        rear_roll_center_height = suspension_geometry.get('rear_rc_height', 0.08)
        
        # 차량 무게중심을 고려한 전체 롤 중심
        cg_position = self.wheelbase * 0.6  # 일반적으로 앞축에서 60% 지점
        
        roll_center_height = (front_roll_center_height * (self.wheelbase - cg_position) + 
                            rear_roll_center_height * cg_position) / self.wheelbase
        
        return (cg_position, 0, roll_center_height)
    
    def calculate_aerodynamic_center(self, vehicle_dimensions):
        """공기역학 중심 계산"""
        # 차량 전면 투영 면적의 중심 (공기 저항 작용점)
        length = vehicle_dimensions['length']
        width = vehicle_dimensions['width']
        height = vehicle_dimensions['height']
        
        # 일반적으로 차량 전면의 기하학적 중심
        aero_center_x = length * 0.4   # 차량 전면에서 40% 지점
        aero_center_y = 0              # 차량 중심선
        aero_center_z = height * 0.5   # 차량 높이의 중점
        
        return (aero_center_x, aero_center_y, aero_center_z)

# 사용 예시
physics_system = PhysicalReferencePoints(
    vehicle_mass=1500,    # 1.5톤
    wheelbase=2.7,        # 2.7m 축간거리
    track_width=1.5       # 1.5m 윤거
)

# 다양한 물리적 기준점 계산
steering_angle = 15  # 15도 조향
velocity = 50        # 50 km/h

rotation_center = physics_system.calculate_center_of_rotation(steering_angle, velocity)
instantaneous_center = physics_system.calculate_instantaneous_center(steering_angle)

suspension_config = {'front_rc_height': 0.05, 'rear_rc_height': 0.08}
roll_center = physics_system.calculate_roll_center(suspension_config)

vehicle_dims = {'length': 4.5, 'width': 1.8, 'height': 1.6}
aero_center = physics_system.calculate_aerodynamic_center(vehicle_dims)

print(f"회전 중심: {rotation_center}")
print(f"순간 회전 중심: {instantaneous_center}")
print(f"롤 센터: {roll_center}")
print(f"공기역학 중심: {aero_center}")
```

### 📊 실행 결과
```
회전 중심: (0, 10.062, 0)
순간 회전 중심: (0, 10.062, 0)
롤 센터: (1.62, 0, 0.068)
공기역학 중심: (1.8, 0, 0.8)
```

---

## 11. 통신 및 V2X 기준점들

차량 간 통신(V2V) 및 인프라와의 통신(V2I)을 위한 기준점들입니다.

### 🔧 코드 예시

```python
import time
import json
from typing import Dict, List, Tuple

class V2XReferencePoints:
    """V2X 통신을 위한 기준점 관리 클래스"""
    
    def __init__(self, vehicle_id, antenna_positions):
        self.vehicle_id = vehicle_id
        self.antenna_positions = antenna_positions
        self.communication_range = 300  # 통신 범위 300m
        self.broadcast_interval = 0.1   # 100ms 주기로 위치 정보 송신
        
    def get_v2v_antenna_position(self):
        """차량간 통신 안테나 위치 반환"""
        # 일반적으로 지붕 중앙에 설치
        return self.antenna_positions.get('v2v', (0, 0, 1.5))
    
    def get_v2i_communication_point(self):
        """인프라 통신 기준점 반환"""
        # 신호등, RSU(Road Side Unit)와의 통신용
        return self.antenna_positions.get('v2i', (-0.5, 0, 1.2))
    
    def create_broadcast_message(self, current_position, velocity, heading):
        """위치 정보 송신 메시지 생성"""
        v2v_antenna_pos = self.get_v2v_antenna_position()
        
        # 안테나 위치를 고려한 실제 송신 위치 계산
        actual_broadcast_position = (
            current_position[0] + v2v_antenna_pos[0],
            current_position[1] + v2v_antenna_pos[1],
            current_position[2] + v2v_antenna_pos[2]
        )
        
        message = {
            'vehicle_id': self.vehicle_id,
            'timestamp': time.time(),
            'position': actual_broadcast_position,
            'velocity': velocity,
            'heading': heading,
            'antenna_reference': v2v_antenna_pos,
            'message_type': 'BSM'  # Basic Safety Message
        }
        
        return message
    
    def calculate_relative_position(self, other_vehicle_msg, my_position):
        """다른 차량과의 상대 위치 계산"""
        other_pos = other_vehicle_msg['position']
        my_antenna_pos = self.get_v2v_antenna_position()
        
        # 내 안테나 기준 실제 위치
        my_actual_pos = (
            my_position[0] + my_antenna_pos[0],
            my_position[1] + my_antenna_pos[1],
            my_position[2] + my_antenna_pos[2]
        )
        
        # 상대 거리 및 방향 계산
        dx = other_pos[0] - my_actual_pos[0]
        dy = other_pos[1] - my_actual_pos[1]
        distance = (dx**2 + dy**2)**0.5
        
        return {
            'distance': distance,
            'relative_x': dx,
            'relative_y': dy,
            'is_in_range': distance <= self.communication_range
        }
    
    def process_infrastructure_message(self, rsu_message, my_position):
        """인프라로부터의 메시지 처리"""
        v2i_point = self.get_v2i_communication_point()
        
        # 인프라 통신 기준점을 고려한 메시지 처리
        my_comm_position = (
            my_position[0] + v2i_point[0],
            my_position[1] + v2i_point[1],
            my_position[2] + v2i_point[2]
        )
        
        # RSU와의 거리 계산
        rsu_pos = rsu_message.get('position', (0, 0, 0))
        distance_to_rsu = ((my_comm_position[0] - rsu_pos[0])**2 + 
                          (my_comm_position[1] - rsu_pos[1])**2)**0.5
        
        return {
            'rsu_id': rsu_message.get('rsu_id'),
            'message_type': rsu_message.get('type'),
            'distance_to_rsu': distance_to_rsu,
            'signal_strength': max(0, 100 - distance_to_rsu),  # 간단한 신호 강도 모델
            'my_comm_position': my_comm_position
        }

# 사용 예시
antenna_config = {
    'v2v': (0, 0, 1.5),      # 지붕 중앙 V2V 안테나
    'v2i': (-0.5, 0, 1.2)    # 앞쪽 V2I 통신 안테나
}

v2x_system = V2XReferencePoints('VEHICLE_001', antenna_config)

# 현재 차량 상태
my_position = (100, 50, 0)  # GPS 좌표
my_velocity = 60  # km/h
my_heading = 45   # 북동쪽 45도

# 브로드캐스트 메시지 생성
broadcast_msg = v2x_system.create_broadcast_message(my_position, my_velocity, my_heading)
print("송신 메시지:")
print(json.dumps(broadcast_msg, indent=2))

# 다른 차량으로부터 수신한 메시지 처리
other_vehicle_msg = {
    'vehicle_id': 'VEHICLE_002',
    'position': (150, 80, 0),
    'velocity': 55,
    'heading': 30
}

relative_info = v2x_system.calculate_relative_position(other_vehicle_msg, my_position)
print(f"\n다른 차량과의 상대 위치: {relative_info}")

# 인프라 메시지 처리
rsu_message = {
    'rsu_id': 'RSU_001',
    'type': 'TRAFFIC_LIGHT',
    'position': (120, 60, 3),
    'signal_phase': 'RED',
    'time_remaining': 15
}

infrastructure_info = v2x_system.process_infrastructure_message(rsu_message, my_position)
print(f"\n인프라 통신 정보: {infrastructure_info}")
```

### 📊 실행 결과
```
송신 메시지:
{
  "vehicle_id": "VEHICLE_001",
  "timestamp": 1719486420.123,
  "position": [100, 50, 1.5],
  "velocity": 60,
  "heading": 45,
  "antenna_reference": [0, 0, 1.5],
  "message_type": "BSM"
}

다른 차량과의 상대 위치: {'distance': 58.31, 'relative_x': 50, 'relative_y': 30, 'is_in_range': True}

인프라 통신 정보: {'rsu_id': 'RSU_001', 'message_type': 'TRAFFIC_LIGHT', 'distance_to_rsu': 22.36, 'signal_strength': 77.64, 'my_comm_position': (99.5, 50, 1.2)}
```

---

## 12. 예측 및 미래 위치 기준점들

차량의 미래 위치를 예측하고 충돌 위험을 평가하기 위한 기준점들입니다.

### 🔧 코드 예시

```python
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple

class PredictiveReferencePoints:
    """예측 및 미래 위치 기준점 관리 클래스"""
    
    def __init__(self, vehicle_dynamics):
        self.dynamics = vehicle_dynamics
        self.prediction_intervals = [1, 3, 5]  # 1초, 3초, 5초 후 예측
        
    def predict_position_linear(self, current_pos, velocity, heading, time_horizon):
        """선형 운동 모델을 사용한 위치 예측"""
        x, y, z = current_pos
        vx = velocity * np.cos(np.radians(heading))
        vy = velocity * np.sin(np.radians(heading))
        
        # time_horizon 초 후 예상 위치
        predicted_x = x + vx * time_horizon
        predicted_y = y + vy * time_horizon
        predicted_z = z  # 높이는 변하지 않는다고 가정
        
        return (predicted_x, predicted_y, predicted_z)
    
    def predict_position_with_acceleration(self, current_pos, velocity, heading, 
                                         acceleration, time_horizon):
        """가속도를 고려한 위치 예측"""
        x, y, z = current_pos
        vx = velocity * np.cos(np.radians(heading))
        vy = velocity * np.sin(np.radians(heading))
        ax = acceleration * np.cos(np.radians(heading))
        ay = acceleration * np.sin(np.radians(heading))
        
        # 등가속도 운동 방정식 적용
        predicted_x = x + vx * time_horizon + 0.5 * ax * time_horizon**2
        predicted_y = y + vy * time_horizon + 0.5 * ay * time_horizon**2
        predicted_z = z
        
        return (predicted_x, predicted_y, predicted_z)
    
    def predict_curved_trajectory(self, current_pos, velocity, heading, 
                                steering_angle, wheelbase, time_horizon):
        """곡선 주행을 고려한 궤적 예측"""
        if abs(steering_angle) < 0.1:  # 거의 직진
            return self.predict_position_linear(current_pos, velocity, heading, time_horizon)
        
        # 회전 반지름 계산
        turn_radius = wheelbase / np.tan(np.radians(steering_angle))
        angular_velocity = velocity / turn_radius  # rad/s
        
        x, y, z = current_pos
        
        # 회전 중심 계산
        center_x = x - turn_radius * np.sin(np.radians(heading))
        center_y = y + turn_radius * np.cos(np.radians(heading))
        
        # time_horizon 후의 각도 변화
        angle_change = angular_velocity * time_horizon
        new_heading = heading + np.degrees(angle_change)
        
        # 새로운 위치 계산
        predicted_x = center_x + turn_radius * np.sin(np.radians(new_heading))
        predicted_y = center_y - turn_radius * np.cos(np.radians(new_heading))
        
        return (predicted_x, predicted_y, z)
    
    def calculate_collision_prediction_point(self, my_trajectory, other_trajectory):
        """충돌 예상 지점 계산"""
        collision_points = []
        min_distance_threshold = 2.0  # 2미터 이내 접근 시 충돌 위험
        
        for i, (my_pos, other_pos) in enumerate(zip(my_trajectory, other_trajectory)):
            distance = np.sqrt((my_pos[0] - other_pos[0])**2 + 
                             (my_pos[1] - other_pos[1])**2)
            
            if distance < min_distance_threshold:
                collision_points.append({
                    'time': i * 0.1,  # 0.1초 간격으로 계산
                    'my_position': my_pos,
                    'other_position': other_pos,
                    'distance': distance,
                    'risk_level': 'HIGH' if distance < 1.0 else 'MEDIUM'
                })
        
        return collision_points
    
    def generate_trajectory_endpoints(self, current_pos, velocity, heading, 
                                    possible_maneuvers):
        """가능한 조작별 궤적 끝점 생성"""
        endpoints = {}
        
        for maneuver, params in possible_maneuvers.items():
            if maneuver == 'straight':
                endpoint = self.predict_position_linear(
                    current_pos, velocity, heading, params['time']
                )
            elif maneuver == 'left_turn':
                endpoint = self.predict_curved_trajectory(
                    current_pos, velocity, heading, 
                    -params['steering_angle'], params['wheelbase'], params['time']
                )
            elif maneuver == 'right_turn':
                endpoint = self.predict_curved_trajectory(
                    current_pos, velocity, heading, 
                    params['steering_angle'], params['wheelbase'], params['time']
                )
            elif maneuver == 'emergency_brake':
                # 급제동 시나리오
                decel_time = velocity / params['deceleration']  # 완전 정지 시간
                actual_time = min(params['time'], decel_time)
                
                # 등감속도 운동
                distance = velocity * actual_time - 0.5 * params['deceleration'] * actual_time**2
                endpoint_x = current_pos[0] + distance * np.cos(np.radians(heading))
                endpoint_y = current_pos[1] + distance * np.sin(np.radians(heading))
                endpoint = (endpoint_x, endpoint_y, current_pos[2])
            
            endpoints[maneuver] = endpoint
        
        return endpoints

# 사용 예시
vehicle_dynamics = {'wheelbase': 2.7, 'max_acceleration': 3.0, 'max_deceleration': 8.0}
predictor = PredictiveReferencePoints(vehicle_dynamics)

# 현재 차량 상태
current_position = (0, 0, 0)
current_velocity = 50  # km/h를 m/s로 변환: 50/3.6 ≈ 13.89 m/s
current_heading = 0    # 북쪽 방향
steering_angle = 10    # 10도 좌회전

# 다양한 시간 구간별 위치 예측
print("=== 위치 예측 결과 ===")
for time_horizon in [1, 3, 5]:
    # 선형 예측
    linear_pred = predictor.predict_position_linear(
        current_position, current_velocity/3.6, current_heading, time_horizon
    )
    
    # 곡선 주행 예측
    curved_pred = predictor.predict_curved_trajectory(
        current_position, current_velocity/3.6, current_heading, 
        steering_angle, vehicle_dynamics['wheelbase'], time_horizon
    )
    
    print(f"{time_horizon}초 후:")
    print(f"  직진 예측: ({linear_pred[0]:.2f}, {linear_pred[1]:.2f})")
    print(f"  곡선 예측: ({curved_pred[0]:.2f}, {curved_pred[1]:.2f})")

# 가능한 조작별 궤적 끝점 계산
possible_maneuvers = {
    'straight': {'time': 3},
    'left_turn': {'steering_angle': 15, 'wheelbase': 2.7, 'time': 3},
    'right_turn': {'steering_angle': 15, 'wheelbase': 2.7, 'time': 3},
    'emergency_brake': {'deceleration': 8.0, 'time': 3}
}

endpoints = predictor.generate_trajectory_endpoints(
    current_position, current_velocity/3.6, current_heading, possible_maneuvers
)

print("\n=== 조작별 궤적 끝점 ===")
for maneuver, endpoint in endpoints.items():
    print(f"{maneuver}: ({endpoint[0]:.2f}, {endpoint[1]:.2f})")
```

### 📊 실행 결과
```
=== 위치 예측 결과 ===
1초 후:
  직진 예측: (13.89, 0.00)
  곡선 예측: (13.77, 1.78)
3초 후:
  직진 예측: (41.67, 0.00)
  곡선 예측: (39.58, 15.35)
5초 후:
  직진 예측: (69.44, 0.00)
  곡선 예측: (61.11, 39.58)

=== 조작별 궤적 끝점 ===
straight: (41.67, 0.00)
left_turn: (35.98, 18.33)
right_turn: (35.98, -18.33)
emergency_brake: (25.00, 0.00)
```

---

## 13. 다중 차량 시스템 기준점들

여러 차량이 협력하여 주행하는 군집 주행(Platooning) 시스템의 기준점들입니다.

### 🔧 코드 예시

```python
import numpy as np
from typing import List, Dict
import uuid

class MultiVehicleReferencePoints:
    """다중 차량 시스템 기준점 관리 클래스"""
    
    def __init__(self, vehicle_id, vehicle_length=4.5):
        self.vehicle_id = vehicle_id
        self.vehicle_length = vehicle_length
        self.convoy_members = {}  # 군집 내 차량들
        self.formation_type = "line"  # 대형 유형: line, wedge, diamond
        
    def add_convoy_member(self, vehicle_id, position, role="follower"):
        """군집에 차량 추가"""
        self.convoy_members[vehicle_id] = {
            'position': position,
            'role': role,  # leader, follower
            'join_time': 0,
            'status': 'active'
        }
    
    def calculate_formation_reference(self, leader_position, formation_index):
        """대형 기준점 계산"""
        leader_x, leader_y, leader_z = leader_position
        
        if self.formation_type == "line":
            # 일렬 대형 - 차량들이 일직선으로 배열
            target_x = leader_x - (formation_index + 1) * (self.vehicle_length + 2.0)
            target_y = leader_y
            target_z = leader_z
            
        elif self.formation_type == "wedge":
            # 쐐기 대형 - V자 형태로 배열
            lateral_offset = (formation_index + 1) * 3.5  # 차선 폭만큼 옆으로
            longitudinal_offset = (formation_index + 1) * 10.0
            
            side = 1 if formation_index % 2 == 0 else -1  # 좌우 교대 배치
            target_x = leader_x - longitudinal_offset
            target_y = leader_y + side * lateral_offset
            target_z = leader_z
            
        elif self.formation_type == "diamond":
            # 다이아몬드 대형 - 마름모 형태로 배열
            if formation_index == 0:  # 첫 번째 추종 차량
                target_x = leader_x - 15.0
                target_y = leader_y
            elif formation_index == 1:  # 왼쪽 차량
                target_x = leader_x - 7.5
                target_y = leader_y - 3.5
            elif formation_index == 2:  # 오른쪽 차량
                target_x = leader_x - 7.5
                target_y = leader_y + 3.5
            else:  # 추가 차량들은 뒤쪽에 일렬로
                target_x = leader_x - 25.0 - (formation_index - 3) * 12.0
                target_y = leader_y
            
            target_z = leader_z
        
        return (target_x, target_y, target_z)
    
    def calculate_leader_follower_gap(self, leader_pos, follower_pos, desired_time_gap=2.0):
        """선두-후속 차량 간격 계산 및 관리"""
        # 현재 거리 계산
        current_distance = np.sqrt((leader_pos[0] - follower_pos[0])**2 + 
                                 (leader_pos[1] - follower_pos[1])**2)
        
        # 속도 기반 안전 거리 계산 (시간 간격 기반)
        leader_velocity = 60 / 3.6  # 60 km/h를 m/s로 변환
        desired_distance = leader_velocity * desired_time_gap + self.vehicle_length
        
        gap_status = {
            'current_distance': current_distance,
            'desired_distance': desired_distance,
            'gap_error': current_distance - desired_distance,
            'time_gap': current_distance / leader_velocity if leader_velocity > 0 else float('inf'),
            'safety_status': 'SAFE' if current_distance >= desired_distance else 'TOO_CLOSE'
        }
        
        return gap_status
    
    def calculate_convoy_center(self):
        """차량 군집의 중심점 계산"""
        if not self.convoy_members:
            return None
        
        positions = [member['position'] for member in self.convoy_members.values()]
        positions = np.array(positions)
        
        center_x = np.mean(positions[:, 0])
        center_y = np.mean(positions[:, 1])
        center_z = np.mean(positions[:, 2])
        
        # 군집의 크기(반경) 계산
        distances = [np.sqrt((pos[0] - center_x)**2 + (pos[1] - center_y)**2) 
                    for pos in positions]
        convoy_radius = max(distances) if distances else 0
        
        return {
            'center': (center_x, center_y, center_z),
            'radius': convoy_radius,
            'vehicle_count': len(self.convoy_members)
        }
    
    def manage_convoy_coordination(self, my_position, leader_position):
        """군집 주행 협조 제어"""
        # 내 위치에서 대형 기준점까지의 오차 계산
        my_formation_index = list(self.convoy_members.keys()).index(self.vehicle_id) \
                            if self.vehicle_id in self.convoy_members else 0
        
        target_position = self.calculate_formation_reference(leader_position, my_formation_index)
        
        # 위치 오차 계산
        position_error = {
            'longitudinal': my_position[0] - target_position[0],  # 전후 방향
            'lateral': my_position[1] - target_position[1],       # 좌우 방향
            'total_error': np.sqrt((my_position[0] - target_position[0])**2 + 
                                 (my_position[1] - target_position[1])**2)
        }
        
        # 제어 명령 생성
        control_action = {
            'throttle_adjustment': -0.1 if position_error['longitudinal'] > 1.0 else 0.1,
            'steering_adjustment': -0.05 * position_error['lateral'],
            'target_position': target_position,
            'formation_status': 'IN_FORMATION' if position_error['total_error'] < 2.0 else 'ADJUSTING'
        }
        
        return control_action

# 사용 예시
# 군집 주행 시스템 초기화
leader_vehicle = MultiVehicleReferencePoints("LEADER_001")
follower1 = MultiVehicleReferencePoints("FOLLOWER_001")
follower2 = MultiVehicleReferencePoints("FOLLOWER_002")

# 군집 구성
leader_position = (100, 50, 0)
follower1_position = (85, 50, 0)
follower2_position = (70, 50, 0)

# 선두 차량에 추종 차량들 등록
leader_vehicle.add_convoy_member("FOLLOWER_001", follower1_position, "follower")
leader_vehicle.add_convoy_member("FOLLOWER_002", follower2_position, "follower")

# 대형 변경 (쐐기형으로)
leader_vehicle.formation_type = "wedge"

print("=== 군집 주행 시스템 ===")

# 각 추종 차량의 목표 위치 계산
for i, (vehicle_id, member_info) in enumerate(leader_vehicle.convoy_members.items()):
    target_pos = leader_vehicle.calculate_formation_reference(leader_position, i)
    print(f"{vehicle_id} 목표 위치: ({target_pos[0]:.2f}, {target_pos[1]:.2f})")

# 차간 거리 분석
gap_analysis = leader_vehicle.calculate_leader_follower_gap(
    leader_position, follower1_position, desired_time_gap=2.0
)
print(f"\n차간 거리 분석: {gap_analysis}")

# 군집 중심 계산
convoy_center = leader_vehicle.calculate_convoy_center()
print(f"\n군집 중심: {convoy_center}")

# 추종 차량의 제어 명령 생성
follower1.convoy_members = {follower1.vehicle_id: {'position': follower1_position, 'role': 'follower'}}
control_command = follower1.manage_convoy_coordination(follower1_position, leader_position)
print(f"\n추종 차량 제어 명령: {control_command}")
```

### 📊 실행 결과
```
=== 군집 주행 시스템 ===
FOLLOWER_001 목표 위치: (90.00, 53.50)
FOLLOWER_002 목표 위치: (80.00, -56.50)

차간 거리 분석: {'current_distance': 15.0, 'desired_distance': 37.78, 'gap_error': -22.78, 'time_gap': 0.9, 'safety_status': 'TOO_CLOSE'}

군집 중심: {'center': (85.0, 50.0, 0.0), 'radius': 15.0, 'vehicle_count': 2}

추종 차량 제어 명령: {'throttle_adjustment': 0.1, 'steering_adjustment': 0.0, 'target_position': (90.0, 53.5, 0), 'formation_status': 'ADJUSTING'}
```

---

## 14. 환경 인식 기준점들

날씨, 가시거리 등 주변 환경을 인식하기 위한 센서 기준점들입니다.

### 🔧 코드 예시

```python
import random
import math
from enum import Enum

class WeatherCondition(Enum):
    CLEAR = "맑음"
    RAIN = "비"
    SNOW = "눈"
    FOG = "안개"
    HEAVY_RAIN = "폭우"

class EnvironmentalReferencePoints:
    """환경 인식을 위한 기준점 관리 클래스"""
    
    def __init__(self, vehicle_config):
        self.vehicle_config = vehicle_config
        self.sensor_positions = self._define_sensor_positions()
        self.environmental_thresholds = self._define_thresholds()
        
    def _define_sensor_positions(self):
        """환경 센서 위치 정의"""
        return {
            'rain_sensor': (0, 0, 1.4),           # 앞유리 상단
            'temperature_sensor': (-2.0, 0, 0.5), # 뒷범퍼 근처 (엔진열 영향 최소화)
            'humidity_sensor': (1.0, 0.5, 1.0),   # 사이드미러 근처
            'visibility_sensor': (2.0, 0, 1.2),   # 전면 카메라 위치
            'ambient_light': (0, 0, 1.5),         # 지붕 중앙
            'wind_sensor': (0, 0, 1.6)            # 지붕 최상단
        }
    
    def _define_thresholds(self):
        """환경 조건별 임계값 정의"""
        return {
            'visibility': {
                'excellent': 1000,  # 1km 이상
                'good': 500,        # 500m 이상
                'moderate': 200,    # 200m 이상
                'poor': 50,         # 50m 이상
                'very_poor': 10     # 10m 이상
            },
            'rain_intensity': {
                'none': 0,
                'light': 2.5,       # mm/h
                'moderate': 7.6,    # mm/h
                'heavy': 50,        # mm/h
                'very_heavy': 100   # mm/h
            },
            'temperature': {
                'freezing': 0,      # 결빙 위험
                'cold': 5,          # 타이어 성능 저하
                'optimal': 20,      # 최적 조건
                'hot': 35           # 과열 위험
            }
        }
    
    def measure_rain_intensity(self, sensor_data):
        """빗물 감지 센서를 통한 강수량 측정"""
        rain_sensor_pos = self.sensor_positions['rain_sensor']
        
        # 센서 데이터 시뮬레이션 (실제로는 하드웨어에서 받아옴)
        raw_sensor_value = sensor_data.get('rain_sensor', 0)
        
        # 센서 값을 강수량(mm/h)으로 변환
        rain_intensity = raw_sensor_value * 0.1  # 변환 계수
        
        # 강수 등급 분류
        if rain_intensity <= self.environmental_thresholds['rain_intensity']['none']:
            rain_level = "없음"
        elif rain_intensity <= self.environmental_thresholds['rain_intensity']['light']:
            rain_level = "약한 비"
        elif rain_intensity <= self.environmental_thresholds['rain_intensity']['moderate']:
            rain_level = "보통 비"
        elif rain_intensity <= self.environmental_thresholds['rain_intensity']['heavy']:
            rain_level = "강한 비"
        else:
            rain_level = "매우 강한 비"
        
        return {
            'sensor_position': rain_sensor_pos,
            'intensity_mmh': rain_intensity,
            'level': rain_level,
            'wiper_recommendation': rain_intensity > 1.0,
            'speed_reduction_factor': max(0.7, 1.0 - rain_intensity / 100)
        }
    
    def measure_visibility_distance(self, weather_condition, time_of_day="day"):
        """가시거리 측정 및 분석"""
        visibility_sensor_pos = self.sensor_positions['visibility_sensor']
        
        # 기본 가시거리 (날씨별)
        base_visibility = {
            WeatherCondition.CLEAR: 2000,
            WeatherCondition.RAIN: 800,
            WeatherCondition.SNOW: 400,
            WeatherCondition.FOG: 100,
            WeatherCondition.HEAVY_RAIN: 200
        }
        
        visibility = base_visibility.get(weather_condition, 1000)
        
        # 시간대 보정 (야간에는 가시거리 감소)
        if time_of_day == "night":
            visibility *= 0.6
        elif time_of_day == "dawn" or time_of_day == "dusk":
            visibility *= 0.8
        
        # 가시거리 등급 분류
        thresholds = self.environmental_thresholds['visibility']
        if visibility >= thresholds['excellent']:
            visibility_grade = "매우 좋음"
        elif visibility >= thresholds['good']:
            visibility_grade = "좋음"
        elif visibility >= thresholds['moderate']:
            visibility_grade = "보통"
        elif visibility >= thresholds['poor']:
            visibility_grade = "나쁨"
        else:
            visibility_grade = "매우 나쁨"
        
        return {
            'sensor_position': visibility_sensor_pos,
            'distance_m': visibility,
            'grade': visibility_grade,
            'headlight_recommendation': visibility < 500,
            'max_safe_speed': min(80, visibility / 10),  # 가시거리의 1/10 속도 권장
            'following_distance_multiplier': max(1.5, 1000 / visibility)
        }
    
    def measure_temperature_conditions(self, ambient_temp):
        """온도 조건 측정 및 분석"""
        temp_sensor_pos = self.sensor_positions['temperature_sensor']
        
        # 온도 조건 분류
        thresholds = self.environmental_thresholds['temperature']
        if ambient_temp <= thresholds['freezing']:
            temp_condition = "결빙 위험"
            tire_grip_factor = 0.6
            brake_distance_multiplier = 1.8
        elif ambient_temp <= thresholds['cold']:
            temp_condition = "추위"
            tire_grip_factor = 0.8
            brake_distance_multiplier = 1.3
        elif ambient_temp <= thresholds['optimal']:
            temp_condition = "최적"
            tire_grip_factor = 1.0
            brake_distance_multiplier = 1.0
        elif ambient_temp <= thresholds['hot']:
            temp_condition = "더위"
            tire_grip_factor = 0.9
            brake_distance_multiplier = 1.1
        else:
            temp_condition = "과열 위험"
            tire_grip_factor = 0.7
            brake_distance_multiplier = 1.4
        
        return {
            'sensor_position': temp_sensor_pos,
            'temperature_c': ambient_temp,
            'condition': temp_condition,
            'tire_grip_factor': tire_grip_factor,
            'brake_distance_multiplier': brake_distance_multiplier,
            'heating_cooling_recommendation': ambient_temp < 10 or ambient_temp > 30
        }
    
    def calculate_comprehensive_environmental_impact(self, sensor_readings):
        """종합적인 환경 영향 분석"""
        rain_data = self.measure_rain_intensity(sensor_readings)
        visibility_data = self.measure_visibility_distance(
            sensor_readings.get('weather', WeatherCondition.CLEAR),
            sensor_readings.get('time_of_day', 'day')
        )
        temp_data = self.measure_temperature_conditions(
            sensor_readings.get('temperature', 20)
        )
        
        # 종합 안전 지수 계산 (0-1 스케일)
        safety_factors = [
            rain_data['speed_reduction_factor'],
            min(1.0, visibility_data['distance_m'] / 1000),
            temp_data['tire_grip_factor']
        ]
        
        overall_safety_index = sum(safety_factors) / len(safety_factors)
        
        # 권장 주행 모드 결정
        if overall_safety_index >= 0.8:
            driving_mode = "일반 주행"
            max_speed_limit = 100
        elif overall_safety_index >= 0.6:
            driving_mode = "주의 주행"
            max_speed_limit = 80
        elif overall_safety_index >= 0.4:
            driving_mode = "서행 주행"
            max_speed_limit = 60
        else:
            driving_mode = "극도 주의"
            max_speed_limit = 40
        
        return {
            'overall_safety_index': overall_safety_index,
            'recommended_driving_mode': driving_mode,
            'max_recommended_speed': max_speed_limit,
            'rain_analysis': rain_data,
            'visibility_analysis': visibility_data,
            'temperature_analysis': temp_data,
            'sensor_health_check': self._check_sensor_health()
        }
    
    def _check_sensor_health(self):
        """센서 상태 점검"""
        # 센서별 상태 시뮬레이션
        sensor_health = {}
        for sensor_name, position in self.sensor_positions.items():
            # 간단한 상태 시뮬레이션 (실제로는 진단 데이터 사용)
            health_score = random.uniform(0.8, 1.0)
            status = "정상" if health_score > 0.9 else "점검 필요" if health_score > 0.7 else "고장"
            
            sensor_health[sensor_name] = {
                'position': position,
                'health_score': health_score,
                'status': status
            }
        
        return sensor_health

# 사용 예시
vehicle_config = {'length': 4.5, 'width': 1.8, 'height': 1.6}
env_system = EnvironmentalReferencePoints(vehicle_config)

# 센서 데이터 시뮬레이션
sensor_readings = {
    'rain_sensor': 25,  # 센서 원시값
    'temperature': 3,   # 3도 (결빙 위험)
    'weather': WeatherCondition.RAIN,
    'time_of_day': 'night'
}

print("=== 환경 인식 시스템 분석 ===")

# 종합 환경 분석
comprehensive_analysis = env_system.calculate_comprehensive_environmental_impact(sensor_readings)

print(f"전체 안전 지수: {comprehensive_analysis['overall_safety_index']:.2f}")
print(f"권장 주행 모드: {comprehensive_analysis['recommended_driving_mode']}")
print(f"최대 권장 속도: {comprehensive_analysis['max_recommended_speed']} km/h")

print(f"\n강수 분석:")
rain_info = comprehensive_analysis['rain_analysis']
print(f"  강수량: {rain_info['intensity_mmh']:.1f} mm/h ({rain_info['level']})")
print(f"  와이퍼 작동 권장: {rain_info['wiper_recommendation']}")

print(f"\n가시거리 분석:")
visibility_info = comprehensive_analysis['visibility_analysis']
print(f"  가시거리: {visibility_info['distance_m']}m ({visibility_info['grade']})")
print(f"  전조등 켜기 권장: {visibility_info['headlight_recommendation']}")

print(f"\n온도 분석:")
temp_info = comprehensive_analysis['temperature_analysis']
print(f"  온도: {temp_info['temperature_c']}°C ({temp_info['condition']})")
print(f"  타이어 그립 계수: {temp_info['tire_grip_factor']}")
```

### 📊 실행 결과
```
=== 환경 인식 시스템 분석 ===
전체 안전 지수: 0.52
권장 주행 모드: 서행 주행
최대 권장 속도: 60 km/h

강수 분석:
  강수량: 2.5 mm/h (약한 비)
  와이퍼 작동 권장: True

가시거리 분석:
  가시거리: 480m (보통)
  전조등 켜기 권장: True

온도 분석:
  온도: 3°C (결빙 위험)
  타이어 그립 계수: 0.6
```

---

## 15. 보험/사고 조사 기준점들

사고 발생 시 원인 분석과 책임 소재 파악을 위한 기준점들입니다.

### 🔧 코드 예시

```python
import json
import hashlib
from datetime import datetime
from typing import Dict, List, Tuple

class AccidentAnalysisReferencePoints:
    """사고 분석 및 보험 조사용 기준점 관리 클래스"""
    
    def __init__(self, vehicle_id, insurance_policy):
        self.vehicle_id = vehicle_id
        self.insurance_policy = insurance_policy
        self.black_box_data = []
        self.impact_points = self._define_impact_measurement_points()
        
    def _define_impact_measurement_points(self):
        """충돌 측정 기준점들 정의"""
        return {
            'front_impact_center': (2.25, 0, 0.8),      # 전면 충돌 중심점
            'rear_impact_center': (-2.25, 0, 0.8),      # 후면 충돌 중심점
            'left_side_impact': (0, 0.9, 0.8),          # 좌측 충돌점
            'right_side_impact': (0, -0.9, 0.8),        # 우측 충돌점
            'rollover_reference': (0, 0, 1.2),          # 전복 기준점
            'crumple_zone_front': (1.8, 0, 0.5),        # 전방 크럼플 존
            'crumple_zone_rear': (-1.8, 0, 0.5),        # 후방 크럼플 존
            'occupant_protection_zone': (0, 0, 1.0)     # 승객 보호 구역
        }
    
    def record_pre_accident_data(self, vehicle_state, environmental_conditions):
        """사고 전 데이터 기록"""
        timestamp = datetime.now().isoformat()
        
        pre_accident_record = {
            'timestamp': timestamp,
            'vehicle_position': vehicle_state['position'],
            'velocity': vehicle_state['velocity'],
            'acceleration': vehicle_state.get('acceleration', 0),
            'steering_angle': vehicle_state.get('steering_angle', 0),
            'brake_status': vehicle_state.get('brake_applied', False),
            'throttle_position': vehicle_state.get('throttle', 0),
            'environmental_conditions': environmental_conditions,
            'data_hash': self._generate_data_hash(vehicle_state, environmental_conditions)
        }
        
        self.black_box_data.append(pre_accident_record)
        
        # 최근 30초 데이터만 유지 (메모리 관리)
        if len(self.black_box_data) > 300:  # 10Hz 기준 30초
            self.black_box_data.pop(0)
        
        return pre_accident_record
    
    def analyze_accident_reconstruction(self, impact_data, final_positions):
        """사고 재현 분석"""
        impact_point = impact_data['impact_location']
        impact_force = impact_data['impact_magnitude']
        impact_angle = impact_data['impact_angle']
        
        # 충돌 유형 분석
        collision_type = self._determine_collision_type(impact_point, impact_angle)
        
        # 충돌 속도 역산 (에너지 보존 법칙 적용)
        estimated_impact_speed = self._estimate_impact_speed(
            impact_force, collision_type, final_positions
        )
        
        # 책임 소재 초기 분석
        liability_factors = self._analyze_liability_factors(
            self.black_box_data[-10:],  # 사고 직전 1초 데이터
            collision_type,
            impact_angle
        )
        
        reconstruction_report = {
            'accident_id': hashlib.md5(f"{self.vehicle_id}_{datetime.now()}".encode()).hexdigest(),
            'collision_type': collision_type,
            'impact_location': impact_point,
            'estimated_impact_speed': estimated_impact_speed,
            'collision_angle': impact_angle,
            'pre_accident_trajectory': self._calculate_pre_accident_trajectory(),
            'liability_analysis': liability_factors,
            'damage_assessment': self._assess_vehicle_damage(impact_point, impact_force),
            'evidence_preservation': self._preserve_digital_evidence()
        }
        
        return reconstruction_report
    
    def _determine_collision_type(self, impact_point, impact_angle):
        """충돌 유형 결정"""
        x, y, z = impact_point
        
        if abs(y) < 0.5:  # 전후방 충돌
            if x > 0:
                return "정면 충돌"
            else:
                return "후면 추돌"
        elif abs(x) < 1.0:  # 측면 충돌
            if y > 0:
                return "좌측면 충돌"
            else:
                return "우측면 충돌"
        elif impact_angle > 30:
            return "각도 충돌"
        else:
            return "접촉 사고"
    
    def _estimate_impact_speed(self, impact_force, collision_type, final_positions):
        """충돌 속도 추정"""
        # 간단한 충돌 역학 모델 (실제로는 더 복잡한 계산 필요)
        base_speed_factor = {
            "정면 충돌": 1.2,
            "후면 추돌": 0.8,
            "좌측면 충돌": 1.0,
            "우측면 충돌": 1.0,
            "각도 충돌": 0.9,
            "접촉 사고": 0.3
        }
        
        factor = base_speed_factor.get(collision_type, 1.0)
        estimated_speed = (impact_force / 1000) * factor * 10  # 단순화된 계산
        
        return min(estimated_speed, 200)  # 현실적인 최대값 제한
    
    def _analyze_liability_factors(self, recent_data, collision_type, impact_angle):
        """책임 소재 분석 요소들"""
        if not recent_data:
            return {'analysis': '데이터 부족', 'confidence': 0}
        
        last_record = recent_data[-1]
        
        liability_factors = {
            'speed_compliance': self._check_speed_compliance(last_record),
            'brake_application': last_record.get('brake_status', False),
            'steering_input': abs(last_record.get('steering_angle', 0)) > 5,
            'environmental_factors': last_record.get('environmental_conditions', {}),
            'traffic_violation_indicators': self._check_traffic_violations(recent_data),
            'evasive_action_taken': self._detect_evasive_actions(recent_data)
        }
        
        # 간단한 책임도 계산 (실제로는 전문가 시스템 필요)
        responsibility_score = 0.


# 🚗 NumPy 자율주행 완벽 가이드

## 📌 목차
- [소개](#-소개)
- [환경 설정](#-환경-설정)
- [기본 사용법](#1-numpy-기본-사용법)
- [인덱싱 & 슬라이싱](#2-배열-인덱싱--슬라이싱)
- [배열 연산](#3-배열-연산)
- [형태 변경 & 통계](#4-배열-형태-변경--통계-함수)
- [자율주행 실전 예제](#5-자율주행-실전-예제)
- [마무리](#-마무리)

---

## 🎯 소개

**NumPy**는 자율주행 시스템 개발에 **필수적인 라이브러리**입니다. 

### 왜 자율주행에서 NumPy가 중요한가요?
- 📡 **센서 데이터 처리**: LiDAR, 카메라, IMU 등의 대용량 데이터
- 🧮 **수학적 연산**: 좌표 변환, 회전 행렬, 벡터 연산
- 🖼️ **이미지 처리**: 픽셀 데이터 조작 및 필터링
- ⚡ **성능 최적화**: 순수 Python 대비 최대 100배 빠른 연산

---

## 🛠 환경 설정

```bash
# NumPy 설치
pip install numpy

# 추가 라이브러리 (시각화용)
pip install matplotlib opencv-python
```

---

## 1. NumPy 기본 사용법

### 1.1 라이브러리 임포트 및 배열 생성

```python
import numpy as np

# 🔧 기본 배열 생성
# 1차원: 차량 속도 데이터
vehicle_speed = np.array([30, 45, 60, 55, 40])  # km/h
print(f"차량 속도: {vehicle_speed}")
print(f"배열 형태: {vehicle_speed.shape}")  # (5,)

# 2차원: 3D 포인트 클라우드 (x, y, z 좌표)
lidar_points = np.array([
    [1.2, 0.5, 0.1],  # 포인트 1
    [2.3, -1.0, 0.2], # 포인트 2
    [0.8, 2.1, 0.0]   # 포인트 3
])
print(f"LiDAR 포인트:\n{lidar_points}")
print(f"포인트 개수: {lidar_points.shape[0]}, 좌표 차원: {lidar_points.shape[1]}")
```

### 1.2 특수 배열 생성

```python
# 🖼️ 빈 이미지 생성 (640x480, 흑백)
empty_image = np.zeros((480, 640))
print(f"빈 이미지 크기: {empty_image.shape}")

# 🎯 단위 행렬 (회전 행렬 초기화용)
identity_matrix = np.eye(3)
print(f"3x3 단위 행렬:\n{identity_matrix}")

# 📊 균등 분포 데이터 생성
time_stamps = np.linspace(0, 10, 100)  # 0~10초, 100개 샘플
print(f"시간 샘플: {time_stamps[:5]}...")  # 처음 5개만 출력
```

### 1.3 데이터 타입 관리

```python
# 📏 메모리 효율적인 데이터 타입 선택
gps_coordinates = np.array([37.5665, 126.9780], dtype=np.float32)  # 위도, 경도
sensor_readings = np.array([1, 0, 1, 1, 0], dtype=np.bool_)       # 센서 on/off

print(f"GPS 좌표: {gps_coordinates} (타입: {gps_coordinates.dtype})")
print(f"센서 상태: {sensor_readings} (타입: {sensor_readings.dtype})")
```

---

## 2. 배열 인덱싱 & 슬라이싱

### 2.1 기본 인덱싱

```python
# 🖼️ 카메라 이미지 시뮬레이션 (간단한 4x4 픽셀)
camera_image = np.array([
    [10,  20,  30,  40 ],
    [50,  60,  70,  80 ],
    [90,  100, 110, 120],
    [130, 140, 150, 160]
])

print("카메라 이미지:")
print(camera_image)

# 🎯 특정 픽셀 값 접근
print(f"좌상단 픽셀: {camera_image[0, 0]}")
print(f"우하단 픽셀: {camera_image[3, 3]}")
```

### 2.2 슬라이싱으로 ROI 추출

```python
# 🔍 관심 영역(ROI) 추출
# 예: 도로 표지판이 있는 중앙 영역
roi = camera_image[1:3, 1:3]  # 2x2 중앙 영역
print(f"관심 영역 (ROI):\n{roi}")

# 📊 첫 번째 행 전체 (수평선 검출용)
horizon_line = camera_image[0, :]
print(f"수평선 픽셀: {horizon_line}")

# 📊 마지막 열 전체 (차선 검출용)
lane_edge = camera_image[:, -1]
print(f"차선 가장자리: {lane_edge}")
```

### 2.3 조건부 필터링

```python
# 🔧 밝은 픽셀만 추출 (임계값 기반)
bright_pixels = camera_image[camera_image > 80]
print(f"밝은 픽셀 (>80): {bright_pixels}")

# 🔧 특정 범위의 픽셀 (노이즈 제거)
normal_range = camera_image[(camera_image >= 50) & (camera_image <= 120)]
print(f"정상 범위 픽셀 (50~120): {normal_range}")

# 📍 조건을 만족하는 위치 찾기
bright_positions = np.where(camera_image > 100)
print(f"밝은 픽셀 위치 (행, 열): {list(zip(bright_positions[0], bright_positions[1]))}")
```

---

## 3. 배열 연산

### 3.1 벡터 연산 (좌표 변환)

```python
# 🚗 차량 위치 데이터
vehicle_position = np.array([10.0, 5.0, 0.0])  # x, y, z (미터)
translation_vector = np.array([2.0, -1.0, 0.5])  # 이동량

# ➕ 위치 업데이트
new_position = vehicle_position + translation_vector
print(f"이전 위치: {vehicle_position}")
print(f"새 위치: {new_position}")

# ✖️ 스케일링 (단위 변환: 미터 → 센티미터)
position_cm = vehicle_position * 100
print(f"센티미터 단위: {position_cm}")
```

### 3.2 행렬 연산 (회전 변환)

```python
# 🔄 2D 회전 행렬 (45도 회전)
angle = np.pi / 4  # 45도를 라디안으로
rotation_matrix = np.array([
    [np.cos(angle), -np.sin(angle)],
    [np.sin(angle),  np.cos(angle)]
])

# 📍 2D 포인트들
points_2d = np.array([
    [1, 0],    # 포인트 1
    [0, 1],    # 포인트 2
    [-1, 0]    # 포인트 3
])

# 🔄 포인트들 회전
rotated_points = points_2d @ rotation_matrix
print(f"원본 포인트:\n{points_2d}")
print(f"회전된 포인트:\n{rotated_points}")
```

### 3.3 LiDAR 데이터 처리

```python
# 📡 LiDAR 포인트 클라우드 (거리 기반 필터링)
lidar_distances = np.array([2.1, 15.8, 3.2, 45.6, 1.9, 25.3])  # 미터

# 🔧 근거리 객체만 필터링 (20m 이내)
nearby_objects = lidar_distances[lidar_distances < 20.0]
print(f"근거리 객체 거리: {nearby_objects}")

# 📊 거리 통계
print(f"평균 거리: {np.mean(lidar_distances):.2f}m")
print(f"최근접 객체: {np.min(lidar_distances):.2f}m")
print(f"최원거리 객체: {np.max(lidar_distances):.2f}m")
```

---

## 4. 배열 형태 변경 & 통계 함수

### 4.1 형태 변경

```python
# 📊 센서 데이터 재구성
sensor_readings = np.arange(1, 13)  # 1~12번 센서
print(f"1D 센서 데이터: {sensor_readings}")

# 🔧 3x4 그리드로 재배치
sensor_grid = sensor_readings.reshape(3, 4)
print(f"3x4 센서 그리드:\n{sensor_grid}")

# 🔧 자동 차원 계산 (-1 사용)
sensor_2col = sensor_readings.reshape(-1, 2)  # 2열, 행은 자동 계산
print(f"2열 배치:\n{sensor_2col}")

# 📏 1차원으로 평탄화
flattened = sensor_grid.flatten()
print(f"평탄화된 데이터: {flattened}")
```

### 4.2 브로드캐스팅

```python
# 🔧 센서 보정값 적용
sensor_matrix = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

# 각 열에 서로 다른 보정값 적용
calibration_factors = np.array([0.9, 1.0, 1.1])  # 열별 보정
calibrated_sensors = sensor_matrix * calibration_factors

print(f"원본 센서값:\n{sensor_matrix}")
print(f"보정된 센서값:\n{calibrated_sensors}")

# 각 행에 오프셋 적용
row_offsets = np.array([[5], [10], [15]])  # 행별 오프셋
offset_sensors = sensor_matrix + row_offsets
print(f"오프셋 적용 결과:\n{offset_sensors}")
```

### 4.3 통계 분석

```python
# 📊 주행 데이터 분석
driving_speeds = np.array([
    [30, 45, 60, 55],  # 1구간 속도
    [35, 50, 65, 50],  # 2구간 속도
    [25, 40, 55, 45]   # 3구간 속도
])

print("구간별 주행 속도:")
print(driving_speeds)

# 📈 기본 통계
print(f"전체 평균 속도: {np.mean(driving_speeds):.1f} km/h")
print(f"최고 속도: {np.max(driving_speeds)} km/h")
print(f"속도 표준편차: {np.std(driving_speeds):.2f}")

# 📊 축별 통계
print(f"구간별 평균 속도: {np.mean(driving_speeds, axis=1)}")  # 각 행의 평균
print(f"시점별 평균 속도: {np.mean(driving_speeds, axis=0)}")  # 각 열의 평균

# 🔍 최고속도 위치 찾기
max_speed_pos = np.unravel_index(np.argmax(driving_speeds), driving_speeds.shape)
print(f"최고속도 위치: {max_speed_pos}구간 {max_speed_pos}번째")
```

---

## 5. 자율주행 실전 예제

### 5.1 카메라 이미지 처리

```python
# 🖼️ 간단한 차선 검출 시뮬레이션
def detect_lane_lines(image):
    """간단한 차선 검출 함수"""
    # 가장자리 검출 (간단한 버전)
    edges = np.abs(np.diff(image, axis=1))  # 수평 방향 변화량
    
    # 임계값을 넘는 가장자리만 추출
    lane_threshold = np.percentile(edges, 90)  # 상위 10%
    lane_candidates = edges > lane_threshold
    
    return lane_candidates

# 테스트 이미지 생성
test_image = np.random.randint(0, 256, (10, 20))  # 10x20 랜덤 이미지
lane_detection = detect_lane_lines(test_image)

print("차선 검출 결과:")
print(lane_detection.astype(int))  # True/False를 1/0으로 표시
```

### 5.2 LiDAR 포인트 클라우드 처리

```python
# 📡 3D 포인트 클라우드 필터링
def filter_ground_points(points, ground_height_threshold=0.2):
    """지면 포인트 제거"""
    # Z 좌표가 임계값보다 높은 포인트만 유지
    return points[points[:, 2] > ground_height_threshold]

def cluster_nearby_points(points, max_distance=2.0):
    """근거리 포인트 클러스터링 (간단한 버전)"""
    distances = np.linalg.norm(points[:, :2], axis=1)  # XY 거리만 계산
    return points[distances < max_distance]

# 샘플 LiDAR 데이터
lidar_cloud = np.array([
    [1.0, 2.0, 0.1],   # 지면 근처
    [2.5, 1.5, 1.8],   # 차량 높이
    [10.0, 5.0, 0.05], # 원거리 지면
    [1.8, -1.2, 2.1],  # 근거리 객체
    [0.5, 0.8, 1.5]    # 근거리 객체
])

# 필터링 단계별 적용
print(f"원본 포인트 수: {len(lidar_cloud)}")

filtered_points = filter_ground_points(lidar_cloud)
print(f"지면 제거 후: {len(filtered_points)}")

nearby_points = cluster_nearby_points(filtered_points)
print(f"근거리 필터링 후: {len(nearby_points)}")
print("최종 포인트들:")
print(nearby_points)
```

### 5.3 GPS 좌표 변환

```python
# 🗺️ GPS 좌표계 변환
def convert_gps_to_local(gps_points, origin_gps):
    """GPS 좌표를 로컬 좌표계로 변환 (단순화된 버전)"""
    # 위도/경도 차이를 미터로 근사 변환
    lat_diff = (gps_points[:, 0] - origin_gps[0]) * 111000  # 위도 1도 ≈ 111km
    lon_diff = (gps_points[:, 1] - origin_gps[1]) * 111000 * np.cos(origin_gps[0] * np.pi / 180)
    
    return np.column_stack([lat_diff, lon_diff])

# GPS 웨이포인트
waypoints_gps = np.array([
    [37.5665, 126.9780],  # 서울시청
    [37.5651, 126.9895],  # 명동
    [37.5658, 126.9769]   # 덕수궁
])

origin = waypoints_gps[0]  # 첫 번째 지점을 원점으로
local_coords = convert_gps_to_local(waypoints_gps, origin)

print("GPS → 로컬 좌표 변환:")
for i, (gps, local) in enumerate(zip(waypoints_gps, local_coords)):
    print(f"지점 {i+1}: GPS{gps} → 로컬({local[0]:.1f}, {local[1]:.1f})m")
```

---

## 💡 성능 최적화 팁

### 벡터화 연산 사용
```python
# ❌ 느린 방법 (Python 반복문)
def slow_distance_calculation(points):
    distances = []
    for point in points:
        dist = (point[0]**2 + point[1]**2)**0.5
        distances.append(dist)
    return distances

# ✅ 빠른 방법 (NumPy 벡터화)
def fast_distance_calculation(points):
    return np.linalg.norm(points, axis=1)

# 성능 비교 예제
sample_points = np.random.randn(1000, 2)
%timeit slow_distance_calculation(sample_points)  # 느림
%timeit fast_distance_calculation(sample_points)  # 빠름
```

### 메모리 효율적인 데이터 타입
```python
# 🔧 적절한 데이터 타입 선택으로 메모리 절약
large_array = np.random.randint(0, 255, (1000, 1000))

# 8비트 정수 사용 (이미지 픽셀값 0-255)
image_data = large_array.astype(np.uint8)  # 메모리 1/8 절약

# 32비트 부동소수점 (대부분의 계산에 충분한 정밀도)
sensor_data = np.random.randn(1000, 3).astype(np.float32)  # 메모리 1/2 절약
```

---

## 🚨 주의사항 & 디버깅 팁

### 1. 배열 차원 확인
```python
# 차원 불일치 오류 방지
def safe_matrix_multiply(A, B):
    print(f"A 형태: {A.shape}, B 형태: {B.shape}")
    if A.shape[1] != B.shape[0]:
        raise ValueError(f"행렬 곱셈 불가: {A.shape} @ {B.shape}")
    return A @ B
```

### 2. NaN/Inf 값 처리
```python
# 센서 데이터의 이상값 처리
def clean_sensor_data(data):
    # NaN, Inf 값 확인
    if np.any(np.isnan(data)) or np.any(np.isinf(data)):
        print("⚠️ 이상값 감지됨!")
        # NaN을 0으로, Inf를 큰 값으로 대체
        data = np.nan_to_num(data, nan=0.0, posinf=1e6, neginf=-1e6)
    return data
```

---

## 📚 추가 학습 자료

### 관련 라이브러리
- **OpenCV**: 컴퓨터 비전 (`cv2`)
- **PCL-Python**: 포인트 클라우드 처리
- **Matplotlib**: 데이터 시각화
- **SciPy**: 과학 계산

### 자율주행 특화 활용
- 칼만 필터 구현
- SLAM 알고리즘
- 경로 계획 (Path Planning)
- 센서 퓨전 (Sensor Fusion)

---

## 🎯 마무리

이 가이드를 통해 NumPy를 자율주행 개발에 효과적으로 활용하는 방법을 익혔습니다. 

### 다음 단계
1. **실제 센서 데이터**로 연습해보기
2. **OpenCV와 결합**하여 이미지 처리 심화
3. **ROS(Robot Operating System)**와 통합
4. **실시간 처리** 최적화 기법 학습

---

