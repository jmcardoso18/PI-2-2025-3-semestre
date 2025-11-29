import { useState, useEffect } from "react";
import Navbar from "../componentes/Navbar";
import Footer from "../componentes/Footer";
import hero from "../assets/images/hero.jpg";
import cardImg from "../assets/images/card.png"; // Renomeei para evitar conflito

// Interface para o Serviço que vem do Django
interface Servico {
    id: number;
    titulo: string;
    descricao: string;
    preco: string | number; // Pode vir como string decimal do Django
}

const Home = () => {
    // Estado para guardar os serviços da API
    const [servicos, setServicos] = useState<Servico[]>([]);
    const [loading, setLoading] = useState(true);

    // --- 1. BUSCAR SERVIÇOS DO DJANGO ---
    useEffect(() => {
        // Use o IP numérico para evitar problemas de CORS/Cookie se estiver logado
        fetch('http://127.0.0.1:8000/api/servicos/')
            .then(res => res.json())
            .then(data => {
                setServicos(data);
                setLoading(false);
            })
            .catch(err => {
                console.error("Erro ao buscar serviços:", err);
                setLoading(false);
            });
    }, []);

    // --- 2. LÓGICA DE ENVIO DO FORMULÁRIO (Exemplo) ---
    const handleContactSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        alert("Obrigado! Em breve implementaremos o envio real para o Django.");
        // Futuramente você pode criar uma view no Django para receber isso
    };

    return (
        <div className="min-h-screen bg-black text-white overflow-hidden">
            <Navbar />

            {/* HERO */}
            <section id="home" className="relative flex min-h-screen items-center justify-center overflow-hidden">
                <div className="absolute inset-0 z-0">
                    <div className="h-full w-full bg-cover bg-center brightness-50 scale-[1.15] animate-[parallax_25s_linear_infinite]"
                        style={{ backgroundImage: `url(${hero})` }} />
                </div>
                <div className="absolute inset-0 bg-black/20 z-[1]" />

                <div className="relative z-[2] max-w-3xl px-4 text-center opacity-0 animate-[fadeInUp_1.2s_ease_forwards]">
                    <h1 className="font-display text-3xl sm:text-4xl md:text-5xl mb-4 drop-shadow-2xl">
                        Transformando momentos <br /> em lembranças inesquecíveis
                    </h1>
                    <p className="text-sm sm:text-base text-white/80 mb-8 max-w-xl mx-auto">
                        Assessoria e cerimonial personalizados para casamentos e eventos sociais, com cuidado em cada detalhe.
                    </p>

                    <div className="flex flex-col sm:flex-row gap-4 justify-center">
                        <a href="#contact" className="rounded-full border border-white px-10 py-3 text-sm font-semibold text-white bg-white/10 backdrop-blur-md shadow-lg shadow-white/10 hover:bg-white hover:text-black hover:shadow-2xl hover:scale-[1.05] active:scale-[0.98] transition-all duration-300">
                            Registre-se
                        </a>
                        <a href="#services" className="rounded-full border border-white/80 px-10 py-3 text-sm font-semibold text-white bg-white/5 backdrop-blur-md shadow-md shadow-white/10 hover:bg-white hover:text-black hover:shadow-2xl hover:scale-[1.05] active:scale-[0.98] transition-all duration-300">
                            Ver serviços
                        </a>
                    </div>
                </div>
            </section>

            {/* SOBRE (Mantido estático pois é texto fixo) */}
            <section id="about" className="bg-[#f9f5ea] text-black py-20 px-4">
                <div className="mx-auto max-w-6xl grid gap-10 md:grid-cols-[1.6fr_1fr] items-center">
                    <div className="md:col-span-2 mb-6">
                        <h2 className="font-display text-3xl md:text-4xl tracking-[0.25em] uppercase text-center">SOBRE</h2>
                    </div>
                    <div className="space-y-4 text-sm sm:text-base leading-relaxed text-neutral-800">
                        <p>Fundada em 2013, a Karine Cerimonialista é uma empresa especializada na organização e planejamento de eventos sociais e corporativos.</p>
                        <p>Com uma equipe qualificada e comprometida, desenvolvemos projetos sob medida para cada cliente, desde a concepção do sonho até a execução impecável.</p>
                        <p>Nosso compromisso é transformar momentos especiais em lembranças inesquecíveis.</p>
                    </div>
                    <div className="flex justify-center">
                        <div className="w-64 h-80 md:w-72 md:h-96 overflow-hidden rounded-xl shadow-xl shadow-neutral-400/40 border border-neutral-200">
                            <img src={hero} alt="Karine Diena" className="w-full h-full object-cover" />
                        </div>
                    </div>
                </div>
            </section>

            {/* SERVIÇOS DINÂMICOS (Conectados ao Django) */}
            <section id="services" className="bg-[#f9f5ea] text-black py-20 px-4 relative">
                <div className="max-w-6xl mx-auto"> 
                    <h2 className="font-display text-3xl md:text-4xl tracking-[0.25em] uppercase text-center mb-12">SERVIÇOS</h2>
                    
                    <div className="grid gap-8 md:grid-cols-3">
                        {loading && <p className="col-span-3 text-center text-gray-500">Carregando serviços...</p>}
                        
                        {!loading && servicos.length === 0 && (
                            // Fallback caso o banco esteja vazio
                            <p className="col-span-3 text-center text-gray-500">Nenhum serviço cadastrado no momento.</p>
                        )}

                        {servicos.map((servico) => (
                            <div key={servico.id} className="rounded-2xl bg-white shadow-md p-6 flex flex-col gap-4 transform hover:-translate-y-2 hover:shadow-2xl transition-all duration-300">
                                <div className="h-36 rounded-xl overflow-hidden">
                                    {/* Imagem estática por enquanto, pode ser dinâmica no futuro */}
                                    <img src={cardImg} alt={servico.titulo} className="w-full h-full object-cover" />
                                </div>
                                <h3 className="font-semibold text-lg">{servico.titulo}</h3>
                                <p className="text-sm text-gray-600 line-clamp-3">
                                    {servico.descricao}
                                </p>
                                {servico.preco && (
                                    <p className="mt-auto font-bold text-neutral-900">
                                        R$ {servico.preco}
                                    </p>
                                )}
                            </div>
                        ))}
                    </div>
                </div>
            </section>

            {/* CONTATO */}
            <section id="contact" className="bg-black text-white py-20 px-4 border-t border-white/10">
                <div className="mx-auto max-w-3xl text-center">
                    <h2 className="font-display text-2xl sm:text-3xl mb-4">Fale com a nossa equipe</h2>
                    <p className="text-sm sm:text-base text-white/70 mb-10 max-w-lg mx-auto">
                        Envie seus dados que entraremos em contato para entender seu evento.
                    </p>

                    <form onSubmit={handleContactSubmit} className="grid gap-5 text-left">
                        <div className="relative">
                            <label className="block text-sm mb-1">Nome completo</label>
                            <input type="text" required className="w-full rounded-lg bg-white/5 border border-white/20 px-3 py-2 text-sm outline-none focus:border-brand-500 focus:bg-white/10 transition" />
                        </div>

                        <div className="grid gap-4 sm:grid-cols-2">
                            <div>
                                <label className="block text-sm mb-1">E-mail</label>
                                <input type="email" required className="w-full rounded-lg bg-white/5 border border-white/20 px-3 py-2 text-sm outline-none focus:border-brand-500 focus:bg-white/10" />
                            </div>
                            <div>
                                <label className="block text-sm mb-1">Telefone</label>
                                <input type="tel" required className="w-full rounded-lg bg-white/5 border border-white/20 px-3 py-2 text-sm outline-none focus:border-brand-500 focus:bg-white/10" />
                            </div>
                        </div>

                        <div>
                            <label className="block text-sm mb-1">Mensagem / Data prevista</label>
                            <textarea rows={3} className="w-full rounded-lg bg-white/5 border border-white/20 px-3 py-2 text-sm outline-none focus:border-brand-500 focus:bg-white/10 resize-none" />
                        </div>

                        <button type="submit" className="mt-4 inline-flex justify-center rounded-full bg-white px-10 py-3 text-sm font-semibold text-black hover:bg-neutral-200 hover:shadow-xl hover:scale-[1.03] transition-all duration-300">
                            Enviar mensagem
                        </button>
                    </form>
                </div>
            </section>

            <Footer />
        </div>
    );
};

export default Home;