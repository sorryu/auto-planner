import React, { useState, useEffect } from 'react';
import './Category.css';

const Category = ({ onBackClick }) => {
    const [categories, setCategories] = useState(['First category']);
    const [isModalOpen, setIsModalOpen] = useState(false);
    const [newCategory, setNewCategory] = useState('');

    const toggleModal = () => {
        setIsModalOpen(prev => !prev);
    };

    const addCategory = () => {
        if (newCategory.trim() === '') {
            alert('카테고리 이름을 입력하세요.');
            return;
        }
        setCategories([...categories, newCategory]);
        setNewCategory('');
    };

    const updateCategory = (index, newCategoryValue) => {
        const updatedCategories = [...categories];
        updatedCategories[index] = newCategoryValue;
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
                    <details key={index}>
                        <summary>{category}</summary>
                        <p>Category 내용</p>
                    </details>
                ))}
            </div>

            {isModalOpen && (
                <div className="modal" onClick={toggleModal}>
                    <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                        <span className="close" onClick={toggleModal}>&times;</span>
                        <h2>Category 관리</h2>
                        <div id="category-container">
                            {categories.map((category, index) => (
                                <div key={index}>
                                    <input 
                                        value={category} 
                                        onChange={(e) => updateCategory(index, e.target.value)} 
                                    />
                                    <button onClick={() => deleteCategory(index)}>삭제</button>
                                </div>
                            ))}
                        </div>
                        <input 
                            type="text" 
                            value={newCategory} 
                            onChange={(e) => setNewCategory(e.target.value)} 
                            placeholder="새 카테고리 이름" 
                        />
                        <button onClick={addCategory}>카테고리 추가</button>
                    </div>
                </div>
            )}
        </div>
    );
};

export default Category;
