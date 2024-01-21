<template>
  <q-page class="flex flex-center">
    <img
      alt="Quasar logo"
      src="~assets/quasar-logo-vertical.svg"
      style="width: 200px; height: 200px"
    >
    <ApiTest />
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import ApiTest from '../components/ApiTest.vue'

export default defineComponent({
  components: {
    ApiTest
  },
  name: 'IndexPage'
})
</script>
