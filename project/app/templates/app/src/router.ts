import Vue from 'vue';
import Router from 'vue-router';
import Home from './views/Home.vue';

import samplePost from './components/sample/Post.vue';
import Login from './components/Login.vue';
import Index from './components/Index.vue';

import store from './store';

Vue.use(Router);

const router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/login',
      name: 'Login',
      component: Login,
      meta: { isPublic: true },
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
      meta: { isPublic: true },
    },
    {
      path: '/index',
      name: 'Index',
      component: Index,
    },
    {
      path: '/sample/post',
      component: samplePost,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue'),
    },
  ],
});

router.beforeEach((to, from, next) => {
  // isPublic でない場合(=認証が必要な場合)、かつ、ログインしていない場合
  // localStorageのトークンの有無でログイン状態を確認。サーバー側でトークンが無効ならログアウト
  if (to.matched.some((record) => !record.meta.isPublic) && !localStorage.getItem('token')) {
    next({ path: '/login', query: { redirect: to.fullPath }});
  } else {
    next();
  }
});

export default router;
