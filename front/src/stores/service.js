import { defineStore } from 'pinia'
import { api } from 'boot/axios'
import { useQuasar } from 'quasar'

const $q = useQuasar()

export const useCounterStore = defineStore('counter', {
  state: () => ({
    counter: 0
  }),

  getters: {
    doubleCount (state) {
      return state.counter * 2
    }
  },

  actions: {
    increment () {
      this.counter++
    },
    async fetchData() {
      api.get('/mock_data')
    }
  
  }
})
