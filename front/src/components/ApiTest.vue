<template>
    <div>
        <h6>API Response: {{ apiResponse }}</h6>
        <q-btn @click="fetchUserInfo" label="Fetch Data" />
    </div>
</template>
  
<script>
import axios from 'axios';
import userData from '/../../bdec/mock_data/getUserInfo.json'

export default {
    data() {
        return {
            apiResponse: null,
        };
    },
    methods: {
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
  