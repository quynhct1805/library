const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  devServer: {
    proxy: {
      '^/api': {
        target: 'http://api:8000/',
        ws: true,
        changeOrigin: true
      },
    },
  },

  // devServer: {
  //   proxy: 'http://api:8000/'
  // },
  transpileDependencies: true,

  pluginOptions: {
    vuetify: {
			// https://github.com/vuetifyjs/vuetify-loader/tree/next/packages/vuetify-loader
		}
  },
  
})
