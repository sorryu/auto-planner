
# Study Planner App API

## Overview
This API allows users to manage their study plans. It provides endpoints for creating, retrieving, updating, and deleting study plans, as well as managing user activities.

- **Version**: 1.0.0

## Endpoints

### 홈 화면 및 로그인 관련 엔드포인트

#### Retrieve All Study Plans
- **URL**: `/api/study-plans`
- **Method**: `GET`
- **Description**: Retrieves a list of all study plans.

#### User Login
- **URL**: `/api/study-plans/login`
- **Method**: `POST`
- **Description**: Authenticates a user and provides a session token.

#### User Signup
- **URL**: `/api/study-plans/signup`
- **Method**: `POST`
- **Description**: Registers a new user.

### 사용자별 이벤트 처리

#### Retrieve User Study Plans
- **URL**: `/api/study-plans/{user_id}/plans`
- **Method**: `GET`
- **Description**: Retrieves all study plans for a specific user.

#### Create a New Study Plan for a User
- **URL**: `/api/study-plans/{user_id}/plans`
- **Method**: `POST`
- **Description**: Creates a new study plan for a specific user.

#### Update a Specific Study Plan for a User
- **URL**: `/api/study-plans/{user_id}/plans/{plan_id}`
- **Method**: `PUT`
- **Description**: Updates a specific study plan for a specific user.

#### Delete a Specific Study Plan for a User
- **URL**: `/api/study-plans/{user_id}/plans/{plan_id}`
- **Method**: `DELETE`
- **Description**: Deletes a specific study plan for a specific user.

### 사용자 활동 로그 관리

#### Retrieve User Activity Logs
- **URL**: `/api/study-plans/{user_id}/log`
- **Method**: `GET`
- **Description**: Retrieves the activity logs for a specific user.

#### Create a User Activity Log
- **URL**: `/api/study-plans/{user_id}/log`
- **Method**: `POST`
- **Description**: Creates a new activity log for a specific user.

#### Update a Specific User Activity Log
- **URL**: `/api/study-plans/{user_id}/log/{log_id}`
- **Method**: `PUT`
- **Description**: Updates a specific activity log for a specific user.

#### Delete a Specific User Activity Log
- **URL**: `/api/study-plans/{user_id}/log/{log_id}`
- **Method**: `DELETE`
- **Description**: Deletes a specific activity log for a specific user.
