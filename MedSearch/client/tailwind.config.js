module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
    backgroundColor: theme => ({
      ...theme('colors'),
      'primary': '#521751',
      'secondary': '#CF8BA3',
      'third': '#854D27',
      'fourth': '#B7E4C7',
      'fifth': '#D8F3DC'

    })
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
