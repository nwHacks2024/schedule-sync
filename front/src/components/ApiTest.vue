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
          const username = "dfroberg";
          const response = await axios.get(`/api/userprofile?username=${username}`);
          this.apiResponse = response.data;
          console.log('The response: ' + this.apiResponse)
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },
    },
  };
  </script>
