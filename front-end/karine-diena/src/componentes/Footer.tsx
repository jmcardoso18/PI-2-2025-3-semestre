const Footer = () => {
    const currentYear = new Date().getFullYear();

    return (
        <footer className="bg-black text-white border-t border-white/10 pt-12 pb-6 px-4">
            <div className="mx-auto max-w-5xl space-y-8">
                {/* CTA no topo do footer */}
                <div
                    className="
                        rounded-2xl 
                        border border-white/10 
                        bg-gradient-to-r from-white/5 via-white/0 to-white/5
                        px-6 py-7 
                        text-center 
                        shadow-[0_0_40px_rgba(0,0,0,0.6)]
                    "
                >
                    <p className="text-[11px] tracking-[0.35em] uppercase text-white/60 mb-3">
                        Pronta para o grande dia?
                    </p>
                    <h3 className="font-display text-xl sm:text-2xl mb-4">
                        Vamos transformar o seu evento em uma lembrança inesquecível.
                    </h3>

                    <a
                        href="https://wa.me/55XXXXXXXXXXX" // TROCAR
                        target="_blank"
                        rel="noreferrer"
                        className="
                            inline-flex items-center justify-center
                            rounded-full 
                            px-8 py-2.5 
                            text-sm font-semibold 
                            bg-[#d4af37] text-black
                            shadow-lg shadow-[#d4af37]/30
                            hover:bg-[#f3d27a]
                            hover:shadow-xl
                            hover:-translate-y-[1px]
                            active:translate-y-[0px]
                            transition-all duration-300
                        "
                    >
                        Falar sobre meu evento
                    </a>
                </div>

                {/* Ornamentação com linhas finas */}
                <div className="flex items-center justify-center gap-3">
                    <span className="h-px w-10 sm:w-20 bg-gradient-to-r from-transparent via-white/40 to-transparent" />
                    <span className="text-[11px] tracking-[0.35em] uppercase text-white/50">
                        Karine Diena
                    </span>
                    <span className="h-px w-10 sm:w-20 bg-gradient-to-r from-transparent via-white/40 to-transparent" />
                </div>

                {/* Conteúdo principal do footer */}
                <div className="flex flex-col sm:flex-row items-center justify-between gap-6 text-sm">
                    {/* Texto / direitos */}
                    <div className="text-center sm:text-left text-white/60">
                        <p>
                            © {currentYear} Karine Diena • Assessoria e Cerimonial
                            <br />
                            Todos os direitos reservados.
                        </p>
                        <p className="mt-2 text-[11px] text-white/40">
                            Desenvolvido por{" "}
                            <a
                                href="#"
                                className="uppercase tracking-[0.25em] hover:text-[#d4af37] transition-colors"
                            >
                                Morgan Devs
                            </a>
                        </p>
                    </div>

                    {/* Redes sociais */}
                    {/* Redes sociais */}
                    <div className="flex flex-wrap items-center justify-center gap-4 text-sm">

                        {/* E-mail */}
                        <a
                            href="mailto:seuemail@exemplo.com"
                            className="
                                    flex items-center gap-2 
                                    text-white/70 hover:text-[#d4af37] 
                                    transition
                                "
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                fill="currentColor"
                                viewBox="0 0 24 24"
                                className="w-5 h-5"
                            >
                                <path d="M4 4h16a2 2 0 0 1 2 2v12a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a2 2 0 0 1 2-2Zm0 2v.51l8 5.49 8-5.49V6H4Zm16 12V9l-8 5.5L4 9v9h16Z" />
                            </svg>
                            <span></span>
                        </a>

                        {/* WhatsApp */}
                        <a
                            href="https://wa.me/55XXXXXXXXXXX"
                            target="_blank"
                            rel="noreferrer"
                            className="
                                    flex items-center gap-2 
                                    text-white/70 hover:text-[#d4af37] 
                                    transition
                                "
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                viewBox="0 0 24 24"
                                fill="currentColor"
                                className="w-5 h-5"
                            >
                                <path d="M12 2a10 10 0 0 0-8.94 14.32L2 22l5.82-1.94A10 10 0 1 0 12 2Zm0 18a8 8 0 0 1-4.14-1.15l-.3-.18-3.45 1.15 1.13-3.36-.2-.33A8 8 0 1 1 12 20Zm4.24-5.24c-.24-.12-1.44-.71-1.67-.79s-.39-.12-.55.12-.63.79-.77.95-.28.18-.52.06a6.51 6.51 0 0 1-3.22-2.82c-.24-.42.24-.39.69-1.29a.45.45 0 0 0 0-.43c-.06-.12-.55-1.33-.76-1.82s-.4-.42-.55-.42-.3 0-.46 0a.89.89 0 0 0-.64.3 2.72 2.72 0 0 0-.88 2.02A4.74 4.74 0 0 0 9 14.25a10.94 10.94 0 0 0 5.92 3.26 2 2 0 0 0 1.3-.08 2.29 2.29 0 0 0 1-1.34c.12-.24.12-.43.06-.55s-.21-.15-.39-.24Z" />
                            </svg>
                            <span></span>
                        </a>

                        {/* Instagram */}
                        <a
                            href="https://instagram.com"
                            target="_blank"
                            rel="noreferrer"
                            className="
                                    flex items-center gap-2 
                                    text-white/70 hover:text-[#d4af37] 
                                    transition
                                "
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                fill="currentColor"
                                viewBox="0 0 24 24"
                                className="w-5 h-5"
                            >
                                <path d="M7 2C4.243 2 2 4.243 2 7v10c0 2.757 2.243 5 5 5h10c2.757 0 5-2.243 5-5V7c0-2.757-2.243-5-5-5H7Zm10 2a3 3 0 0 1 3 3v10a3 3 0 0 1-3 3H7a3 3 0 0 1-3-3V7a3 3 0 0 1 3-3h10Zm-5 3a5 5 0 1 0 5 5 5.006 5.006 0 0 0-5-5Zm0 2a3 3 0 1 1-3 3 3.009 3.009 0 0 1 3-3Zm4.5-.75a1.25 1.25 0 1 0-1.25-1.25A1.252 1.252 0 0 0 16.5 8.25Z" />
                            </svg>
                            <span></span>
                        </a>

                        {/* Facebook */}
                        <a
                            href="https://facebook.com"
                            target="_blank"
                            rel="noreferrer"
                            className="
                                    flex items-center gap-2 
                                    text-white/70 hover:text-[#d4af37] 
                                    transition
                                "
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                fill="currentColor"
                                viewBox="0 0 24 24"
                                className="w-5 h-5"
                            >
                                <path d="M22 12a10 10 0 1 0-11.5 9.87v-7H8v-3h2.5V9.5A3.5 3.5 0 0 1 14.3 6h2.2v3h-2.2c-.43 0-1.3.21-1.3 1.1V12H16l-.5 3h-2.2v7A10 10 0 0 0 22 12Z" />
                            </svg>
                            <span></span>
                        </a>

                        {/* TikTok */}
                        <a
                            href="https://tiktok.com"
                            target="_blank"
                            rel="noreferrer"
                            className="
                                flex items-center gap-2 
                                text-white/70 hover:text-[#d4af37] 
                                transition
                            "
                        >
                            <svg
                                xmlns="http://www.w3.org/2000/svg"
                                fill="currentColor"
                                viewBox="0 0 24 24"
                                className="w-5 h-5"
                            >
                                <path d="M21 8.5a5.49 5.49 0 0 1-3.2-1V14a7 7 0 1 1-7-7 7.2 7.2 0 0 1 .9 0V9.9A4.2 4.2 0 1 0 14.2 14V2h3a3 3 0 0 0 3 3Z" />
                            </svg>
                            <span></span>
                        </a>

                    </div>

                </div>
            </div>
        </footer>
    );
};

export default Footer;
