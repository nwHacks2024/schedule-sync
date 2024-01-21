<template>
  <div class="q-pa-md">
    <q-btn-dropdown color="primary" label="Dropdown Button" no-shadow @show="loadFriends">
      <q-list>
        <q-item v-for="friend in friends.results" :key="friend.id" clickable v-close-popup @click="onItemClick(friend)">
          <q-item-section>
            <q-item-label>{{ friend.friendUsername }}</q-item-label>
          </q-item-section>
        </q-item>
      </q-list>
    </q-btn-dropdown>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      friends: { results: [] },
    };
  },
  mounted() {
    this.loadFriends();
  },
  methods: {
    async loadFriends() {
      try {
        // Make a POST request to the /friends API to get the data
        const response = await axios.post('/api/friends', {
          username: "dfroberg"
        });

        // Assuming the API response is an object with a 'results' property
        this.friends = response.data;
        console.log(this.friends);
      } catch (error) {
        console.error('Error fetching data from /friends API:', error);
      }
    },
    onItemClick(friend) {
      // Handle item click event here, you can access the selected friend object
      console.log('Selected friend:', friend);
    },
  },
};
</script>

<style scoped>
/* Add component-specific styles here */
</style>
