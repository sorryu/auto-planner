import React, { useState } from 'react';
import { Helmet } from 'react-helmet';
import './Main.css';
import Calendar from './Calendar';
import Todo from './todo';
import settingpic from './settings.png';
import Modal from './Modal';

const Main = () => {
    const [selectedDay, setSelectedDay] = useState(new Date());
    const [isModalOpen, setIsModalOpen] = useState(false);

    const toggleModal = () => {
        setIsModalOpen(prev => !prev);
    };

    // `onDayClick` 함수 정의: 날짜가 클릭될 때 `selectedDay` 상태를 업데이트함
    const handleDayClick = (day) => {
        setSelectedDay(day);
    };

    return (
        <>
            <Helmet>
                <meta charSet="utf-8" />
                <title>Main: PlanA</title>
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
            </Helmet>

            <div className="Maindisplay">
                <header className="head">
                    <h1 className="MainLogo">
                        <a id="MainLogo" href="/main">PlanA</a>
                    </h1>
                    <div className="auto-mypage">
                        <button className="add-button" onClick={toggleModal}>계획 추가하기</button>
                        {isModalOpen && <Modal onOpenModal={toggleModal} />}
                        <a href="/setting">
                            <img className="settingpic" src={settingpic} alt="설정" />
                        </a>
                    </div>
                </header>
            </div>

            <section className="home">
                <div className="container">
                    <div className="space" />
                    <Calendar selectedDay={selectedDay} onDayClick={handleDayClick} />
                    <div className="space" />
                    <Todo selectedDay={selectedDay} />
                    <div className="space" />
                </div>
            </section>

        </>
    );
}

export default Main;
