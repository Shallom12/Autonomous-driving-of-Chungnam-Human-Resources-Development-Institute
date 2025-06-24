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
- [GitHub 사용법](#github-사용법)


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
![colab1](https://github.com/user-attachments/assets/13ad41ca-8f7c-40fe-b6d6-a47800bea3a9)
<img width="300" alt="Screenshot 2025-06-24 at 10 45 03" src="https://github.com/user-attachments/assets/37f62aea-798a-4ac1-a0e0-8fb144b5a9de" />

<img width="300" alt="Screenshot 2025-06-24 at 10 45 14" src="https://github.com/user-attachments/assets/2344ba13-f2fc-4d82-93f5-b56a7c7f0b9a" />

<img width="300" alt="Screenshot 2025-06-24 at 10 45 24" src="https://github.com/user-attachments/assets/efbb15f8-0d9a-4003-898c-f98c90401663" />

<img width="300" alt="Screenshot 2025-06-24 at 10 45 37" src="https://github.com/user-attachments/assets/adf26217-906d-4215-8dde-3fac6a967d90" />

<img width="300" alt="Screenshot 2025-06-24 at 10 45 29" src="https://github.com/user-attachments/assets/82905dee-8ffb-463a-838a-465f74471da1" />

<img width="300" alt="Screenshot 2025-06-24 at 10 45 43" src="https://github.com/user-attachments/assets/91835109-9fed-4aeb-9a12-e488bb864150" />

<img width="300" alt="Screenshot 2025-06-24 at 10 45 48" src="https://github.com/user-attachments/assets/f9e7f2f5-d6e3-497e-883b-e80f5c23d714" />

<img width="300" alt="Screenshot 2025-06-24 at 10 45 54" src="https://github.com/user-attachments/assets/0c95a212-c2de-47af-adf3-f43655610663" />

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
