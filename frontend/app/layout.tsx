import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'OSINT Platform Dashboard',
  description: 'Defensive OSINT aggregation dashboard'
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en" className="dark">
      <body>{children}</body>
    </html>
  );
}
