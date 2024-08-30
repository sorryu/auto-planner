import React, { useEffect, useState } from 'react';
import './todo.css';
import Category from './Category';

const Todo = ({ selectedDay }) => {
  const [currentDate, setCurrentDate] = useState('');
  const [isCategoryView, setIsCategoryView] = useState(false);

  const toggleView = () => {
    setIsCategoryView(true); // 카테고리 보기로 전환
  };

  // 컴포넌트가 마운트되거나 selectedDay가 변경될 때 날짜 업데이트
  useEffect(() => {
    const date = selectedDay || new Date(); // selectedDay가 없으면 오늘 날짜를 기본값으로 사용
    const year = date.getFullYear();
    const month = date.getMonth() + 1; // 월은 0부터 시작하므로 1을 더함
    const day = date.getDate();
    setCurrentDate(`${year}년 ${month}월 ${day}일`);
  }, [selectedDay]);

  const todos = [
    { id: 'check1', text: 'FIRST' },
    { id: 'check2', text: 'SECOND' },
    { id: 'check3', text: 'THIRD' },
    { id: 'check4', text: 'FOURTH' }
    // 추가 항목을 이곳에 작성합니다.
  ];

  return (
    <>
      <div className='todolist'>
        {!isCategoryView && ( // 카테고리 보기가 아닐 때만 표시
          <header>
            <div id="current-date">{currentDate}</div>
            <button onClick={toggleView} className="category-button">카테고리</button>
          </header>
        )}

        {isCategoryView ? (
          <Category selectedDay={selectedDay} /> // selectedDay를 Category로 전달
        ) : (
          <div id="todo-container">
            {todos.map((todo) => (
              <div key={todo.id} className="Todo">
                <input type="checkbox" id={todo.id} />
                <label className='todoLabel' htmlFor={todo.id}></label>
                <p>{todo.text}</p>
              </div>
            ))}
          </div>
        )}
      </div>
    </>
  );
};

export default Todo;
