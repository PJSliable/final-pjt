module.exports = {
  content: [
    "./public/*.html",
    "./src/**/*.{html,js,vue}"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('tw-elements/dist/plugin')
  ],
}
