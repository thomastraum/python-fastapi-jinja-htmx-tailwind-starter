/** @type {import('tailwindcss').Config} */
module.exports = {
    darkMode: "class",
    content: ["./app/templates/**/*.{html, jinja}", "./resources/js/**/*.tsx"],
    theme: {
      extend: {
        fontFamily: {
          sans: [ "Helvetica Neue", "Helvetica", "sans-serif"],
          // other font families
        },
        letterSpacing: {
          tighter: '-0.35',
        },
        lineHeight: {
          tighter: '0.8',
        },
        
      },
    },
    plugins: [
      require("@tailwindcss/forms"),
      require("@tailwindcss/aspect-ratio"),
      require("@tailwindcss/typography"),
    ],
  };