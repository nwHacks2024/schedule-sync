<template>
  <vue-cal
  selected-date="2024-01-20"
  :time-from="8 * 60"
  :time-to="23 * 60"
  hide-weekends
  events-count-on-year-view
  :events="events">
</vue-cal>
</template>

<script>
import { defineComponent } from "vue";
import VueCal from "vue-cal";
import "vue-cal/dist/vuecal.css";

export default defineComponent({
  components: {
    VueCal,
  },
  data: () => ({
    events: [
      {
        start: "2018-11-19 22:00",
        end: "2018-11-20 11:00",
        title: "Nightclub",
        content: '<i class="icon material-icons">local_drink</i>',
        class: "leisure",
        repeat: {
          weekdays: [1, 3], // You can repeat on multiple days of the week.
          until: "2020-11-30", // Don't need a time here as it will take the same as original event date.
        },
      },
      {
        start: "2018-11-23", // You can put time or not, will be discarded if all-day.
        end: "2018-11-23",
        title: "Pizza day!",
        content: '<i class="icon material-icons">local_pizza</i>',
        class: "pink-event",
        allDay: true,
        repeat: {
          weekdays: [5], // If original event day is not in these days, original event will still show up.
          // Without `until` property, it will go on forever.
        },
      },
      {
        start: "2018-11-22 10:00",
        end: "2018-11-22 12:00",
        title: "Piano lesson",
        content: '<i class="icon material-icons">queue_music</i>',
        class: "leisure",
        repeat: {
          every: "week",
          until: new Date("2019/06/01"), // You can also use a Javascript Date.
        },
      },
      {
        start: "2018-11-20 18:00",
        end: "2018-11-20 20:00",
        title: "Tennis tournament",
        content: '<i class="icon material-icons">sports_tennis</i>',
        class: "sport",
        repeat: {
          every: 14,
          until: "2019-01-20",
        },
      },
      {
        start: "2018-11-01",
        end: "2018-11-01",
        title: "Crêpes day",
        content: '<i class="icon material-icons">restaurant</i>',
        class: "yellow-event",
        allDay: true,
        repeat: {
          every: "month",
          until: "2019-12-26",
        },
      },
      {
        start: "2015-06-15",
        end: "2015-06-15",
        title: "My Birthday",
        content: '<i class="icon material-icons">cake</i><br>I am 4.',
        class: "blue-event",
        allDay: true,
        repeat: {
          every: "year",
        },
      },
    ],
  }),
  name: "IndexPage",
});
</script>
