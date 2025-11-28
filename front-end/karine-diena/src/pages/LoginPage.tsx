import { useState } from "react";
import Navbar from "../componentes/Navbar";
import Footer from "../componentes/Footer";
import hero from "../assets/images/hero.jpg";

export default function LoginPage() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [erro, setErro] = useState("");

    const handleLogin = async (e: React.FormEvent) => {
        e.preventDefault();
        setErro("");

        try {
            const response = await fetch("http://127.0.0.1:8000/api/login-session/", {
                method: "POST",
                credentials: "include", 
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    username: username,
                    password: password,
                }),
            });

            const data = await response.json();

            if (response.ok) {
            
                localStorage.removeItem("token"); 

                window.location.href = "http://127.0.0.1:8000" + data.redirect;
            } else {
                setErro("Usuário ou senha inválidos.");
            }
        } catch (error) {
            setErro("Erro ao conectar com o servidor.");
            console.error(error);
        }
    };

    return (
        <div className="min-h-screen relative flex flex-col text-white">
            
            <div className="absolute inset-0 z-0">
                <div 
                    className="h-full w-full bg-cover bg-center brightness-50"
                    style={{ backgroundImage: `url(${hero})` }}
                />
            </div>
            <div className="absolute inset-0 bg-black/40 z-[1]" />

            <div className="relative z-10 flex flex-col min-h-screen">
                
                <Navbar />

                <main className="flex-grow flex items-center justify-center pt-24 pb-16 px-4">
                    <form 
                        onSubmit={handleLogin}
                        className="w-full max-w-sm space-y-6 bg-black/60 backdrop-blur-md p-8 rounded-xl border border-white/20 shadow-2xl"
                    >
                        <div className="text-center">
                            <h2 className="text-2xl font-display font-semibold mb-1">Bem-vindo</h2>
                            <p className="text-sm text-white/70">Acesse sua conta para continuar</p>
                        </div>

                        {erro && (
                            <div className="bg-red-500/20 border border-red-500 text-red-200 text-xs p-3 rounded text-center">
                                {erro}
                            </div>
                        )}

                        <div>
                            <label className="block text-xs uppercase tracking-wider text-white/80 mb-2">Usuário</label>
                            <input
                                type="text"
                                value={username}
                                onChange={(e) => setUsername(e.target.value)}
                                className="w-full rounded-lg border border-white/20 bg-white/5 px-4 py-3 text-sm focus:outline-none focus:border-brand-500 focus:bg-white/10 transition-all"
                                placeholder="Digite seu usuário"
                            />
                        </div>

                        <div>
                            <label className="block text-xs uppercase tracking-wider text-white/80 mb-2">Senha</label>
                            <input
                                type="password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                                className="w-full rounded-lg border border-white/20 bg-white/5 px-4 py-3 text-sm focus:outline-none focus:border-brand-500 focus:bg-white/10 transition-all"
                                placeholder="••••••••"
                            />
                        </div>

                        <button
                            type="submit"
                            className="w-full bg-white text-black py-3 rounded-full text-sm font-bold hover:bg-neutral-200 hover:scale-[1.02] transition-all duration-200 shadow-lg mt-4"
                        >
                            ENTRAR
                        </button>
                    </form>
                </main>

                <Footer />
            </div>
        </div>
    );
}