import Vue from 'vue'
import App from './App.vue'
import router from './router'
import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
Vue.use(BootstrapVue);
Vue.config.productionTip = false

import VueParticles from 'vue-particles'
Vue.use(VueParticles)



import NProgress from 'nprogress'
import 'nprogress/nprogress.css'

NProgress.configure({
    easing: 'ease',
    speed: 500,
    showSpinner: false, // 是否显示加载ico    
    trickleSpeed: 200,
    minimum: 0.3
})
router.beforeEach((to, from, next) => {
    // 每次切换页面时，调用进度条
    NProgress.start();
    next();
});

router.afterEach(() => {
    NProgress.done()
})

new Vue({
    router,
    render: h => h(App)
}).$mount('#app')