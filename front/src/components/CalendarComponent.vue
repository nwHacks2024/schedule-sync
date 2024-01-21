<template>
  <vue-cal
    :time-from="8 * 60"
    :time-to="23 * 60"
    events-count-on-year-view
    :events="events"
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
        const response = await axios.post("/registeredcourses");
        const sections = response.data;

        // Process sections and convert them to events
        const newEvents = sections.map((section) => {
          return {
            start: section.startDate, // Replace with the actual start date property from your API
            end: section.endDate, // Replace with the actual end date property from your API
            title: section.title, // Replace with the actual title property from your API
            content: section.content, // Replace with the actual content property from your API
            class: section.eventClass, // Replace with the actual class property from your API
            // Add other properties as needed
          };
        });

        // Update the events array with the new events
        this.events = newEvents;
      } catch (error) {
        console.error("Error fetching sections:", error);
      }
    },
  },
});
</script>
