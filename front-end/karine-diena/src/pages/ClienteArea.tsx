import React, { useEffect, useMemo, useState } from "react";

type Task = {
  id: number;
  title: string;
  description: string;
  deadline: string;
  completed: boolean;
};

type Vendor = {
  id: number;
  service: string;
  company: string;
  status: "pendente" | "confirmado" | "em negociação";
  hasDocuments: boolean;
};

type ScheduleItem = {
  id: number;
  activity: string;
  time: string;
};

const EVENT_DATE = new Date("2026-02-15");

const ClientArea: React.FC = () => {
  const [tasks, setTasks] = useState<Task[]>([
    {
      id: 1,
      title: "Tarefa 1",
      description: "Definir estilo do evento",
      deadline: "10/01/2026",
      completed: false,
    },
    {
      id: 2,
      title: "Tarefa 2",
      description: "Fechar lista de convidados",
      deadline: "20/01/2026",
      completed: false,
    },
  ]);

  const [vendorTab, setVendorTab] = useState<
    "servico" | "empresa" | "status" | "documentos"
  >("servico");

  const [vendors] = useState<Vendor[]>([
    {
      id: 1,
      service: "Buffet",
      company: "Sabores & Cia",
      status: "confirmado",
      hasDocuments: true,
    },
    {
      id: 2,
      service: "Fotógrafo",
      company: "Luz & Lente",
      status: "pendente",
      hasDocuments: false,
    },
  ]);

  const [schedule] = useState<ScheduleItem[]>([
    { id: 1, activity: "Cerimônia", time: "16:00" },
    { id: 2, activity: "Coquetel", time: "17:30" },
    { id: 3, activity: "Jantar", time: "19:00" },
    { id: 4, activity: "Balada", time: "21:00" },
  ]);

  // CONTAGEM REGRESSIVA
  const [now, setNow] = useState<Date>(new Date());

  useEffect(() => {
    const interval = setInterval(() => {
      setNow(new Date());
    }, 1000 * 60); // a cada 1 min

    return () => clearInterval(interval);
  }, []);

  const countdown = useMemo(() => {
    const diff = EVENT_DATE.getTime() - now.getTime();
    if (diff <= 0) {
      return { days: 0, hours: 0, minutes: 0 };
    }
    const days = Math.floor(diff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
    const minutes = Math.floor((diff / (1000 * 60)) % 60);
    return { days, hours, minutes };
  }, [now]);

  // Mini calendário (mês do evento)
  const calendarDays = useMemo(() => {
    const year = EVENT_DATE.getFullYear();
    const month = EVENT_DATE.getMonth(); // 0-11
    const firstDay = new Date(year, month, 1);
    const lastDay = new Date(year, month + 1, 0);

    const startWeekDay = firstDay.getDay(); // 0-6 (Dom-Sáb)
    const totalDays = lastDay.getDate();

    const cells: (number | null)[] = [];

    for (let i = 0; i < startWeekDay; i++) {
      cells.push(null);
    }
    for (let d = 1; d <= totalDays; d++) {
      cells.push(d);
    }

    return cells;
  }, []);

  const toggleTask = (id: number) => {
    setTasks((prev) =>
      prev.map((task) =>
        task.id === id ? { ...task, completed: !task.completed } : task
      )
    );
  };

  return (
    <div className="min-h-screen bg-black text-white overflow-hidden">


      {/* CONTEÚDO PRINCIPAL – mesmo clima da Home (fundo bege + cards brancos) */}
      <main className="bg-[#f9f5ea] text-black py-16 px-4">
        <div className="mx-auto max-w-6xl space-y-8">
          {/* HEADER / RESUMO DO EVENTO */}
          <header className="rounded-2xl border border-neutral-200 bg-white/80 px-5 py-6 shadow-md flex flex-col gap-4 sm:flex-row sm:items-end sm:justify-between">
            <div className="space-y-1">
              <p className="text-xs font-semibold tracking-[0.25em] uppercase text-neutral-500">
                Área do cliente
              </p>
              <h1 className="font-display text-2xl sm:text-3xl">
                Casamento Laila &amp; Lucas
              </h1>
              <p className="text-sm text-neutral-700">
                15/02/2026 · Recanto da Fazenda · Evento social
              </p>
            </div>

            <div className="flex flex-col items-start gap-3 sm:items-end">
              <div className="grid grid-cols-3 gap-2 text-center text-xs">
                <div className="rounded-xl bg-neutral-100 px-3 py-2">
                  <p className="text-[10px] uppercase tracking-wide text-neutral-500">
                    Dias
                  </p>
                  <p className="text-lg font-semibold text-neutral-900">
                    {countdown.days}
                  </p>
                </div>
                <div className="rounded-xl bg-neutral-100 px-3 py-2">
                  <p className="text-[10px] uppercase tracking-wide text-neutral-500">
                    Horas
                  </p>
                  <p className="text-lg font-semibold text-neutral-900">
                    {countdown.hours}
                  </p>
                </div>
                <div className="rounded-xl bg-neutral-100 px-3 py-2">
                  <p className="text-[10px] uppercase tracking-wide text-neutral-500">
                    Min
                  </p>
                  <p className="text-lg font-semibold text-neutral-900">
                    {countdown.minutes}
                  </p>
                </div>
              </div>

              <button className="inline-flex items-center justify-center rounded-full border border-neutral-300 px-5 py-2 text-xs font-semibold text-neutral-800 hover:bg-neutral-800 hover:text-white transition">
                Logout
              </button>
            </div>
          </header>

          {/* GRID PRINCIPAL */}
          <div className="grid gap-8 lg:grid-cols-[1.7fr_1fr] items-start">
            {/* COLUNA ESQUERDA */}
            <section className="space-y-6">
              {/* CARD: DADOS DO EVENTO */}
              <div className="rounded-2xl border border-neutral-200 bg-white/80 p-5 shadow-sm">
                <h2 className="mb-3 text-sm font-semibold tracking-wide text-neutral-700 uppercase">
                  Dados do evento
                </h2>

                <div className="grid gap-2 text-sm sm:grid-cols-2 text-neutral-800">
                  <p>
                    <span className="font-semibold">Cliente: </span>Laila
                  </p>
                  <p>
                    <span className="font-semibold">Data: </span>15/02/2026
                  </p>
                  <p>
                    <span className="font-semibold">Local: </span>
                    Recanto da Fazenda
                  </p>
                  <p>
                    <span className="font-semibold">Tipo: </span>Casamento
                  </p>
                </div>
              </div>

              {/* CARD: TAREFAS PREPARATÓRIAS */}
              <div className="rounded-2xl border border-neutral-200 bg-white/80 p-5 shadow-sm">
                <h2 className="mb-3 text-sm font-semibold tracking-wide text-neutral-700 uppercase">
                  Tarefas preparatórias
                </h2>

                <div className="space-y-3">
                  {tasks.map((task) => (
                    <div
                      key={task.id}
                      className="grid grid-cols-[auto,1fr,auto] items-start gap-3 rounded-xl border border-neutral-200 bg-neutral-50 px-3 py-2 text-xs sm:text-sm"
                    >
                      <button
                        onClick={() => toggleTask(task.id)}
                        className={`mt-1 flex h-4 w-4 items-center justify-center rounded border ${task.completed
                          ? "border-neutral-900 bg-neutral-900"
                          : "border-neutral-400 bg-white"
                          }`}
                        aria-label={`Marcar ${task.title} como concluída`}
                      >
                        {task.completed && (
                          <span className="h-[2px] w-2.5 rotate-[-45deg] border-b-2 border-r-2 border-white" />
                        )}
                      </button>

                      <div>
                        <p className="font-medium text-neutral-900">
                          {task.title} –{" "}
                          <span className="font-normal">
                            {task.description}
                          </span>
                        </p>
                        <p className="mt-1 text-[11px] text-neutral-500">
                          Data limite:{" "}
                          <span className="font-semibold">
                            {task.deadline}
                          </span>
                        </p>
                      </div>

                      <button className="mt-1 h-6 w-6 rounded-full border border-neutral-300 text-[11px] text-neutral-700 hover:bg-neutral-900 hover:text-white transition">
                        ✎
                      </button>
                    </div>
                  ))}
                </div>
              </div>

              {/* CARD: FORNECEDORES */}
              <div className="rounded-2xl border border-neutral-200 bg-white/80 p-5 shadow-sm">
                <h2 className="mb-3 text-sm font-semibold tracking-wide text-neutral-700 uppercase">
                  Gerenciamento de fornecedores
                </h2>

                {/* Abas simples */}
                <div className="mb-4 flex flex-wrap gap-2 text-xs sm:text-sm">
                  {[
                    { id: "servico", label: "Serviço" },
                    { id: "empresa", label: "Empresa" },
                    { id: "status", label: "Status" },
                    { id: "documentos", label: "Documentos" },
                  ].map((tab) => (
                    <button
                      key={tab.id}
                      onClick={() =>
                        setVendorTab(tab.id as typeof vendorTab)
                      }
                      className={`rounded-full border px-3 py-1 transition ${vendorTab === tab.id
                        ? "border-neutral-900 bg-neutral-900 text-white"
                        : "border-neutral-300 bg-white text-neutral-800 hover:bg-neutral-900 hover:text-white"
                        }`}
                    >
                      {tab.label}
                    </button>
                  ))}
                </div>

                <div className="overflow-x-auto">
                  <table className="min-w-full text-left text-xs sm:text-sm">
                    <thead>
                      <tr className="border-b border-neutral-200 text-[11px] uppercase tracking-wide text-neutral-500">
                        <th className="py-2 pr-4">Serviço</th>
                        <th className="py-2 pr-4">Empresa</th>
                        <th className="py-2 pr-4">Status</th>
                        <th className="py-2 pr-4">Docs</th>
                      </tr>
                    </thead>
                    <tbody>
                      {vendors.map((v) => (
                        <tr
                          key={v.id}
                          className="border-b border-neutral-100 text-neutral-800"
                        >
                          <td className="py-2 pr-4">{v.service}</td>
                          <td className="py-2 pr-4">{v.company}</td>
                          <td className="py-2 pr-4">
                            <span
                              className={`rounded-full px-2 py-0.5 text-[11px] ${v.status === "confirmado"
                                ? "bg-emerald-50 text-emerald-800"
                                : v.status === "pendente"
                                  ? "bg-amber-50 text-amber-800"
                                  : "bg-sky-50 text-sky-800"
                                }`}
                            >
                              {v.status}
                            </span>
                          </td>
                          <td className="py-2 pr-4">
                            {v.hasDocuments ? (
                              <span className="text-xs text-emerald-700">
                                Enviado
                              </span>
                            ) : (
                              <button className="text-xs text-neutral-900 underline">
                                Enviar
                              </button>
                            )}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>

              {/* CARD: CRONOGRAMA */}
              <div className="mb-6 rounded-2xl border border-neutral-200 bg-white/80 p-5 shadow-sm">
                <h2 className="mb-3 text-sm font-semibold tracking-wide text-neutral-700 uppercase">
                  Cronograma do evento
                </h2>

                <div className="space-y-2 text-xs sm:text-sm">
                  {schedule.map((item) => (
                    <div
                      key={item.id}
                      className="grid grid-cols-[auto,1fr,auto] items-center gap-3 rounded-xl border border-neutral-200 bg-neutral-50 px-3 py-2"
                    >
                      <span className="text-[11px] font-semibold uppercase tracking-wide text-neutral-500">
                        Atividade
                      </span>
                      <span className="font-medium text-neutral-900">
                        {item.activity}
                      </span>
                      <span className="rounded-full border border-neutral-300 bg-white px-3 py-0.5 text-[11px] font-semibold text-neutral-800">
                        {item.time}
                      </span>
                    </div>
                  ))}
                </div>
              </div>
            </section>

            {/* COLUNA DIREITA */}
            <aside className="space-y-5">
              {/* CONTAGEM RESUMIDA JÁ ESTÁ NO HEADER – AQUI INFO EXTRA + TEXTO */}
              <div className="rounded-2xl border border-neutral-200 bg-white/85 p-5 shadow-sm">
                <p className="text-xs font-semibold tracking-[0.25em] uppercase text-neutral-500">
                  Contagem regressiva
                </p>
                <p className="mt-2 text-sm text-neutral-700">
                  Faltam{" "}
                  <span className="font-semibold text-neutral-900">
                    {countdown.days} dias
                  </span>{" "}
                  para o grande dia.
                </p>
                <p className="mt-1 text-xs text-neutral-500">
                  Aproveite para revisar as tarefas e alinhar com os
                  fornecedores.
                </p>
              </div>

              {/* CALENDÁRIO + RESUMO DE TAREFAS */}
              <div className="space-y-4 rounded-2xl border border-neutral-200 bg-white/85 p-5 shadow-sm">
                {/* MINI CALENDÁRIO */}
                <div>
                  <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-neutral-500">
                    Outubro 2025
                  </p>
                  <div className="grid grid-cols-7 gap-1 text-center text-[10px]">
                    {["D", "S", "T", "Q", "Q", "S", "S"].map((d) => (
                      <div
                        key={d}
                        className="py-1 text-[10px] font-semibold text-neutral-500"
                      >
                        {d}
                      </div>
                    ))}
                    {calendarDays.map((day, index) => {
                      const isEventDay = day === EVENT_DATE.getDate();
                      return (
                        <div
                          key={index}
                          className={`flex h-7 items-center justify-center rounded text-[11px] ${day
                            ? isEventDay
                              ? "bg-neutral-900 text-white font-bold"
                              : "bg-neutral-100 text-neutral-800"
                            : ""
                            }`}
                        >
                          {day}
                        </div>
                      );
                    })}
                  </div>
                </div>

                {/* RESUMO TAREFAS */}
                <div>
                  <p className="mb-2 text-xs font-semibold uppercase tracking-wide text-neutral-500">
                    Tarefas importantes
                  </p>
                  <div className="space-y-2 text-xs">
                    <div className="flex items-center justify-between rounded-lg border border-neutral-200 bg-neutral-50 px-3 py-1.5">
                      <span>Buffet</span>
                      <span className="text-[11px] text-neutral-500">
                        11/11/2025
                      </span>
                    </div>
                    <div className="flex items-center justify-between rounded-lg border border-neutral-200 bg-neutral-50 px-3 py-1.5">
                      <span>Fotógrafo</span>
                      <span className="text-[11px] text-neutral-500">
                        01/01/2026
                      </span>
                    </div>
                  </div>
                </div>
              </div>

              {/* SECTION 2 / 3 – RESERVA PARA FUTURO */}
              <div className="rounded-2xl border border-neutral-200 bg-white/80 p-4 text-center text-xs font-semibold uppercase tracking-[0.2em] text-neutral-600">
                Section 2
              </div>
              <div className="rounded-2xl border border-neutral-200 bg-white/80 p-4 text-center text-xs font-semibold uppercase tracking-[0.2em] text-neutral-600">
                Section 3
              </div>
            </aside>
          </div>
        </div>
      </main>
    </div>
  );
};

export default ClientArea;
