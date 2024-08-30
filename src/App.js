import React from "react";
import { BrowserRouter as Router, Route, Routes, Navigate} from "react-router-dom";
import Login from "./Login/Login";
import Main from "./Main/Main";
import Gaip from "./Gaip/Gaip";
import Setting from "./Setting/Setting";
import Todo from "./Main/todo";
import SelfAdd from "./Self_add/SelfAdd";
import AutoAdd from "./Auto_add/AutoAdd";


function App(){
  return(
    <Router>
        <Routes>
          <Route path="/" element={<Navigate to="/login" />}></Route>
          <Route path="/login" element={<Login />}></Route>
          <Route path="/main" element={<Main />}></Route>
          <Route path="/gaip" element={<Gaip />}></Route>
          <Route path="/setting" element={<Setting />}></Route>
          <Route path="/todo" element={<Todo />}></Route>
          <Route path="/selfadd" element={<SelfAdd />}></Route>
          <Route path="/autoadd" element={<AutoAdd />}></Route>
        </Routes>
    </Router>
  );
}

export default App;