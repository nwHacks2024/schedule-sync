<template>
  <q-page class="flex flex-center">
    <CalendarComponent />
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
// import ApiTest from '../components/ApiTest.vue'
import CalendarComponent from '../components/CalendarComponent.vue'

export default defineComponent({
  components: {
    CalendarComponent
  },
  name: 'IndexPage'
})
</script>


