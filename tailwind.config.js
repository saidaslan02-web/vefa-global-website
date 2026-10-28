/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./index.html', './gizlilik.html', './en/*.html'],
  theme: {
    extend: {
      colors: {
        coral: '#f97316',
        'coral-deep': '#c2410c',
        'coral-tint': '#ffedd5',
        ink: '#09090b',
        'ink-soft': '#3f3f46',
        muted: '#71717a',
        cream: '#ffffff',
        'cream-2': '#fafafa',
        'cream-3': '#f4f4f5',
        hairline: '#e4e4e7',
        espresso: '#18181b',
        'dark-text': '#f4f4f5',
        'dark-muted': '#a1a1aa',
        'dark-line': '#3f3f46'
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
        mono: ['ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace']
      }
    }
  }
}
