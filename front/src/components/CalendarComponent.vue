<template>
  <vue-cal
    :time-from="8 * 60"
    :time-to="23 * 60"
    events-count-on-year-view
    :events="events"
    :disable-views="['years', 'year', 'month']"
    style="height: 600px; width: 1200px"
  />
</template>

<script>
import { defineComponent } from "vue";
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";
import axios from "axios";

export default defineComponent({
  components: {
    VueCal,
  },
  data: () => ({
    events: [],
  }),
  mounted() {
    this.fetchSections();

  },
  methods: {
    async fetchSections() {
      try {
        const username = "dfroberg";
        const response = await axios.get(`/api/registeredcourses?username=${username}`);
        const sections = response.data.results;
        console.log(sections);

        // Process API response and convert it into events format
        this.events = sections.flatMap((section) => {
          // Assuming each section has an 'events' key with a list of event dates
          const eventDates = section.events || [];

          return eventDates.map((date) => ({
            start: `${date} ${section.startTime}`,
            end: `${date} ${section.endTime}`, // You need to define endTime in your API response
            title: section.courseName,
            class: 'me'
          }));
        });

        console.log("finished processing");
        console.log(this.events);
      } catch (error) {
        console.error("Error fetching sections:", error);
      }
    },
  },
});
</script>
<style>
.vuecal__event.me {
  background-color: rgba(253, 156, 66, 0.9);
  border: 1px solid rgb(233, 136, 46);
  color: #fff;
}
.vuecal__event.friend {
  background-color: rgba(255, 102, 102, 0.9);
  border: 1px solid rgb(235, 82, 82);
  color: #fff;
}
</style>
