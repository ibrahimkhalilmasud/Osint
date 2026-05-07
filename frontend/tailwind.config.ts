import type { Config } from 'tailwindcss';

export default {
  content: ['./app/**/*.{js,ts,jsx,tsx}', './components/**/*.{js,ts,jsx,tsx}'],
  theme: {
    extend: {
      colors: {
        panel: '#111827',
        accent: '#38bdf8'
      }
    }
  },
  darkMode: 'class',
  plugins: []
} satisfies Config;
