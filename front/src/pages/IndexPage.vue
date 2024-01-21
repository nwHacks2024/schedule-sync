<template>
  <q-page class="flex flex-center">

    <div v-if="selectedContent === 'mySchedule'">
      <CalendarComponent />
    </div>

    <div v-else-if="selectedContent === 'degreePlanner'">
      <DegreePlanner />
    </div>

    <div v-else-if="selectedContent === 'addCourses'" >
      <AddCourses />
    </div>

    <div v-else-if="selectedContent === 'compareSchedules'">
      <FriendsDropdown />
      <CalendarComponentFriend />

    </div>

    <div v-else>
      <img src="/public/icons/logo_words.jpeg" style="max-width: 50%; height: auto; margin-left: auto; margin-right: auto;" />

    </div>

  </q-page>
</template>

<script>
import { defineComponent } from 'vue'
import CalendarComponent from '../components/CalendarComponent.vue'
import CalendarComponentFriend from '../components/CalendarComponentFriend.vue'
import FriendsDropdown from '../components/FriendsDropdown.vue'
import AddCourses from '../components/AddCourses.vue'
import DegreePlanner from '../components/DegreePlanner.vue'

export default defineComponent({
  components: {
    CalendarComponent,
    FriendsDropdown,
    AddCourses,
    DegreePlanner,
    CalendarComponentFriend
  },
  props: {
    selectedContent: String,
  },
  name: 'IndexPage'
})
</script>


