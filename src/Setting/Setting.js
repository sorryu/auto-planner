import React from "react";
import "./Setting.css";
import { Helmet } from "react-helmet";

function savePersonalInfo(){
    const userEmail = document.getElementById('user-email').value;
    const password = document.getElementById('password').value;
    const mbti = document.getElementById('mbti').value;

    // 서버나 로컬 스토리지에 저장하는 로직 추가 
    console.log('UserEmail: ${userEmail}, Password: ${password}, MBTI: ${mbti}');
    alert('개인정보가 저장되었습니다.');
}

function Setting(){
    return(
        <>
            <Helmet>
                <meta charSet="utf-8" />
                <title>Setting</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            </Helmet>
            <header className="SettingHead">
                <a className="backbutton" href="/main">&#8592;</a>
            </header>
            <div className="SettingTotal" id="personal-info">
                <h2 className="info">개인정보</h2>
                <label for="name">이름</label>
                <input type="email" id="name" placeholder="이름 입력"></input>

                <label for="user-email">E-mail</label>
                <input type="email" id="user-email" placeholder="E-mail 입력"></input>

                <label for="password">비밀번호</label>
                <input type="password" id="password" placeholder="비밀번호 입력"></input>

                <label for="mbti">MBTI</label>
                <input type="text" id="mbti" placeholder="MBTI 입력"></input>
                <div className="SaveButton">
                    <button onClick={savePersonalInfo}>저장</button>
                </div>
            </div>
            
        </>
    );
}

export default Setting;