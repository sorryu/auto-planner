import React, { useState } from 'react';
import './Calendar.css';

const Calendar = () => {
  const today = new Date();
  const [currentMonth, setCurrentMonth] = useState(today.getMonth());
  const [currentYear, setCurrentYear] = useState(today.getFullYear());
  const [selectedDay, setSelectedDay] = useState(null);

  const daysOfWeek = ['일', '월', '화', '수', '목', '금', '토'];
  const monthNames = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"];

  const getDaysInMonth = (month, year) => 32 - new Date(year, month, 32).getDate();

  const handlePrevMonth = () => {
    setCurrentMonth(prev => (prev === 0 ? 11 : prev - 1));
    setCurrentYear(prev => (currentMonth === 0 ? prev - 1 : prev));
    setSelectedDay(null); // 새로운 월로 이동 시 선택된 날짜 초기화
  };

  const handleNextMonth = () => {
    setCurrentMonth(prev => (prev === 11 ? 0 : prev + 1));
    setCurrentYear(prev => (currentMonth === 11 ? prev + 1 : prev));
    setSelectedDay(null); // 새로운 월로 이동 시 선택된 날짜 초기화
  };

  const handleDayClick = (day) => {
    setSelectedDay({ day, month: currentMonth, year: currentYear });
  };

  const renderCalendarDays = () => {
    const firstDay = new Date(currentYear, currentMonth).getDay();
    const daysInMonth = getDaysInMonth(currentMonth, currentYear);
    const days = [];

    for (let i = 0; i < firstDay; i++) {
      days.push(<div key={`empty-${i}`} className="day empty"></div>);
    }

    for (let day = 1; day <= daysInMonth; day++) {
      const isToday = day === today.getDate() && currentMonth === today.getMonth() && currentYear === today.getFullYear();
      const isSelected = selectedDay && day === selectedDay.day && currentMonth === selectedDay.month && currentYear === selectedDay.year;

      days.push(
        <div
          key={day}
          className={`day ${isSelected ? 'selected' : isToday ? 'today' : ''}`}
          onClick={() => handleDayClick(day)}
        >
          {day}
        </div>
      );
    }

    return days;
  };

  const handleTitleClick = () => {
    setCurrentMonth(today.getMonth());
    setCurrentYear(today.getFullYear());
    setSelectedDay({
      day: today.getDate(),
      month: today.getMonth(),
      year: today.getFullYear()
    });
  };

  return (
    <div className="calendar">
      <div className="Calendar-header">
        <button className="pre-button" onClick={handlePrevMonth}>&#10094;</button>
        <h1 id="calendar-title" onClick={handleTitleClick}>
          {`${currentYear}년 ${monthNames[currentMonth]}`}
        </h1>
        <button className="next-button" onClick={handleNextMonth}>&#10095;</button>
      </div>
      <div className="days-of-week">
        {daysOfWeek.map((day, index) => (
          <div key={index} className="day-of-week">{day}</div>
        ))}
      </div>
      <div className="days" id="days-container">
        {renderCalendarDays()}
      </div>
    </div>
  );
};

export default Calendar;
