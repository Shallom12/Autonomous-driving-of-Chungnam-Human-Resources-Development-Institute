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
- [예외 처리](#예외-처리)
- [파일 처리](#파일-처리)
- [성능 최적화](#성능-최적화)
- [일반적인 실수들](#일반적인-실수들)

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

### pass - 아무것도 하지 않음

나중에 구현할 함수나 조건문에서 임시로 사용합니다.

```python
# 미구현 함수 플레이스홀더
def emergency_brake():
    # TODO: 긴급 제동 로직 구현
    pass

def lane_change_left():
    # TODO: 좌측 차선 변경 로직
    pass

def calculate_safe_distance():
    # TODO: 안전거리 계산 로직
    pass
```

```python
# 조건부 처리에서 빈 블록
for detection in detections:
    if detection.cls == 0:         # person
        handle_pedestrian(detection)
    elif detection.cls == 2:       # car
        handle_vehicle(detection)
    elif detection.cls == 3:       # motorcycle
        handle_motorcycle(detection)
    else:
        pass                       # 다른 객체는 무시
```

---

🛡️ 예외 처리
예외 처리 습관화
사용자 입력이나 외부 데이터를 다룰 때는 항상 예외 처리를 고려해야 합니다.
❌ 위험한 코드
python# 이 코드는 사용자가 잘못된 값을 입력하면 프로그램이 중단됩니다
def dangerous_calculator():
    number = int(input("숫자 입력: "))  # ValueError 가능성
    result = 10 / number  # ZeroDivisionError 가능성
    return result
✅ 안전한 코드
pythondef safe_calculator():
    """안전한 계산기 함수"""
    while True:
        try:
            # 사용자 입력 받기
            user_input = input("숫자를 입력하세요 (종료: 'q'): ")
            
            # 종료 조건
            if user_input.lower() == 'q':
                print("계산기를 종료합니다.")
                break
            
            # 숫자 변환 시도
            number = float(user_input)  # int 대신 float 사용으로 더 유연하게
            
            # 계산 수행
            result = 10 / number
            
            print(f"10 ÷ {number} = {result:.2f}")
            
        except ValueError:
            print("❌ 오류: 올바른 숫자를 입력해주세요.")
            continue
            
        except ZeroDivisionError:
            print("❌ 오류: 0으로 나눌 수 없습니다.")
            continue
            
        except KeyboardInterrupt:
            print("\n\n👋 프로그램을 중단합니다.")
            break
            
        except Exception as e:
            print(f"❌ 예상치 못한 오류가 발생했습니다: {e}")
            continue

# 파일 처리 예외 처리 예시
def safe_file_reader(filename):
    """안전한 파일 읽기 함수"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(f"✅ 파일 '{filename}' 읽기 성공")
            return content
            
    except FileNotFoundError:
        print(f"❌ 오류: 파일 '{filename}'을 찾을 수 없습니다.")
        return None
        
    except PermissionError:
        print(f"❌ 오류: 파일 '{filename}'에 접근할 권한이 없습니다.")
        return None
        
    except UnicodeDecodeError:
        print(f"❌ 오류: 파일 '{filename}'의 인코딩을 해석할 수 없습니다.")
        return None
        
    except Exception as e:
        print(f"❌ 파일 읽기 중 오류 발생: {e}")
        return None

# 네트워크 요청 예외 처리 예시
def safe_network_request(url):
    """안전한 네트워크 요청 (예시)"""
    import time
    
    max_retries = 3
    retry_delay = 1
    
    for attempt in range(max_retries):
        try:
            print(f"🌐 네트워크 요청 시도 {attempt + 1}/{max_retries}: {url}")
            
            # 실제로는 requests 라이브러리 등을 사용
            # response = requests.get(url, timeout=10)
            
            # 시뮬레이션을 위한 임의 처리
            if attempt < 2:  # 처음 두 번은 실패 시뮬레이션
                raise ConnectionError("네트워크 연결 실패")
            
            print("✅ 네트워크 요청 성공!")
            return "데이터 수신 완료"
            
        except ConnectionError as e:
            print(f"❌ 연결 오류: {e}")
            if attempt < max_retries - 1:
                print(f"⏳ {retry_delay}초 후 재시도...")
                time.sleep(retry_delay)
                retry_delay *= 2  # 지수 백오프
            else:
                print("❌ 최대 재시도 횟수에 도달했습니다.")
                return None
                
        except Exception as e:
            print(f"❌ 예상치 못한 오류: {e}")
            return None

# 예외 처리 테스트
print("📁 파일 읽기 테스트:")
result = safe_file_reader("nonexistent_file.txt")

print("\n🌐 네트워크 요청 테스트:")
result = safe_network_request("https://example.com")
실행 결과:
📁 파일 읽기 테스트:
❌ 오류: 파일 'nonexistent_file.txt'을 찾을 수 없습니다.

🌐 네트워크 요청 테스트:
🌐 네트워크 요청 시도 1/3: https://example.com
❌ 연결 오류: 네트워크 연결 실패
⏳ 1초 후 재시도...
🌐 네트워크 요청 시도 2/3: https://example.com
❌ 연결 오류: 네트워크 연결 실패
⏳ 2초 후 재시도...
🌐 네트워크 요청 시도 3/3: https://example.com
✅ 네트워크 요청 성공!

📁 파일 처리
파일 닫기 잊지 말기
파일을 열었으면 반드시 닫아야 합니다. with 문을 사용하면 자동으로 처리됩니다.
❌ 위험한 코드
python# 파일을 열고 닫는 것을 잊기 쉬운 방식
def dangerous_file_handling():
    file = open("data.txt", "w")
    file.write("Hello World")
    # file.close()를 잊으면 메모리 누수 가능성!
    
# 예외 발생 시 파일이 닫히지 않을 수 있는 경우
def risky_file_handling():
    file = open("data.txt", "r")
    try:
        data = file.read()
        # 여기서 오류가 발생하면?
        result = int(data)  # 숫자가 아니면 ValueError
    except ValueError:
        print("숫자 변환 오류")
        # file.close()가 실행되지 않음!
    finally:
        file.close()  # finally를 사용해야 함
✅ 안전한 코드
pythondef safe_file_writing():
    """with 문을 사용한 안전한 파일 쓰기"""
    try:
        with open("data.txt", "w", encoding="utf-8") as file:
            file.write("안녕하세요, Python!")
            file.write("\n두 번째 줄입니다.")
            file.write(f"\n현재 시간: {datetime.now()}")
        print("✅ 파일 쓰기 완료 (자동으로 파일이 닫힘)")
        
    except IOError as e:
        print(f"❌ 파일 쓰기 오류: {e}")

def safe_file_reading():
    """with 문을 사용한 안전한 파일 읽기"""
    try:
        with open("data.txt", "r", encoding="utf-8") as file:
            print("📖 파일 내용:")
            line_number = 1
            for line in file:
                print(f"{line_number:2d}: {line.strip()}")
                line_number += 1
        print("✅ 파일 읽기 완료")
        
    except FileNotFoundError:
        print("❌ 파일을 찾을 수 없습니다.")
    except IOError as e:
        print(f"❌ 파일 읽기 오류: {e}")

def advanced_file_operations():
    """고급 파일 처리 예시"""
    import json
    import csv
    from pathlib import Path
    
    # JSON 파일 처리
    data = {
        "name": "홍길동",
        "age": 30,
        "skills": ["Python", "JavaScript", "SQL"],
        "active": True
    }
    
    # JSON 파일 쓰기
    try:
        with open("user_data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=2)
        print("✅ JSON 파일 저장 완료")
    except Exception as e:
        print(f"❌ JSON 저장 오류: {e}")
    
    # JSON 파일 읽기
    try:
        with open("user_data.json", "r", encoding="utf-8") as json_file:
            loaded_data = json.load(json_file)
        print(f"📄 JSON 데이터: {loaded_data}")
    except Exception as e:
        print(f"❌ JSON 읽기 오류: {e}")
    
    # CSV 파일 처리
    csv_data = [
        ["이름", "나이", "직업"],
        ["김철수", 25, "개발자"],
        ["이영희", 30, "디자이너"],
        ["박민수", 35, "기획자"]
    ]
    
    try:
        with open("employees.csv", "w", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(csv_data)
        print("✅ CSV 파일 저장 완료")
        
        # CSV 파일 읽기
        with open("employees.csv", "r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            print("📊 CSV 데이터:")
            for row_num, row in enumerate(reader, 1):
                print(f"  {row_num}: {row}")
                
    except Exception as e:
        print(f"❌ CSV 처리 오류: {e}")

# 파일 처리 함수들 실행
print("📝 파일 처리 예제 실행:")
safe_file_writing()
safe_file_reading()
print()
advanced_file_operations()
실행 결과:
📝 파일 처리 예제 실행:
✅ 파일 쓰기 완료 (자동으로 파일이 닫힘)
📖 파일 내용:
 1: 안녕하세요, Python!
 2: 두 번째 줄입니다.
 3: 현재 시간: 2024-06-27 10:30:45.123456

✅ JSON 파일 저장 완료
📄 JSON 데이터: {'name': '홍길동', 'age': 30, 'skills': ['Python', 'JavaScript', 'SQL'], 'active': True}
✅ CSV 파일 저장 완료
📊 CSV 데이터:
  1: ['이름', '나이', '직업']
  2: ['김철수', '25', '개발자']
  3: ['이영희', '30', '디자이너']
  4: ['박민수', '35', '기획자']

⚡ 성능 최적화
문자열 연결 최적화
많은 문자열을 연결할 때는 효율적인 방법을 사용해야 합니다.
❌ 비효율적인 방법
pythonimport time

def inefficient_string_concat():
    """비효율적인 문자열 연결"""
    start_time = time.time()
    
    result = ""
    for i in range(10000):
        result += str(i) + ", "  # 매번 새로운 문자열 객체 생성
    
    end_time = time.time()
    return result[:50] + "...", end_time - start_time

# 비효율적인 방법 테스트
result, duration = inefficient_string_concat()
print(f"❌ 비효율적 방법:")
print(f"   결과: {result}")
print(f"   소요시간: {duration:.4f}초")
✅ 효율적인 방법
pythondef efficient_string_concat():
    """효율적인 문자열 연결 방법들"""
    
    # 방법 1: join() 사용 (가장 효율적)
    start_time = time.time()
    result1 = ", ".join(str(i) for i in range(10000))
    time1 = time.time() - start_time
    
    # 방법 2: 리스트 사용 후 join
    start_time = time.time()
    parts = []
    for i in range(10000):
        parts.append(str(i))
    result2 = ", ".join(parts)
    time2 = time.time() - start_time
    
    # 방법 3: f-string과 join 조합
    start_time = time.time()
    result3 = ", ".join(f"number_{i}" for i in range(10000))
    time3 = time.time() - start_time
    
    return [
        (result1[:50] + "...", time1, "join() with generator"),
        (result2[:50] + "...", time2, "list + join()"),
        (result3[:50] + "...", time3, "f-string + join()")
    ]

# 효율적인 방법들 테스트
results = efficient_string_concat()
print(f"\n✅ 효율적인 방법들:")
for i, (result, duration, method) in enumerate(results, 1):
    print(f"   방법 {i} ({method}):")
    print(f"     결과: {result}")
    print(f"     소요시간: {duration:.4f}초")
실행 결과:
❌ 비효율적 방법:
   결과: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ...
   소요시간: 0.2845초

✅ 효율적인 방법들:
   방법 1 (join() with generator):
     결과: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ...
     소요시간: 0.0034초
   방법 2 (list + join()):
     결과: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, ...
     소요시간: 0.0038초
   방법 3 (f-string + join()):
     결과: number_0, number_1, number_2, number_3, number_4, n...
     소요시간: 0.0055초
리스트 컴프리헨션 활용
반복문보다 리스트 컴프리헨션이 더 효율적이고 가독성이 좋습니다.
pythondef compare_list_creation_methods():
    """리스트 생성 방법별 성능 비교"""
    import time
    
    # 데이터 크기
    size = 100000
    
    # 방법 1: 일반 for 루프
    start = time.time()
    result1 = []
    for i in range(size):
        if i % 2 == 0:
            result1.append(i ** 2)
    time1 = time.time() - start
    
    # 방법 2: 리스트 컴프리헨션
    start = time.time()
    result2 = [i ** 2 for i in range(size) if i % 2 == 0]
    time2 = time.time() - start
    
    # 방법 3: filter와 map 조합
    start = time.time()
    result3 = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(size))))
    time3 = time.time() - start
    
    # 방법 4: 제너레이터 표현식
    start = time.time()
    result4 = list(i ** 2 for i in range(size) if i % 2 == 0)
    time4 = time.time() - start
    
    print(f"📊 리스트 생성 방법별 성능 비교 (크기: {size:,})")
    print(f"   1. 일반 for 루프:      {time1:.4f}초")
    print(f"   2. 리스트 컴프리헨션:   {time2:.4f}초 (🏆 가장 빠름)")
    print(f"   3. filter + map:      {time3:.4f}초")
    print(f"   4. 제너레이터 표현식:   {time4:.4f}초")
    
    # 결과 확인 (모든 방법이 같은 결과를 생성하는지)
    print(f"\n🔍 결과 일치 여부:")
    print(f"   길이: {len(result1)} = {len(result2)} = {len(result3)} = {len(result4)}")
    print(f"   내용 일치: {result1 == result2 == result3 == result4}")
    print(f"   첫 10개 요소: {result1[:10]}")

compare_list_creation_methods()
실행 결과:
📊 리스트 생성 방법별 성능 비교 (크기: 100,000)
   1. 일반 for 루프:      0.0298초
   2. 리스트 컴프리헨션:   0.0187초 (🏆 가장 빠름)
   3. filter + map:      0.0312초
   4. 제너레이터 표현식:   0.0195초

🔍 결과 일치 여부:
   길이: 50000 = 50000 = 50000 = 50000
   내용 일치: True
   첫 10개 요소: [0, 4, 16, 36, 64, 100, 144, 196, 256, 324]

🚫 일반적인 실수들
print문에서 괄호 빠뜨리기
Python 3에서는 print가 함수이므로 반드시 괄호를 사용해야 합니다.
❌ Python 2 스타일 (오류)
python# Python 2 스타일 - Python 3에서는 SyntaxError
# print "Hello World"  # 이 코드는 실행되지 않습니다!
✅ Python 3 스타일 (올바름)
python# 기본 사용법
print("Hello World")

# 여러 값 출력
name = "홍길동"
age = 30
print("이름:", name, "나이:", age)

# 구분자 변경
print("사과", "바나나", "오렌지", sep=" | ")

# 끝 문자 변경
print("Loading", end="")
for i in range(3):
    print(".", end="")
print(" 완료!")

# 파일에 출력
with open("output.txt", "w") as f:
    print("파일에 저장된 내용", file=f)
    
print("다양한 print 옵션 예제 완료")
실행 결과:
Hello World
이름: 홍길동 나이: 30
사과 | 바나나 | 오렌지
Loading... 완료!
다양한 print 옵션 예제 완료
들여쓰기 혼용 문제
탭과 스페이스를 혼용하면 IndentationError가 발생합니다.
❌ 문제가 되는 코드
python# 이 코드는 보기에는 정상이지만 들여쓰기가 혼용된 경우
def mixed_indentation_example():
    if True:
        print("첫 번째 줄")  # 스페이스 4개
	print("두 번째 줄")  # 탭 문자 - IndentationError!
✅ 올바른 해결책
pythondef proper_indentation_example():
    """일관된 들여쓰기 사용 예제"""
    
    # 모든 들여쓰기를 스페이스 4개로 통일
    conditions = [
        ("sunny", "맑음"),
        ("rainy", "비"),
        ("cloudy", "흐림"),
        ("snowy", "눈")
    ]
    
    for weather_code, weather_name in conditions:
        if weather_code == "sunny":
            print(f"☀️ 날씨: {weather_name} - 외출하기 좋은 날씨입니다!")
        elif weather_code == "rainy":
            print(f"🌧️ 날씨: {weather_name} - 우산을 챙기세요!")
        elif weather_code == "cloudy":
            print(f"☁️ 날씨: {weather_name} - 적당한 날씨네요.")
        else:
            print(f"❄️ 날씨: {weather_name} - 따뜻하게 입으세요!")

proper_indentation_example()
실행 결과:
☀️ 날씨: 맑음 - 외출하기 좋은 날씨입니다!
🌧️ 날씨: 비 - 우산을 챙기세요!
☁️ 날씨: 흐림 - 적당한 날씨네요.
❄️ 날씨: 눈 - 따뜻하게 입으세요!
전역변수 사용 주의
함수 내에서 전역변수를 수정할 때는 global 키워드가 필요합니다.
❌ 잘못된 예시
pythoncounter = 0

def increment_wrong():
    counter += 1  # UnboundLocalError: local variable 'counter' referenced before assignment
    return counter

# 이 함수를 호출하면 오류 발생
# print(increment_wrong())
✅ 올바른 예시
python# 전역변수 사용 방법
global_counter = 0

def increment_global():
    """global 키워드를 사용한 전역변수 수정"""
    global global_counter
    global_counter += 1
    return global_counter

def get_global_counter():
    """전역변수 읽기는 global 없이도 가능"""
    return global_counter

# 더 좋은 방법: 클래스 사용
class Counter:
    """카운터 클래스 - 전역변수보다 안전한 방법"""
    
    def __init__(self, initial_value=0):
        self.value = initial_value
        self.history = [initial_value]
    
    def increment(self, amount=1):
        """카운터 증가"""
        self.value += amount
        self.history.append(self.value)
        return self.value
    
    def decrement(self, amount=1):
        """카운터 감소"""
        self.value -= amount
        self.history.append(self.value)
        return self.value
    
    def reset(self):
        """카운터 리셋"""
        self.value = 0
        self.history.append(0)
        return self.value
    
    def get_history(self):
        """변경 이력 반환"""
        return self.history.copy()

# 사용 예시
print("🔢 카운터 예제:")

# 전역변수 방식
print("전역변수 방식:")
print(f"  현재 값: {get_global_counter()}")
print(f"  증가 후: {increment_global()}")
print(f"  증가 후: {increment_global()}")
print(f"  현재 값: {get_global_counter()}")

# 클래스 방식 (권장)
print("\n클래스 방식 (권장):")
counter1 = Counter(10)
counter2 = Counter(100)

print(f"  counter1 초기값: {counter1.value}")
print(f"  counter2 초기값: {counter2.value}")

print(f"  counter1 증가: {counter1.increment(5)}")
print(f"  counter2 감소: {counter2.decrement(20)}")

print(f"  counter1 이력: {counter1.get_history()}")
print(f"  counter2 이력: {counter2.get_history()}")
실행 결과:
🔢 카운터 예제:
전역변수 방식:
  현재 값: 0
  증가 후: 1
  증가 후: 2
  현재 값: 2

클래스 방식 (권장):
  counter1 초기값: 10
  counter2 초기값: 100
  counter1 증가: 15
  counter2 감소: 80
  counter1 이력: [10, 15]
  counter2 이력: [100, 80]

## 💡 실전 팁

### 성능 최적화
- 반복문에서 불필요한 계산을 피하세요
- 배열 크기를 제한하여 메모리 사용량을 관리하세요
- 조건문에서 가장 가능성이 높은 조건을 먼저 배치하세요

### 코드 가독성
- 함수와 변수에 의미있는 이름을 사용하세요
- 복잡한 조건문은 함수로 분리하세요
- 주석을 활용하여 로직을 설명하세요

### 디버깅
- `print()` 문을 활용하여 값을 확인하세요
- 단계별로 결과를 시각화하세요
- 예외 상황을 미리 고려하여 방어적으로 코딩하세요

---

## 📚 참고 자료

- [OpenCV 공식 문서](https://opencv.org/)
- [YOLO 객체 탐지](https://github.com/ultralytics/yolov5)
- [Python 공식 문서](https://docs.python.org/3/)

---

*이 가이드가 자율주행 개발에 도움이 되었다면 ⭐ 스타를 눌러주세요!*

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


