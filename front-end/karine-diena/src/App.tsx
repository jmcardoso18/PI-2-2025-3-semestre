import { BrowserRouter, Route, Routes } from "react-router-dom";
import LoginPage from "./pages/LoginPage";
import Home from "./pages/Home";
import ColaboradorArea from "./pages/ColaboradorArea";
import ClienteArea from "./pages/ClienteArea";


const App: React.FC = () => {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<LoginPage />} />
        <Route path="/area-cliente" element={<ClienteArea />} />
        <Route path="/area-colaborador" element={<ColaboradorArea />} />
      </Routes>
    </BrowserRouter>
  );
};

export default App;
