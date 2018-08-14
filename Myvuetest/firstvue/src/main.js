// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import Axios from 'axios'
Vue.config.productionTip = false

// 全局接口中间件
Vue.prototype.$http = Axios;
Axios.interceptors.request.use(
	config => {
		config.url = config.url.replace('/api','http://192.168.99.100:8010')
		let tbkt_token = localStorage.getItem("Tbkt-Token") || '';
		if(tbkt_token) config.headers['Tbkt-Token'] = tbkt_token;
		return config
	},
	err => {
		return Promise.reject(err)
	}
);

new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
