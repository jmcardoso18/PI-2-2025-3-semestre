import { useState, useEffect } from "react";
import Navbar from "../componentes/Navbar";
import Footer from "../componentes/Footer";
import hero from "../assets/images/hero.jpg";
import { useLocation } from "react-router-dom";

export default function LoginPage() {
    const [erro, setErro] = useState("");
    const location = useLocation();

    // Captura erro se o Django redirecionar de volta (ex: ?error=true)
    useEffect(() => {
        const params = new URLSearchParams(location.search);
        if (params.get("error") === "true") {
            setErro("Usuário ou senha inválidos.");
        }
    }, [location]);

    return (
        <div className="min-h-screen relative flex flex-col text-white">
            <div className="absolute inset-0 z-0">
                <div className="h-full w-full bg-cover bg-center brightness-50" style={{ backgroundImage: `url(${hero})` }} />
            </div>
            <div className="absolute inset-0 bg-black/40 z-[1]" />

            <div className="relative z-10 flex flex-col min-h-screen">
                <Navbar />
                <main className="flex-grow flex items-center justify-center pt-24 pb-16 px-4">
                    
                    {/* O SEGREDO: Action aponta direto para o Django na porta 8000 */}
                    <form 
                        action="http://127.0.0.1:8000/api/login-session/" 
                        method="POST"
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
                            <input type="text" name="username" required className="w-full rounded-lg border border-white/20 bg-white/5 px-4 py-3 text-sm focus:outline-none focus:border-brand-500 focus:bg-white/10" placeholder="Digite seu usuário" />
                        </div>

                        <div>
                            <label className="block text-xs uppercase tracking-wider text-white/80 mb-2">Senha</label>
                            <input type="password" name="password" required className="w-full rounded-lg border border-white/20 bg-white/5 px-4 py-3 text-sm focus:outline-none focus:border-brand-500 focus:bg-white/10" placeholder="••••••••" />
                        </div>

                        <button type="submit" className="w-full bg-white text-black py-3 rounded-full text-sm font-bold hover:bg-neutral-200 transition-all mt-4">
                            ENTRAR
                        </button>
                    </form>
                </main>
                <Footer />
            </div>
        </div>
    );
}