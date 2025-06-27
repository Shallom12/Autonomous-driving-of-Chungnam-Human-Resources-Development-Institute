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

    ```
    
    ```

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





































