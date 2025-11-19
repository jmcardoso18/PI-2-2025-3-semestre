import Navbar from "../componentes/Navbar";
import Footer from "../componentes/Footer";

export default function LoginPage() {
    return (
        <div className="min-h-screen bg-neutral-950 text-white">
            {/* NAVBAR FIXO NO TOPO */}
            <Navbar />

            {/* MAIN  */}
            <main className="min-h-screen flex items-center justify-center pt-24 pb-16">
                <form className="w-full max-w-sm space-y-4 bg-black/40 p-8 rounded-xl border border-white/10">
                    <h2 className="text-xl font-semibold mb-2">Login</h2>

                    <div>
                        <label className="block text-xs mb-1">E-mail</label>
                        <input
                            type="email"
                            className="w-full rounded-md border border-white/20 bg-transparent px-3 py-2 text-sm focus:outline-none focus:border-white"
                        />
                    </div>

                    <div>
                        <label className="block text-xs mb-1">Senha</label>
                        <input
                            type="password"
                            className="w-full rounded-md border border-white/20 bg-transparent px-3 py-2 text-sm focus:outline-none focus:border-white"
                        />
                    </div>

                    <button
                        type="submit"
                        className="mt-2 w-full bg-white text-black py-2 rounded-md text-sm font-medium"
                    >
                        Entrar
                    </button>
                </form>
            </main>

            {/* FOOTER  */}
            <Footer />
        </div>
    );
}
