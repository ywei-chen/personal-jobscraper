import { createRouter, createWebHistory } from 'vue-router'
import JobList from '@/view/jobList.vue'
import JobDetail from '@/view/jobDetail.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: JobList,
    },
    {
      path: '/jobs/:id',
      name: 'job-detail',
      component: JobDetail,
    },
  ],
})

export default router
