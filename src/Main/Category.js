import React, { useState, useEffect } from 'react';
import './Category.css';

const Category = ({ onBackClick }) => {
    const [categories, setCategories] = useState([
        { name: '과목', startDate: '2024-08-08', endDate: '2024-08-30' }
    ]);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [newCategory, setNewCategory] = useState({ name: '', startDate: '', endDate: '' });

    const toggleModal = () => {
        setIsModalOpen(prev => !prev);
    };

    const addCategory = () => {
        if (newCategory.name.trim() === '') {
            alert('카테고리 이름을 입력하세요.');
            return;
        }
        setCategories([...categories, newCategory]);
        setNewCategory({ name: '', startDate: '', endDate: '' });
        setIsModalOpen(false); // 카테고리 추가 후 모달 닫기
    };

    const updateCategory = (index, key, value) => {
        const updatedCategories = [...categories];
        updatedCategories[index][key] = value;
        setCategories(updatedCategories);
    };

    const deleteCategory = (index) => {
        const updatedCategories = categories.filter((_, i) => i !== index);
        setCategories(updatedCategories);
    };

    const handleModalClose = (e) => {
        if (e.key === 'Escape') {
            setIsModalOpen(false);
        }
    };

    useEffect(() => {
        if (isModalOpen) {
            window.addEventListener('keydown', handleModalClose);
        } else {
            window.removeEventListener('keydown', handleModalClose);
        }

        return () => {
            window.removeEventListener('keydown', handleModalClose);
        };
    }, [isModalOpen]);

    return (
        <div>
            <header className='category-header'>
                <a className="back-button" href="/main">&#8592;</a>
                <button className="category-button" onClick={toggleModal}>Category 수정</button>
            </header>
            <div>
                {categories.map((category, index) => (
                    <details key={index} className="category-item">
                        <summary className="category-name">
                            {category.name}
                            <br/>
                            {category.startDate.replace(/-/g, '.')} ~ {category.endDate.replace(/-/g, '.')}
                        </summary>
                        <p></p>
                        <li> To Do List</li>
                    </details>
                ))}
            </div>

            {isModalOpen && (
                <div className="category-modal" onClick={toggleModal}>
                    <div className="category-modal-content" onClick={(e) => e.stopPropagation()}>
                        <span className="close" onClick={toggleModal}>&times;</span>
                        <h2>Category 관리</h2>
                        <div id="category-container">
                            {categories.map((category, index) => (
                                <div key={index} className="category-item">
                                    <input
                                        className="category-name"
                                        value={category.name}
                                        onChange={(e) => updateCategory(index, 'name', e.target.value)}
                                    />
                                    <div>
                                        <span>시작일: {category.startDate.replace(/-/g, '.')}</span><br />
                                        <span>마감일: {category.endDate.replace(/-/g, '.')}</span>
                                    </div>
                                    <button
                                        className="category-delete"
                                        onClick={() => deleteCategory(index)}
                                    >
                                        삭제
                                    </button>
                                </div>
                            ))}
                        </div>
                        <input
                            className='added-category-name'
                            type="text"
                            value={newCategory.name}
                            onChange={(e) => setNewCategory({ ...newCategory, name: e.target.value })}
                            placeholder="새 카테고리 이름"
                        /><br/>
                        <label>시작일:</label>
                        <input
                            className='add-start'
                            type="date"
                            value={newCategory.startDate}
                            onChange={(e) => setNewCategory({ ...newCategory, startDate: e.target.value })}
                        />
                        <label>마감일:</label>
                        <input
                            className='add-finish'
                            type="date"
                            value={newCategory.endDate}
                            onChange={(e) => setNewCategory({ ...newCategory, endDate: e.target.value })}
                        />
                        <button className='add-category' onClick={addCategory}>카테고리 추가</button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default Category;
