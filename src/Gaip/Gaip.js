import React from "react";
import "./Gaip.css";
import { Helmet } from "react-helmet";
import { useNavigate } from "react-router-dom";

function Gaip() {
    const Navigate = useNavigate();

    return (
        <>
            <Helmet>
                <title>AutoPlanner: 회원가입</title>
                <meta charSet="utf-8"></meta>
            </Helmet>
            <header className="GaipHead">
                <a className="backbutton" href="/login">&#8592;</a>
            </header>
            <div className="Gaipbody">
                <h2 className="Gaiph2">회원가입</h2>
                <form className="join" action="first.html" method="post">
                    <div className="GaipName">
                        <label for="name">이름</label><br />
                        <input type="text" id="name" name="name" placeholder="홍길동" />
                    </div>
                    <div className="GaipEmail">
                        <label for="email">E-mail</label><br />
                        <input type="email" id="email" name="email" placeholder="example@email.com" />
                    </div>
                    <div class="PW">
                        <label for="password">비밀번호</label><br />
                        <input type="password" id="password" name="password" placeholder="password"
                            required minlength="5" />
                    </div>
                    <div className="PWCheck">
                        <label for="password">비밀번호 확인</label><br />
                        <input type="password" id="password" name="password" placeholder="password"
                            required minlength="5" />
                    </div>
                    <div className="MBTI">
                        <label for="mbti">MBTI 입력</label><br />
                        <input type="text" id="mbti" name="mbti" placeholder="예) ENFP"
                            required maxLength="4" />
                    </div>
                    <div className="GaiploginBT">
                        <button onClick={() => Navigate('/login')} className="GaipBtn">가입하기</button>
                    </div>
                </form>
            </div>
        </>
    );
}

export default Gaip;