import React from "react";
import "./Login.css";
import { Helmet } from "react-helmet";
import { useNavigate } from "react-router-dom";

function Login() {
    const Navigate = useNavigate();

    const handleLogin = (e) => {
        e.preventDefault();
        Navigate('/main');
    };

    const handleGaip = (i) => {
        i.preventDefault();
        Navigate('/gaip');
    };

    return (
        <>
            <Helmet>
                <title>Login</title>
                <meta charSet="utf-8"></meta>
            </Helmet>
            <div className="login">
                <p className="Logo">PlanA</p>
                <div className="login-form">
                    <form onSubmit={handleLogin}>
                        <input type="email" id="emil" name="email" 
                        className="text-field" placeholder="E-mail"></input>
                        <input type="password" id="password" name="password"
                        className="text-field" placeholder="비밀번호"></input>
                        <button type="submit" className="submit-btn">로그인</button>
                    </form>
                    <div className="links">
                        <a onClick={handleGaip}>회원가입</a><br/>
                        <a href="pw.js">비밀번호를 잊어버리셨나요?</a>
                    </div>
                </div>
            </div>
        </>
    );
}


export default Login;