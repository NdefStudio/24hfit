import Vue from 'vue'
import Router from 'vue-router'
import HomePage from '@/components/HomePage'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'HomePage',
      component: HomePage
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: resolve => (require(['@/components/LoginPage'], resolve))
    },
    {
      path: '/main/:id',
      name: 'MainPage',
      component: resolve => (require(['@/components/MainPage'], resolve)),
      children: [
        {
          path: 'routine',
          name: 'RoutinePage',
          component: resolve => (require(['@/components/RoutinePage'], resolve))
        },
        {
          path: 'posts',
          name: 'PostsPage',
          component: resolve => (require(['@/components/PostsPage'], resolve))
        },
        {
          path: 'my',
          name: 'MyPage',
          component: resolve => (require(['@/components/MyPage'], resolve))
        }
      ]
    },
    {
      path: '/report/:id',
      name: 'ReportPage',
      component: resolve => (require(['@/components/ReportPage'], resolve))
    }
  ]
})
