<template>
    <div>
        <h6>API Response: {{ apiResponse }}</h6>
        <q-btn @click="fetchUserInfo" label="Fetch Data" />
    </div>
  </template>

  <script>
  import axios from 'axios';

  export default {
    data() {
        return {
            apiResponse: null,
        };
    },
    methods: {
      async fetchUserInfo() {
        try {
          const response = await axios.post('/api/userprofile', {
            username: "dfroberg"
          });
          this.apiResponse = response.data;
          console.log('The response: ' + this.apiResponse)
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },
    },
  };
  </script>
