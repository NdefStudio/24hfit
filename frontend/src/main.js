// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import FastClick from 'fastclick'
import router from './router'
import App from './App'
import global from './utils/glbval'
import axios from 'axios'
import qs from 'qs'

Vue.prototype.global = global
Vue.prototype.$axios = axios
Vue.prototype.qs = qs

FastClick.attach(document.body)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  router,
  render: h => h(App)
}).$mount('#app-box')
