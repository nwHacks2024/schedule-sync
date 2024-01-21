// store/index.js

import { defineStore } from 'pinia';

export const useAuthStore = defineStore('auth', {
  state: () => ({
    username: "",
  }),
  actions: {
    setUsername(username) {
      this.username = username;
    },
  },
});
