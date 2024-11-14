import { createRouter, createWebHistory } from 'vue-router';
import StandingsView from '@/views/StandingsView.vue';
import RaceResultsView from '@/views/RaceResultsView.vue';

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'standings',
      component: StandingsView,
    },
    {
      path: '/race-results',
      name: 'race-results',
      component: RaceResultsView
    },
  ],
});

export default router;
