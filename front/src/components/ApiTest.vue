<template>
    <div>
      <h1>API Response: {{ apiResponse }}</h1>
      <q-btn @click="fetchData" label="Fetch Data" />
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
      async fetchData() {
        try {
          const response = await axios.get('http://localhost:6543/mock_data');
          this.apiResponse = response.data;
          console.log('The response: ' + this.apiResponse)
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      },
    },
  };
  </script>
  