import React, { useState } from "react";
import "./SelfAdd.css";
import { Helmet } from "react-helmet";

function SelfAdd() {
    const [task, setTask] = useState("");
    const [date, setDate] = useState("");
    const [category, setCategory] = useState("work");
    const [taskList, setTaskList] = useState([]);

    const addTask = () => {
        if (task === "" || date === "") {
            alert("모든 필드를 채워주세요.");
            return;
        }

        const newTask = `${category} - ${date}: ${task}`;
        setTaskList([...taskList, newTask]);

        // 입력 필드 초기화
        setTask("");
        setDate("");
    };

    return (
        <>
            <Helmet>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>self_add</title>
            </Helmet>
            <header className="SelfAddHead">
                <a className="backbutton" href="/main">&#8592;</a>
            </header>
            <div className="SelfAdd-total">
                <h1>직접 계획 추가</h1>
                <div className="form-group">
                    <input 
                        type="text" 
                        id="task" 
                        placeholder="할 일을 입력하세요" 
                        value={task}
                        onChange={(e) => setTask(e.target.value)}
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="category">카테고리:</label>
                    <select 
                        id="category" 
                        value={category} 
                        onChange={(e) => setCategory(e.target.value)}
                    >
                        <option value="work">일</option>
                        <option value="personal">개인</option>
                        <option value="other">기타</option>
                    </select>
                </div>
                <div className="form-group">
                    <label htmlFor="date">날짜:</label>
                    <input 
                        type="date" 
                        id="date" 
                        value={date}
                        onChange={(e) => setDate(e.target.value)}
                    />
                </div>
                <button onClick={addTask}>추가</button>
                <ul id="task-list">
                    {taskList.map((task, index) => (
                        <li key={index}>{task}</li>
                    ))}
                </ul>
            </div>
        </>
    );
}

export default SelfAdd;
