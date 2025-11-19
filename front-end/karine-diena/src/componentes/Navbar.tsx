import { HashLink } from "react-router-hash-link";
import { Link } from "react-router-dom";

const Navbar = () => {
    return (
        <header className="fixed top-0 left-0 w-full z-20 bg-black/40 backdrop-blur border-b border-white/10">
            <div className="mx-auto flex max-w-6xl items-center justify-between px-4 py-3">

                {/* LOGO */}
                <Link
                    to="/"
                    className="font-display text-xl tracking-[0.25em] uppercase cursor-pointer hover:opacity-80 transition"
                >
                    Karine Diena
                </Link>

                {/* MENU */}
                <nav className="flex gap-6 text-sm">

                    <HashLink smooth to="/#home" className="hover:text-brand-200 transition">
                        Página Inicial
                    </HashLink>

                    <HashLink smooth to="/#services" className="hover:text-brand-200 transition">
                        Serviços
                    </HashLink>

                    <HashLink smooth to="/#contact" className="hover:text-brand-200 transition">
                        Contato
                    </HashLink>

                    <Link
                        to="/login"
                        className="border border-white/60 px-4 py-1 rounded-full text-sm hover:bg-white hover:text-black transition"
                    >
                        Login
                    </Link>

                </nav>
            </div>
        </header>
    );
};

export default Navbar;
