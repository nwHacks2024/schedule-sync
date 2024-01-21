<template>
    <div>
        <h6>API Response: {{ apiResponse }}</h6>
        <q-btn @click="fetchUserInfo" label="Fetch Data" />
    </div>
<<<<<<< Updated upstream
</template>
  
<script>
import axios from 'axios';
import userData from '/../../bdec/mock_data/getUserInfo.json'

export default {
=======
  </template>

  <script>
  import axios from 'axios';

  export default {
>>>>>>> Stashed changes
    data() {
        return {
            apiResponse: null,
        };
    },
    methods: {
<<<<<<< Updated upstream
        async fetchUserInfo() {
                            try {
                                this.apiResponse = userData;
                                console.log('The response:', this.apiResponse);
                            } catch (error) {
                                console.error('Error fetching user info:', error);
                            }
                        },
    },
};
</script>
  
=======
      async fetchData() {
        try {

          debugger;
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
>>>>>>> Stashed changes
