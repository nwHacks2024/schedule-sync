<template>
  <div class="q-pa-md">
    <q-btn-dropdown color="primary" label="Choose Friend" no-shadow>
      <q-list v-if="!loading">
        <q-item v-for="friend in friends.results" :key="friend.id" clickable v-close-popup @click="onItemClick(friend)">
          <q-item-section>
            <q-item-label>{{ friend.friendUsername }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>

      <q-spinner-gears v-else size="50px"></q-spinner-gears>
    </q-btn-dropdown>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      friends: { results: [] },
      loading: false,
    };
  },
  mounted() {
    this.loadFriends();
  },
  methods: {
    async loadFriends() {
      try {
        this.loading = true;
        const username = "dfroberg";
        // Make a POST request to the /friends API to get the data
        const response = await axios.get(`/api/friends?username=${username}`);

        // Assuming the API response is an object with a 'results' property
        this.friends = response.data;
        console.log(this.friends);
      } catch (error) {
        console.error('Error fetching data from /friends API:', error);
      } finally {
        this.loading = false;
      }
    },
    onItemClick(friend) {
      console.log('Selected friend:', friend);
    },
  },
};
</script>

<style scoped>
/* Add component-specific styles here */
</style>
