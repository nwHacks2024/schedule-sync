import { boot } from 'quasar/wrappers'
import axios from 'axios'

// const api = axios.create({ baseURL: 'http://localhost:6543' })
// "async" is optional;
// more info on params: https://v2.quasar.dev/quasar-cli/boot-files
export default boot(({ app }) => {
  app.config.globalProperties.$axios = axios
  app.config.globalProperties.$api = api
})

export { axios, api}