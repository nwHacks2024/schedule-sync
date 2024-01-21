<template>
  <q-page class="flex flex-center">

    <div v-if="selectedContent === 'mySchedule'">
      <CalendarComponent />
    </div>

    <div v-else-if="selectedContent === 'degreePlanner'">
      <h6>Coming Soon!</h6>
      <p>This is your degree planner!</p>
    </div>

    <div v-else-if="selectedContent === 'addCourses'">
      <AddCourses />
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
import AddCourses from '../components/AddCourses.vue'

export default defineComponent({
  components: {
    CalendarComponent,
    FriendsDropdown,
    AddCourses,
    CalendarComponentFriend
  },
  props: {
    selectedContent: String,
  },

  name: 'IndexPage'

})
</script>


