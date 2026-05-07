'use client';

import { useState } from 'react';

const fields = [
  { key: 'full_name', label: 'Full name' },
  { key: 'phone_number', label: 'Phone number' },
  { key: 'email_address', label: 'Email address' },
  { key: 'username', label: 'Username' },
  { key: 'domain', label: 'Domain' },
  { key: 'company_name', label: 'Company name' }
] as const;

export function Dashboard() {
  const [payload, setPayload] = useState<Record<string, string>>({});

  return (
    <main className="mx-auto grid max-w-6xl gap-4 p-6 lg:grid-cols-3">
      <section className="card lg:col-span-2">
        <h1 className="mb-4 text-2xl font-semibold text-accent">Investigation Console</h1>
        <div className="grid gap-3 md:grid-cols-2">
          {fields.map((field) => (
            <label key={field.key} className="text-sm">
              <span className="mb-1 block text-slate-300">{field.label}</span>
              <input
                className="w-full rounded border border-slate-700 bg-slate-900 px-3 py-2"
                value={payload[field.key] ?? ''}
                onChange={(event) => setPayload((prev) => ({ ...prev, [field.key]: event.target.value }))}
              />
            </label>
          ))}
        </div>
        <div className="mt-4 flex gap-2">
          <button className="rounded bg-accent px-4 py-2 font-medium text-slate-900">Create Investigation</button>
          <button className="rounded border border-slate-600 px-4 py-2">Run Tools</button>
          <button className="rounded border border-slate-600 px-4 py-2">Export Report</button>
        </div>
      </section>

      <aside className="card space-y-4">
        <h2 className="text-lg font-semibold">Live Status</h2>
        <p className="text-sm text-slate-300">Queue: healthy</p>
        <p className="text-sm text-slate-300">Workers: 2 active</p>
        <p className="text-sm text-slate-300">Neo4j: connected</p>
        <div>
          <h3 className="mb-2 text-sm font-semibold">Entity Correlation</h3>
          <div className="h-40 rounded border border-dashed border-slate-700" />
        </div>
      </aside>
    </main>
  );
}
