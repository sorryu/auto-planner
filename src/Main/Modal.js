import React, { useEffect } from "react";
import "./Modal.css";

const Modal = ({ onOpenModal }) => {

    useEffect(() => {
        // 모달이 열리면 스크롤을 비활성화
        document.body.style.overflow = "hidden";
        return () => {
            // 모달이 닫히면 스크롤을 다시 활성화
            document.body.style.overflow = "auto";
        };
    }, []);

    return (
        <div className="modal" onClick={onOpenModal}>
            <div className="modal-content" onClick={(e) => e.stopPropagation()}>
                <span className="close" onClick={onOpenModal}>&#10006;</span>
                    <div className="select">
                        <a className="SelfAdd-Button" href="/selfadd">직접 추가하기</a>
                        <a className="AutoAdd-Button" href="/autoadd">자동으로 추가하기</a>
                    </div>
            </div>
        </div>
    );
}

export default Modal;
