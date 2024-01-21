<template>
  <q-page class="flex flex-center">

    <div v-if="selectedContent === 'mySchedule'">
      <CalendarComponent />
    </div>

    <div v-else-if="selectedContent === 'degreePlanner'">
      <p>This is your degree planner!</p>
    </div>

    <div v-else-if="selectedContent === 'addCourses'">
      <p>Here is where you can add courses</p>
    </div>

    <div v-else-if="selectedContent === 'compareSchedules'">
      <FriendsDropdown />
      <CalendarComponentFriend />

    </div>

    <div v-else>
      <h1> Welcome to BDEC! The better SSC.</h1>
    </div>
  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
// import ApiTest from '../components/ApiTest.vue'
import CalendarComponent from '../components/CalendarComponent.vue'
import CalendarComponentFriend from '../components/CalendarComponentFriend.vue'
import FriendsDropdown from '../components/FriendsDropdown.vue'

export default defineComponent({
  components: {
    CalendarComponent,
    FriendsDropdown,
    CalendarComponentFriend
  },
  props: {
    selectedContent: String,
  },

  name: 'IndexPage'

})
</script>


