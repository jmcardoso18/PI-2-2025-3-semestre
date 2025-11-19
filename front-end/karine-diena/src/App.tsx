import { Routes, Route, Link } from 'react-router-dom'

import LoginPage from './pages/LoginPage'
import Home from './pages/Home'

export default function App() {
  return (
    <div className="min-h-screen bg-black text-white">
      <header className="flex items-center justify-between px-8 py-4">
        <span className="font-semibold tracking-[0.35em] text-sm">
          KARINE DIENA
        </span>

        <nav className="flex gap-6 text-sm">
          <a href="#servicos" className="hover:underline">
            Serviços
          </a>
          <a href="#contato" className="hover:underline">
            Contato
          </a>
          <Link to="/login" className="hover:underline">
            Login
          </Link>
        </nav>
      </header>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<LoginPage />} />
      </Routes>
    </div>
  )
}
