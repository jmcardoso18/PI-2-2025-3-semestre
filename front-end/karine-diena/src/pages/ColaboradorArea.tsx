import React, { useState } from "react";


type ScheduleItem = {
    id: number;
    activity: string;
    time: string;
    done: boolean;
};

const ColaboradorArea: React.FC = () => {
    const [schedule, setSchedule] = useState<ScheduleItem[]>([
        { id: 1, activity: "Chegada ao local", time: "14:00", done: false },
        { id: 2, activity: "Briefing da equipe", time: "15:00", done: false },
        { id: 3, activity: "Início da cerimônia", time: "16:30", done: false },
        { id: 4, activity: "Coquetel / recepção", time: "17:30", done: false },
        { id: 5, activity: "Início da festa", time: "19:00", done: false },
    ]);

    const toggleDone = (id: number) => {
        setSchedule((prev) =>
            prev.map((item) =>
                item.id === id ? { ...item, done: !item.done } : item
            )
        );
    };

    return (

        <div className="min-h-screen bg-black text-white flex flex-col">
            {/* BARRA SUPERIOR */}
            <header className="border-b border-white/10 bg-black/80 px-4 sm:px-8 py-3 flex items-center justify-between">
                <span className="text-xs sm:text-sm font-medium tracking-wide uppercase">
                    Página do colaborador
                </span>

                <button className="text-xs sm:text-sm rounded-full border border-white/40 px-4 py-1.5 text-white hover:bg-white/10 transition">
                    Logout
                </button>
            </header>

            {/* CONTEÚDO PRINCIPAL */}
            <main className="flex-1 bg-[#f9f5ea] text-black">
                <div className="mx-auto max-w-5xl px-4 sm:px-6 py-10 space-y-10">
                    {/* TÍTULO + INFO RESUMO */}
                    <div className="flex flex-col sm:flex-row sm:items-end sm:justify-between gap-4">
                        <div>
                            <h1 className="font-display text-2xl sm:text-3xl">
                                Cronograma do evento
                            </h1>
                            <p className="mt-2 text-sm text-neutral-700">
                                Aqui você acompanha as atividades e horários do evento para
                                manter toda a equipe alinhada.
                            </p>
                        </div>

                        <div className="text-xs sm:text-sm text-neutral-600">
                            <p>
                                <span className="font-semibold">Evento:</span> Casamento Laila e
                                Lucas
                            </p>
                            <p>
                                <span className="font-semibold">Data:</span> 15/02/2026
                            </p>
                            <p>
                                <span className="font-semibold">Local:</span> Recanto da
                                Fazenda
                            </p>
                        </div>
                    </div>

                    {/* CARD: CRONOGRAMA */}
                    <section
                        className="
              rounded-2xl bg-white shadow-md 
              p-5 sm:p-6 space-y-4
            "
                    >
                        <div className="flex items-center justify-between gap-4">
                            <h2 className="text-sm sm:text-base font-semibold tracking-wide text-neutral-800">
                                Atividades do dia
                            </h2>
                            <span className="text-[11px] uppercase tracking-[0.15em] text-neutral-500">
                                Atividade · Horário · Check
                            </span>
                        </div>

                        <div className="border border-neutral-200 rounded-xl overflow-hidden bg-neutral-50/80">
                            {/* Cabeçalho da tabela */}
                            <div className="grid grid-cols-[1fr_auto_auto] gap-2 px-4 py-2 text-[11px] sm:text-xs font-semibold uppercase tracking-wide text-neutral-500 bg-neutral-100/70">
                                <span>Atividade</span>
                                <span className="text-center">Horário</span>
                                <span className="text-center">Status</span>
                            </div>

                            {/* Linhas */}
                            <div className="divide-y divide-neutral-200">
                                {schedule.map((item) => (
                                    <div
                                        key={item.id}
                                        className="grid grid-cols-[1fr_auto_auto] gap-2 px-4 py-3 items-center text-sm bg-white/60 hover:bg-neutral-50 transition"
                                    >
                                        <div>
                                            <p
                                                className={`font-medium text-neutral-900 ${item.done ? "line-through text-neutral-400" : ""
                                                    }`}
                                            >
                                                {item.activity}
                                            </p>
                                        </div>

                                        <span className="inline-flex justify-center rounded-full border border-neutral-300 bg-white px-3 py-1 text-xs font-semibold text-neutral-800">
                                            {item.time}
                                        </span>

                                        <button
                                            onClick={() => toggleDone(item.id)}
                                            className={`
                        inline-flex h-7 w-7 items-center justify-center rounded-full border text-xs font-semibold
                        ${item.done
                                                    ? "border-emerald-500 bg-emerald-500 text-white"
                                                    : "border-neutral-300 bg-white text-neutral-700 hover:bg-neutral-100"
                                                }
                        transition
                      `}
                                            aria-label="Marcar atividade como concluída"
                                        >
                                            {item.done ? "✓" : "OK"}
                                        </button>
                                    </div>
                                ))}
                            </div>
                        </div>

                        <p className="text-xs text-neutral-500">
                            Marque como concluídas as atividades que já foram realizadas para
                            manter o controle em tempo real.
                        </p>
                    </section>

                    {/* BOTÃO DE OCORRÊNCIAS */}
                    <section className="pt-2">
                        <div className="max-w-xl mx-auto">
                            <button
                                type="button"
                                className="
                  w-full 
                  rounded-full 
                  px-10 py-4 
                  text-sm sm:text-base font-semibold 
                  text-black 
                  bg-neutral-200 
                  hover:bg-neutral-300 
                  hover:shadow-2xl 
                  hover:scale-[1.02]
                  active:scale-[0.98]
                  transition-all duration-300
                "
                            >
                                Ocorrências
                            </button>
                            <p className="mt-2 text-[11px] text-center text-neutral-500">
                                Clique para registrar ou visualizar ocorrências durante o evento
                                (atrasos, imprevistos, solicitações especiais, etc.).
                            </p>
                        </div>
                    </section>
                </div>
            </main>


        </div>
    );
};

export default ColaboradorArea;
