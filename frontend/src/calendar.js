document.addEventListener('DOMContentLoaded', function() {
    let selectedDate = null;
    let currentMonth = new Date().getMonth();
    let currentYear = new Date().getFullYear();
    let category = '';

    const daysContainer = document.getElementById('days-container');
    const calendarTitle = document.getElementById('calendar-title');
    const today = new Date();  // 오늘 날짜

    function renderCalendar(month, year) {
        daysContainer.innerHTML = '';

        const firstDay = new Date(year, month).getDay();
        const daysInMonth = 32 - new Date(year, month, 32).getDate();
        const monthNames = ["1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월", "12월"];

        calendarTitle.textContent = `${year}년 ${monthNames[month]}`;

        for (let i = 0; i < firstDay; i++) {
            const emptyDiv = document.createElement('div');
            emptyDiv.className = 'day empty';
            daysContainer.appendChild(emptyDiv);
        }

        for (let day = 1; day <= daysInMonth; day++) {
            const dayDiv = document.createElement('div');
            dayDiv.className = 'day';
            dayDiv.textContent = day;

            // 오늘 날짜인 경우에 배경색을 회색으로 고정
            if (day === today.getDate() && month === today.getMonth() && year === today.getFullYear()) {
                dayDiv.classList.add('active');
            }

            dayDiv.addEventListener('click', function() {
                document.querySelectorAll('.day').forEach(d => d.classList.remove('active'));
                this.classList.add('active');
            });

            daysContainer.appendChild(dayDiv);
        }
    }

    function handlePrevMonth() {
        currentMonth--;
        if (currentMonth < 0) {
            currentMonth = 11;
            currentYear--;
        }
        renderCalendar(currentMonth, currentYear);
    }

    function handleNextMonth() {
        currentMonth++;
        if (currentMonth > 11) {
            currentMonth = 0;
            currentYear++;
        }
        renderCalendar(currentMonth, currentYear);
    }

    calendarTitle.addEventListener('click', function() {
        document.querySelectorAll('.day').forEach(d => d.classList.remove('active'));

        const todayDivs = Array.from(document.querySelectorAll('.day')).filter(dayDiv => {
            return parseInt(dayDiv.textContent) === today.getDate() && currentMonth === today.getMonth()
            && currentYear === today.getFullYear();
        });

        if (todayDivs.length > 0){
            todayDivs[0].classList.add('active');
        }
    });

    document.querySelector('.pre-button').addEventListener('click', handlePrevMonth);
    document.querySelector('.next-button').addEventListener('click', handleNextMonth);

    renderCalendar(currentMonth, currentYear);
});
