# Study Planner App API

## Overview
This API allows users to manage their study plans, user authentication, and activity logs.

- **Version**: 1.0.0

## Endpoints

### 홈 화면 관련 엔드포인트

#### `/api/study-plans/home`
- **Method**: `HEAD`
- **Description**: Checks if the user is not logged in.

  - **Request Headers**: 없음
  
  - **Response Status Codes**:
    - `401 Unauthorized`: 사용자 비로그인 상태

#### `/api/study-plans/home/{user_id}`
- **Method**: `HEAD`
- **Description**: Checks if the user is logged in.

  - **Request Headers**:
    - `Authorization`: `Bearer <token>` (사용자의 인증 토큰)
  
  - **Response Status Codes**:
    - `200 OK`: 사용자 로그인 상태

### 로그인 관련 엔드포인트

#### `/api/study-plans/login`
- **Method**: `POST`
- **Description**: Authenticates a user and provides a session token.

  - **Request Body** (JSON):
    ```json
    {
      "email": "user@example.com",
      "password": "user_password"
    }
    ```

  - **Response Status Codes**:
    - `200 OK`: 로그인 성공
    - `401 Unauthorized`: 로그인 실패

  - **Response Body** (JSON):
    ```json
    {
      "token": "session_token",
      "user_id": "user_id"
    }
    ```

### 회원가입 관련 엔드포인트

#### `/api/study-plans/signup`
- **Method**: `POST`
- **Description**: Registers a new user.

  - **Request Body** (JSON):
    ```json
    {
      "email": "user@example.com",
      "password": "user_password",
      "name": "user_name",
      "mbti": "user_mbti"
    }
    ```

  - **Response Status Codes**:
    - `201 Created`: 회원가입 성공
    - `400 Bad Request`: 회원가입 실패 (잘못된 요청)

  - **Response Body** (JSON):

    - 성공 시:
    ```json
    {
      "user_id": "new_user_id"
    }
    ```
    - 실패 시 (예시):
    ```json
    {
      "error": "Email already exists"
    }
    ```
    ```json
    {
      "error": "Invalid password format"
    }
    ```
    ```json
    {
      "error": "Missing required fields"
    }
    ```

### 사용자별 계획 관리 엔드포인트

#### `/api/study-plans/{user_id}/manage`

- **Method**: `GET`
- **Description**: Retrieves all study plans for a specific user.

  - **Request Headers**:
    - `Authorization`: `Bearer <token>` (사용자의 인증 토큰)

  - **Response Status Codes**:
    - `200 OK`: 성공적으로 사용자 계획 조회
    - `401 Unauthorized`: 인증되지 않은 요청
   
  - **Response Body** (JSON):
    ```json
    [
      {
        "plan_id": "plan_id_1",
        "title": "Study Plan 1",
        "description": "Description of study plan 1"
      },
      {
        "plan_id": "plan_id_2",
        "title": "Study Plan 2",
        "description": "Description of study plan 2"
      }
    ]
    ```

- **Method**: `POST`
- **Description**: Creates a new study plan for a specific user.

  - **Request Headers**:
    - `Authorization`: `Bearer <token>` (사용자의 인증 토큰)
      
  - **Request Body** (JSON):
    ```json
    {
      "title": "New Study Plan",
      "description": "Description of the new study plan"
    }
    ```

  - **Response Status Codes**:
    - `201 Created`: 새로운 계획이 성공적으로 생성됨
    - `400 Bad Request`: 잘못된 요청 (예: 필수 필드 누락)
    - `401 Unauthorized`: 인증되지 않은 요청

  - **Response Body** (JSON):
    ```json
    {
      "plan_id": "new_plan_id"
    }
    ```

### 계획별 과목 관리 엔드포인트

#### `/api/study-plans/{user_id}/manage/{plan_id}/{class_id}`

- **Method**: `GET`
- **Description**: Retrieves a specific class within a study plan for a user.

  - **Request Headers**:
    - `Authorization`: `Bearer <token>` (사용자의 인증 토큰)

  - **Response Status Codes**:
    - `200 OK`: 성공적으로 과목 조회
    - `401 Unauthorized`: 인증되지 않은 요청
    - `404 Not Found`: 과목을 찾을 수 없음

  - **Response Body** (JSON):
    ```json
    {
      "class_id": "class_id_1",
      "class_name": "Mathematics",
      "description": "Description of the class"
    }
    ```

- **Method**: `POST`
- **Description**: Creates a new class within a study plan for a user.

  - **Request Headers**:
    - `Authorization`: `Bearer <token>` (사용자의 인증 토큰)
    
  - **Request Body** (JSON):
    ```json
    {
      "class_name": "New Class",
      "description": "Description of the new class"
    }
    ```

  - **Response Status Codes**:
    - `201 Created`: 새로운 과목이 성공적으로 생성됨
    - `400 Bad Request`: 잘못된 요청 (예: 필수 필드 누락)
    - `401 Unauthorized`: 인증되지 않은 요청

  - **Response Body** (JSON):
    ```json
    {
      "class_id": "new_class_id"
    }
    ```

- **Method**: `PUT`
- **Description**: Updates a specific class within a study plan for a user.

  - **Request Headers**:
    - `Authorization`: `Bearer <token>` (사용자의 인증 토큰)
    
  - **Request Body** (JSON):
    ```json
    {
      "class_name": "Updated Class",
      "description": "Updated description of the class"
    }
    ```

  - **Response Status Codes**:
    - `200 OK`: 과목이 성공적으로 업데이트됨
    - `400 Bad Request`: 잘못된 요청 (예: 필수 필드 누락)
    - `401 Unauthorized`: 인증되지 않은 요청
    - `404 Not Found`: 과목을 찾을 수 없음

  - **Response Body** (JSON):
    ```json
    {
      "class_id": "class_id_1"
    }
    ```

- **Method**: `DELETE`
- **Description**: Deletes a specific class within a study plan for a user.

  - **Request Headers**:
    - `Authorization`: `Bearer <token>` (사용자의 인증 토큰)

  - **Response Status Codes**:
    - `200 OK`: 과목이 성공적으로 삭제됨
    - `401 Unauthorized`: 인증되지 않은 요청
    - `404 Not Found`: 과목을 찾을 수 없음
