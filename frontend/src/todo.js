const todos = [
    { id: 'check1', text: 'FIRST' },
    { id: 'check2', text: 'SECOND' },
    { id: 'check3', text: 'THIRD' },
    { id: 'check4', text: 'FOURTH' }
    // 등등등.... 추가로!
];

const todoContainer = document.getElementById('todo-container');

todos.forEach(todo => {
    const todoDiv = document.createElement('div');
    todoDiv.className = 'Todo';

    const checkbox = document.createElement('input');
    checkbox.type = 'checkbox';
    checkbox.id = todo.id;

    const label = document.createElement('label');
    label.htmlFor = todo.id;

    const p = document.createElement('p');
    p.textContent = todo.text;

    todoDiv.appendChild(checkbox);
    todoDiv.appendChild(label);
    todoDiv.appendChild(p);

    todoContainer.appendChild(todoDiv);
});
