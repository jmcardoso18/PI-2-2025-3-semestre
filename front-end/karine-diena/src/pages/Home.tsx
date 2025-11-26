import Navbar from "../componentes/Navbar";
import hero from "../assets/images/hero.jpg";
import card from "../assets/images/card.png";
import Footer from "../componentes/Footer";

const Home = () => {
    return (
        <div className="min-h-screen bg-black text-white overflow-hidden">
            <Navbar />

            {/* HERO */}
            <section
                id="home"
                className="relative flex min-h-screen items-center justify-center overflow-hidden"
            >
                {/* BG Parallax */}
                <div className="absolute inset-0 z-0">
                    <div
                        className="
                            h-full w-full 
                            bg-cover bg-center 
                            brightness-50 
                            scale-[1.15]
                            animate-[parallax_25s_linear_infinite]
                        "
                        style={{ backgroundImage: `url(${hero})` }}
                    />
                </div>

                {/* Overlay para garantir contraste */}
                <div className="absolute inset-0 bg-black/20 z-[1]" />

                {/* TEXTO + BOTÕES */}
                <div
                    className="
                        relative z-[2] 
                        max-w-3xl 
                        px-4 
                        text-center 
                        opacity-0 
                        animate-[fadeInUp_1.2s_ease_forwards]
                    "
                >
                    <h1 className="font-display text-3xl sm:text-4xl md:text-5xl mb-4 drop-shadow-2xl">
                        Transformando momentos
                        <br />
                        em lembranças inesquecíveis
                    </h1>

                    <p className="text-sm sm:text-base text-white/80 mb-8 max-w-xl mx-auto">
                        Assessoria e cerimonial personalizados para casamentos e eventos
                        sociais, com cuidado em cada detalhe.
                    </p>

                    {/* BOTÕES — VERSÃO FUNCIONAL + LUXUOSA */}
                    <div className="flex flex-col sm:flex-row gap-4 justify-center">
                        <a
                            href="#contact"
                            className="
                                rounded-full 
                                border border-white 
                                px-10 py-3 
                                text-sm font-semibold 
                                text-white
                                bg-white/10
                                backdrop-blur-md
                                shadow-lg shadow-white/10
                                hover:bg-white 
                                hover:text-black 
                                hover:shadow-2xl
                                hover:scale-[1.05]
                                active:scale-[0.98]
                                transition-all duration-300
                            "
                        >
                            Registre-se
                        </a>

                        <a
                            href="#services"
                            className="
                                rounded-full 
                                border border-white/80 
                                px-10 py-3 
                                text-sm font-semibold 
                                text-white 
                                bg-white/5
                                backdrop-blur-md
                                shadow-md shadow-white/10
                                hover:bg-white 
                                hover:text-black 
                                hover:shadow-2xl
                                hover:scale-[1.05]
                                active:scale-[0.98]
                                transition-all duration-300
                            "
                        >
                            Ver serviços
                        </a>
                    </div>
                </div>
            </section>

            {/* SOBRE */}
            <section
                id="about"
                className="bg-[#f9f5ea] text-black py-20 px-4"
            >
                <div className="mx-auto max-w-6xl grid gap-10 md:grid-cols-[1.6fr_1fr] items-center">
                    <div className="md:col-span-2 mb-6">
                        <h2 className="font-display text-3xl md:text-4xl tracking-[0.25em] uppercase text-center">
                            SOBRE
                        </h2>
                    </div>

                    {/* TEXTO */}
                    <div className="space-y-4 text-sm sm:text-base leading-relaxed text-neutral-800">
                        <p>
                            Fundada em 2013, a Karine Cerimonialista é uma empresa
                            especializada na organização e planejamento de eventos
                            sociais e corporativos. Sob a liderança da cerimonialista
                            Karine, pedagoga, o escritório se destaca pela atenção
                            aos detalhes e pela condução acolhedora de cada celebração.
                        </p>
                        <p>
                            Com uma equipe qualificada e comprometida, desenvolvemos
                            projetos sob medida para cada cliente, desde a concepção
                            do sonho até a execução impecável no grande dia. Ao longo
                            dos anos, foram dezenas de casamentos e eventos realizados
                            com excelência, sempre prezando pela tranquilidade dos
                            anfitriões e pela experiência dos convidados.
                        </p>
                        <p>
                            Acreditamos que cada evento precisa refletir a identidade,
                            a história e os desejos dos noivos ou anfitriões. Por isso,
                            cuidamos de cada etapa com carinho, criatividade e
                            responsabilidade, garantindo que tudo esteja alinhado ao
                            estilo e às expectativas de quem confia em nosso trabalho.
                        </p>
                        <p>
                            Nosso compromisso é transformar momentos especiais
                            em lembranças inesquecíveis.
                        </p>
                    </div>

                    {/* FOTO */}
                    <div className="flex justify-center">
                        <div className="w-64 h-80 md:w-72 md:h-96 overflow-hidden rounded-xl shadow-xl shadow-neutral-400/40 border border-neutral-200">
                            <img
                                src={hero}
                                alt="Karine Diena"
                                className="w-full h-full object-cover"
                            />
                        </div>
                    </div>
                </div>
            </section>

            {/* SERVIÇOS */}
            <section
                id="services"
                className="bg-[#f9f5ea] text-black py-20 px-4 relative"
            >
                <div className="grid gap-8 md:grid-cols-3">

                    {/* Básico */}
                    <div
                        className="
            rounded-2xl bg-white shadow-md 
            p-6 flex flex-col gap-4 
            transform hover:-translate-y-2 
            hover:shadow-2xl 
            transition-all duration-300
        "
                    >
                        <div className="h-36 rounded-xl overflow-hidden">
                            <img
                                src={card}
                                alt="Pacote Básico"
                                className="w-full h-full object-cover"
                            />
                        </div>
                        <h3 className="font-semibold text-lg">Pacote Básico</h3>
                        <p className="text-sm text-gray-600">
                            Para quem já contratou fornecedores e precisa de apoio no
                            checklist final e na coordenação do dia do evento.
                        </p>
                    </div>

                    {/* Completo */}
                    <div
                        className="
            rounded-2xl bg-white shadow-md 
            p-6 flex flex-col gap-4 
            transform hover:-translate-y-2 
            hover:shadow-2xl 
            transition-all duration-300
        "
                    >
                        <div className="h-36 rounded-xl overflow-hidden">
                            <img
                                src={card}
                                alt="Pacote Completo"
                                className="w-full h-full object-cover"
                            />
                        </div>
                        <h3 className="font-semibold text-lg">Pacote Completo</h3>
                        <p className="text-sm text-gray-600">
                            Acompanhamento desde o planejamento até o grande dia, com visitas
                            técnicas e suporte nas decisões principais.
                        </p>
                    </div>

                    {/* Premium */}
                    <div
                        className="
            rounded-2xl bg-white shadow-md 
            p-6 flex flex-col gap-4 
            transform hover:-translate-y-2 
            hover:shadow-2xl 
            transition-all duration-300
        "
                    >
                        <div className="h-36 rounded-xl overflow-hidden">
                            <img
                                src={card}
                                alt="Pacote Premium"
                                className="w-full h-full object-cover"
                            />
                        </div>
                        <h3 className="font-semibold text-lg">Pacote Premium</h3>
                        <p className="text-sm text-gray-600">
                            Experiência totalmente personalizada, com gestão financeira,
                            confirmação de presença e acompanhamento completo do evento.
                        </p>
                    </div>

                </div>
            </section>

            {/* CONTATO */}
            <section
                id="contact"
                className="bg-black text-white py-20 px-4 border-t border-white/10"
            >
                <div className="mx-auto max-w-3xl text-center">
                    <h2 className="font-display text-2xl sm:text-3xl mb-4">
                        Fale com a nossa equipe
                    </h2>

                    <p className="text-sm sm:text-base text-white/70 mb-10 max-w-lg mx-auto">
                        Envie seus dados que entraremos em contato para entender seu
                        evento e indicar o melhor pacote para você.
                    </p>

                    <form className="grid gap-5 text-left">
                        <div className="relative">
                            <label className="block text-sm mb-1">Nome completo</label>
                            <input
                                type="text"
                                className="
                                    w-full rounded-lg bg-white/5 border border-white/20 
                                    px-3 py-2 text-sm outline-none 
                                    focus:border-brand-500
                                    focus:bg-white/10 transition
                                "
                            />
                        </div>

                        <div className="grid gap-4 sm:grid-cols-2">
                            <div>
                                <label className="block text-sm mb-1">E-mail</label>
                                <input
                                    type="email"
                                    className="
                                        w-full rounded-lg bg-white/5 border border-white/20 
                                        px-3 py-2 text-sm outline-none 
                                        focus:border-brand-500 focus:bg-white/10
                                    "
                                />
                            </div>

                            <div>
                                <label className="block text-sm mb-1">Telefone</label>
                                <input
                                    type="tel"
                                    className="
                                        w-full rounded-lg bg-white/5 border border-white/20 
                                        px-3 py-2 text-sm outline-none 
                                        focus:border-brand-500 focus:bg-white/10
                                    "
                                />
                            </div>
                        </div>

                        <div>
                            <label className="block text-sm mb-1">
                                Tipo de evento / data prevista
                            </label>
                            <textarea
                                rows={3}
                                className="
                                    w-full rounded-lg bg-white/5 border border-white/20 
                                    px-3 py-2 text-sm outline-none 
                                    focus:border-brand-500 focus:bg-white/10 
                                    resize-none
                                "
                            />
                        </div>

                        <button
                            type="submit"
                            className="
                                mt-4 inline-flex justify-center rounded-full 
                                bg-brand-500 px-10 py-3 text-sm font-semibold text-black 
                                hover:bg-brand-600 hover:shadow-xl hover:scale-[1.03]
                                transition-all duration-300
                            "
                        >
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
