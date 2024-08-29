import React from "react";
import { Helmet } from "react-helmet";
import "./AutoAdd.css";

function AutoAdd() {
    return (
        <>
            <Helmet>
                <meta charSet="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>auto_add</title>
            </Helmet>
            <header className="SettingHead">
                <a className="backbutton" href="/main">&#8592;</a>
            </header>
            <div className="AutoAdd-total">
                <h1>자동 계획 추가</h1>
                <div class="form-group">
                    <label for="category">카테고리:</label>
                    <select id="category">
                        <option value="work">일</option>
                        <option value="personal">개인</option>
                        <option value="other">기타</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="estimated-time">예상 소요 시간:</label>
                    <div class="time-inputs">
                        <input type="number" id="estimated-time" placeholder="시간" min="0"></input>
                        <p>시간</p>
                        <input type="number" id="estimated-minutes" placeholder="분" min="0" max="59"></input>
                        <p>분</p>
                    </div>
                </div>
                <div class="form-group">
                    <label for="start-date">시작일:</label>
                    <input type="date" id="start-date" />
                </div>
                <div class="form-group">
                    <label for="end-date">종료일:</label>
                    <input type="date" id="end-date" />
                </div>
                <button id="add-plan">완료</button>
            </div>
        </>
    );
}

export default AutoAdd;