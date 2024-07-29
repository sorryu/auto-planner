# auto-planner

## 프로젝트 개요
학생들과 수험생들의 공부 계획을 효율적으로 관리하기 위한 **자동 계획 수립 앱**이다.

## 목차
1. [프로젝트 개요](#프로젝트-개요)
2. [디렉토리 구조](#디렉토리-구조)
3. [설치 및 설정](#설치-및-설정)
4. [사용법](#사용법)
5. [기여 가이드라인](#기여-가이드라인)
6. [문서화 및 추가자료](#문서화-및-추가자료)
7. [License](#license)

## 디렉토리 구조
```markdown
AUTO-PLANNER/
├── backend/
│   ├── app/        # Flask 애플리케이션 코드
│   ├── tests/      # 테스트 코드
│   ├── README.md
│   ├── requirements.txt    # 백엔드 의존성 목록
│
├── frontend/
│   ├── (node_modules/)     # Node.js 패키지, git에 포함되지 않음
│   ├── public/     # 정적 파일 (HTML, 이미지 등)
│   ├── src/        # React 애플리케이션 코드
│   ├── .gitignore
│   ├── package-lock.json   # Node.js 의존성 트리
│   ├── package.json        # 프론트엔드 프로젝트 메타데이터 및 의존성
│   ├── README.md           # 프론트엔드 설명서
│
├── docs/
│   ├── API.md  # API 문서
│
├── LICENSE     # 프로젝트 라이선스
├── README.md   # 프로젝트 전체 설명서
```

## 설치 및 설정

**전제 조건**\
이 가이드는 다음 소프트웨어가 시스템에 설치되어 있다고 가정합니다:
- [**Git**](https://git-scm.com) : 버전 관리 도구
- [**Python**](https://www.python.org) : 3.12+
- **pip3** : **Python** 패키지 관리 도구
- **CURL** : API 테스트 도구

### 1. 프로젝트 클론
먼저, [**GitHub**](https://github.com/)에서 프로젝트를 클론합니다.
```bash
git clone https://github.com/sorryu/auto-planner.git
cd auto-planner
```

### 2. 백엔드 설정
백엔드 디렉토리로 이동하여 가상 환경을 만들고 필요한 의존성을 설치합니다.
```bash
cd backend
python -m venv projectenv
source projectenv/bin/activate # Windows: projectenv\Scripts\activate
pip install -r requirements.txt
```

### 3. 데이터베이스 설정 (필요시)
백엔드 서버에서 필요한 데이터베이스를 설정합니다. 
```bash
python app/manage.py db init
python app/manage.py db migrate
python app/manage.py db upgrade
```

### 4. 백엔드 서버 실행
백엔드 서버를 실행합니다.
```bash
export FLASK_APP=app
export FLASK_ENV=development
flask run
```

### 5. 프론트엔드 설정
프론트엔드 디렉토리로 이동하여 필요한 의존성을 설치합니다.
```bash
cd ../frontend
npm install
```

### 6. 프론트엔드 서버 실행
프론트엔드 서버를 실행합니다.
```bash
npm start
```

### 주의사항
- 백엔드와 프론트엔드 서버가 동시에 실행 중이어야 합니다.
- 환경 변수를 설정할 때, 운영체제에 따라 명령어가 다를 수 있습니다.\
(Windows의 경우 `set` 명령어 사용)

## 사용법
이 섹션에서는 `auto-planner` 프로젝트를 사용하는 방법을 설명합니다.

### 1. 백엔드 서버 시작
1. 가상 환경 활성화:
    ```bash
    source projectenv/bin/activate # Windows: projectenv\Scripts\activate
    ```

2. 백엔드 서버 실행:
    ```bash
    export FLASK_APP=app
    export FLASK_ENV=development
    flask run
    ```

3. 브라우저에서 백엔드 API를 테스트합니다. 기본 URL은 `http://127.0.0.1:5000/`입니다.

### 2. 프론트엔드 서버 시작
1. 프론트엔드 디렉토리로 이동:
    ```bash
    cd ../frontend
    ```

2. 프론트엔드 서버 실행:
    ```bash
    npm start
    ```

3. 브라우저에서 프론트엔드 애플리케이션을 엽니다. 기본 URL은 `http://localhost:3000/`입니다.

### 3. 주요 기능 사용
어플리케이션의 주요 기능과 사용법을 설명합니다.

***추가 예정***

### 4. API 테스트
CURL으로 HTTP 요청을 보내고 API를 테스트합니다.

#### `GET`
```bash
curl -X GET http://localhost:5000/api/endpoint
```

#### `POST`
```bash
curl -X POST http://localhost:5000/api/endpoint -H "Content-Type: application/json" -d '{"key1":"value1", "key2":"value2"}'
```

#### `PUT`
```bash
curl -X PUT http://localhost:5000/api/endpoint/1 -H "Content-Type: application/json" -d '{"key1":"newvalue1", "key2":"newvalue2"}'
```

#### `DELETE`
```bash
curl -X DELETE http://localhost:5000/api/endpoint/1
```

#### CURL의 주요 옵션
- `-X`: HTTP 메서드를 지정합니다. (`GET`, `POST`, `PUT`, `DELETE` 등)
- `-H`: 요청 헤더를 설정합니다.
- `-d`: 요청 본문 데이터를 설정합니다.

## 기여 가이드라인
이 가이드라인은 팀 내에서 직접 협업하는 방식으로 설정되었습니다.
자세한 사항은 [GitHub Flow](https://docs.github.com/ko/get-started/using-github/github-flow)를 참고하세요.

### 1. 기여 절차
1. **Clone**: 팀원의 레포지토리를 로컬 환경에 클론합니다.
```bash
git clone https://github.com/username/auto-planner.git
cd auto-planner
```

2. **Branch 생성**: 새로운 기능이나 버그 수정을 위해 새로운 브랜치를 만듭니다.
```bash
git checkout -b feature/new-feature
```

3. **Commit**: 변경 사항을 커밋합니다. 커밋 메시지는 간결하고 명확하게 작성합니다.
```bash
git add .
git commit -m "Add a new feature"
```

4. **Push**: 변경 사항을 원격 레포지토리에 푸시합니다.
```bash
git push origin feature/new-feature
```

5. **Pull Request**: GitHub에서 Pull Request를 생성하여 변경 사항 병합을 요청합니다.

### 2. 코드 스타일 가이드

- **Python**: [PEP 8 스타일 가이드](https://pep8.org/)
- **JavaScript/React**: [Airbnb JavaScript 스타이 가이드](https://github.com/airbnb/javascript)
- **Linting**: `eslint`와 `flake8`을 사용하여 코드 스타일을 유지합니다.

### 3. 테스트

- 새로운 기능 추가 시 테스트 코드를 작성하고, 기존 테스트가 통과되었는지 확인합니다.
- `backend/tests` 디렉토리에 유닛 테스트를 작성합니다.
- `npm test` 명령어를 사용하여 프론트엔드 테스트를 실행합니다.

### 4. 문서화
- 새로운 기능이나 변경 사항에 대해 README나 관련 문서를 업데이트합니다.
- 코드 내 주석을 통해 중요한 로직을 설명합니다.

### 5. 코드 리뷰
- Pull Request를 생성한 후 다른 개발자들의 리뷰를 기다립니다.
- 리뷰어의 피드백을 반영하여 코드를 수정합니다.

## 문서화 및 추가자료

### 1. 프로젝트 문서화

- **README.md**: 프로젝트의 개요, 설치 방법, 사용법, 기여 가이드라인, 라이선스 정보를 포함합니다.
- **API 문서**: API 엔드포인트, 요청 및 응답 형식, 예제 등을 포함하여 docs 디렉토리에 저장합니다.

### 2. 추가 자료

- **테스트 전략**: 유닛 테스트, 통합 테스트 방법 및 도구 설명.
- **기여자 가이드**: 코드 기여 절차, 리뷰 프로세스, 이슈 트래킹 방법 등.

### 3. 샘플 데이터 및 스키마

- **sample.json**: 샘플 API 요청 및 응답 데이터를 포함합니다.
- **schema.json**: JSON 스키마 파일로, API 응답의 유효성을 검사합니다.

## License
[MIT License](LICENSE)
