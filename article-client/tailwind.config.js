module.exports = {
  content: [
    "./public/*.html",
    "./src/**/*.{html,js,vue}"
  ],
  theme: {
    extend: {
      fontFamily: {
        'Jua': ['Jua', 'sans-serif'],
        'DoHyeon' : ['Do Hyeon', 'sans-serif'],
        'GowunDodum': ['Gowun Dodum', 'sans-serif']
      },
    },
  },
  plugins: [
    require('tw-elements/dist/plugin')
  ],
}
